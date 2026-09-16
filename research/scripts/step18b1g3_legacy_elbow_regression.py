from pathlib import Path
import pickle, json, gc, sys
import numpy as np
import torch
from smplx.lbs import batch_rodrigues, blend_shapes, vertices2joints, batch_rigid_transform

ROOT = Path('/content/drive/MyDrive/interactive-digital-humans')
EXP8 = ROOT / 'experiments/08-second-joint-generalization'
SMPL_PATH = ROOT / 'private_assets/smpl/SMPL_NEUTRAL_clean.pkl'
B1_PATH = EXP8 / '17B1_left_elbow_frame2_displacements.npz'
MASK_PATH = EXP8 / '17A2_frozen_canonical_anatomy_masks.npz'
OUT_PATH = EXP8 / '18B1G3_legacy_torch113_cuda117_regression.json'

SEQ = {
    'seattle': {
        'G': 472958,
        'learned': ROOT / 'experiments/04-k6-support-mapping/13E_learned_lbs_weights.npz',
        'learned_key': 'learned_lbs',
        'k6': ROOT / 'experiments/04-k6-support-mapping/13A_k6_effective_mapping.npz',
        'k6_key': 'effective_lbs',
        'xyz': ROOT / 'experiments/01-baseline/probe_results/frame000_left_wrist_z_10deg.npz',
        'xyz_key': 'xyz_canon',
        'pose': ROOT / 'datasets/neuman/seattle/4d_humans/smpl_optimized_aligned_scale.npz',
    },
    'parkinglot': {
        'G': 614157,
        'learned': ROOT / 'experiments/07-cross-sequence-replication/16C1_parkinglot_learned_lbs.npz',
        'learned_key': 'learned_lbs',
        'k6': ROOT / 'experiments/07-cross-sequence-replication/16C2_parkinglot_k6_effective_mapping.npz',
        'k6_key': 'effective_lbs',
        'xyz': ROOT / 'experiments/07-cross-sequence-replication/16C1_parkinglot_learned_lbs.npz',
        'xyz_key': 'xyz_canon',
        'pose': ROOT / 'datasets/neuman/parkinglot/4d_humans/smpl_optimized_aligned_scale.npz',
    },
    'jogging': {
        'G': 311723,
        'learned': ROOT / 'experiments/07-cross-sequence-replication/16D2_jogging_learned_lbs.npz',
        'learned_key': 'learned_lbs',
        'k6': ROOT / 'experiments/07-cross-sequence-replication/16D3_jogging_k6_effective_mapping.npz',
        'k6_key': 'effective_lbs',
        'xyz': ROOT / 'experiments/07-cross-sequence-replication/16D2_jogging_learned_lbs.npz',
        'xyz_key': 'xyz_canon',
        'pose': ROOT / 'datasets/neuman/jogging/4d_humans/smpl_optimized_aligned_scale.npz',
    },
}

FRAME = 2
ELBOW = 18
AXIS = 2
ANGLE = np.float32(np.deg2rad(10.0))
EXPECTED = [18, 20, 22]
GATE = 1e-5
DEVICE = torch.device('cuda:0')

print('=' * 100)
print('STEP 18B1G3 LEGACY SUBPROCESS')
print('=' * 100)
print('Python:', sys.version)
print('NumPy:', np.__version__)
print('Torch:', torch.__version__)
print('Torch CUDA:', torch.version.cuda)
print('CUDA available:', torch.cuda.is_available())
assert torch.cuda.is_available()
print('GPU:', torch.cuda.get_device_name(0))
print('capability:', torch.cuda.get_device_capability(0))
print('allow_tf32 before:', torch.backends.cuda.matmul.allow_tf32)
torch.backends.cuda.matmul.allow_tf32 = False
if hasattr(torch.backends, 'cudnn'):
    torch.backends.cudnn.allow_tf32 = False
print('allow_tf32 after:', torch.backends.cuda.matmul.allow_tf32)
assert torch.__version__.startswith('1.13.1')
assert torch.version.cuda == '11.7'

with open(SMPL_PATH, 'rb') as f:
    smpl = pickle.load(f)

def get(k):
    if k in smpl:
        return smpl[k]
    kb = k.encode()
    if kb in smpl:
        return smpl[kb]
    raise KeyError(k)

vt_np = np.asarray(get('v_template'), dtype=np.float32)
sd_np = np.asarray(get('shapedirs'), dtype=np.float32)[..., :10]
jr_raw = get('J_regressor')
if hasattr(jr_raw, 'toarray'):
    jr_raw = jr_raw.toarray()
jr_np = np.asarray(jr_raw, dtype=np.float32)
parents_np = np.asarray(get('kintree_table'))[0].astype(np.int64).copy()
parents_np[0] = -1

vt = torch.from_numpy(vt_np).to(DEVICE)
sd = torch.from_numpy(sd_np).to(DEVICE)
jr = torch.from_numpy(jr_np).to(DEVICE)
parents = torch.from_numpy(parents_np).to(DEVICE)

@torch.no_grad()
def compute_A(betas_np, global_np, body_np):
    betas = torch.from_numpy(np.asarray(betas_np, dtype=np.float32).reshape(1, -1)[:, :10]).to(DEVICE)
    go = torch.from_numpy(np.asarray(global_np, dtype=np.float32).reshape(1, 3)).to(DEVICE)
    body = torch.from_numpy(np.asarray(body_np, dtype=np.float32).reshape(1, 69)).to(DEVICE)
    full = torch.cat([go, body], dim=1)
    v_shaped = vt.unsqueeze(0) + blend_shapes(betas, sd)
    joints = vertices2joints(jr, v_shaped)
    rot = batch_rodrigues(full.reshape(-1, 3)).reshape(1, 24, 3, 3)
    _, A = batch_rigid_transform(rot, joints, parents, dtype=torch.float32)
    return A[0].contiguous()

@torch.no_grad()
def make_A(pose, perturb=False):
    vit = np.zeros(69, dtype=np.float32)
    vit[2] = 1.0
    vit[5] = -1.0
    A_vit = compute_A(pose['betas'], np.zeros(3, dtype=np.float32), vit)
    inv_A = torch.inverse(A_vit)
    body = pose['body_pose'].copy()
    if perturb:
        b = body.reshape(23, 3)
        b[ELBOW - 1, AXIS] += ANGLE
        body = b.reshape(69)
    A_pose = compute_A(pose['betas'], pose['global_orient'], body)
    return torch.matmul(A_pose, inv_A).contiguous()

@torch.no_grad()
def deform(xyz_np, weights_np, A, scale, transl):
    xyz = torch.from_numpy(np.ascontiguousarray(xyz_np)).to(DEVICE)
    W = torch.from_numpy(np.ascontiguousarray(weights_np)).to(DEVICE).unsqueeze(0)
    G = xyz.shape[0]
    Ab = A.unsqueeze(0)
    T = torch.matmul(W, Ab.view(1, 24, 16)).view(1, G, 4, 4)
    homo = torch.cat([xyz.unsqueeze(0), torch.ones((1, G, 1), dtype=torch.float32, device=DEVICE)], dim=2)
    y = torch.matmul(T, homo.unsqueeze(-1))[0, :, :3, 0]
    scale_t = torch.tensor(float(scale), dtype=torch.float32, device=DEVICE)
    trans_t = torch.from_numpy(np.asarray(transl, dtype=np.float32)).to(DEVICE)
    return y * scale_t + trans_t

def load_npz(path, key):
    with np.load(path, allow_pickle=False) as d:
        return np.asarray(d[key], dtype=np.float32).copy()

def frame_value(arr, frame, width):
    a = np.asarray(arr)
    if a.ndim == 0:
        return a.item()
    if a.ndim == 1 and a.shape[0] == width:
        return a.copy()
    if a.ndim >= 2:
        return a[frame].copy()
    if a.ndim == 1 and a.shape[0] > frame:
        return a[frame].copy()
    return a.copy()

def load_pose(path):
    with np.load(path, allow_pickle=False) as d:
        betas = frame_value(d['betas'], FRAME, 10)
        go = frame_value(d['global_orient'], FRAME, 3)
        body = frame_value(d['body_pose'], FRAME, 69)
        transl = frame_value(d['transl'], FRAME, 3)
        sc = np.asarray(d['scale'])
        if sc.ndim == 0 or sc.size == 1:
            scale = float(sc.reshape(-1)[0])
        else:
            scale = float(np.asarray(sc[FRAME]).reshape(-1)[0])
    return {
        'betas': np.asarray(betas, dtype=np.float32).reshape(-1)[:10],
        'global_orient': np.asarray(go, dtype=np.float32).reshape(3),
        'body_pose': np.asarray(body, dtype=np.float32).reshape(69),
        'transl': np.asarray(transl, dtype=np.float32).reshape(3),
        'scale': np.float32(scale),
    }

def compare(cand, ref, contra):
    cand = np.asarray(cand, dtype=np.float32)
    ref = np.asarray(ref, dtype=np.float32)
    c64 = float(cand[contra].sum(dtype=np.float64))
    r64 = float(ref[contra].sum(dtype=np.float64))
    c32 = float(cand[contra].sum(dtype=np.float32))
    r32 = float(ref[contra].sum(dtype=np.float32))
    diff = np.abs(cand.astype(np.float64) - ref.astype(np.float64))
    err = c64 - r64
    return {
        'candidate_contra_sum64': c64,
        'reference_contra_sum64': r64,
        'contra_error_sum64': float(err),
        'gate_pass_1e5': bool(abs(err) <= GATE),
        'candidate_contra_sum32': c32,
        'reference_contra_sum32': r32,
        'contra_error_sum32': float(c32-r32),
        'mean_abs_diff': float(diff.mean()),
        'p99_abs_diff': float(np.quantile(diff, 0.99)),
        'max_abs_diff': float(diff.max(initial=0.0)),
        'pearson': float(np.corrcoef(cand.astype(np.float64), ref.astype(np.float64))[0,1]),
        'exact_equal': bool(np.array_equal(cand, ref)),
    }

with np.load(B1_PATH, allow_pickle=False) as d:
    archived = {k: np.asarray(d[k]).copy() for k in d.files}
with np.load(MASK_PATH, allow_pickle=False) as d:
    masks = {k: np.asarray(d[k]).copy() for k in d.files}

results = {}
for seq, cfg in SEQ.items():
    print('\n' + '=' * 100)
    print(seq.upper())
    print('=' * 100)
    G = cfg['G']
    learned = load_npz(cfg['learned'], cfg['learned_key'])
    k6 = load_npz(cfg['k6'], cfg['k6_key'])
    xyz = load_npz(cfg['xyz'], cfg['xyz_key'])
    contra = np.asarray(masks[f'{seq}_contralateral'], dtype=bool)
    pose = load_pose(cfg['pose'])
    assert learned.shape == (G,24)
    assert k6.shape == (G,24)
    assert xyz.shape == (G,3)
    assert contra.shape == (G,)
    print('G:', G, 'contra:', int(contra.sum()), 'scale:', float(pose['scale']))

    A0 = make_A(pose, False)
    A1 = make_A(pose, True)
    delta = (A1 - A0).abs().amax(dim=(1,2))
    changed = torch.nonzero(delta > 1e-7, as_tuple=False).reshape(-1).cpu().tolist()
    print('changed transforms:', changed, 'expected:', EXPECTED, 'PASS:', changed == EXPECTED)
    seq_res = {'changed_transforms': changed, 'kinematic_pass': bool(changed == EXPECTED), 'conditions': {}}

    for cond, weights in [('learned', learned), ('k6', k6)]:
        print('\n[' + cond.upper() + ']')
        before = deform(xyz, weights, A0, pose['scale'], pose['transl'])
        after = deform(xyz, weights, A1, pose['scale'], pose['transl'])
        disp_t = torch.norm(after - before, p=2, dim=1)
        native_sum32 = float(disp_t[torch.from_numpy(contra).to(DEVICE)].sum().item())
        disp = disp_t.cpu().numpy().astype(np.float32, copy=False)
        ref = archived[f'{seq}_{cond}_displacement']
        stats = compare(disp, ref, contra)
        stats['native_cuda_float32_contra_sum'] = native_sum32
        print('candidate sum64:', stats['candidate_contra_sum64'])
        print('archive sum64:', stats['reference_contra_sum64'])
        print('error:', stats['contra_error_sum64'])
        print('gate <=1e-5:', stats['gate_pass_1e5'])
        print('candidate native CUDA sum32:', native_sum32)
        print('archive NumPy sum32:', stats['reference_contra_sum32'])
        print('mean abs diff:', stats['mean_abs_diff'])
        print('max abs diff:', stats['max_abs_diff'])
        print('Pearson:', stats['pearson'])
        seq_res['conditions'][cond] = stats
        del before, after, disp_t, disp
        torch.cuda.empty_cache()

    results[seq] = seq_res
    del A0, A1, delta, learned, k6, xyz
    torch.cuda.empty_cache(); gc.collect()

print('\n' + '=' * 100)
print('STEP 18B1G3 SYNTHESIS')
print('=' * 100)
learned_pass = 0
k6_pass = 0
kin_pass = 0
for seq in ['seattle','parkinglot','jogging']:
    r = results[seq]
    L = r['conditions']['learned']
    K = r['conditions']['k6']
    learned_pass += int(L['gate_pass_1e5'])
    k6_pass += int(K['gate_pass_1e5'])
    kin_pass += int(r['kinematic_pass'])
    print(seq, '| learned err =', L['contra_error_sum64'], 'PASS =', L['gate_pass_1e5'], '| k6 err =', K['contra_error_sum64'], 'PASS =', K['gate_pass_1e5'])

total = learned_pass + k6_pass
recovered = bool(total == 6 and kin_pass == 3)
print('learned passes:', f'{learned_pass}/3')
print('K6 passes:', f'{k6_pass}/3')
print('total:', f'{total}/6')
print('kinematics:', f'{kin_pass}/3')
print('LEGACY ENV REGRESSION RECOVERY:', recovered)

payload = {
    'continuation_metadata': '2026-09-16',
    'step': '18B1G3',
    'python': sys.version,
    'numpy': np.__version__,
    'torch': torch.__version__,
    'cuda': torch.version.cuda,
    'gpu': torch.cuda.get_device_name(0),
    'tf32': False,
    'joint': 'left_elbow',
    'frame': 2,
    'frozen_gate': GATE,
    'shoulder_computed': False,
    'tolerance_changed': False,
    'learned_passes': learned_pass,
    'k6_passes': k6_pass,
    'kinematic_passes': kin_pass,
    'total_passes': total,
    'legacy_env_regression_recovery': recovered,
    'results': results,
}
with open(OUT_PATH, 'w') as f:
    json.dump(payload, f, indent=2)
print('\nSAVED:', OUT_PATH)
print('STEP 18B1G3 COMPLETE')

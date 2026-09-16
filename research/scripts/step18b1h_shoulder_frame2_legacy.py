from pathlib import Path
import pickle, json, gc, sys
import numpy as np
import torch
from smplx.lbs import batch_rodrigues, blend_shapes, vertices2joints, batch_rigid_transform

ROOT = Path('/content/drive/MyDrive/interactive-digital-humans')
EXP8 = ROOT / 'experiments/08-second-joint-generalization'
SMPL_PATH = ROOT / 'private_assets/smpl/SMPL_NEUTRAL_clean.pkl'
MASK_PATH = EXP8 / '17A2_frozen_canonical_anatomy_masks.npz'
OUT_JSON = EXP8 / '18B1H_left_shoulder_frame2_cross_checkpoint.json'
OUT_NPZ = EXP8 / '18B1H_left_shoulder_frame2_displacements.npz'

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
SHOULDER = 16
AXIS = 2
ANGLE = np.float32(np.deg2rad(10.0))
BRANCH = [16, 18, 20, 22]
EXPECTED = [16, 18, 20, 22]
DEVICE = torch.device('cuda:0')

THRESH_K6_REDUCTION = 95.0
THRESH_ABLATION_REDUCTION = 99.999
THRESH_ABLATED_MAX = 1e-8
THRESH_ABLATED_SUM = 1e-8
THRESH_CORR = 0.90

print('=' * 100)
print('STEP 18B1H — FROZEN LEFT-SHOULDER FRAME-2 CAUSAL TEST')
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
assert 'T4' in torch.cuda.get_device_name(0).upper()

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
        b[SHOULDER - 1, AXIS] += ANGLE
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

def safe_corr(x, y):
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    if x.size < 2 or np.std(x) == 0.0 or np.std(y) == 0.0:
        return float('nan')
    return float(np.corrcoef(x, y)[0, 1])

with np.load(MASK_PATH, allow_pickle=False) as d:
    masks = {k: np.asarray(d[k]).copy() for k in d.files}

results = {}
raw = {}

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

    assert learned.shape == (G, 24)
    assert k6.shape == (G, 24)
    assert xyz.shape == (G, 3)
    assert contra.shape == (G,)
    assert np.isfinite(learned).all() and np.isfinite(k6).all() and np.isfinite(xyz).all()

    learned_rowsum_err = float(np.max(np.abs(learned.sum(axis=1) - 1.0)))
    k6_rowsum_err = float(np.max(np.abs(k6.sum(axis=1) - 1.0)))

    print('G:', G, 'contra:', int(contra.sum()), 'scale:', float(pose['scale']))
    print('learned row-sum max err:', learned_rowsum_err)
    print('K6 row-sum max err:', k6_rowsum_err)

    A0 = make_A(pose, False)
    A1 = make_A(pose, True)
    delta = (A1 - A0).abs().amax(dim=(1, 2))
    changed = torch.nonzero(delta > 1e-7, as_tuple=False).reshape(-1).cpu().tolist()
    kinematic_pass = bool(changed == EXPECTED)
    print('changed transforms:', changed, 'expected:', EXPECTED, 'PASS:', kinematic_pass)

    # Selective ablation is applied ONLY to the frozen contralateral rows.
    # Remove the predeclared shoulder-descendant branch, then renormalize
    # the remaining weights. Other rows stay identical to learned weights.
    ablated_weights = learned.copy()
    removed_mass_full = learned[:, BRANCH].sum(axis=1).astype(np.float32)
    rows = np.where(contra)[0]
    ablated_weights[np.ix_(rows, BRANCH)] = 0.0
    remaining = ablated_weights[rows].sum(axis=1, keepdims=True)
    assert np.all(remaining > 1e-8), 'Selective ablation produced zero remaining mass in contra rows.'
    ablated_weights[rows] /= remaining

    cond_disp = {}
    for cond, weights in [('learned', learned), ('k6', k6), ('ablated', ablated_weights)]:
        before = deform(xyz, weights, A0, pose['scale'], pose['transl'])
        after = deform(xyz, weights, A1, pose['scale'], pose['transl'])
        disp_t = torch.norm(after - before, p=2, dim=1)
        disp = disp_t.cpu().numpy().astype(np.float32, copy=False)
        cond_disp[cond] = disp.copy()
        del before, after, disp_t, disp
        torch.cuda.empty_cache()

    learned_disp = cond_disp['learned']
    k6_disp = cond_disp['k6']
    ablated_disp = cond_disp['ablated']

    learned_contra = float(learned_disp[contra].sum(dtype=np.float64))
    k6_contra = float(k6_disp[contra].sum(dtype=np.float64))
    ablated_contra = float(ablated_disp[contra].sum(dtype=np.float64))
    ablated_max = float(ablated_disp[contra].max(initial=0.0))

    k6_reduction = float((1.0 - k6_contra / learned_contra) * 100.0)
    ablation_reduction = float((1.0 - ablated_contra / learned_contra) * 100.0)

    removed_mass = removed_mass_full[contra].astype(np.float32, copy=False)
    displacement_reduction = (learned_disp[contra] - ablated_disp[contra]).astype(np.float32, copy=False)
    corr = safe_corr(removed_mass, displacement_reduction)

    pass_k6 = bool(k6_reduction >= THRESH_K6_REDUCTION)
    pass_abl_reduction = bool(ablation_reduction >= THRESH_ABLATION_REDUCTION)
    pass_abl_max = bool(ablated_max <= THRESH_ABLATED_MAX)
    pass_abl_sum = bool(ablated_contra <= THRESH_ABLATED_SUM)
    pass_corr = bool(np.isfinite(corr) and corr >= THRESH_CORR)
    overall_pass = bool(kinematic_pass and pass_k6 and pass_abl_reduction and pass_abl_max and pass_abl_sum and pass_corr)

    print('\nCAUSAL METRICS')
    print('learned contra sum:', learned_contra)
    print('K6 contra sum:', k6_contra)
    print('ablated contra sum:', ablated_contra)
    print('ablated contra max:', ablated_max)
    print('K6 reduction %:', k6_reduction, 'PASS:', pass_k6)
    print('selective-ablation reduction %:', ablation_reduction, 'PASS:', pass_abl_reduction)
    print('ablated max <=1e-8:', pass_abl_max)
    print('ablated sum <=1e-8:', pass_abl_sum)
    print('removed-mass / displacement-reduction corr:', corr, 'PASS:', pass_corr)
    print('OVERALL FRAME-2 PASS:', overall_pass)

    results[seq] = {
        'G': G,
        'contra_count': int(contra.sum()),
        'scale': float(pose['scale']),
        'changed_transforms': changed,
        'expected_changed_transforms': EXPECTED,
        'kinematic_pass': kinematic_pass,
        'learned_rowsum_max_err': learned_rowsum_err,
        'k6_rowsum_max_err': k6_rowsum_err,
        'learned_contra_sum': learned_contra,
        'k6_contra_sum': k6_contra,
        'ablated_contra_sum': ablated_contra,
        'ablated_contra_max': ablated_max,
        'k6_reduction_pct': k6_reduction,
        'selective_ablation_reduction_pct': ablation_reduction,
        'removed_mass_displacement_reduction_corr': corr,
        'passes': {
            'k6_reduction': pass_k6,
            'selective_ablation_reduction': pass_abl_reduction,
            'ablated_max': pass_abl_max,
            'ablated_sum': pass_abl_sum,
            'correlation': pass_corr,
            'overall': overall_pass,
        },
        'removed_mass_stats': {
            'mean': float(removed_mass.mean()),
            'median': float(np.median(removed_mass)),
            'p95': float(np.quantile(removed_mass, 0.95)),
            'max': float(removed_mass.max(initial=0.0)),
        },
    }

    raw[f'{seq}_learned_displacement'] = learned_disp
    raw[f'{seq}_k6_displacement'] = k6_disp
    raw[f'{seq}_ablated_displacement'] = ablated_disp
    raw[f'{seq}_removed_branch_mass'] = removed_mass

    del A0, A1, delta, learned, k6, xyz, ablated_weights, removed_mass_full
    del learned_disp, k6_disp, ablated_disp, removed_mass, displacement_reduction, cond_disp
    torch.cuda.empty_cache(); gc.collect()

all_pass = bool(all(results[s]['passes']['overall'] for s in ['seattle', 'parkinglot', 'jogging']))

print('\n' + '=' * 100)
print('STEP 18B1H SYNTHESIS')
print('=' * 100)
for seq in ['seattle', 'parkinglot', 'jogging']:
    r = results[seq]
    print(seq,
          '| K6 red =', r['k6_reduction_pct'], r['passes']['k6_reduction'],
          '| ablation red =', r['selective_ablation_reduction_pct'], r['passes']['selective_ablation_reduction'],
          '| corr =', r['removed_mass_displacement_reduction_corr'], r['passes']['correlation'],
          '| overall =', r['passes']['overall'])
print('ALL THREE FRAME-2 SHOULDER CELLS PASS:', all_pass)

np.savez_compressed(OUT_NPZ, **raw)

payload = {
    'continuation_metadata': '2026-09-16',
    'step': '18B1H',
    'runtime_policy': 'research/protocols/2026-09-16-step18-runtime-continuation-policy.md',
    'python': sys.version,
    'numpy': np.__version__,
    'torch': torch.__version__,
    'cuda': torch.version.cuda,
    'gpu': torch.cuda.get_device_name(0),
    'tf32': False,
    'frame': FRAME,
    'joint': 'left_shoulder',
    'joint_id': SHOULDER,
    'axis': 'z',
    'angle_deg': 10.0,
    'branch': BRANCH,
    'expected_changed_transforms': EXPECTED,
    'thresholds': {
        'k6_reduction_pct_min': THRESH_K6_REDUCTION,
        'selective_ablation_reduction_pct_min': THRESH_ABLATION_REDUCTION,
        'ablated_contra_max_max': THRESH_ABLATED_MAX,
        'ablated_contra_sum_max': THRESH_ABLATED_SUM,
        'removed_mass_displacement_reduction_corr_min': THRESH_CORR,
    },
    'results': results,
    'all_three_frame2_pass': all_pass,
    'shoulder_computed': True,
    'tolerance_changed': False,
}

with open(OUT_JSON, 'w') as f:
    json.dump(payload, f, indent=2)

print('\nSAVED JSON:', OUT_JSON)
print('SAVED NPZ:', OUT_NPZ)
print('STEP 18B1H COMPLETE')

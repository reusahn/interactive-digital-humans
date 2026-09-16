from pathlib import Path
import pickle, json, gc, sys
import numpy as np
import torch
from smplx.lbs import batch_rodrigues, blend_shapes, vertices2joints, batch_rigid_transform

ROOT = Path('/content/drive/MyDrive/interactive-digital-humans')
EXP8 = ROOT / 'experiments/08-second-joint-generalization'
SMPL_PATH = ROOT / 'private_assets/smpl/SMPL_NEUTRAL_clean.pkl'
MASK_PATH = EXP8 / '17A2_frozen_canonical_anatomy_masks.npz'
FRAME2_JSON = EXP8 / '18B1H_left_shoulder_frame2_cross_checkpoint.json'
OUT_JSON = EXP8 / '18B2_left_shoulder_full_pose_metadata.json'
OUT_NPZ = EXP8 / '18B2_left_shoulder_full_pose_displacements.npz'

SEQ = {
    'seattle': {
        'G': 472958,
        'frames': [2, 7, 12, 17],
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
        'frames': [2, 7, 12, 17],
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
        'frames': [2, 7, 12, 17, 22, 27, 32, 37, 42, 47],
        'learned': ROOT / 'experiments/07-cross-sequence-replication/16D2_jogging_learned_lbs.npz',
        'learned_key': 'learned_lbs',
        'k6': ROOT / 'experiments/07-cross-sequence-replication/16D3_jogging_k6_effective_mapping.npz',
        'k6_key': 'effective_lbs',
        'xyz': ROOT / 'experiments/07-cross-sequence-replication/16D2_jogging_learned_lbs.npz',
        'xyz_key': 'xyz_canon',
        'pose': ROOT / 'datasets/neuman/jogging/4d_humans/smpl_optimized_aligned_scale.npz',
    },
}

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
print('STEP 18B2 — FROZEN LEFT-SHOULDER FULL-POSE FAILURE CHARACTERIZATION')
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
    homo = torch.cat([
        xyz.unsqueeze(0),
        torch.ones((1, G, 1), dtype=torch.float32, device=DEVICE)
    ], dim=2)
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

def load_pose(path, frame):
    with np.load(path, allow_pickle=False) as d:
        betas = frame_value(d['betas'], frame, 10)
        go = frame_value(d['global_orient'], frame, 3)
        body = frame_value(d['body_pose'], frame, 69)
        transl = frame_value(d['transl'], frame, 3)
        sc = np.asarray(d['scale'])
        if sc.ndim == 0 or sc.size == 1:
            scale = float(sc.reshape(-1)[0])
        else:
            scale = float(np.asarray(sc[frame]).reshape(-1)[0])
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

frame2_reference = None
if FRAME2_JSON.exists():
    with open(FRAME2_JSON, 'r') as f:
        frame2_reference = json.load(f)

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

    assert learned.shape == (G, 24)
    assert k6.shape == (G, 24)
    assert xyz.shape == (G, 3)
    assert contra.shape == (G,)
    assert np.isfinite(learned).all() and np.isfinite(k6).all() and np.isfinite(xyz).all()

    learned_rowsum_err = float(np.max(np.abs(learned.sum(axis=1) - 1.0)))
    k6_rowsum_err = float(np.max(np.abs(k6.sum(axis=1) - 1.0)))
    print('G:', G, 'contra:', int(contra.sum()))
    print('learned row-sum max err:', learned_rowsum_err)
    print('K6 row-sum max err:', k6_rowsum_err)

    # Selective ablation is frozen and pose-independent because learned weights and masks are fixed.
    ablated_weights = learned.copy()
    removed_mass_full = learned[:, BRANCH].sum(axis=1).astype(np.float32)
    rows = np.where(contra)[0]
    ablated_weights[np.ix_(rows, BRANCH)] = 0.0
    remaining = ablated_weights[rows].sum(axis=1, keepdims=True)
    assert np.all(remaining > 1e-8)
    ablated_weights[rows] /= remaining
    removed_mass = removed_mass_full[contra].astype(np.float32, copy=False)

    pose_rows = []

    for frame in cfg['frames']:
        pose = load_pose(cfg['pose'], frame)
        A0 = make_A(pose, False)
        A1 = make_A(pose, True)
        delta = (A1 - A0).abs().amax(dim=(1, 2))
        changed = torch.nonzero(delta > 1e-7, as_tuple=False).reshape(-1).cpu().tolist()
        kinematic_pass = bool(changed == EXPECTED)

        cond_disp = {}
        for cond, weights in [('learned', learned), ('k6', k6), ('ablated', ablated_weights)]:
            before = deform(xyz, weights, A0, pose['scale'], pose['transl'])
            after = deform(xyz, weights, A1, pose['scale'], pose['transl'])
            disp_t = torch.norm(after - before, p=2, dim=1)
            disp = disp_t.cpu().numpy().astype(np.float32, copy=False)
            cond_disp[cond] = disp.copy()
            raw[f'{seq}_frame{frame:02d}_{cond}'] = disp.copy()
            del before, after, disp_t, disp
            torch.cuda.empty_cache()

        learned_disp = cond_disp['learned']
        k6_disp = cond_disp['k6']
        ablated_disp = cond_disp['ablated']

        learned_contra = float(learned_disp[contra].sum(dtype=np.float64))
        k6_contra = float(k6_disp[contra].sum(dtype=np.float64))
        ablated_contra = float(ablated_disp[contra].sum(dtype=np.float64))
        ablated_max = float(np.max(ablated_disp[contra])) if np.any(contra) else 0.0

        k6_reduction = float((1.0 - k6_contra / learned_contra) * 100.0)
        ablation_reduction = float((1.0 - ablated_contra / learned_contra) * 100.0)
        displacement_reduction = (learned_disp[contra] - ablated_disp[contra]).astype(np.float32, copy=False)
        corr = safe_corr(removed_mass, displacement_reduction)

        pass_k6 = bool(k6_reduction >= THRESH_K6_REDUCTION)
        pass_abl_reduction = bool(ablation_reduction >= THRESH_ABLATION_REDUCTION)
        pass_abl_max = bool(ablated_max <= THRESH_ABLATED_MAX)
        pass_abl_sum = bool(ablated_contra <= THRESH_ABLATED_SUM)
        pass_corr = bool(np.isfinite(corr) and corr >= THRESH_CORR)
        overall_pass = bool(
            kinematic_pass and pass_k6 and pass_abl_reduction and
            pass_abl_max and pass_abl_sum and pass_corr
        )

        row = {
            'frame': int(frame),
            'scale': float(pose['scale']),
            'changed_transforms': changed,
            'kinematic_pass': kinematic_pass,
            'learned_contra_sum': learned_contra,
            'k6_contra_sum': k6_contra,
            'ablated_contra_sum': ablated_contra,
            'ablated_contra_max': ablated_max,
            'k6_reduction_pct': k6_reduction,
            'selective_ablation_reduction_pct': ablation_reduction,
            'removed_mass_displacement_reduction_corr': corr,
            'pass_k6': pass_k6,
            'pass_selective_ablation_reduction': pass_abl_reduction,
            'pass_ablated_max': pass_abl_max,
            'pass_ablated_sum': pass_abl_sum,
            'pass_corr': pass_corr,
            'overall_pass': overall_pass,
        }
        pose_rows.append(row)

        print(
            f"frame {frame:02d} | changed={changed} | "
            f"learned={learned_contra:.9g} | K6={k6_contra:.9g} | "
            f"K6red={k6_reduction:.6f}% ({pass_k6}) | "
            f"ablred={ablation_reduction:.6f}% ({pass_abl_reduction}) | "
            f"corr={corr:.9f} ({pass_corr}) | overall={overall_pass}"
        )

        if frame == 2 and frame2_reference is not None:
            ref = frame2_reference['results'][seq]
            print(
                '  frame-2 regression deltas:',
                'learned=', learned_contra - float(ref['learned_contra_sum']),
                'k6=', k6_contra - float(ref['k6_contra_sum']),
                'ablated=', ablated_contra - float(ref['ablated_contra_sum']),
                'corr=', corr - float(ref['removed_mass_displacement_reduction_corr']),
            )

        del A0, A1, delta, cond_disp, learned_disp, k6_disp, ablated_disp, displacement_reduction
        torch.cuda.empty_cache()
        gc.collect()

    k6_vals = np.asarray([r['k6_reduction_pct'] for r in pose_rows], dtype=np.float64)
    abl_vals = np.asarray([r['selective_ablation_reduction_pct'] for r in pose_rows], dtype=np.float64)
    corr_vals = np.asarray([r['removed_mass_displacement_reduction_corr'] for r in pose_rows], dtype=np.float64)

    summary = {
        'pose_count': len(pose_rows),
        'kinematic_pass_count': int(sum(r['kinematic_pass'] for r in pose_rows)),
        'k6_pass_count': int(sum(r['pass_k6'] for r in pose_rows)),
        'selective_ablation_pass_count': int(sum(r['pass_selective_ablation_reduction'] for r in pose_rows)),
        'corr_pass_count': int(sum(r['pass_corr'] for r in pose_rows)),
        'overall_pass_count': int(sum(r['overall_pass'] for r in pose_rows)),
        'negative_k6_reduction_count': int(np.sum(k6_vals < 0.0)),
        'k6_reduction_min': float(np.min(k6_vals)),
        'k6_reduction_median': float(np.median(k6_vals)),
        'k6_reduction_max': float(np.max(k6_vals)),
        'selective_ablation_reduction_min': float(np.min(abl_vals)),
        'selective_ablation_reduction_max': float(np.max(abl_vals)),
        'corr_min': float(np.min(corr_vals)),
        'corr_median': float(np.median(corr_vals)),
        'corr_max': float(np.max(corr_vals)),
    }

    print('\nSUMMARY', seq.upper())
    print('poses:', summary['pose_count'])
    print('kinematic passes:', summary['kinematic_pass_count'])
    print('K6 passes:', summary['k6_pass_count'])
    print('selective-ablation passes:', summary['selective_ablation_pass_count'])
    print('corr passes:', summary['corr_pass_count'])
    print('overall passes:', summary['overall_pass_count'])
    print('negative K6 reductions:', summary['negative_k6_reduction_count'])
    print('K6 reduction min/median/max:', summary['k6_reduction_min'], summary['k6_reduction_median'], summary['k6_reduction_max'])
    print('corr min/median/max:', summary['corr_min'], summary['corr_median'], summary['corr_max'])

    results[seq] = {
        'G': G,
        'contra_count': int(contra.sum()),
        'frames': cfg['frames'],
        'learned_rowsum_max_err': learned_rowsum_err,
        'k6_rowsum_max_err': k6_rowsum_err,
        'poses': pose_rows,
        'summary': summary,
    }

    del learned, k6, xyz, ablated_weights, removed_mass_full, removed_mass
    torch.cuda.empty_cache()
    gc.collect()

all_rows = [row for seq in results.values() for row in seq['poses']]
GLOBAL = {
    'nested_pose_count': len(all_rows),
    'kinematic_pass_count': int(sum(r['kinematic_pass'] for r in all_rows)),
    'k6_pass_count': int(sum(r['pass_k6'] for r in all_rows)),
    'selective_ablation_pass_count': int(sum(r['pass_selective_ablation_reduction'] for r in all_rows)),
    'corr_pass_count': int(sum(r['pass_corr'] for r in all_rows)),
    'overall_pass_count': int(sum(r['overall_pass'] for r in all_rows)),
    'negative_k6_reduction_count': int(sum(r['k6_reduction_pct'] < 0.0 for r in all_rows)),
    'global_k6_reduction_min': float(min(r['k6_reduction_pct'] for r in all_rows)),
    'global_k6_reduction_max': float(max(r['k6_reduction_pct'] for r in all_rows)),
    'global_corr_min': float(min(r['removed_mass_displacement_reduction_corr'] for r in all_rows)),
    'global_corr_max': float(max(r['removed_mass_displacement_reduction_corr'] for r in all_rows)),
    'predeclared_third_joint_universal_pass': bool(all(r['overall_pass'] for r in all_rows)),
}

print('\n' + '=' * 100)
print('STEP 18B2 GLOBAL SYNTHESIS')
print('=' * 100)
for k, v in GLOBAL.items():
    print(k + ':', v)
print('NOTE: pose diagnostics are nested within 3 pretrained checkpoints and are not independent model-level replicates.')

payload = {
    'continuation_metadata': '2026-09-16',
    'step': '18B2',
    'status': 'predeclared_shoulder_full_pose_failure_characterization',
    'runtime': {
        'python': sys.version,
        'numpy': np.__version__,
        'torch': torch.__version__,
        'cuda': torch.version.cuda,
        'gpu': torch.cuda.get_device_name(0),
        'tf32': False,
    },
    'protocol': {
        'joint': 'left_shoulder',
        'joint_id': SHOULDER,
        'axis': 'z',
        'angle_deg': 10.0,
        'branch': BRANCH,
        'expected_changed_transforms': EXPECTED,
        'k6_reduction_threshold_pct': THRESH_K6_REDUCTION,
        'selective_ablation_reduction_threshold_pct': THRESH_ABLATION_REDUCTION,
        'ablated_max_threshold': THRESH_ABLATED_MAX,
        'ablated_sum_threshold': THRESH_ABLATED_SUM,
        'correlation_threshold': THRESH_CORR,
        'thresholds_changed_after_frame2': False,
    },
    'interpretation_rule': 'Frame 2 already failed the universal third-joint criterion. Remaining poses characterize robustness/pose dependence and cannot rescue the predeclared universal pass.',
    'results': results,
    'global': GLOBAL,
}

with open(OUT_JSON, 'w') as f:
    json.dump(payload, f, indent=2)
np.savez_compressed(OUT_NPZ, **raw)

print('\nSAVED JSON:', OUT_JSON)
print('SAVED NPZ:', OUT_NPZ)
print('STEP 18B2 COMPLETE')

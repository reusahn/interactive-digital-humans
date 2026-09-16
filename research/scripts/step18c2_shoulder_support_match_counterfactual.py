from pathlib import Path
import pickle, json, sys
import numpy as np
import torch
from smplx.lbs import batch_rodrigues, blend_shapes, vertices2joints, batch_rigid_transform

ROOT = Path('/content/drive/MyDrive/interactive-digital-humans')
EXP8 = ROOT / 'experiments/08-second-joint-generalization'
SMPL_PATH = ROOT / 'private_assets/smpl/SMPL_NEUTRAL_clean.pkl'
MASK_PATH = EXP8 / '17A2_frozen_canonical_anatomy_masks.npz'
DISP_PATH = EXP8 / '18B2_left_shoulder_full_pose_displacements.npz'
OUT_JSON = EXP8 / '18C2_shoulder_support_match_counterfactual.json'
OUT_NPZ = EXP8 / '18C2_shoulder_support_match_counterfactual_displacements.npz'

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
BRANCH = np.array([16, 18, 20, 22], dtype=np.int64)
NONBRANCH = np.array([j for j in range(24) if j not in set(BRANCH.tolist())], dtype=np.int64)
EXPECTED = [16, 18, 20, 22]
EPS = np.float32(1e-12)
DEVICE = torch.device('cuda:0')

print('=' * 100)
print('STEP 18C2 — EXPLORATORY SHOULDER SUPPORT-MATCHING COUNTERFACTUAL')
print('=' * 100)
print('STATUS: EXPLORATORY / POST-HOC')
print('New joint perturbation: False')
print('Confirmatory threshold change: False')
print('Counterfactual: learned within-branch composition + K6 total branch mass')
print('Python:', sys.version)
print('NumPy:', np.__version__)
print('Torch:', torch.__version__)
print('Torch CUDA:', torch.version.cuda)
print('CUDA available:', torch.cuda.is_available())
assert torch.cuda.is_available()
print('GPU:', torch.cuda.get_device_name(0))
print('capability:', torch.cuda.get_device_capability(0))
torch.backends.cuda.matmul.allow_tf32 = False
if hasattr(torch.backends, 'cudnn'):
    torch.backends.cudnn.allow_tf32 = False
print('allow_tf32:', torch.backends.cuda.matmul.allow_tf32)
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
def deform_subset(xyz_np, weights_np, A, scale, transl):
    xyz = torch.from_numpy(np.ascontiguousarray(xyz_np)).to(DEVICE)
    W = torch.from_numpy(np.ascontiguousarray(weights_np)).to(DEVICE).unsqueeze(0)
    n = xyz.shape[0]
    Ab = A.unsqueeze(0)
    T = torch.matmul(W, Ab.view(1, 24, 16)).view(1, n, 4, 4)
    homo = torch.cat([
        xyz.unsqueeze(0),
        torch.ones((1, n, 1), dtype=torch.float32, device=DEVICE)
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
    finite = np.isfinite(x) & np.isfinite(y)
    x = x[finite]
    y = y[finite]
    if x.size < 2 or np.std(x) == 0.0 or np.std(y) == 0.0:
        return float('nan')
    return float(np.corrcoef(x, y)[0, 1])

def gap_metrics(learned, k6, cf):
    learned = np.asarray(learned, dtype=np.float64)
    k6 = np.asarray(k6, dtype=np.float64)
    cf = np.asarray(cf, dtype=np.float64)
    orig_abs = np.abs(learned - k6)
    cf_abs = np.abs(cf - k6)
    orig_mae = float(np.mean(orig_abs))
    cf_mae = float(np.mean(cf_abs))
    if orig_mae > 0.0:
        mae_reduction = float((1.0 - cf_mae / orig_mae) * 100.0)
    else:
        mae_reduction = float('nan')
    orig_rmse = float(np.sqrt(np.mean((learned - k6) ** 2)))
    cf_rmse = float(np.sqrt(np.mean((cf - k6) ** 2)))
    if orig_rmse > 0.0:
        rmse_reduction = float((1.0 - cf_rmse / orig_rmse) * 100.0)
    else:
        rmse_reduction = float('nan')
    fraction_improved = float(np.mean(cf_abs < orig_abs))
    return {
        'original_gap_mae': orig_mae,
        'counterfactual_gap_mae': cf_mae,
        'mae_gap_reduction_pct': mae_reduction,
        'original_gap_rmse': orig_rmse,
        'counterfactual_gap_rmse': cf_rmse,
        'rmse_gap_reduction_pct': rmse_reduction,
        'fraction_gaussians_gap_improved': fraction_improved,
        'counterfactual_vs_k6_pearson': safe_corr(cf, k6),
    }

with np.load(MASK_PATH, allow_pickle=False) as d:
    masks = {k: np.asarray(d[k]).copy() for k in d.files}

disp_archive = np.load(DISP_PATH, allow_pickle=False)
results = {}
raw = {}

for seq, cfg in SEQ.items():
    print('\n' + '=' * 100)
    print(seq.upper())
    print('=' * 100)

    learned = load_npz(cfg['learned'], cfg['learned_key'])
    k6 = load_npz(cfg['k6'], cfg['k6_key'])
    xyz = load_npz(cfg['xyz'], cfg['xyz_key'])
    contra = np.asarray(masks[f'{seq}_contralateral'], dtype=bool)

    assert learned.shape == (cfg['G'], 24)
    assert k6.shape == learned.shape
    assert xyz.shape == (cfg['G'], 3)
    assert contra.shape == (cfg['G'],)

    L = learned[contra].copy()
    K = k6[contra].copy()
    X = xyz[contra].copy()

    mL = L[:, BRANCH].sum(axis=1, dtype=np.float32)
    mK = K[:, BRANCH].sum(axis=1, dtype=np.float32)
    outL = L[:, NONBRANCH].sum(axis=1, dtype=np.float32)
    target_out = (np.float32(1.0) - mK).astype(np.float32, copy=False)

    cf = np.zeros_like(L, dtype=np.float32)

    branch_defined = mL > EPS
    branch_fallback = (~branch_defined) & (mK > EPS)
    branch_both_zero = (~branch_defined) & (mK <= EPS)

    if np.any(branch_defined):
        scale_b = (mK[branch_defined] / mL[branch_defined]).astype(np.float32)
        cf[np.ix_(branch_defined, BRANCH)] = (
            L[np.ix_(branch_defined, BRANCH)] * scale_b[:, None]
        ).astype(np.float32)

    if np.any(branch_fallback):
        # Learned branch composition is undefined because learned branch mass is zero.
        # Use the K6 branch composition only for these explicitly counted fallback rows.
        cf[np.ix_(branch_fallback, BRANCH)] = K[np.ix_(branch_fallback, BRANCH)]

    if np.any(branch_both_zero):
        cf[np.ix_(branch_both_zero, BRANCH)] = 0.0

    out_defined = outL > EPS
    out_fallback = (~out_defined) & (target_out > EPS)
    out_both_zero = (~out_defined) & (target_out <= EPS)

    if np.any(out_defined):
        scale_o = (target_out[out_defined] / outL[out_defined]).astype(np.float32)
        cf[np.ix_(out_defined, NONBRANCH)] = (
            L[np.ix_(out_defined, NONBRANCH)] * scale_o[:, None]
        ).astype(np.float32)

    if np.any(out_fallback):
        # Learned outside-branch composition is undefined. Use K6 composition only here.
        k_out = K[np.ix_(out_fallback, NONBRANCH)].copy()
        k_out_sum = k_out.sum(axis=1, dtype=np.float32)
        assert np.all(k_out_sum > EPS)
        k_out *= (target_out[out_fallback] / k_out_sum)[:, None]
        cf[np.ix_(out_fallback, NONBRANCH)] = k_out.astype(np.float32)

    if np.any(out_both_zero):
        cf[np.ix_(out_both_zero, NONBRANCH)] = 0.0

    row_sum_err = float(np.max(np.abs(cf.sum(axis=1, dtype=np.float32) - 1.0)))
    cf_mass = cf[:, BRANCH].sum(axis=1, dtype=np.float32)
    mass_match_err = float(np.max(np.abs(cf_mass - mK)))
    min_weight = float(np.min(cf))

    pure = ~(branch_fallback | out_fallback)
    pure_count = int(np.sum(pure))

    print('contra rows:', L.shape[0])
    print('branch fallback rows:', int(np.sum(branch_fallback)))
    print('outside fallback rows:', int(np.sum(out_fallback)))
    print('pure learned-composition rows:', pure_count)
    print('pure fraction:', float(pure_count / L.shape[0]))
    print('counterfactual row-sum max error:', row_sum_err)
    print('counterfactual K6 branch-mass match max error:', mass_match_err)
    print('counterfactual minimum weight:', min_weight)

    assert row_sum_err <= 2e-6
    assert mass_match_err <= 2e-6
    assert min_weight >= -1e-7

    pose_rows = []

    for frame in cfg['frames']:
        pose = load_pose(cfg['pose'], frame)
        A0 = make_A(pose, False)
        A1 = make_A(pose, True)
        delta = (A1 - A0).abs().amax(dim=(1, 2))
        changed = torch.nonzero(delta > 1e-7, as_tuple=False).reshape(-1).cpu().tolist()
        assert changed == EXPECTED, (seq, frame, changed)

        before = deform_subset(X, cf, A0, pose['scale'], pose['transl'])
        after = deform_subset(X, cf, A1, pose['scale'], pose['transl'])
        cf_disp_t = torch.norm(after - before, p=2, dim=1)
        cf_disp = cf_disp_t.cpu().numpy().astype(np.float32, copy=False).copy()

        learned_disp = np.asarray(
            disp_archive[f'{seq}_frame{frame:02d}_learned'], dtype=np.float32
        )[contra]
        k6_disp = np.asarray(
            disp_archive[f'{seq}_frame{frame:02d}_k6'], dtype=np.float32
        )[contra]

        full_metrics = gap_metrics(learned_disp, k6_disp, cf_disp)
        pure_metrics = gap_metrics(
            learned_disp[pure], k6_disp[pure], cf_disp[pure]
        ) if pure_count >= 2 else None

        learned_sum = float(learned_disp.sum(dtype=np.float64))
        k6_sum = float(k6_disp.sum(dtype=np.float64))
        cf_sum = float(cf_disp.sum(dtype=np.float64))
        original_sum_gap = abs(learned_sum - k6_sum)
        cf_sum_gap = abs(cf_sum - k6_sum)
        aggregate_gap_reduction = (
            float((1.0 - cf_sum_gap / original_sum_gap) * 100.0)
            if original_sum_gap > 0.0 else float('nan')
        )

        row = {
            'frame': int(frame),
            'changed_transforms': changed,
            'learned_contra_sum': learned_sum,
            'k6_contra_sum': k6_sum,
            'counterfactual_contra_sum': cf_sum,
            'aggregate_sum_gap_reduction_pct': aggregate_gap_reduction,
            'full_field': full_metrics,
            'pure_rows_field': pure_metrics,
        }
        pose_rows.append(row)
        raw[f'{seq}_frame{frame:02d}_learnedcomp_k6mass'] = cf_disp

        print(
            f"frame {frame:02d} | "
            f"L={learned_sum:.9g} K6={k6_sum:.9g} CF={cf_sum:.9g} | "
            f"field MAE gap reduction={full_metrics['mae_gap_reduction_pct']:.6f}% | "
            f"field RMSE gap reduction={full_metrics['rmse_gap_reduction_pct']:.6f}% | "
            f"fraction improved={full_metrics['fraction_gaussians_gap_improved']:.6f} | "
            f"CF-vs-K6 corr={full_metrics['counterfactual_vs_k6_pearson']:.9f} | "
            f"aggregate gap reduction={aggregate_gap_reduction:.6f}%"
        )

        del before, after, cf_disp_t, cf_disp
        torch.cuda.empty_cache()

    mae_reductions = np.asarray(
        [r['full_field']['mae_gap_reduction_pct'] for r in pose_rows], dtype=np.float64
    )
    rmse_reductions = np.asarray(
        [r['full_field']['rmse_gap_reduction_pct'] for r in pose_rows], dtype=np.float64
    )
    frac_improved = np.asarray(
        [r['full_field']['fraction_gaussians_gap_improved'] for r in pose_rows], dtype=np.float64
    )
    cf_corr = np.asarray(
        [r['full_field']['counterfactual_vs_k6_pearson'] for r in pose_rows], dtype=np.float64
    )

    results[seq] = {
        'contra_count': int(L.shape[0]),
        'branch_fallback_count': int(np.sum(branch_fallback)),
        'outside_fallback_count': int(np.sum(out_fallback)),
        'pure_learned_composition_count': pure_count,
        'pure_fraction': float(pure_count / L.shape[0]),
        'counterfactual_rowsum_max_error': row_sum_err,
        'counterfactual_branch_mass_match_max_error': mass_match_err,
        'mae_gap_reduction_min_median_max_pct': [
            float(np.nanmin(mae_reductions)),
            float(np.nanmedian(mae_reductions)),
            float(np.nanmax(mae_reductions)),
        ],
        'rmse_gap_reduction_min_median_max_pct': [
            float(np.nanmin(rmse_reductions)),
            float(np.nanmedian(rmse_reductions)),
            float(np.nanmax(rmse_reductions)),
        ],
        'fraction_gaussians_improved_min_median_max': [
            float(np.nanmin(frac_improved)),
            float(np.nanmedian(frac_improved)),
            float(np.nanmax(frac_improved)),
        ],
        'counterfactual_vs_k6_corr_min_median_max': [
            float(np.nanmin(cf_corr)),
            float(np.nanmedian(cf_corr)),
            float(np.nanmax(cf_corr)),
        ],
        'poses': pose_rows,
    }

    print('\nSUMMARY', seq.upper())
    print('MAE gap reduction min/median/max %:', results[seq]['mae_gap_reduction_min_median_max_pct'])
    print('RMSE gap reduction min/median/max %:', results[seq]['rmse_gap_reduction_min_median_max_pct'])
    print('fraction improved min/median/max:', results[seq]['fraction_gaussians_improved_min_median_max'])
    print('CF-vs-K6 corr min/median/max:', results[seq]['counterfactual_vs_k6_corr_min_median_max'])

payload = {
    'continuation_metadata': '2026-09-16',
    'step': '18C2',
    'analysis_status': 'EXPLORATORY_POST_HOC',
    'new_joint_perturbation': False,
    'confirmatory_thresholds_changed': False,
    'independent_model_level_n': 3,
    'counterfactual_definition': (
        'For each frozen contralateral Gaussian, set total shoulder-descendant branch mass '
        'to the corresponding K6 branch mass while preserving learned within-branch proportions '
        'where defined. Rescale learned non-branch weights proportionally to preserve row sum. '
        'Rows with undefined learned composition are explicitly counted and use K6 composition only as fallback.'
    ),
    'branch': BRANCH.tolist(),
    'results': results,
    'interpretation_guardrail': (
        'This is exploratory and cannot rescue the failed predeclared shoulder generalization. '
        'A large field-gap reduction would support branch-support magnitude as a major explanatory factor. '
        'Residual gap remains attributable to within-branch composition, pose geometry, and scalar-norm effects.'
    ),
}

with open(OUT_JSON, 'w') as f:
    json.dump(payload, f, indent=2)

np.savez_compressed(OUT_NPZ, **raw)

disp_archive.close()

print('\n' + '=' * 100)
print('STEP 18C2 GLOBAL SYNTHESIS')
print('=' * 100)
for seq in SEQ:
    r = results[seq]
    print(
        seq,
        '| pure fraction =', r['pure_fraction'],
        '| MAE gap reduction min/median/max % =', r['mae_gap_reduction_min_median_max_pct'],
        '| CF-vs-K6 corr min/median/max =', r['counterfactual_vs_k6_corr_min_median_max'],
    )
print('IMPORTANT: exploratory/post-hoc, checkpoint n=3, poses are nested diagnostics.')
print('SAVED JSON:', OUT_JSON)
print('SAVED NPZ:', OUT_NPZ)
print('STEP 18C2 COMPLETE')

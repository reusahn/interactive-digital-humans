# State of the Field — Interactive Digital Humans, 2026

_Last updated: September 2026_

## Scope

This review tracks the convergence of four research areas:

1. real-time 3D/4D human representation,
2. controllable human generation,
3. embodied and conversational behavior,
4. physically and socially grounded interaction.

The goal is not to treat Gaussian Splatting as the research identity. Gaussian representations are one current mechanism inside a larger question: **how can a digital human remain visually coherent, controllable, temporally stable, and responsive while interacting with people and environments in real time?**

## 1. What is becoming solved

### Real-time rendering alone is no longer a sufficient research contribution

Recent avatar systems already operate at interactive or real-time rates. GauHuman reported up to 189 FPS for articulated Gaussian humans (CVPR 2024). HUGS reported 60 FPS while reconstructing an animatable human and scene from a short monocular video. GASP reported 70 FPS for 360-degree animatable avatars reconstructed from limited input. PoseGaussian reported 100 FPS in 2026.

Implication: a project whose only claim is "a Gaussian human that renders in real time" is unlikely to remain a strong research contribution.

Sources:
- GauHuman, CVPR 2024: https://openaccess.thecvf.com/content/CVPR2024/html/Hu_GauHuman_Articulated_Gaussian_Splatting_from_Monocular_Human_Videos_CVPR_2024_paper.html
- HUGS, CVPR 2024: https://openaccess.thecvf.com/content/CVPR2024/html/Kocabas_HUGS_Human_Gaussian_Splats_CVPR_2024_paper.html
- GASP, CVPR 2025: https://openaccess.thecvf.com/content/CVPR2025/html/Saunders_GASP_Gaussian_Avatars_with_Synthetic_Priors_CVPR_2025_paper.html
- PoseGaussian, WACV 2026: https://openaccess.thecvf.com/content/WACV2026/html/Shen_PoseGaussian_Pose-Driven_Novel_View_Synthesis_for_Robust_3D_Human_Reconstruction_WACV_2026_paper.html

### Single-view and monocular avatar creation is rapidly improving

GaussianAvatar established realistic animatable avatars from a single video. AniGS and IDOL push toward single-image, generalizable reconstruction. Vid2Avatar-Pro uses a learned universal prior to improve novel-view and novel-pose generalization from in-the-wild monocular video. GeoDiff4D uses geometry-aware diffusion to improve single-image 4D head reconstruction.

Implication: capture convenience is still important, but "single image to avatar" is already a crowded direction. A new project needs a more specific failure mode or interaction requirement.

Sources:
- GaussianAvatar, CVPR 2024: https://openaccess.thecvf.com/content/CVPR2024/html/Hu_GaussianAvatar_Towards_Realistic_Human_Avatar_Modeling_from_a_Single_Video_CVPR_2024_paper.html
- AniGS, CVPR 2025: https://openaccess.thecvf.com/content/CVPR2025/html/Qiu_AniGS_Animatable_Gaussian_Avatar_from_a_Single_Image_with_Inconsistent_CVPR_2025_paper.html
- IDOL, CVPR 2025: https://openaccess.thecvf.com/content/CVPR2025/html/Zhuang_IDOL_Instant_Photorealistic_3D_Human_Creation_from_a_Single_Image_CVPR_2025_paper.html
- Vid2Avatar-Pro, CVPR 2025: https://openaccess.thecvf.com/content/CVPR2025/html/Guo_Vid2Avatar-Pro_Authentic_Avatar_from_Videos_in_the_Wild_via_Universal_CVPR_2025_paper.html
- GeoDiff4D, CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Xu_GeoDiff4D_Geometry-Aware_Diffusion_for_4D_Head_Avatar_Reconstruction_CVPR_2026_paper.html

## 2. Where the field is moving

### A. Representation is becoming structured and controllable

The field is moving away from treating the human as an unstructured cloud of appearance primitives. Recent work adds body anchoring, layers, topology, low-dimensional control spaces, and hybrid mesh/Gaussian structure.

DAMA explicitly separates clothing layers and anchors Gaussians to SMPL-X while enforcing physically plausible garment ordering. LUCAS separates face and hair in a layered universal codec-avatar representation. Gaussian Eigen Models distill expensive avatar models into efficient low-dimensional linear Gaussian bases. PiG-Avatar decouples representation geometry from the body-template topology while retaining kinematic transport.

Working interpretation: **the important question is increasingly not just how to render humans, but how to expose structure that downstream systems can control and interact with.**

Sources:
- DAMA, CVPR Workshops 2026: https://openaccess.thecvf.com/content/CVPR2026W/PhysHuman/html/Eskandar_DAMA_Disentangled_Body-Anchored_Gaussians_for_Controllable_Multi-Layered_Avatars_CVPRW_2026_paper.html
- LUCAS, CVPR 2025: https://openaccess.thecvf.com/content/CVPR2025/html/Liu_LUCAS_Layered_Universal_Codec_Avatars_CVPR_2025_paper.html
- Gaussian Eigen Models, CVPR 2025: https://openaccess.thecvf.com/content/CVPR2025/html/Zielonka_Gaussian_Eigen_Models_for_Human_Heads_CVPR_2025_paper.html
- PiG-Avatar, 2026: https://arxiv.org/abs/2605.20185

### B. Rendering and behavior generation are converging

StreamAvatar demonstrates real-time streaming avatar generation with natural talking and listening behavior. Avatar Forcing responds causally to user audio and motion. AudioAvatar directly drives a particle/Gaussian whole-body avatar from audio without an intermediate parametric pose bottleneck. NVIDIA's ARDY generates long-horizon interactive motion with online text and kinematic constraints.

Implication: the old pipeline "generate pose first, render avatar second" is being challenged by systems that jointly optimize appearance, dynamics, and conditioning.

Sources:
- StreamAvatar, CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Sun_StreamAvatar_Streaming_Diffusion_Models_for_Real-Time_Interactive_Human_Avatars_CVPR_2026_paper.html
- Avatar Forcing, CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.html
- AudioAvatar, CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_AudioAvatar_Personalized_Audio-driven_Whole-body_Talking_Avatars_CVPR_2026_paper.html
- ARDY, SIGGRAPH 2026: https://research.nvidia.com/labs/sil/projects/ardy/

### C. Social interaction is becoming a first-class modeling target

Meta's Seamless Interaction models dyadic conversation rather than isolated speaking animation. The dataset contains more than 4,000 hours of face-to-face interactions, and the models use speech and visual behavior from both parties to generate gestures, facial responses, listening behavior, turn-taking cues, and visual synchrony.

NVIDIA's Interactive Physical AI framing similarly defines interaction as a loop of perception, communication, and action, and explicitly includes environment-aware avatars as an embodiment of physical AI.

Implication: **an interactive human should be conditioned on the other participant and the shared world, not only on its own speech or target motion.**

Sources:
- Seamless Interaction: https://ai.meta.com/research/seamless-interaction/
- Meta technical overview: https://ai.meta.com/blog/seamless-interaction-natural-conversational-dynamics/
- NVIDIA Interactive Physical AI Workshop 2026: https://research.nvidia.com/labs/amri/projects/IPA/2026/

### D. Physical interaction remains difficult

InteractAvatar models hand-face contact and the local deformations/shadows caused by that interaction. DAMA focuses on physically plausible clothing layers. PhyGenHOI couples generative motion with explicit physical simulation for 4D human-object interaction. Dexterous World Models addresses interaction in digital twins because reconstructed environments are still largely static and non-interactive.

These works suggest that **contact, local deformation, scene response, and physical plausibility remain less mature than free-space animation and view synthesis.**

Sources:
- InteractAvatar, ICCV 2025: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_InteractAvatar_Modeling_Hand-Face_Interaction_in_Photorealistic_Avatars_with_Deformable_Gaussians_ICCV_2025_paper.html
- PhyGenHOI, 2026: https://arxiv.org/abs/2605.30268
- Dexterous World Models, CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html

## 3. Working research gap

This is a **working gap, not yet a claim of novelty**. It must be tested against a broader systematic literature review before publication.

Current avatar research tends to optimize one or two of the following very well:

- visual fidelity,
- real-time rendering,
- animatability,
- generative behavior,
- conversational response,
- physical interaction.

Fewer systems appear to make the **underlying 3D/4D human representation itself interaction-ready**: semantically structured, locally deformable, identity-preserving, physically aware, and directly conditionable by another human and the environment at interactive rates.

### Candidate gap statement

> Existing real-time avatar representations are highly effective at view synthesis and animation, while interactive behavior models are increasingly effective at generating reactions. However, the representation and interaction layers are still often optimized separately. This creates a gap for 4D human representations whose internal structure is explicitly designed for real-time social and physical interaction.

## 4. Research direction

### Interactive 4D Human Representation

We will investigate a human representation with four properties:

1. **Identity persistence** — appearance and person-specific geometry remain stable across time and novel actions.
2. **Semantic controllability** — face, gaze, hands, body, clothing, and contact regions can be addressed explicitly.
3. **Local interaction response** — contact or social signals can drive localized deformation/appearance changes instead of requiring full-scene regeneration.
4. **Real-time operation** — the representation remains usable inside an interactive engine rather than only for offline rendering.

The initial implementation can use Gaussian primitives plus an articulated body prior because that is currently practical and well-supported. The research question is representation-agnostic and should survive a future shift toward mesh, hybrid, or learned 4D representations.

## 5. Evaluation dimensions

A future benchmark should not be limited to PSNR/SSIM/LPIPS. For interactive humans we should evaluate:

### Visual
- PSNR
- SSIM
- LPIPS
- identity similarity

### Temporal
- temporal consistency
- flicker / drift
- long-horizon identity preservation

### Control
- pose fidelity
- gaze target error
- hand/contact target error
- local edit leakage

### Interaction
- response latency
- contact penetration / separation error
- reaction appropriateness
- synchronization with the partner

### Systems
- FPS
- end-to-end latency
- VRAM
- model size
- update bandwidth

## 6. Current conclusion

The long-term research identity should be **Interactive Digital Humans / 4D Human Intelligence**, not "Gaussian Splatting research."

The first technical program should begin with a reproducible Gaussian-human baseline, then test whether the representation can be augmented with semantic interaction anchors and local response mechanisms without sacrificing identity, temporal stability, or real-time performance.

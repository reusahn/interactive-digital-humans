# Core Reading List — Interactive Digital Humans

This list is ordered as a research path rather than a historical bibliography.

## Stage 1 — Understand Gaussian human representations

### 1. GaussianAvatar — CVPR 2024
**Why read:** canonical-space animatable Gaussians, monocular avatar reconstruction, motion-conditioned appearance.

Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Hu_GaussianAvatar_Towards_Realistic_Human_Avatar_Modeling_from_a_Single_Video_CVPR_2024_paper.html

Code: https://github.com/aipixel/GaussianAvatar

Questions while reading:
- What is canonical vs posed space?
- Which Gaussian properties are static and which are pose-dependent?
- Where does SMPL constrain the representation?
- What breaks under unseen motion?

### 2. HUGS: Human Gaussian Splats — CVPR 2024
**Why read:** human + scene decomposition, learned skinning weights, short monocular sequence, accessible official implementation.

Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Kocabas_HUGS_Human_Gaussian_Splats_CVPR_2024_paper.html

Code: https://github.com/apple/ml-hugs

Questions:
- How are human and background separated?
- How are Gaussians associated with the body?
- How does learned skinning improve animation?
- Which parts of the representation could carry semantic labels?

### 3. GauHuman — CVPR 2024
**Why read:** strong efficiency baseline and evidence that rendering speed alone is already highly optimized.

Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Hu_GauHuman_Articulated_Gaussian_Splatting_from_Monocular_Human_Videos_CVPR_2024_paper.html

## Stage 2 — Understand the shift toward structure and control

### 4. Real-time High-fidelity Gaussian Human Avatars — CVPR 2025
**Why read:** pose-dependent appearance with spatially distributed MLPs and surface-constrained Gaussians.

Paper: https://openaccess.thecvf.com/content/CVPR2025/html/Zhan_Real-time_High-fidelity_Gaussian_Human_Avatars_with_Position-based_Interpolation_of_Spatially_CVPR_2025_paper.html

### 5. Vid2Avatar-Pro — CVPR 2025
**Why read:** universal human prior, generalization under limited monocular observations, novel-pose problem.

Paper: https://openaccess.thecvf.com/content/CVPR2025/html/Guo_Vid2Avatar-Pro_Authentic_Avatar_from_Videos_in_the_Wild_via_Universal_CVPR_2025_paper.html

### 6. LUCAS — CVPR 2025
**Why read:** layered representations and disentanglement of face/hair; important example of representation structure serving control and deployment.

Paper: https://openaccess.thecvf.com/content/CVPR2025/html/Liu_LUCAS_Layered_Universal_Codec_Avatars_CVPR_2025_paper.html

### 7. DAMA — CVPR Workshops 2026
**Why read:** explicit garment separation, body anchoring, physical plausibility, layer control, mesh conversion.

Paper: https://openaccess.thecvf.com/content/CVPR2026W/PhysHuman/html/Eskandar_DAMA_Disentangled_Body-Anchored_Gaussians_for_Controllable_Multi-Layered_Avatars_CVPRW_2026_paper.html

Code: https://github.com/danieleskandar/DAMA-code

Questions:
- What does body anchoring make easier?
- Which freedoms are lost by anchoring to SMPL-X?
- Can its semantic structure be generalized from garments to interaction regions?

## Stage 3 — Understand interaction-specific failure modes

### 8. InteractAvatar — ICCV 2025
**Why read:** direct evidence that ordinary avatar models do not adequately model contact-induced local deformation and appearance changes.

Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_InteractAvatar_Modeling_Hand-Face_Interaction_in_Photorealistic_Avatars_with_Deformable_Gaussians_ICCV_2025_paper.html

Questions:
- How is contact represented?
- Which deformation is local vs global?
- What additional representation is needed for hands?
- How are shadows and wrinkles handled?

### 9. PhyGenHOI — 2026
**Why read:** 4D human-object interaction using motion generation plus explicit physical simulation.

Paper: https://arxiv.org/abs/2605.30268

### 10. Dexterous World Models — CVPR 2026
**Why read:** shows the parallel problem on the environment side: realistic digital twins remain difficult to interact with.

Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html

## Stage 4 — Understand behavior and social intelligence

### 11. Seamless Interaction — Meta FAIR, 2025
**Why read:** large-scale dyadic modeling of speaking, listening, turn-taking, gaze-related visual synchrony, facial expression, and whole-body gesture.

Project: https://ai.meta.com/research/seamless-interaction/

Overview: https://ai.meta.com/blog/seamless-interaction-natural-conversational-dynamics/

Questions:
- Which signals from the partner condition behavior?
- What behavior representation is generated?
- Where does behavior generation stop and rendering begin?
- How could a 3D human representation expose control interfaces for this model?

### 12. Avatar Forcing — CVPR 2026
**Why read:** causal low-latency response to live audio and motion, with explicit focus on natural interaction.

Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.html

### 13. StreamAvatar — CVPR 2026
**Why read:** streaming diffusion, full-body gestures, talking/listening behavior, long-term consistency.

Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Sun_StreamAvatar_Streaming_Diffusion_Models_for_Real-Time_Interactive_Human_Avatars_CVPR_2026_paper.html

### 14. AudioAvatar — CVPR 2026
**Why read:** important challenge to modular pose-then-render pipelines; directly drives Gaussian dynamics from audio.

Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Lee_AudioAvatar_Personalized_Audio-driven_Whole-body_Talking_Avatars_CVPR_2026_paper.html

### 15. ARDY — SIGGRAPH 2026
**Why read:** real-time interactive long-horizon motion generation with text and kinematic constraints.

Project: https://research.nvidia.com/labs/sil/projects/ardy/

## Stage 5 — Read the field as a system problem

### 16. NVIDIA Interactive Physical AI Workshop — CVPR 2026
**Why read:** useful framing: perceive humans/scenes, generate communication, and act under constraints. It explicitly includes environment-aware avatars.

Page: https://research.nvidia.com/labs/amri/projects/IPA/2026/

## Reading protocol

For every paper, record five things:

1. **Representation** — mesh, Gaussians, neural field, video latent, hybrid.
2. **Control input** — pose, audio, text, partner motion, contact, object state.
3. **Output** — render, geometry, motion, behavior, physical state.
4. **Real-time boundary** — which part actually runs interactively?
5. **Failure mode** — what does the paper explicitly say previous methods cannot do?

The fifth item is the most important. Research questions should be built from recurring failure modes, not from technology names.

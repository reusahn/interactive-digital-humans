# Interactive Digital Humans

**4D Human Intelligence Research**

Research on real-time 4D human representation, generation, control, and embodied interaction.

## Core research question

> How can AI-driven digital humans be represented, generated, and embodied in real time for natural interaction with humans and virtual environments?

## Research pillars

### 01 · Represent
Real-time 4D representations that preserve identity, appearance, geometry, and motion as coherent, controllable human signals.

Current technical interests include Gaussian avatars, neural fields, parametric humans, and hybrid explicit/neural representations.

### 02 · Generate
Generative systems for human motion, appearance, expression, gaze, and behavior that remain controllable across time.

Current technical interests include motion generation, neural rendering, behavior synthesis, and multimodal conditioning.

### 03 · Interact
Embodied digital humans that perceive people and environments, reason about context, and respond through coordinated action.

Current technical interests include embodied agents, social intelligence, multimodal perception, and real-time control.

## Research framework

**Perceive → Understand → Generate → Act**

The long-term goal is to close the loop between perception and action while maintaining identity, physical plausibility, temporal continuity, and social context.

## Current research program

The repository now starts from an explicit 2026 literature review and a falsifiable first experiment rather than from a technology-specific claim.

- [State of the Field — Interactive Digital Humans, 2026](research/state-of-field-2026.md)
- [Project 001 — Interaction-Ready 4D Human Representation](research/project-001-interaction-ready-human.md)
- [Core Reading List](literature/reading-list.md)
- [Experiment 01 — Gaussian Human Baseline + Locality Probe](experiments/01-baseline/README.md)

### Working research gap

Current real-time avatar representations are increasingly strong at reconstruction, rendering, and animation, while behavior models are increasingly strong at generating conversational and interactive responses. The working hypothesis is that the **representation layer itself is still insufficiently designed for interaction**: semantic control, local physical response, identity persistence, and low-latency coupling to another human or environment.

This is a research hypothesis, not yet a novelty claim. The first experiments are explicitly designed to test and potentially reject it.

## First project

**Interaction-Ready 4D Humans: Semantically Anchored Real-Time Avatars for Social and Physical Response**

First question:

> Can a real-time 4D human representation expose semantically meaningful, locally controllable interaction regions while preserving identity, temporal coherence, and rendering quality?

The first technical step is to reproduce an established Gaussian-human baseline and measure whether a targeted local change remains local across poses.

## Website

The repository includes a research-site interface. Performance numbers shown in early design mockups were intentionally removed because they were not experimental results. The current interface presents research directions rather than unverified benchmarks.

## Run locally

```bash
npm install
npm run dev
```

Build for production:

```bash
npm run build
```

Lint:

```bash
npm run lint
```

## Current status

Research scoping + baseline reproduction stage, 2026.

---

Jonghoon Ahn

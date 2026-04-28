# Legion Systems SE

**Independent research in emergent field dynamics and resonant architectures.**

> *Mattias Hammarsten — overwatch@legionsystems.se*  
> *Swedish R&D*

---

## Critical Fold

**[`critical-fold`](https://github.com/Legion-Systems-SE/critical-fold)** — our primary research engine.

A dual-channel coupled PDE system seeded by the Riemann zeta function ζ(s) on a 3D cubic grid. Two scalar fields evolve through wave propagation, Laplacian diffusion, and conservative energy exchange across a dynamic membrane. Zero imposed constants — the field's own curvature spectrum derives all rates, scales, and timing.

### What we found

**The fold requires the critical line.** A sweep across σ (the real part of s = σ + it) shows sustained dynamics exclusively at σ = 1/2. Off the critical line, the field either superheats to dead equilibrium (σ = 1.1) or goes inert (σ ≥ 5). The transition is continuous — curvature ratio drops from 0.72 at σ = 1/2 to 0.28 at σ = 11, natural frequency collapses by four orders of magnitude.

**550 laps of invariance.** The engine was rolled continuously along the critical line from t = 0 to t = 5,910 across 550 independent runs. Curvature ratio: 0.741 ± 0.112. Characteristic length: 1.387 ± 0.256. Fold survival: 100%.

**Time signature spectrum.** Beat modulation at 5/4 converges in 39 periods (vs 88 at 4/4). At 7/8 it takes 130 — the engine's internal prime lock is k = 7, creating resonant interference. The architecture responds to musical structure.

### How it was built

This engine was developed through sustained human–AI collaboration — Mattias Hammarsten and Claude (Anthropic, Opus 4.6) working as co-developers through iterative hypothesis, implementation, measurement, and revision. Every line of mathematics used predates this project. Nothing was invented — structures were found.

The [original architecture document](https://github.com/Legion-Systems-SE/.github) describes the theoretical framework: a 4D latent folded into 3D as two coupled channels with curvature-driven exchange, beat entrainment, and self-regulating convergence. The engine validates the core predictions — the dual channels maintain productive asymmetry, the membrane forms at the curvature zero-crossing, and the system self-regulates through field-derived timing.

---

## Getting Started

```bash
git clone git@github.com:Legion-Systems-SE/critical-fold.git
cd critical-fold
pip install torch mpmath numpy

# Run the engine — field determines everything
python manifold_sim/engine_emergent.py --bifurcation zeta --auto

# Roll along the critical line
python manifold_sim/roll.py 100
```

See the [critical-fold README](https://github.com/Legion-Systems-SE/critical-fold#readme) for full documentation.

---

*Active research. Results are measurements, not claims. The engine is a tool — what it reveals belongs to the mathematics.*

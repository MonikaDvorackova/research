---
id: pub-03-c4-minimal-environment
title: "C4 minimal environment (specified; not authorized)"
type: research-notes
status: specified-not-run
created: 2026-08-02
updated: 2026-08-02
---

# C4 minimal environment

Specified only for audit completeness. **Not authorized** under go/no-go (**ABANDON**).

## Latent state

\(s=(u,v,w)\) with histories \(H\) containing all factors.

| Task | Requires |
|---|---|
| \(\mathcal{T}_1\) | subset (e.g. \(u\) only, or \(u,v\)) |
| \(\mathcal{T}_2\) | overlapping / orthogonal factors (vary overlap) |

## Components

- Learned bottleneck encoder \(g_\theta\) with fixed dim \(k\)
- Raw-history oracle \(h_2^\star(H)\)
- Retrained decoder \(d_2^\star(Z)\) after shift (adequate labels; **no** \(H\))
- Baselines: task-agnostic / multi-task consolidation; capacity-matched random projection; \(\mathcal{T}_1\)-only IB

## Factors

Capacity \(k\); SS overlap; shift timing; one-shot vs repeated consolidation; raw replay on/off; future-task uncertainty.

## Essential controls (would be required if run)

1. Encoder loss — \(d_2^\star\) still fails  
2. Decoder mismatch — retraining solves it  
3. Capacity insufficiency — all objectives fail equally  
4. Objective-induced selective loss — capacity enough; \(\mathcal{T}_1\) training discards \(\mathcal{T}_2\) factors  
5. Ordinary catastrophic forgetting — encoder params changed after \(\mathcal{T}_2\) begins  
6. Irreversible consolidation — \(H\) unavailable before \(\mathcal{T}_2\) adaptation  

## Why not run

Even a clean demonstration of (4)+(6) would instantiate **standard SS / state-abstraction theory** and the obvious statement that task-specific compression loses unused information — failing the hostile novelty bar and collapsing toward closed S4.

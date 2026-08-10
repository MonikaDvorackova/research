---
id: pub-03-c1-minimal-mdp
title: "C1 minimal MDP (specified; not implemented)"
type: research-notes
status: specified-not-run
created: 2026-08-01
updated: 2026-08-01
---

# C1 minimal synthetic memory MDP

Specified for completeness of the audit. **Not authorized for implementation** under the go/no-go (C1 abandoned as Pub-03 object).

## Design goals

Isolate observational write-value estimation vs interventional oracle, with capacity interference and delayed utility — exact computation of oracle counterfactual write values.

## Entities

- Capacity \(K\in\{1,2,4\}\)
- Candidate stream \(X_t\in\{\text{critical},\text{distractor},\text{noise}\}\)
- Write \(W_t\in\{0,1\}\); on write with full store, evict by fixed rule (FIFO or learned; pilot uses FIFO)
- Delay horizon \(H\in\{1,4,8\}\): query arrives \(H\) steps after critical item appears
- Query needs the critical item in \(M\); reward \(R\in\{0,1\}\)
- Distractors: correlate with short-horizon spurious features under \(\mu\)
- Behavior \(\mu_\varepsilon\): Bernoulli(\(\varepsilon\)) exploration write, or class-conditional logging with known propensity
- Hidden vs observed context: latent query schedule \(U\) in \(H_t\) or not

## Oracle interventional values

For each history \(H_t\) (or stratified state), estimate
\(V^{\mathrm{write}}\) by paired interventions: clone state, force \(W_t=1\) and \(W_t=0\), roll forward with frozen future write regime \(\nu\) (to make unit value well-defined under capacity), average \(R\).

## Estimators (no LLM)

| # | Estimator | Expected bias | Expected variance |
|---|---|---|---|
| 1 | Naive return attribution \(\mathbb{E}[R\mid W,H]\) contrast | High under confounding / interference; can **sign-flip** | Moderate |
| 2 | Observational Q / regression of \(R\) on \((H,W)\) | Biased if ignorability fails; smoother | Lower than naive if well-specified |
| 3 | IPS / doubly robust using known \(\mu\) | Unbiased under positivity+ignorability+consistency; **still wrong under interference** if unit potential outcomes ill-defined | High when \(\mu\) near 0/1 or \(H\) large |
| 4 | Local interventional (Memory-R2-style): resample \(W_t\) from shared \(M_{t-1}\) | Low for session/write contrast under fixed future regime | Cost × rerolls |
| 5 | Oracle CF value | Zero (definition) | Monte Carlo only |

## Dependent variables

**Primary:** \(\rho\) with oracle \(V^{\mathrm{write}}\); sign accuracy; absolute bias; delayed-critical retention rate; task return.  
**Secondary:** variance; regret; sensitivity to \(H\), \(K\), positivity \(\varepsilon\).

## Factors to vary

\(H\in\{1,4,8\}\); \(\varepsilon\) (positivity); \(K\); hidden vs observed \(U\); write-policy determinism.

## Relation to TCM / Memory-R2

This MDP is **in the same experimental neighborhood** as TCM’s synthetic delayed-query store and Memory-R2’s shared-state rerolls. Running it would largely **confirm known motivational claims**, not establish a new Pub-03 object.

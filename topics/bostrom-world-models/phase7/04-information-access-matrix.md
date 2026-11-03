---
id: topic-bostrom-world-models-phase7-info-matrix
title: "Information-access matrix for policies P0–P5"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [audit, fairness, X1]
---

# Information-access matrix (read from `src/eid/x1.py`; written before outcomes were analysed)

| | P0 | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| Rule | uniform over actions {0,1} | action 2 w.p. 0.02, else uniform {0,1} | uniform over {0,1,2} | argmax mutual information between member identity in **M** and next observation | argmax Jensen–Shannon divergence between posterior-predictives of **M** and of **W** | argmax mutual information between member identity in **M ∪ W** and next observation |
| Hypothesis classes used for the *action choice* | none | none | none | M (4) | M (4) and W (42) | M ∪ W (46) |
| Access to alternative mechanisms (W) in the action rule | no | no | no | **no** | **yes** | **yes** |
| Oracle likelihoods | not used | not used | not used | exact member likelihoods (exact filtering) | same | same |
| Observations / actions | own past only | own past only | own past only | own past only | own past only | own past only |
| Intervention options | {0,1} | {0,1,2} | {0,1,2} | {0,1,2} | {0,1,2} | {0,1,2} |
| Budget | N = 3000 episodes × 4 steps (same for all) | same | same | same | same | same |
| Objective | – (negative control) | – | – | identify member of M | separate class M from W | identify member of M ∪ W |
| **Test statistic and stopping rule (identical for all policies)** | E_t with mixture alternative over M ∪ W; reject at first E_t ≥ 20 (α = 0.05) after any observation; stop on rejection | same | same | same | same | same |
| Compute per step | O(1) | O(1) | O(1) | O(K·A·S²), K = 4 | O(K·A·S²), K = 46 | O(K·A·S²), K = 46 |

Notes.
- **The test statistic itself uses W for every policy** (the mixture alternative). So *detection* always has access to W; only the *action choice* differs. This is by design (power requires an alternative) and is stated as a limitation.
- Differences between policies decompose as: **information** (P3 vs P4/P5: W in the action rule), **objective** (P4 vs P5: same information, different target variable: class indicator vs member identity), **compute** (P3 cheaper than P4/P5 by a factor ≈ K_total/K_M ≈ 11; P2 cheapest; P4 and P5 equal in complexity). The fair comparison for the *objective* is P4 vs P5 only (preregistered H4c). The comparison P4 vs P2 (H4a/H4b) mixes information and objective; P2 vs P3 (H5) concerns whether M-only EIG is a good detector.
- No policy sees the truth, the hidden state, or the confirmatory outcome. Truth access is through `Sampler.act` only (source-inspection test).
- Positive controls pc0–pc2 are **members of W**: the action rule of P4/P5 and the alternative mixture contain the truth. Results on pc truths describe *anticipated* inadequacy.

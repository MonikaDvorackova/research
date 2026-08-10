---
id: pub-03-c1-closest-work-matrix
title: "C1 closest-work matrix (methods-level)"
type: research-notes
status: audit-complete
created: 2026-08-01
updated: 2026-08-01
---

# C1 closest-work matrix

Inspected **methods, objectives, theory/appendices, ablations** — not abstracts alone.  
Sources: Memory-R2 (arXiv:2605.21768), Mem-T (arXiv:2601.23014), HiMPO (arXiv:2606.16285), MemQ (arXiv:2605.08374), Memory-R1 (ACL 2026 / arXiv:2508.19828), TCM (Zenodo 20615557, 2026-06-09), plus related MemCon/MemPO/MemRL where relevant.

Legend for C1 overlap: **A**=statistical identifiability of \(V^{\mathrm{write}}\); **B**=finite-sample estimation; **C**=retention-policy consequence.

| Work | State / action | Write action | Reward timing | Credit method | Interventions / CF rollouts? | Assumes observational traj sufficient? | Identifiability discussed/proved? | Estimator bias characterized? | Delay \(H\) varied? | Retention consequence of biased values measured? | Exact overlap with C1 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Memory-R2** | Multi-session; shared LLM extractor+manager; ops INSERT/UPDATE/DELETE over chunked dialogue | Yes (manager ops on bank) | Session QA F1 − compression; terminal + session-attributed | LoGo-GRPO: global group-relative + **local rerollouts from shared \(\mathcal{M}_{t-1}\)** | **Yes** — local interventional rerolls | Explicitly **no** for fair GRPO; traj-level comparisons “unfair / biased” when memory diverges | Informal: unfair comparison under diverging memory; **no** potential-outcome identifiability theorem | Qualitative: contamination / unfair group norm; **no** bias-as-\(H\) law vs oracle \(V^{\mathrm{write}}\) | Curriculum 8→16→32 sessions (horizon), not controlled \(H\) write→utility | Ablations: −local GRPO hurts F1; curriculum prevents collapse — **not** delayed-critical retention vs oracle write value | **High on informal A/B motivation + interventional fix**; **zero on formal A**; weak C |
| **Mem-T** | Hierarchical store; formation/evolution/retrieval ops | Formation/evolution create/update entries | Sparse terminal QA; densified via trees | MoT-GRPO: tree reward backprop (retrieval) + **hindsight credit** to construction (evidence alignment + retrieval-trace gates); offline distill | Tree branching / hindsight linking — not write 0/1 potential outcomes | Uses on-policy trees + hindsight labels; not OPE identifiability | No | No formal bias of observational \(V^{\mathrm{write}}\) | Long construction chains; not \(H\in\{1,4,8\}\) write-value study | Improves F1; densifies credit — **not** estimator-vs-oracle retention gap | **B (densify delayed credit)**; not A; not C1’s OPE object |
| **HiMPO** | Compressed memory agent; write summary then reason/tool | Memory write \(m_{t-1}\!\to m_t\) | Terminal task reward + memory-specific advantage | **Local counterfactual utility** \(\Delta=S(H,m_t,z^\star)-S(H,m_{t-1},z^\star)\) under **same pre-write state**; hindsight relevance gate; apply only to memory tokens | **Yes** — memory-replacement counterfactual scoring (log-prob of target); not env reroll of \(W\in\{0,1\}\) | Trajectory RL insufficient alone (entanglement); supplements with CF utility | No Pearl-style identifiability | Empirical **blame leakage** under tool corruption / memory drop interventions | Optional EMA backprop for delayed prefatory writes; not systematic \(H\) law | Controlled interventions measure attribution fidelity — **C for entanglement**, not observational OPE of write value | **High on counterfactual write utility (B)**; different estimand (content replacement under \(H\), not \(R(W{=}1)-R(W{=}0)\)) |
| **MemQ** | EC-MDP: exogenous task + endogenous store; action = retrieve subset | Write via Build after retrieve (not binary write policy as primary action) | Per-task success | Per-memory \(Q\); TD(\(\lambda\)) on **provenance DAG** depth | No write intervention; online Q updates from observed outcomes | Treats observed (retrieve→reward→new memory) as sufficient for TD updates | No causal identifiability of write; structural Bellman over DAG | Compares \(\gamma,\lambda\); single-step vs multi-step — estimation, not identification | Depth \(d\) of DAG, not calendar delay \(H\) of write | Improves multi-step tasks — retrieval valuation, not write OPE | **B for multi-step retrieval credit**; **low A/C for write \(W_t\)** |
| **Memory-R1** | Manager ADD/UPDATE/DELETE/NOOP; Answer distillation | Yes | Downstream EM/QA after op | PPO/GRPO on outcome reward; no special credit structure | Group sampling of actions (GRPO), not local memory-state CF for value ID | Implicitly yes — outcome RL from rollouts | No | No | Not as scientific IV | Manager RL improves QA — method paper | **Naive outcome credit** — baseline for C1, not C1 |
| **TCM** (Mazzella 2026) | Factored MDP: \(\pi_{\mathrm{mem}}\) write/forget/retain + \(\pi_{\mathrm{env}}\); capacity \(K\); slot traces \(z_i\), values \(V_i\) | First-class Write/Forget/Retain | Delayed query reward after **operation-free silence** of length \(B\) | Eligibility on **memory-operation clock** vs env-clock TD(\(\lambda\)); two-timescale \(V,Q\) | Synthetic control of silence/capacity; oracle vs learned write head; **not** Pearl OPE of \(V^{\mathrm{write}}\) from observational law alone | Studies when env-clock **fails to keep write credit identifiable through silence** (trace magnitude / finite-sample rate) | Uses “identifiability” for **credit-signal through gaps** (App. A.5); **not** observational identification of potential outcomes | Proves env-clock decays \((\gamma\lambda)^B\); op-clock invariant; **scope condition** when policy outcome changes | **Yes** — \(B\) / stream length / callback distance varied | **Yes** — write/skip policy, delayed-critical retention, LoCoMo/LongMemEval; continuation vs abandonment style findings | **Highest overlap with delayed write credit + synthetic MDP + retention (B→C)**; different scientific object than Pearl observational ID of \(V^{\mathrm{write}}\) |
| MemCon / MemRL / MemPO | Bandit / Q / self-memory advantages | Various | Online / trajectory | Bandit or TD / MemPO advantages | Mostly online adaptation | Assumed sufficient for their estimators | No | Methodological | Limited | Task metrics | Adjacent methods; not C1 |

## Summary for audit

| Claim layer | Already present? |
|---|---|
| Informal: traj-level memory credit is unfair/biased; need shared-state comparisons | **Memory-R2** |
| Counterfactual local utility of a memory update | **HiMPO** |
| Densify / hindsight delayed construction credit | **Mem-T** |
| Multi-step credit along memory provenance | **MemQ** |
| Delayed write→reward silence; synthetic \(K\); policy consequence of bad credit clocks | **TCM** |
| Formal observational identifiability of \(V_t^{\mathrm{write}}=\mathbb{E}[R(1)-R(0)\mid H_t]\) + bias law of naive OPE → retention | **Not proved as such** — but residual collapses toward **standard causal inference / OPE** once Memory-R2/HiMPO/TCM are subtracted |

---
id: pub-03-learning-centric-rq-search
title: "Learning-centric RQ search — agent long-term memory"
type: research-notes
status: search-complete
created: 2026-08-01
updated: 2026-08-01
---

# Learning-centric RQ search (Publication 03)

**Mandate:** Find an ICLR-level question about how memory behavior is **learned, adapted, optimized, or stabilized** over interaction. Hierarchical LTKM = platform only. Closed objects (CR-Gap, Archive Pareto, P-Bind, F1×F4, AUG, sufficiency, access dissociation, plan-vs-execute) are out of scope — see [`closed-scientific-objects.md`](closed-scientific-objects.md).

**Constraint:** No static inference failure; no benchmark-only claim; no architecture-as-claim; begin from learning dynamics.

**Literature base:** [`memory-learning-literature-matrix.md`](memory-learning-literature-matrix.md).

---

## Search summary

Spaces A–F were surveyed against 2024–2026 primary sources (ACL/NeurIPS/ICLR/ICML/COLM/OpenReview/arXiv). The **method space** for learned write/retrieve/forget (Memory-R1, Mem-α, MemCon, MemPO, AdaMEM, ALMA, Oblivion, OSL-MR, …) and for **memory credit assignment** (Mem-T, Memory-R2/LoGo-GRPO, HiMPO, MemQ, MemPO) is **heavily occupied**. Feedback/stability of reflective memory is occupied by Honest Lying and EDV. Representation/abstraction learning is partially occupied by MCMA and joint compress–reason RL (e.g. LycheeMemory, InfoMem).

Surviving residual is **not** “can RL learn a memory manager?” It is narrower: **characterizing learning dynamics / identifiability / representation preservation** under constraints compatible with local compute.

Six candidates below. Required coverage: credit (C1), non-stationarity (C2), feedback/stability (C3), representation (C4), plus policy-learning (C5) and test-time (C6).

---

## Candidate C1 — Observational identifiability of delayed write value

**Space:** B (credit assignment)

1. **Frozen RQ:** Under what conditions is the delayed counterfactual value of a memory write observationally identifiable from ordinary agent trajectories, and when does naive credit assignment induce systematically biased retention?
2. **Scientific object:** Identifiability (and bias structure) of delayed write advantages under observational vs interventional credit.
3. **Learned/adaptive component:** Write (and optionally retain) policy trained from observational returns vs local counterfactual advantages.
4. **Central falsifiable hypothesis:** When write utility is delayed by horizon \(H>1\) and rollouts diverge in memory state, observational return-based estimators of write advantage are systematically biased relative to interventional local counterfactuals; the bias grows with \(H\) and state divergence, causing over-retention of short-horizon cues and under-retention of delayed-critical facts.
5. **Independent variable:** Delay horizon \(H\); estimator class (observational TD / trajectory GRPO-style vs local interventional reroll); degree of cross-rollout memory divergence.
6. **Dependent variable:** Correlation / regret of estimated write advantage vs oracle counterfactual value; resulting retention composition; downstream task success after training.
7. **Smallest environment:** Synthetic memory MDP: capacity-\(K\) store, binary write/skip, sparse reward at lag \(H\), known oracle write values; tabular or linear policy.
8. **Why fixed heuristic insufficient:** Heuristics (always-write, recency) do not explain **estimator-induced** bias in a *learned* policy; the claim is about credit dynamics, not a retention rule ranking.
9. **Closest 2024–2026 literature:** Memory-R2 + LoGo-GRPO (arXiv 2026; local rerolls for fair credit); Mem-T / MoT-GRPO; HiMPO; MemQ (provenance DAG TD); MemPO; Memory-R1 (outcome RL without formal identifiability).
10. **Exact residual:** Methods papers **assert** unfairness of trajectory-level credit and propose algorithms. Residual: a **characterization** of when observational write value is (non-)identifiable and what **bias law** results — not another GRPO variant on LoCoMo.
11. **Fastest novelty-kill check:** Does Memory-R2 (or Mem-T/HiMPO/MemQ) already state a formal identifiability theorem / measured bias-vs-\(H\) law? If yes with comparable dependent variables → OCCUPIED. (Inspected abstracts/methods: algorithm + empirics; no general identifiability characterization found.)
12. **Fastest empirical-kill:** Synthetic MDP, \(H\in\{1,2,4,8\}\), train write policy with observational advantage only; if policy recovers oracle delayed writes within ε of interventional training → hypothesis dies.
13. **Local-compute feasibility:** **Yes** — tabular/REINFORCE/small MLP; no LLM fine-tune for pilot; optional frozen ≤4B reader later.
14. **Expected ICLR contribution type:** Learning dynamics + (light) theory / mechanism.
15. **Likely AC rejection:** “Memory-R2 already diagnosed this; incremental characterization without a competitive training method.”

**Novelty class:** **PARTIALLY OPEN** (strong residual on characterization; method space occupied).

**Depth filter:** Survives if framed as credit-assignment failure + bias law; fails if framed as “better RL memory manager.”

---

## Candidate C2 — Catastrophic persistence under distribution shift

**Space:** C (non-stationarity)

1. **Frozen RQ:** Do retention policies trained under distribution \(D\) systematically over-persist after a shift to \(D'\), producing catastrophic persistence relative to a re-trained oracle?
2. **Scientific object:** Adaptation lag / persistence bias of learned retention after task-distribution shift.
3. **Learned component:** Retention (keep/evict/decay) policy trained on \(D\), evaluated frozen or online-adapted on \(D'\).
4. **Hypothesis:** After shift, retained mass on \(D\)-optimal but \(D'\)-irrelevant entries remains significantly above oracle; adaptation lag scales with pre-shift training length.
5. **IV:** Shift severity; pre-shift training duration; online adaptation allowed vs frozen.
6. **DV:** Persistence gap (fraction of capacity on obsolete entries); post-shift task regret vs oracle retrained retention.
7. **Smallest environment:** Two-phase synthetic store with changing query distribution over a fixed fact set; capacity budget; bandit/tabular retention.
8. **Why heuristic insufficient:** Recency/decay heuristics are baselines; the object is **learned-policy staleness dynamics**, not that decay helps.
9. **Closest literature:** OSL-MR (retention under budget + demand shift, arXiv 2026); Oblivion; Memory Worth / When to Forget; ALMA; MemCon; MCMA (shift/transfer).
10. **Exact residual:** Thin — OSL-MR already optimizes retention under stale risk and demand shift; Oblivion/Memory Worth target staleness.
11. **Novelty-kill:** If OSL-MR’s shift experiments already measure over-persistence of learned policies vs oracle → OCCUPIED.
12. **Empirical-kill:** After shift, if learned policy’s obsolete-mass ≤ heuristic decay within noise → no distinct law.
13. **Local feasibility:** Yes (bandit/tabular).
14. **Contribution type:** Learning dynamics / non-stationary adaptation.
15. **AC rejection:** “Staleness under shift is already the OSL-MR/Oblivion problem; incremental.”

**Novelty class:** **OCCUPIED** (strongly overlapped by OSL-MR + Oblivion + Memory Worth).

---

## Candidate C3 — Retrieval-conditioned rewrite hysteresis

**Space:** D (stability / feedback)

1. **Frozen RQ:** Can retrieval-conditioned rewriting create absorbing error states (hysteresis) that persist even after corrective evidence reappears?
2. **Scientific object:** Path-dependent / absorbing error equilibria in write←retrieve feedback loops.
3. **Learned/adaptive component:** Rewrite policy conditioned on retrieved memory (or Reflexion-style write); optional learned gate.
4. **Hypothesis:** Once a false entry is written and preferentially retrieved, rewrite updates reinforce it; corrective evidence fails to displace it until an external reset — measurable hysteresis width.
5. **IV:** Presence of retrieval-conditioned rewrite; corrective-evidence schedule; write validation on/off.
6. **DV:** Absorption probability; recovery time after corrective evidence; Reflection Repetition–style metrics.
7. **Smallest environment:** Two-fact store (true/false), retrieval by similarity, rewrite step, scheduled corrective observation.
8. **Why heuristic insufficient:** Fixed “don’t rewrite” is a control; claim is about **feedback-induced absorbing dynamics**.
9. **Closest literature:** **Honest Lying** (memory confabulation; self-reinforcing false beliefs despite reset); EDV (self-confirmation trap); SSGM.
10. **Exact residual:** Near-zero for the core phenomenon; Honest Lying already establishes self-reinforcing false reflective memory.
11. **Novelty-kill:** Honest Lying + RRR — **kills** as primary object.
12. **Empirical-kill:** N/A (occupied).
13. **Local feasibility:** Yes, but irrelevant.
14. **Contribution type:** Mechanism / evaluation (occupied).
15. **AC rejection:** “Honest Lying already.”

**Novelty class:** **OCCUPIED**.

---

## Candidate C4 — Consolidation and sufficient-statistic preservation

**Space:** E (representation learning)

1. **Frozen RQ:** Does learned consolidation preserve the task-relevant sufficient statistics needed after task change, or does it induce irreversible information collapse?
2. **Scientific object:** Whether consolidation maps preserve (or destroy) known sufficient statistics for future tasks.
3. **Learned component:** Consolidation / abstraction encoder (small network or learned compress policy) trained under capacity pressure on task family \(\mathcal{T}_1\), tested on \(\mathcal{T}_2\).
4. **Hypothesis:** Capacity-constrained learned consolidation that maximizes \(\mathcal{T}_1\) reward discards coordinates that are sufficient for \(\mathcal{T}_2\); irreversible collapse is detectable by SS-recovery probes and is not explained by raw storage limits alone.
5. **IV:** Consolidation capacity; training task family; probe tasks requiring held-out SS dimensions.
6. **DV:** SS-recovery accuracy; downstream \(\mathcal{T}_2\) regret; mutual information between consolidated state and oracle SS.
7. **Smallest environment:** Synthetic facts with explicit sufficient-statistic coordinates; consolidate-to-\(k\) bits; change which coordinates matter.
8. **Why heuristic insufficient:** Fixed summarization baselines exist; claim is about **learned** consolidation destroying identifiable SS under shift.
9. **Closest literature:** MCMA (learnable abstraction / transfer); Mem-α multi-store; LycheeMemory joint compress–reason RL; InfoMem (reward-induced degenerate memory content).
10. **Exact residual:** MCMA shows abstraction helps transfer; does **not** measure irreversible loss of known SS. InfoMem studies reward collapse (query-copy), not SS preservation laws.
11. **Novelty-kill:** Paper that already measures consolidation SS preservation / irreversible collapse under task change with oracle SS → OCCUPIED. (Not found as primary claim.)
12. **Empirical-kill:** If learned consolidator matches oracle SS retention of a mutual-information upper bound within ε on \(\mathcal{T}_2\) → no collapse law.
13. **Local feasibility:** **Yes** — synthetic SS + small encoder; frozen LLM optional for language wrapper.
14. **Contribution type:** Representation / learning dynamics.
15. **AC rejection:** “Compression quality under shift; incremental on MCMA / memory compression.”

**Novelty class:** **PARTIALLY OPEN**.

**Depth filter:** Survives only with oracle-SS probes and irreversibility (not “abstraction helps accuracy”).

---

## Candidate C5 — Joint write–retrieve degenerate equilibria

**Space:** A (memory-policy learning) + D (stability)

1. **Frozen RQ:** Does joint learning of write and retrieve policies under sparse delayed reward collapse to degenerate equilibria (write-nothing, retrieve-all, or query-echo memory)?
2. **Scientific object:** Existence and basins of degenerate Nash/equilibria of coupled write×retrieve learners.
3. **Learned component:** Jointly trained write and retrieve controllers (small policies).
4. **Hypothesis:** Under sparse delayed reward and coupled updates, joint training enters degenerate attractors with positive probability; separate training or staged curriculum avoids them under the same reward.
5. **IV:** Joint vs separate training; reward sparsity; capacity; initialization.
6. **DV:** Equilibrium type frequency; entropy of write/retrieve actions; task return vs oracle.
7. **Smallest environment:** Memory MDP with discrete write and retrieve actions; sparse terminal reward.
8. **Why heuristic insufficient:** Heuristics are not joint learners; object is **coupled learning dynamics**.
9. **Closest literature:** Memory-R1 (joint manager + answer agent, reports success); MemPO; InfoMem (documents reward-induced degeneration / query-copy); LycheeMemory joint compress–reason.
10. **Exact residual:** InfoMem already identifies degeneration under bad memory rewards. Residual for **write×retrieve coupling equilibria** is thin.
11. **Novelty-kill:** InfoMem + Memory-R1 success recipes → treat as **near-occupied**.
12. **Empirical-kill:** If joint training never collapses under standard sparse rewards in the small MDP → no phenomenon.
13. **Local feasibility:** Yes.
14. **Contribution type:** Learning dynamics / optimization.
15. **AC rejection:** “InfoMem already; or just use their reward design / curriculum.”

**Novelty class:** **OCCUPIED** (degeneration under memory RL rewards already a primary finding in InfoMem; joint success recipes in Memory-R1/MemPO).

---

## Candidate C6 — Test-time memory-policy adaptation without weight updates

**Space:** F (test-time learning)

1. **Frozen RQ:** Can a memory allocation/retrieval policy adapt online from retrieval failures without updating backbone parameters, and does that adaptation transfer across environments?
2. **Scientific object:** Non-parametric / bandit test-time adaptation of memory control.
3. **Learned component:** Online contextual bandit or Q-table over retrieve/consolidate actions; frozen LLM.
4. **Hypothesis:** Test-time updates from retrieval failure signals improve allocation vs frozen heuristic; gains transfer under shift.
5. **IV:** Adaptation on/off; failure-signal type; environment transfer.
6. **DV:** Cumulative regret; post-adaptation success; transfer gap.
7. **Smallest environment:** Bandit over memory actions with delayed binary feedback.
8. **Why heuristic insufficient:** Claim is online learning from failures, not a fixed schedule.
9. **Closest literature:** AdaMEM; MemCon; MemRL; ALMA; Oblivion.
10. **Exact residual:** Negligible for the core claim.
11. **Novelty-kill:** AdaMEM / MemCon / MemRL — **kills**.
12. **Empirical-kill:** N/A.
13. **Local feasibility:** Yes, but occupied.
14. **Contribution type:** Optimization / evaluation (occupied).
15. **AC rejection:** “AdaMEM/MemCon.”

**Novelty class:** **OCCUPIED**.

---

## Hard depth filter (apply)

| ID | Depth criterion met? | Survive? |
|---|---|---|
| C1 | Credit-assignment failure + bias law | **Yes** (if characterization, not new LoCoMo SOTA) |
| C2 | Non-stationary adaptation | No — occupied mechanism |
| C3 | Stability/feedback | No — occupied (Honest Lying) |
| C4 | Representation-learning result | **Yes** (if oracle-SS irreversibility) |
| C5 | Stability/convergence of joint learning | No — occupied degeneration story |
| C6 | Test-time adaptation | No — occupied |

---

## Ranking (OPEN / strongly PARTIALLY OPEN only)

See [`learning-candidate-comparison.md`](learning-candidate-comparison.md).

**Shortlist:** C1 > C4.

**Occupied (do not rank):** C2, C3, C5, C6.

---

## Final recommendation

**Recommend: C1 — Observational identifiability of delayed memory-write value.**

### Frozen research question

Under what conditions is the delayed counterfactual value of a memory write observationally identifiable from ordinary agent trajectories, and when does naive credit assignment induce systematically biased retention?

### Exact scientific hypothesis

In memory MDPs where write utility is delayed and rollouts diverge in memory state, observational advantage estimators are biased relative to interventional local counterfactuals; the bias magnitude increases with delay horizon and cross-rollout memory divergence, producing systematically distorted learned retention.

### Why categorically different from closed directions

Closed objects were static inference / retrieval / sufficiency / archive-allocation failures. C1 is a **learning-dynamics / credit-assignment** question about how memory policies acquire value from delayed outcomes.

### Minimum learned component

Tabular or small linear/MLP **write policy** plus two advantage estimators (observational vs local interventional). Frozen LLM optional; not required for decisive pilot.

### Fastest decisive pilot

Synthetic capacity-\(K\) memory MDP; oracle write values; \(H\in\{1,4,8\}\); train with observational advantages only vs interventional local rerolls; measure advantage correlation with oracle and retention composition.

### Quantitative continuation criterion

At \(H\ge 4\), observational-trained policy’s correlation with oracle write value \(\rho_{\text{obs}} \le \rho_{\text{int}} - 0.25\) **and** delayed-critical retention rate at least 15pp below interventional (same seed budget, \(N\ge 20\) seeds).

### Quantitative abandonment criterion

For all \(H\le 8\), \(|\rho_{\text{obs}}-\rho_{\text{int}}| < 0.1\) **or** retention composition indistinguishable (difference < 5pp) — credit gap not real in the minimal setting.

### Required data/environment

Fully synthetic memory MDP (no cloud API). Optional later: frozen ≤4B MLX reader on toy QA over the same store.

### Seven-day plan

| Day | Work |
|---|---|
| 1 | Formalize MDP, oracle counterfactual value, bias metrics; novelty-kill deep-read of Memory-R2/Mem-T/HiMPO/MemQ methods sections |
| 2 | Implement environment + oracle + observational/interventional estimators |
| 3 | Pilot \(H\in\{1,4\}\) tabular write policy; verify instrumentation |
| 4 | Full \(H\) sweep + seeds; plot bias vs \(H\) |
| 5 | Ablate memory-divergence (force shared vs divergent states) |
| 6 | Write go/no-go from continuation/abandonment criteria |
| 7 | If CONTINUE: draft theory sketch (bias source) + map to LTKM platform hooks (write router only) |

### Proposed repository directory

`experiments/obs-mem-credit-pilot/`

### Exact next novelty-or-implementation prompt

See final report §10.

### Strongest novelty risk

Area Chair treats C1 as a restatement of Memory-R2’s motivation without a new training method or theorem that changes practice.

### Status if C1 fails novelty-kill or pilot abandon

Fall back shortlist item **C4** only after a dedicated novelty deep-dive on MCMA / InfoMem / LycheeMemory SS-related claims. If both fail: **no authorized learning-centric object**.

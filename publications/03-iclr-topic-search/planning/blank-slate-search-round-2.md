---
id: pub-03-blank-slate-search-round-2
title: "Blank-slate ICLR search — round 2"
type: research-notes
status: complete
created: 2026-07-31
updated: 2026-07-31
verdict: NO_VIABLE_TOPIC_FOUND
literature_checked: 2026-07-31
---

# Blank-slate ICLR problem search — round 2

**Goal:** Find one scientific question that survives an aggressive 2024–2026 novelty audit.  
**Posture:** Phenomenon-first; no architecture; no reopen of closed/occupied register.  
**Verdict:** `NO VIABLE TOPIC FOUND`

---

## Method

1. Generated ≤5 diagnostic candidates in preferred forms (dissociation, metric overestimate, collateral failure of a standard intervention, test-time assumption failure).
2. For each, searched ICLR / NeurIPS / ICML / ACL / EMNLP / COLM / OpenReview / arXiv 2024–2026 and inspected experimental designs (not titles alone).
3. Classified `OPEN` / `PARTIALLY OPEN` / `OCCUPIED` / `NOT ICLR-SHAPED`.
4. Rejected occupied and non-ICLR immediately without cosmetic rename.
5. Ranked only survivors — **none**.

Hard exclusions enforced: CR-Gap family; LiC / FULL–CONCAT–SHARDED; plan–execute sole claims; progressive disclosure; parallel-tool latency; generic tool-use tax; generic multi-turn hardness.

Local constraints noted: Apple Silicon MLX ~0.5B–4B; limited disk; no frontier pretraining; pilot must be days-scale.

---

## Candidate R2-A — Self-correction accuracy–calibration dissociation

1. **RQ:** Does iterative self-correction that improves task accuracy systematically worsen calibration (ECE / overconfidence)?
2. **Hypothesis:** Accuracy↑ and ECE↑ co-occur under iterative self-refine; calibration interventions trade accuracy for ECE.
3. **Object:** Self-improvement dynamics / reliability.
4. **ICLR care:** Trustworthy ML under test-time refinement.
5. **Closest:** Zhu et al. 2025 *Beyond Accuracy: Calibration in Self-Improving LLMs*; Self-Correction as Feedback Control (EIR/ECR thresholds, 2026); dark side of intrinsic self-correction (ACL 2025).
6. **Residual:** Thin at best (local small-model replication) — not a new phenomenon.
7. **Novelty kill:** Find Zhu et al. design → **killed**.
8. **Empirical kill:** N/A.
9. **Compute:** Low.
10. **Rejection:** Already published.
11. **Surprise:** Would need opposite finding (self-correction *improves* calibration) — unlikely / not claimed.
12. **Team fit:** Good conceptually, but occupied.

**Verdict:** `OCCUPIED`

---

## Candidate R2-B — Verbal confidence vs risk-sensitive action dissociation

1. **RQ:** Can models produce calibrated verbal confidence yet fail to abstain or change actions under high error penalties?
2. **Hypothesis:** Verbal confidence and abstention/commit policy are dissociable; extreme penalties do not induce optimal abstention.
3. **Object:** Uncertainty–action coupling.
4. **ICLR care:** Capability–reliability dissociation.
5. **Closest:** RiskEval / *Are LLM Decisions Faithful to Verbal Confidence?* (2026); *Reported Confidence Tracks Commitment More Than Correctness* (2026); causal confidence→behavior (2026).
6. **Residual:** Tool-use gating of abstention would be transfer, not new.
7. **Novelty kill:** RiskEval already tests penalty-conditioned abstention + verbal confidence → **killed**.
8.–12. Feasible but occupied.

**Verdict:** `OCCUPIED`

---

## Candidate R2-C — Test-time compute under hidden assumptions

1. **RQ:** Does increasing test-time compute improve accuracy only when the task is reasoning-bound rather than knowledge-bound (or only within an inverted-U length regime)?
2. **Hypothesis:** Extra thinking tokens fail to improve (or worsen) knowledge-intensive accuracy / induce overthinking on easy items.
3. **Object:** Test-time scaling assumptions.
4. **ICLR care:** Challenges TTS as general capability booster.
5. **Closest:** *TTS Not Effective for Knowledge-Intensive Tasks Yet* (ICLR 2026 workshop / OpenReview); *When More Thinking Hurts*; *When More is Less* (CoT length); Cuadron et al. agent overthinking.
6. **Residual:** Local 0.5–4B “thinking” models lack genuine TTS knobs → weak pilot; phenomenon occupied for frontier reasoners.
7. **Novelty kill:** Existing TTS/knowledge and overthinking papers → **killed**.
8.–12. Occupied; also compute-feasibility weak for true reasoning models locally.

**Verdict:** `OCCUPIED` (also poor local feasibility for the interesting regime)

---

## Candidate R2-D — Information-equivalent representation / format collapse

1. **RQ:** Holding information fixed, does changing serialization / output format / state encoding collapse task success?
2. **Hypothesis:** Informationally equivalent formats yield large accuracy gaps unexplained by length or missing facts.
3. **Object:** Representation sensitivity under equivalence.
4. **ICLR care:** Challenges assumption that models operate on abstract content.
5. **Closest:** *Lost in Formatting* (EACL 2026, >40pp F1 swings); *Lost in Serialization* (graphs); graph isomorphism failure (2026); CSE compositional constraints; *State Design Matters* / StateAct JSON harm.
6. **Residual:** Another domain transfer (e.g. agent tool JSON) is cosmetic relative to occupied core claim.
7. **Novelty kill:** Multiple 2025–26 controlled format-equivalence papers → **killed**.
8.–12. Occupied.

**Verdict:** `OCCUPIED`

---

## Candidate R2-E — Outcome success conceals invalid procedure; Tool Ignored

1. **RQ:** Do standard success metrics systematically count procedurally invalid or tool-inconsistent trajectories as successes?
2. **Hypothesis:** A large fraction of “successes” violate integrity constraints; or models ignore correct tool outputs (“Tool Ignored”).
3. **Object:** Evaluation methodology / tool–reason integration.
4. **ICLR care:** Metrics that change conclusions about capability.
5. **Closest:** PAE *Corrupt Success* (2026); ReliabilityBench / Beyond pass@1 reliability science; AgentLTL; ATTC *Tool Ignored* (ACL Findings 2026); TIM tool-induced myopia (ACL 2026); unreliable feedback agents (2026).
6. **Residual:** None that clears “transfer of known effect” bar.
7. **Novelty kill:** Direct matches → **killed**.
8.–12. Occupied.

**Verdict:** `OCCUPIED`

---

## Additional probes (not full candidates; also fail)

| Probe | Why rejected |
|---|---|
| Mid-episode schema / API drift as ML claim | **NOT ICLR-SHAPED** (systems/contract engineering); ReliabilityBench already injects schema drift |
| Mid-episode environment dynamics | **OCCUPIED** (STT-Arena; robust adaptation envs) |
| Reward hacking measurement | **OCCUPIED** (Hack-Verifiable Environments) |
| Credit assignment for agent failures | **OCCUPIED** (CAR, CausalFlow, AgentSHAP) |
| Corrupted tool feedback | **OCCUPIED** (Don’t Blindly Trust It, 2026) |
| Belief inertia | **OCCUPIED** (EVU, BeliefMem adjacent) |
| Compositional skill vs joint constraints | **OCCUPIED** (CSE; Logical Phase Transitions) |
| Paraphrase inconsistency as sole claim | **OCCUPIED** (*Same Question, Different Answers*, 2026) |

---

## Ranking

**No surviving candidates.** Ranking table empty by rule (do not rank occupied above open).

---

## Final recommendation

`NO VIABLE TOPIC FOUND`

Among preferred diagnostic forms (dissociations, metric overestimates, TTS assumption failures, format equivalence, procedure-vs-outcome), the 2025–2026 literature already contains multiple primary papers per form, including ICLR Best Paper–adjacent and ACL/ICLR 2026 work. Forcing a recommendation would violate the hard novelty standard (transfer ≠ novelty).

---

## What to search next (programme guidance)

Shift **away** from another behavioral dissociation in prompting/agent scaffolds. Prefer spaces where a three-author team can still clear novelty:

1. **Mechanistic explanation of a *already documented* dissociation** — causal circuit / activation interventions that explain *why* (not that) a known failure occurs; local GPT-2 / small MLX models feasible; risk: MechRL / HyVE / SAE-Track occupy automation, so the residual must be a *specific* unexplained mechanism, not “agents explain circuits.”
2. **Small-scale training dynamics with a falsifiable theoretical prediction** — e.g. when a learning rule induces a phase change in compositionality or calibration; needs theory + tiny models; not another eval-only paper.
3. **Cross-modal binding / multimodal agentic dissociations** not reducible to text LiC or format papers — only if design-level residual survives audit.
4. **Formal verification–coupled learning objectives** where the *learning consequence* (not the verifier) is the claim — avoid process-supervision surveys already dense in 2026.
5. **Outside pure LLM-agent behavioral eval** — representation learning under interaction with non-LLM environments, or optimization theory of test-time adaptation under explicit POMDP assumptions with local experiments.

Do **not** return to agent memory, LiC renames, plan–execute, or format-equivalence transfers.

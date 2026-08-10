---
id: pub-03-c1-identifiability-novelty-audit
title: "C1 identifiability novelty audit"
type: research-notes
status: audit-complete
created: 2026-08-01
updated: 2026-08-01
---

# C1 novelty audit — observational identifiability of delayed write credit

**Provisional RQ:** Under what conditions is the delayed counterfactual value of a memory write observationally identifiable from ordinary agent trajectories, and when does naive credit assignment induce systematically biased retention?

**Intended object:** observational identifiability and bias of delayed memory-write credit — **not** a new memory manager.

## Duplicate test — classification

### Verdict: `STANDARD RESULT APPLIED TO MEMORY`

with **informationally adjacent occupation** by Memory-R2 (interventional rerolls for unfair traj credit), HiMPO (local counterfactual write utility), and TCM (delayed write credit through silence → retention policy).

Not cleanly `OPEN`.  
Not `OCCUPIED` as a verbatim Pearl theorem (none of the five managers prove observational non-ID of \(V^{\mathrm{write}}\)).  
Not `TOO THEORETICAL FOR CURRENT PROJECT` as the main failure mode — the failure mode is **novelty / distinctiveness**.

### Why not PARTIALLY OPEN (surviving)

For C1 to survive, the memory setting must introduce structure beyond positivity / confounding / generic OPE. Capacity interference, delayed query, and write→retrieval channels are real — but:

1. **Memory-R2** already treats diverging memory as making traj-level credit **biased/unfair** and responds with **interventions** (local rerolls). C1’s “need intervention / observational credit fails” is their **motivating claim**, not a residual theorem.
2. **HiMPO** already estimates **local counterfactual utility of memory writes** under a shared pre-write state and links credit quality to retention-relevant failure modes (blame leakage).
3. **TCM** already formalizes **delayed write→reward gaps**, proves clock-dependent credit survival, and measures **learned retention consequences** in a synthetic capacity-limited MDP — the empirical spine C1 wanted for B→C.
4. What remains for a “formal identifiability” paper is essentially: positivity, ignorability, interference/SUTVA, IPS/DR variance — **standard causal inference / OPE** with memory nouns.

Hostile filter triggered: **do not publish standard CI as memory research.**

## Closest occupying paper

**Primary (informal A + interventional practice):** Memory-R2.  
**Primary (delayed write credit B→C in synthetic MDP):** TCM.  
**Primary (counterfactual write utility):** HiMPO.

Exact residual after subtracting these: a textbook identification discussion of \(V^{\mathrm{write}}\) plus a synthetic OPE bakeoff that would **replicate their motivations** rather than open a new law.

## Three-claim map

| Claim | Status |
|---|---|
| A Identifiability | Residual = standard CI; informal occupation by Memory-R2 |
| B Estimation | Occupied by TCM (delay clocks), Mem-T (densify), MemQ (DAG TD), HiMPO (CF utility) |
| C Policy consequence | Occupied/demonstrated in TCM; partially in Memory-R2/HiMPO ablations |

C1’s hoped A→C bridge does not clear the duplicate bar.

## Strongest formal proposition considered

Capacity-induced interference sign-flip of naive observational attribution vs ceteris-paribus interventional write advantage ([`c1-causal-formalization.md`](c1-causal-formalization.md)).  
**Rejected as Pub-03 spine:** still standard interference + confounding through a mediator.

## ICLR-depth assessment

| Plausible contribution shape | Viable? |
|---|---|
| Causal-identifiability result | Only as CI-in-memory costume → **no** |
| Delayed-credit-assignment law | **TCM already** |
| Memory-policy learning result | Method space saturated (Memory-R1 family) |
| Application of standard OPE | **Not ICLR-worthy** under hostile filter |
| Engineering observational vs interventional comparison | Confirms Memory-R2; **evaluation-only** |

What would have made C1 ICLR-worthy (unsupported now): a **new memory-native identification obstruction** with a theorem that is not a corollary of positivity/confounding/interference, plus estimators that are not LoGo-GRPO/HiMPO/TCM, plus C-level retention law those papers do not already imply.

## Decision

**ABANDON C1** as provisional Publication 03 direction.

Do **not** implement `experiments/obs-mem-credit-pilot/`.

Next programme step: return to learning-centric search without reviving C1; prior runner-up C4 remains unevaluated at this audit depth — **not auto-authorized**.

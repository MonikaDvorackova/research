---
id: topic-bostrom-world-models-phase1-decision
title: "Phase 1 decision"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [decision]
---

## Phase 1 decision: GO, narrowed (conditional)

### Revised research question

When an agent embedded in an environment detects, or fails to detect, a discrepancy between that environment and a learned world model, what may it infer about how the environment is generated, and which additional premises does the inference to "simulated" require?

This replaces the earlier wording, which asked whether an agent can distinguish E1 from E0. That wording invites the trivial answer (an oracle likelihood-ratio test works).

### Why GO and not REVISE

- The earlier preliminary REVISE was driven by a loose research question and an unsupported novelty framing. Both are now addressed by narrowing the claims to C1–C3 in [novelty-and-gap.md](novelty-and-gap.md).
- No prior work was found that occupies the narrowed gap, with the limits stated below.

### Conditions that must be met before major implementation

1. Read Ikram et al. (2026) in full (OpenReview was blocked). If it already covers latent-prior mismatch detection with intervention policies, C3 must be reframed as replication plus the negative-control contribution.
2. Run backward and forward citation searches (Semantic Scholar or Google Scholar) on Bostrom 2003, Armstrong 2018, Castro et al. 2009. This has not been done.
3. Read arXiv:1404.1718 and arXiv:2609.10864, the closest philosophical-formal neighbours.
4. Verify P5 and the simulation-lemma / compounding-error sources behind P6.
5. Search the philosophical literature individually (Chalmers text, Hanson, Dainton, Kulczycki).

If condition 1 or 3 shows that C1 is already established, the decision reverts to REVISE.

### Limits of this assessment

Search was done with a web search tool, not bibliographic databases. Most sources were read at abstract level. "No prior work found" means exactly that.

### Next step

Phase 2 formal write-up of P6–P8 with proofs, in parallel with closing conditions 1–5. No experiments have been executed.

## Phase 2 update (2026-11-03)

Status of the five conditions set in Phase 1:

| # | Condition | Status |
|---|---|---|
| 1 | Read Ikram et al. in full | **Partly met.** Abstract obtained through a search-tool summary only (OpenReview blocks automated access). It concerns unrealistic *generated* states inside model-based RL, not environment discrimination by an agent. Overlap with this project is small; the full text is still unread. |
| 2 | Citation searches (Bostrom, Armstrong, Castro) | **Partly met.** 512 Bostrom citing records filtered; none pairs the argument with learned world models or agent-side detection. Armstrong and Castro forward searches failed. |
| 3 | Read arXiv:1404.1718 and 2609.10864 | **Met at abstract level.** 2609.10864 is not about simulation (earlier characterisation withdrawn); 1404.1718 uses algorithmic probability with no visible detection analysis. New neighbours to read: Brogioli (empirical equivalence via simulation), the 2026 "glitch" detection paper, Campbell et al. |
| 4 | Verify P5 and sources for P6 | **Proofs written; sources not verified.** Propositions 1–6 are proved in `notes/formal-framework.md` and checked by exact enumeration; provenance labels say Known or Elementary. Literature check of Proposition 1 against Armstrong/Castro is obligation O4. |
| 5 | Philosophical literature search | **Not met.** Chalmers, Hanson, Dainton, Kulczycki, Weatherson not read. |

### Decision after Phase 2: REVISE (continue, do not write the manuscript yet)

- The narrowed gap is **defensible but narrow and unproven**: absence of discovered prior work, from partial citation analysis.
- No theorem is claimed as new. The mathematics is framing; the philosophical theses may already exist in the literature.
- The proof-of-concept gives an informative negative result (the agent's own learned theory is the failure point under OOD interventions) and a passing equivalent negative control, but the result may depend on Q and W sharing architecture.
- Required before any manuscript: close conditions 1, 2 and 5; run the two ablations in `reviews/2026-11-03-minds-and-machines-reviewer-assessment.md` (different architecture for Q; an analytically correct theory in place of Q).
- No large-scale experiments are justified yet.


## Phase 3 update (2026-11-03)

### What was done

Philosophical literature review ([philosophical-review.md](../literature/philosophical-review.md)); attempts to access Brogioli and the 2026 glitch paper (both inaccessible, recorded); four experimental ablations plus an exact-theory upper bound; review of Propositions 1-6; reproducibility checks.

### Findings that change the decision

1. **Philosophical novelty is lower than hoped.** The qualitative content of T1-T3 is anticipated (Chalmers 2024; Beane et al.; Laudan and Leplin). Not defensible as the contribution.
2. **The experimental failure is robust and explained.** The failure of active detection is caused by the agent's learned theory being misspecified outside its training coverage, not by active selection and not by one shared architecture. Evidence: exact theory (calibrated, perfect active detection); theory trained over the probed range (works); ReLU theory (failure reproduced); polynomial theory (ranking works, calibration does not).
3. **A narrower candidate contribution exists** (T4/T5: theory-relativity of detection and its coverage dependence), but it is a quantified instance of a known point (Duhem-Quine).
4. **The mathematics is correct, elementary and not original.**

### Decision: REVISE (do not submit to Minds and Machines as framed)

- **Smallest defensible reformulation:** a paper on *what an anomaly shows when the observer's own theory is a learned model*, with the L1/L2/L3 distinction and Propositions 4-6 as framework, the ablation table as evidence, and Bostrom as motivation. Philosophy & Technology is the more realistic first target; Minds and Machines is possible but doubtful.
- **Before drafting:** read Kelly's definitions and the Glymour-Malament-Manchak-Norton papers; obtain Brogioli and the glitch paper (or have the user paste their abstracts); read Weatherson; check for precedents of quantified theory-relativity in philosophy of science and ML-evaluation literature; add a second environment (partially observed) and a second W architecture.
- **Not justified:** large-scale experiments; any claim of a new theorem.

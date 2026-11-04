---
id: topic-bostrom-world-models-decision-log
title: "Research decision log"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [governance, decisions]
---

# Decision log (append-only)
| Date | Decision | Reason | Evidence |
|---|---|---|---|
| 2026-11-03 | Repository `MonikaDvorackova/research`, branch `research/bostrom-world-models`, draft PR #10; never AIGov | User instruction | brief |
| 2026-11-03 (Ph. 1) | Conditional GO | Gap plausible, unproven | `notes/phase1-decision.md` |
| 2026-11-03 (Ph. 2–3) | REVISE; drop "learned models cannot detect simulation" framing | Experiments test observer limits only | `reviews/` |
| 2026-11-03 (Ph. 4) | Original adaptive-observer thesis not supported | Absorption; coverage | `notes/results.md` |
| 2026-11-03 (Ph. 5) | REVISE; original framing NO-GO; pre-register Bayesian observer runs | Gates 4–5 not passed | `notes/results-phase5.md` |
| 2026-11-03 (Ph. 6) | Treat project as open-ended programme; question may change. Candidate directions X1–X7 designed; X1, X3, X2 selected; X4–X7 deferred | `phase6/05-prioritisation.md` | `phase6/*` |
| 2026-11-03 (Ph. 6) | Do not implement X1 until L1 (primary-source reading) and D1 (design review) gates | Novelty risk from Gelman–Shalizi/universal inference | `phase6/07-roadmap.md` |
| 2026-11-03 (Ph. 7) | L1 passed with downgraded ambition: X1 is a known application (universal inference + EDI-style design) | partial full-text reading of three sources | `phase7/01-…` |
| 2026-11-03 (Ph. 7) | D1 passed (self-review) after revision: new alternative family, P5 added, RMST, N = 3000, 30 seeds | exact feasibility; information confound | `phase7/02-…` |
| 2026-11-03 (Ph. 7) | Preregistration frozen at 02bad01 (13:01:50) before the confirmatory run (13:01:59) | – | `phase7/03-…` |
| 2026-11-03 (Ph. 7B) | Integrity passed; frozen analysis executed unmodified; X1 design-benefit hypothesis not supported under the fair comparison | `phase7/05-…`, `06-…` | – |
| 2026-11-03 (Ph. 7B) | X1 closed as a separate line; next: X3 combined with X4 (learned-null test); X2 as a bounded proof attempt | `phase7/08-…` | – |
| 2026-11-03 (Ph. 8) | Question reformulated: identifiability of the four explanations is relative to declared structure; first experiment E6 (validity map) subject to external design review | Gates A–F | `phase8/06-…` |
| 2026-11-04 (Ph. 9) | Corrected formal-null semantics; withdrew T4′ robustness and T5 monotone claims; E6 re-scoped to E6′ (price of validity); **no confirmatory E6/E6′**: REVISE | audit + gates G1–G7 | `phase9/09` |
| 2026-11-04 (Ph. 10) | Price of validity defined as (exponent loss, evidence overhead); certified LR-set learned null adopted; EM denominators excluded from validity claims; confirmatory E6′ NOT authorised; theory (PO-13) prioritised | `phase10/12`, `phase10/11` |
| 2026-11-05 (Ph. 11 closure / WM programme) | Phase 11 closed; world-models programme started in `world-models-programme/`; pilot (precision vs stiction) completed; verdict REVISE; no novelty claimed | `world-models-programme/00`–`06` |
| 2026-11-04 (WM execution) | Learned-world-model study implemented (RSSM-style, det-GRU, ICI variant; families A,B,E); development evaluation only; H2 primary outcome not supported, H4 negative for ordinary probes; verdict REVISE; no novelty claimed | `world-models-programme/07`–`10` | – |
| 2026-11-04 (epistemic abstention) | Epistemic-state framework (A–D, certified vs uncertified abstention); new benchmark categories (4 exact-equivalence sources, approx, budget-limited, out-of-class); H1 supported, H2 only for same-signature source, H3 not supported (learned persistence test inverted), H4 conditional on hypothesis class; verdict REVISE; no novelty claimed | `world-models-programme/11`–`12` | – |
| 2026-11-04 (reassessment) | Programme comparison A/B/C; B selected in narrow form (determinism/computational origin of environment randomness; interface asymmetry replay vs prediction; bounded learners); C rejected (hidden-state augmentation); kick-world prototype built; no original contribution identified; verdict REVISE; roadmap gated on full-text literature reading | `world-models-programme/13`–`15` | – |
| 2026-11-05 (active discovery) | Novelty gate with 5 full texts (Dasgupta, Plan2Explore, Wagenmaker–Jamieson, Toth, Tao): D known for closed families, E not settled by sources read; MDW experiment (3 train + 2 held-out coupling constructions); no advantage of meta-trained world model or learned planner over direct probing/SysID/declared-class Bayes; Bayes GOF is the reliable out-of-family flag; verdict NO-GO for the proposed direction, programme REVISE toward misfit-triggered hypothesis generation | `world-models-programme/16`–`17` | – |

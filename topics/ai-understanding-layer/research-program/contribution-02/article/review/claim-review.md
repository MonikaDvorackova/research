---
id: note-contribution-02-article-review-claim-review
title: "Contribution 2 Article — Claim-by-Claim Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, review, claims]
refs: [../draft-v1.md, reviewer-report.md]
---

## Claim-by-Claim Review

Every major claim extracted from `../draft-v1.md`, in order of
appearance. Classification: SUPPORTED / SUPPORTED WITH QUALIFICATION /
SYNTHESIS / UNSUPPORTED / OVERSTATED / AMBIGUOUS.

| # | Claim (paraphrased) | Location | Class | Required change |
|---|---|---|---|---|
| 1 | Every artifact can still exist while reconstruction is impossible | Opening | SYNTHESIS | None — correctly framed as the article's thesis, not a bare fact |
| 2 | Existing mechanisms (versioning, audit logs, event sourcing, bitemporal, PROV, tracing) are real and often sufficient | "Version History..." | SUPPORTED | None |
| 3 | Retaining history and identifying what was consumed are different properties | "Version History..." | SYNTHESIS | None — correctly labeled as the article's argument, not an experimental fact in this sentence |
| 4 | "Consumed context" / "decision-context identifiability" definitions | "What a Historical Decision..." | SUPPORTED (definitional) | Optional: pre-empt the referential-integrity comparison (P2, `reviewer-report.md` Objection 5) |
| 5 | Regime B TC 1.00→0.00 on retroactive case; C stays 1.00 | Experiment 1 | SUPPORTED (numbers) / **OVERSTATED (interpretation)** | Numbers are exact and traceable (`empirical-traceability.md`). The word **"cannot"** in the same section's follow-on sentence ("A query against retained history... cannot substitute...") and **"No amount of additional bitemporal completeness fixes this"** are OVERSTATED — a `SYSTEM_TIME AS OF t0` query, using only retained data, does fix it. **Required: replace "no amount of... fixes this" with a claim scoped to the specific query algorithm tested; see `revision-plan-v2.md` P0.** |
| 6 | B and C identical (1.00/1.00) on forward-drift cases | Experiment 1 | SUPPORTED | None — verified exactly |
| 7 | The problem "isn't missing data — it's that the record's own account... has been revised" | Experiment 1 | SUPPORTED WITH QUALIFICATION | True of the data; not true that no query against that same data can recover the original answer. Needs the same P0 fix as claim 5. |
| 8 | FHC = 0.50 (Case 3) / 1.00 (Case 8, one combined case) for B; 0.00 for C everywhere | "The More Dangerous Failure" | SUPPORTED (numbers) | Exact, traceable |
| 9 | The dangerous failure is "internally coherent... and simply wrong," not missing data | "The More Dangerous Failure" | SUPPORTED WITH QUALIFICATION | True as far as it goes; should eventually note the wrongness is specific to the query algorithm tested, once claim 5's fix lands (dependent P0/P1) |
| 10 | "This is a result from one synthetic testbed... not a claim about how often this happens" | "The More Dangerous Failure" | SUPPORTED (self-limiting) | None — correct scope discipline |
| 11 | Original Case 10 failed to induce ambiguity; timestamps 60s from boundary | Experiment 2 | SUPPORTED | Verified directly against `experiment/src/cases.py` |
| 12 | Follow-up: B correctly reports AMBIGUOUS on every genuinely ambiguous case, never elsewhere; C resolves every case | Experiment 2 | SUPPORTED | Exact, traceable — `adr=1.0000` on all four ambiguous cases, `CORRECT_UNIQUE` for C throughout |
| 13 | This is a structurally different (honest vs. confident) failure than Experiment 1's | Experiment 2 | SYNTHESIS | Correctly labeled as interpretation; supported by the data pattern |
| 14 | F10-6: B given a non-binding causal event matches C exactly | Negative Control | SUPPORTED | Exact, traceable — identical scores on every metric |
| 15 | "Explicit, decision-time binding is what's required" does not survive F10-6 | Negative Control | SUPPORTED | Directly follows from claim 14 |
| 16 | "Some preserved relation... is necessary — binding is one way, not the only way" | Negative Control | SYNTHESIS | Correctly labeled; well-supported synthesis of claims 5 (qualified), 12, 14 |
| 17 | PROV models the right relation but lacks native valid-time intervals | "Not a New Provenance System" | SUPPORTED | Matches `../../prior-art-audit.md` Objection 1 exactly |
| 18 | Event sourcing solves it if it captures identifiers, not values | "Not a New Provenance System" | SUPPORTED | Directly demonstrated by F10-6 |
| 19 | "Bitemporal databases... solve it completely — for exactly the cases without retroactive correction" | "Not a New Provenance System" | **OVERSTATED** | Same root issue as claim 5 — bitemporal databases, queried with `SYSTEM_TIME AS OF t0`, also solve the retroactive-correction case using only retained data. **Required P0 fix**, see `revision-plan-v2.md`. |
| 20 | Tracing/audit logs/lineage: real, useful, but not schema'd to distinguish version identifiers from incidental context | "Not a New Provenance System" | SUPPORTED | Matches prior-art audit |
| 21 | "What's missing by default is not a new artifact type — it's the discipline of capturing identifiers rather than values" | "Not a New Provenance System" | SYNTHESIS | Reasonable summary once claim 19 is corrected — this sentence itself does not need to change, but it currently sits awkwardly next to the overstated claim 19 and should read consistently once fixed |
| 22 | The design question ("does a preserved relation exist that identifies... which version D consumed") | "The Property to Design For" | SYNTHESIS (practical restatement) | None |
| 23 | Two implementation patterns both close the gap "in these tests" | "Two Ways to Preserve It" | SUPPORTED | Scoped correctly ("in these tests"), not generalized |
| 24 | No prevalence claim / no universal-mechanism claim / binding not shown required / only two mechanisms tested / external validity open | "What the Experiments Do — and Do Not — Show" | SUPPORTED (all self-limiting) | None — add one more bullet per `section-review.md` once claim 19 is fixed |
| 25 | "Complete version history, competently implemented, is not sufficient for two independently demonstrated reasons" | "What the Experiments Do..." (summary sentence) | **AMBIGUOUS, borderline OVERSTATED** | "Competently implemented" is doing a lot of work this sentence doesn't earn for reason 1 (retroactive correction) once claim 19's fix is applied — "competently implemented" needs a footnote-level qualifier (competently implemented *valid-time* semantics; the transaction-time cutoff was not optimally chosen). See `revision-plan-v2.md` P0. |
| 26 | "The question is... did we preserve enough of a causal trail... and if the honest answer is 'we'd have to guess,' that gap is worth closing" | Closing | SYNTHESIS | Fine as a practical closing recommendation; not a new empirical claim |
| 27 | "Historical reconstructability is only one dimension of what it means to preserve understanding of a system over time" | Closing bridge sentence | SYNTHESIS (deliberately undeveloped) | None — correctly scoped per `../../drafting-readiness/contribution-boundary-check.md`; an editorial-taste question, not a claims issue |

## Words flagged for specific audit, per the authorizing brief's list

- **"enough"** — used appropriately throughout (e.g., "enough of a causal
  trail"), always in a qualified, non-absolute sense. No violation.
- **"cannot"** — one violation found: claim 5's "no amount of... fixes
  this" region. See P0 fix.
- **"requires"** — used correctly and consistently in the qualified sense
  ("requires a preserved relation," never "requires binding"). No
  violation.
- **"guarantees"** — not used anywhere in draft-v1's body. No violation
  (confirmed by grep).
- **"historical"** — used consistently and correctly as a scoping
  adjective, never expanded into a general historical/epistemological
  claim. No violation.
- **"causal"** — technically imprecise (risk of statistical-causal-
  inference misreading) per `reviewer-report.md`'s terminology attack;
  not a claim-support violation, but a precision issue. See
  `revision-plan-v2.md` P1.
- **"exact"** — used once ("exact model version," etc.) in the
  definitional sense (a specific version, not an approximate one) — no
  violation.
- **"every"** — checked every occurrence: "every artifact," "every
  version," "every single time," "every one of the same cases," "every
  case in the experiment." All are either (a) part of the opening
  scenario's premise (not a claim about the world) or (b) scoped
  explicitly to "in the experiment" / "in these tests." No unscoped
  universal claim about real systems uses "every." No violation.
- **"always"** — not used anywhere in draft-v1's body (confirmed by
  grep). No violation.
- **"uniquely"** — used correctly, exclusively in stating what was
  *narrowed away* ("explicit... binding is what's required" is what does
  NOT survive; "uniquely necessary" language is used to name the
  falsified claim, not to assert it). No violation.

## Summary

**Two claims (5/7 and 19, both stemming from the same root issue) are
OVERSTATED and require correction before v2. One claim (25) is
AMBIGUOUS/borderline and requires a qualifying phrase.** Every other
claim in the draft is SUPPORTED, SUPPORTED WITH QUALIFICATION, or
correctly labeled SYNTHESIS. No claim is flatly UNSUPPORTED. This is a
narrow, well-defined revision surface — one root technical issue with
three textual manifestations — not a broad claim-discipline failure.

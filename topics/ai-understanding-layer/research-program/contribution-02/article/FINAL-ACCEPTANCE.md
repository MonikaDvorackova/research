---
id: note-contribution-02-article-final-acceptance
title: "Article 2 Final Acceptance"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, final-acceptance]
refs: [draft-v2.md, review/VERDICT.md, review/BITEMPORAL-VERDICT.md]
---

# Article 2 Final Acceptance

Independent re-verification performed against `draft-v2.md` as it
currently stands, the full review package, and the committed raw
experiment results — not a re-trust of `draft-v2-audit.md`'s own prior
self-audit. Every empirical claim below was re-checked directly against
`../experiment/results/case_level_results.csv` and
`../experiment/followup-case10/results/case_level_results.csv` in this
session, fresh.

## Verdict

**ACCEPT.**

No blocking issue was found. Per Section 8's rule ("If there are ZERO
blocking issues: DO NOT modify draft-v2"), **draft-v2.md is unmodified by
this acceptance gate.**

## Frozen title

**"Retained Is Not Consumed: Why Version History Doesn't Guarantee
Decision Reconstruction"**

## Frozen contribution

> Article 2 contributes a controlled empirical demonstration that
> retaining every version of a decision's dependencies does not by
> itself guarantee that the decision can be uniquely reconstructed, that
> the gap manifests in at least two distinguishable ways (an honestly
> flagged ambiguity, and — in one specific, clean case — a genuine
> information-architecture gap), and that the property required to close
> it is a general preserved consumption relation rather than any one
> named architecture such as explicit decision-time binding.

## Explicit non-claim

> Article 2 does not claim that version history is generally
> insufficient, that bitemporal databases cannot solve reconstruction,
> that explicit binding is necessary, that a new architecture has been
> invented, or that this problem is unique to AI.

## Empirical acceptance

| Claim | Evidence | Status |
|---|---|---|
| Case 8 information gap | Primary experiment, Case 8: B `tc=0`, `fhc_rate=1.0000`; C `tc=1`, `fhc_rate=0.0000`; authority dimension has no raw-identity field in the event trace to cross-reference (`../review/bitemporal-verification.md` §2) | **PASS** |
| Cases 3/9 algorithm limitation | Primary experiment, Cases 3/9: B `tc=0`; event trace's `threshold_value_read=0.50` uniquely matches the correct policy row among retained candidates, unused by the tested algorithm (`../review/bitemporal-verification.md` §2, §6) | **PASS** |
| Timestamp ambiguity | Follow-up F10-2/3/4/5: `adr=1.0000` on each case's one genuinely ambiguous dimension, `0.0000`/blank elsewhere — re-verified fresh against `followup-case10/results/case_level_results.csv` in this session | **PASS** |
| AMBIGUOUS interpretation | Follow-up: `fhc_rate=0.0000` on all 12 rows (both regimes, all six cases) — re-verified fresh; article states AMBIGUOUS is "an honest non-answer, not a wrong one," matching the FHC=0 result exactly | **PASS** |
| F10-6 binding non-uniqueness | Follow-up F10-6: B and C rows identical on every column (`CORRECT_UNIQUE`/`CORRECT_UNIQUE`/`CORRECT_UNIQUE`, `tc=1`, `urr=1.0000`, `ac=1`, `fhc_rate=0.0000`) — re-verified fresh | **PASS** |
| No statistical generalization | Article's Limitations section states "not a statistical sample," "no p-value," "no claim of statistical representativeness"; no instance of "33+12 rows," "sample," or "p-value" language anywhere in the article (re-grepped in this session) | **PASS** |

**No FAIL. Acceptance proceeds.**

## Technical acceptance

| Item | Status | Basis |
|---|---|---|
| Bitemporal correctness | **PASS** | The article's claim ("system-versioned database implementations are explicitly designed to preserve a superseded record's original system time rather than overwrite it... the test system's retained history did not fully implement that discipline") matches, without exceeding, the two live-fetched sources in `../review/bitemporal-verification.md` §4 (Microsoft SQL Server and MariaDB documentation, both confirming original `ROW_START`/system time is preserved, never overwritten, on update). |
| Provenance (W3C PROV) correctness | **PASS** | "Usage relation... structurally exactly a consumption record" and "does not natively provide a valid-time interval on the Entity" match `../../prior-art-audit.md`'s directly-verified PROV-DM finding (point-in-time properties only: `generatedAtTime`/`usedAtTime`/`invalidatedAtTime`, no interval). |
| Event-sourcing correctness | **PASS** | The article's claim about typical instrumentation capturing values rather than identifiers is the programme's own, previously-verified empirical/conceptual finding (confirmed directly by the F10-6 negative control), correctly not over-attributed to the cited source ([5] supports the existence and shape of the pattern, not the values-vs-identifiers finding, which the article does not claim originates from Fowler). |
| Tracing (OpenTelemetry) correctness | **PASS** | "Span attributes are undifferentiated key-value pairs with no schema distinction" matches `../../prior-art-audit.md`'s directly-verified OpenTelemetry finding. |
| Terminology correctness | **PASS** | "Consumption relation" is defined at first use and used consistently thereafter; "causal" appears twice, the first occurrence explicitly disclaiming the statistical-causal-inference reading, the second a narrow, accurate technical description of span relationships unrelated to the article's own central term; "explainability" does not appear anywhere in the article, avoiding the XAI-conflation risk the title revision was meant to fix; zero occurrences of "State Is Not Knowledge" or bare "knowledge." |

## Citation acceptance

**PASS.** All five references audited:

- **[1] W3C PROV-DM** — exists, authoritative (W3C Recommendation), supports the exact sentence it's attached to, not dangling (cited once, appropriately).
- **[2] Microsoft SQL Server system-versioned temporal tables** — exists, authoritative vendor documentation of the SQL:2011 model, supports the exact bitemporal claim, cited twice, not dangling.
- **[3] MariaDB system-versioned tables** — exists, authoritative vendor documentation of the same standard, independently corroborates [2], cited twice, not dangling.
- **[4] OpenTelemetry Traces** — exists, authoritative (project's own documentation), supports the exact tracing claim, cited twice, not dangling.
- **[5] Fowler, "Event Sourcing"** — exists, is the standard, widely-cited reference for this pattern, supports naming the pattern (not over-extended to support the values-vs-identifiers claim, which is correctly presented as this programme's own finding), cited once inline (confirmed present — the dangling-reference issue caught and fixed during v2's drafting pass remains fixed).

No citation found wrong, dangling, or materially exceeding its source.

## Boundary acceptance

- **Contribution 1 untouched:** **PASS** — `git diff` against the prior commit shows zero changes under `article-01-decision-level-control/`.
- **Contribution 3 unconsumed:** **PASS** — re-grepped `draft-v2.md` for "understanding layer," "capability... understanding," "epistemic debt," "fragmentation": zero matches. Bare "understanding": exactly one occurrence, the same permitted, undeveloped closing bridge sentence carried from draft-v1, not expanded.
- **O'Reilly untouched:** **PASS** — zero changes to either O'Reilly draft.

## Remaining non-blocking issues

Carried forward from `editorial-notes-v2.md`, genuinely optional, no action taken:

- Whether to keep or cut the closing bridge sentence ("Historical reconstructability is only one dimension...") — editorial taste.
- Whether to reinstate more numeric density in the two experiment sections — stylistic alternative, not a correctness gap.
- Whether the restructured (follow-up-first) order reads better than draft-v1's chronological order — narrative-flow preference.
- Diagram production (none of the three planned diagrams from `../drafting-readiness/diagram-plan.md` are rendered as images in either draft) — deferred, as in draft-v1, no repository convention for rendering exists yet.
- Publication venue formatting — not yet chosen, out of scope for this gate.

## Publication state

**ARTICLE COMPLETE — publication-ready at the argument/evidence level;
venue-specific editorial adaptation may still be required.**

## Later O'Reilly synthesis

Article 2 may later contribute:

- The retained-vs-consumed distinction.
- Unique reconstruction vs. retained history as separate properties.
- Honest ambiguity vs. confident wrongness as distinct failure modes.
- Consumption relation as the relevant engineering property.

Article 2 should **not** force the O'Reilly synthesis to reproduce
experimental implementation details, case numbering, metric tables, or
the detailed bitemporal-verification history. No O'Reilly drafting was
performed in this session.

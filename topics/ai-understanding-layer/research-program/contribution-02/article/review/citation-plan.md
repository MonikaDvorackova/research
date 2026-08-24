---
id: note-contribution-02-article-review-citation-plan
title: "Contribution 2 Article — Citation Plan"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, review, citations]
refs: [../draft-v1.md, ../../prior-art-audit.md]
---

## Citation Plan

Draft-v1's body currently has zero inline citations
(`../editorial-notes.md` already flags this as an open decision). This
plan identifies every externally-sourced factual/technical claim in the
draft and its required source, using sources already verified via live
retrieval during the prior-art audit (`../../prior-art-audit.md`, dated
2026-08-22/23) wherever possible. **No citation below is fabricated; any
source not already verified in this programme is explicitly flagged.**

| Claim in draft-v1 | Location | Required source | Preferred primary source | Importance |
|---|---|---|---|---|
| Bitemporal databases solved "what was true at a given point in time" since the 1980s | "Version History Is Not Decision History" | Bitemporal/temporal database theory origin | Snodgrass, R.T. (ed.), *The TSQL2 Temporal Query Language* material; Snodgrass, "Developing Time-Oriented Database Applications in SQL" | **REQUIRED** |
| Bitemporal databases as a standardized query mechanism (valid-time/transaction-time) | "This Is Not a New Provenance System" | SQL:2011 temporal extensions | ISO/IEC 9075-2:2011 (SQL:2011), Part 2, temporal features; secondary: Kulkarni & Michels, "Temporal features in SQL:2011," SIGMOD Record 2012 | **REQUIRED** |
| **`SYSTEM_TIME AS OF t0` as a standard bitemporal query idiom that avoids the retroactive-correction failure using only Regime B's own data** | New material required for the P0 fix (`revision-plan-v2.md`) | SQL:2011 `SYSTEM_TIME` period specification, or Snodgrass's transaction-time "as of" query semantics | ISO/IEC 9075-2:2011; Kulkarni & Michels 2012 (same source as above, different section) | **REQUIRED — EXTERNAL VERIFICATION REQUIRED.** This specific claim (that SQL:2011 or equivalent bitemporal systems support anchoring the transaction-time cutoff to an arbitrary past instant, not only "now") was reasoned from general bitemporal-database semantics during this review, not confirmed against a freshly fetched primary source in this session. Before this claim appears in v2's body, re-fetch and confirm the exact SQL:2011 `SYSTEM_TIME AS OF <timestamp>` (or vendor-equivalent, e.g., PostgreSQL/temporal-table extensions, SQL Server temporal tables `FOR SYSTEM_TIME AS OF`) syntax and semantics against a primary or authoritative secondary source. |
| W3C PROV's Usage/Association/Delegation model and its point-in-time-only temporal properties | "This Is Not a New Provenance System" | W3C PROV-DM specification | W3C, "PROV-DM: The PROV Data Model," W3C Recommendation, 30 April 2013, https://www.w3.org/TR/prov-dm/ | **REQUIRED** (already fetched and read directly per `../../prior-art-audit.md`'s stated methodology) |
| Event sourcing pattern and its default behavior (captures domain events, not necessarily external reads) | "This Is Not a New Provenance System" | Event sourcing primary/recognized source | Fowler, M., "Event Sourcing," 2005, https://martinfowler.com/eaaDev/EventSourcing.html; secondary: Microsoft Learn, "Event Sourcing pattern" | **REQUIRED** |
| Distributed tracing / OpenTelemetry span attributes as undifferentiated key-value pairs | "This Is Not a New Provenance System" | OpenTelemetry specification | OpenTelemetry, "Traces," https://opentelemetry.io/docs/concepts/signals/traces/; OpenTelemetry Specification (GitHub) | **STRONGLY RECOMMENDED** |
| Audit logs — general reference (grouped with tracing/lineage in one paragraph, not individually argued) | "This Is Not a New Provenance System" | NIST log-management guidance, if audit logs are named explicitly in v2 | NIST SP 800-92, "Guide to Computer Security Log Management" | **OPTIONAL** — only required if v2 gives audit logs their own sentence rather than a grouped mention |
| Model/data lineage tooling (grouped mention) | "This Is Not a New Provenance System" | ML platform lineage documentation, if named explicitly | MLflow Documentation, "ML Experiment Tracking" / "ML Model Registry," https://mlflow.org/docs/latest/ | **OPTIONAL** — same condition as above |
| in-toto / SLSA / Sigstore | Not currently named in draft-v1's body | Not required unless added in v2 | in-toto Attestation Framework spec; slsa.dev v1.0; Sigstore/Rekor docs | **OPTIONAL** — no citation debt exists unless this mechanism is added to the article |

## Sources NOT required

- No citation is needed for any *experimental* result — those are
  internal artifacts (`../../experiment/`, `../../experiment/followup-case10/`),
  correctly treated as primary data from this programme, not external
  literature. `empirical-traceability.md` covers their sourcing
  separately from this citation plan, per the authorizing brief's
  explicit instruction to keep "our experimental result" separate from
  "external prior art."
- No citation is needed for the ACM reproducibility taxonomy — draft-v1
  does not currently discuss replay vs. reconstruction at all (that
  distinction lives in `../../collision-tests.md` Task 6 but was not
  carried into the article). Not a gap requiring action unless a future
  revision adds this material.
- No citation is needed for XACML/PDP-PEP — mentioned only in
  `../../drafting-readiness/prior-art-matrix.md`, not in draft-v1's body,
  and that matrix entry was itself already flagged there as not
  independently re-verified in this programme; carries no obligation for
  the article unless added.

## Count

- **REQUIRED: 6** (bitemporal origin; SQL:2011 temporal extensions; the
  new `SYSTEM_TIME AS OF` claim; W3C PROV-DM; event sourcing; distributed
  tracing is STRONGLY RECOMMENDED not REQUIRED, adjusting the strict
  REQUIRED count to 5 core mechanism citations plus the new P0-driven
  citation = 6 total REQUIRED-tier items.)
- **STRONGLY RECOMMENDED: 1** (OpenTelemetry).
- **OPTIONAL: 3** (audit logs, lineage tooling, in-toto/SLSA/Sigstore —
  all conditional on v2 adding material not currently in draft-v1).

## External verification still required before v2 inserts citations

**One item, and it is the most important one in this table:** the
`SYSTEM_TIME AS OF t0` bitemporal query claim underlying this review's
central technical finding (`reviewer-report.md`). This must be confirmed
against a primary or authoritative secondary source before it is used to
justify the P0 revision in `revision-plan-v2.md` — the *logical*
argument (a transaction-time cutoff anchored to t0 rather than to query
time avoids the retroactive-correction failure) is sound and verifiable
by direct inspection of the experiment's own data model regardless of
citation status, but the claim that this is *standard, named bitemporal
practice* (as opposed to a novel technique invented for this review)
should not be asserted in the article without checking it against
SQL:2011 or an equivalent authoritative source first.

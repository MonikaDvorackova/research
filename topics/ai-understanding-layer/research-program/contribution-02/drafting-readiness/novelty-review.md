---
id: note-contribution-02-drafting-novelty-review
title: "Contribution 2 Drafting Readiness — Adversarial Novelty Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, novelty-review, adversarial]
refs: [../collision-tests.md, ../prior-art-audit.md, ../novelty-verdict.md, contribution-definition.md]
---

## Adversarial Novelty Review

This document re-runs the adversarial collision test from
`../collision-tests.md` against the **updated, post-experiment,
causal-relation thesis** (`../novelty-verdict.md`'s follow-up-dated
update), not the original binding-centric formulation. Several answers
below differ from `../collision-tests.md`'s original wording for exactly
this reason: the narrowed thesis is *more* exposed to some objections
(anything that supplies a causal relation now counts as a full solution,
not merely a partial one) and *no less* exposed to others. Where an
objection destroys part of the claim, the claim is narrowed here, not
defended.

Objections 1–9 restate and re-evaluate `../collision-tests.md`'s own nine
objections under the new thesis. Objection 10 is new.

---

### 1. Isn't this just provenance (W3C PROV)?

**Strongest version:** PROV's Entity/Activity/Agent/Usage/Association
model already expresses exactly "which evidence was used by which
activity, under whose authority" — a causal relation, fully formalized
since 2013.

**Correct / partly correct / incorrect:** Partly correct, and *more*
correct under the narrowed thesis than under the original. A populated
PROV graph, correctly capturing Usage relations with version-identified
Entities, **is** a preserved causal relation — the F10-6 negative control
shows this class of solution is not a strawman to dismiss.

**Evidence from prior art:** `../collision-tests.md` Objection 1,
confirmed by direct inspection of PROV-DM.

**What remains distinctive:** PROV's temporal properties are point-in-time
markers, not valid-time intervals — it cannot natively express "this was
the operative policy from t_a to t_b," which the primary experiment's
retroactive-correction mechanism specifically exploits. A PROV Usage
relation pointing at a value (not a version identifier with a validity
interval) still leaves the retroactive-correction failure mode open, even
though it would resolve the Case 10 follow-up's precision-ambiguity
failure mode. **The two experiments test two different failure modes, and
PROV-as-typically-populated only closes one of them.**

**How the article must phrase this:** PROV is one legitimate way to
implement the required causal relation for the concurrency-ambiguity
mechanism; it does not, by itself, close the retroactive-correction
mechanism unless extended with valid-time semantics on the Entities it
references.

---

### 2. Isn't this just event sourcing?

**Strongest version:** An append-only event log capturing every state
transition, replayed to t0, reconstructs exact state at t0 — including,
if the events are rich enough, which version of every dependency was
read.

**Correct / partly correct / incorrect:** Partly correct, and this
objection is where the narrowed thesis concedes the most ground.
`../preservation-regimes.md`'s own event-sourcing analysis already stated,
before any experiment ran, that "explicit causal event recording of
version identifiers at consultation time" and "explicit decision-time
binding" are two descriptions of the same discipline. F10-6 is the
empirical confirmation of exactly this: a plain event-sourced consumption
record (never called "binding") fully matched Regime C.

**Evidence from prior art:** `../collision-tests.md` Objection 2; primary
experiment's Case 5 (evidence supersession, solved by B's event trace
without any binding); follow-up's F10-6.

**What remains distinctive:** Event sourcing captures the system's *own*
domain events by default; it does not, without deliberate instrumentation,
capture *externally sourced, mutable reads* as version-identified events
— by default it captures **values** ("threshold read: 0.62"), not
**version identifiers** ("policy v7 read"). The primary experiment's
Regime B is exactly this: a strong, genuine event-sourcing implementation
that captures raw values and therefore fails specifically where version
identity, not value, is what matters (retroactive correction).

**How the article must phrase this:** Event sourcing is not a distinct
category from the proposed solution — it is one of its legitimate
implementations, *if and only if* it is deliberately extended to capture
version identifiers (not raw values) for every dependency at consultation
time. Most real event-sourcing implementations, per the audit's own
finding, do not do this by default.

---

### 3. Isn't this just bitemporal data?

**Strongest version:** Store every dependency (policy, authority) with
valid-time and transaction-time columns per Snodgrass/SQL:2011, and "what
was true at t0" becomes a solved, standard query.

**Correct / partly correct / incorrect:** Partly correct, and this is
where the primary experiment's central result lives. Bitemporal storage,
correctly implemented (as Regime B was, deliberately, to avoid
strawmanning it), is **necessary but not sufficient**: the primary
experiment showed a genuinely correct bitemporal query returning a
confidently wrong answer once a retroactive correction was recorded,
precisely because the query has no way to distinguish "what we now believe
was true at t0" from "what the decision-maker actually relied on at t0."

**Evidence from prior art:** `../collision-tests.md` Objection 4
(theoretical); primary experiment Cases 3, 8, 9 (empirical confirmation,
TC: B=0.00, C=1.00, categorically).

**What remains distinctive:** This objection is the one the primary
experiment was specifically designed to test, and it survives cleanly:
bitemporal completeness is not sufficient under retroactive correction,
demonstrated, not merely argued. It says nothing, either way, about the
follow-up's precision-ambiguity mechanism (bitemporal semantics were not
what failed there — observable timestamp granularity was).

**How the article must phrase this:** Bitemporal modeling is the correct
theoretical answer for policy/authority validity in the *absence* of
retroactive correction (confirmed: B=C on Cases 1, 2, 4, 6); it is
demonstrably insufficient once retroactive correction occurs, and this is
not a hypothetical — it was measured.

---

### 4. Isn't this just distributed tracing?

**Strongest version:** OpenTelemetry captures the full execution path and
whatever attributes a developer chooses to attach — including, if they
choose, version identifiers for every dependency consulted.

**Correct / partly correct / incorrect:** Partly correct in principle,
incorrect as a default-practice claim.

**Evidence from prior art:** `../collision-tests.md` Objection 6 — OTel
span attributes are undifferentiated key-value pairs with no schema
distinction between "this is the applicable policy version" and
incidental debug context; typical retention windows (days-to-weeks) are
also mismatched with a reconstruction problem defined to arise months
later.

**What remains distinctive:** Nothing structurally distinct from
Objection 2's answer — tracing is event sourcing's cousin for the same
purpose, and the same "values vs. version identifiers" distinction
applies. The operational retention-horizon mismatch is a separate,
practical (not conceptual) reason tracing under-serves this problem by
default.

**How the article must phrase this:** A trace *could* carry the required
causal relation if its attributes were deliberately schema'd to
distinguish version-identifying fields from incidental context and
retained long enough — neither is typical practice today.

---

### 5. Isn't this just foreign keys / version IDs?

**Strongest version:** Every table already has a primary key; every
version already has an ID; joining a decision row to a policy_version_id
column is not a research contribution, it's Tuesday.

**Correct / partly correct / incorrect:** Correct that the *mechanism* is
trivial — and this must be conceded plainly, not argued around.

**Evidence from prior art:** `../minimal-decision-record.md`'s own
conclusion: the binding record "does not assert any new fact about the
world... it asserts exactly one new thing" — a reference. This is, by
the contribution's own account, mechanically as simple as a foreign key.

**What remains distinctive:** The contribution was never that adding a
foreign key is hard. It is that **doing so is not standard practice by
default** for the specific dimensions (policy-as-config, delegated
authority, live retrieval) the audit found are rarely versioned this way
at all, let alone bound per-decision — and that *omitting* it produces a
measurable, not merely theoretical, failure (both experiments). A trivial
mechanism, absent by default, producing a measurable failure when absent,
is still a legitimate — if modest — engineering finding.

**How the article must phrase this:** Explicitly concede the mechanism is
simple. The contribution is diagnostic and empirical (identifying the gap
and measuring its consequence), not mechanistic (the fix, once named, is
not novel engineering).

---

### 6. Isn't this just W3C PROV?

Duplicate of Objection 1 in the authorizing brief's list; answered there.
No additional distinct content — the article should merge these into one
treatment to avoid arguing against the same objection twice under
different numbers.

---

### 7. Isn't this just audit logging?

**Strongest version:** EU AI Act Article 12 already mandates automatic,
retained logging for high-risk systems; NIST SP 800-92 already covers
tamper-evident log integrity. A compliant system already produces the
required durable record.

**Correct / partly correct / incorrect:** Incorrect as stated, for a
specific, checkable reason.

**Evidence from prior art:** `../collision-tests.md` Objection 3 — Article
12's specified minimum content (period of use, reference database,
matched input, verifying person) is execution/outcome-scoped; it does not
require recording which policy version applied or preserving a causal
relation to it. Tamper-evidence (integrity — was the record altered)
is a different property from completeness (does the record contain what's
needed) and the objection conflates them.

**What remains distinctive:** Fully survives, unchanged by the narrowed
thesis — this objection was never really about causal linkage in the
first place, it was about record existence and integrity, which are
orthogonal.

**How the article must phrase this:** A fully Article-12-compliant, fully
tamper-evident log can still fail sub-problems D/E/G entirely; regulatory
minimums are not a proxy for reconstruction sufficiency.

---

### 8. Isn't this just reproducibility?

**Strongest version:** Reproducible-ML practice (versioned code/data/
model, deterministic pipelines) already solves "get the same result
again."

**Correct / partly correct / incorrect:** Correct, and orthogonal rather
than competing — this objection targets a different property
(**replay**) than the one this contribution addresses (**reconstruction**
of *why* a result was authorized).

**Evidence from prior art:** `../collision-tests.md` Objection 5 and Task
6 — the replay/reconstruction distinction, the cleanest surviving
distinction in the original audit, unaffected by the causal-relation
narrowing (it was never about binding specifically).

**What remains distinctive:** Fully survives. Reproducing an output tells
you nothing about which threshold applied to it, or under what policy
version, or by whose authority.

**How the article must phrase this:** State plainly that replay and
reconstruction are different properties, cite the ACM reproducibility
taxonomy as the adjacent-but-non-overlapping formalization for replay
only, and do not let a reader conflate "we can regenerate the number"
with "we know why the number authorized an action."

---

### 9. Isn't this just data lineage?

**Strongest version:** Model/data lineage tools (dataset lineage in MLflow,
lineage graphs in modern data catalogs) already track which data produced
which model, which model produced which output.

**Correct / partly correct / incorrect:** Partly correct, narrowly scoped.

**Evidence from prior art:** `../prior-art-audit.md`'s MLflow entry —
lineage stops at "which run produced this model," not "which production
decision consumed this model version under what authority." Training-time
lineage and decision-time consumption are different edges in the graph.

**What remains distinctive:** Lineage tooling answers a training-pipeline
question; the contribution's object is a runtime, per-decision question.
The two are structurally similar (both are "what produced/consumed what"
graphs) but scoped to different life-cycle stages, and no surveyed lineage
tool extends its model to runtime decision consumption of policy/authority
context.

**How the article must phrase this:** Lineage is the right graph shape,
applied to the wrong life-cycle stage by default — extending it to
runtime decision consumption is exactly the synthesis this contribution
proposes, not something existing lineage tooling already does.

---

### 10. Isn't this obvious good engineering — wouldn't any competent architect already do this?

**Strongest version:** No practicing systems engineer needs a research
programme to be told "record which config version you used." This is
Engineering 101, dressed up in academic language.

**Correct / partly correct / incorrect:** Partly correct as a normative
claim about what *good* engineering would do; incorrect as a description
of *default* practice, which is the only claim this contribution actually
makes.

**Evidence from prior art:** the prior-art audit's own repeated finding
(`../prior-art-audit.md`) that prompt stores, retrieval corpora, and
policy-as-config services are "essentially never built with valid-time
semantics by default," combined with both experiments' own design choice
to make Regime B *stronger* than typical real tooling
(`../experiment/experiment-design/validity-and-confounders.md`: "this
makes Regime B, if anything, more favorable to H0 than a typical real
system would be") — and Regime B still failed under both tested
mechanisms.

**What remains distinctive:** The contribution is not "this is hard
engineering" — it explicitly is not (see Objection 5) — it is "this is
not what happens by default, even in systems built more carefully than
typical practice, and the consequence of its absence is measurable, not
merely aesthetic." A reviewer who has personally always done this is
agreeing with the article's recommendation, not refuting its diagnosis of
default practice.

**How the article must phrase this:** Concede immediately that the fix is
unglamorous. The article's contribution is naming the gap precisely,
showing it is not closed by strong versioning/event-sourcing/bitemporal
practice alone, and measuring two independent ways it manifests — not
claiming engineering difficulty.

---

## Summary

| # | Objection | Verdict | Claim narrowed? |
|---|---|---|---|
| 1 | Just provenance | Survives, narrowly | No — but scope stated: closes precision-ambiguity, not retroactive-correction |
| 2 | Just event sourcing | Survives, narrowly — biggest concession | **Yes** — event sourcing IS a solution if it captures identifiers, per F10-6 |
| 3 | Just bitemporal data | Survives cleanly — strongest empirical confirmation | No |
| 4 | Just tracing | Survives, narrowly | No — same concession as #2 applies if attributes are schema'd |
| 5 | Just foreign keys | Mechanism conceded entirely | **Yes** — contribution is diagnostic/empirical, not mechanistic |
| 6 | Just PROV (dup.) | Merged with #1 | — |
| 7 | Just audit logging | Survives cleanly | No |
| 8 | Just reproducibility | Survives cleanly — orthogonal, not competing | No |
| 9 | Just data lineage | Survives, narrowly | No — scope stated: training-time vs. runtime |
| 10 | Just obvious engineering | Survives — normative/descriptive distinction holds | No — but framing must lead with the concession, not fight it |

**No objection destroys the contribution outright.** Two (2, 5) require
real, disclosed narrowing already reflected in `contribution-definition.md`
and `../novelty-verdict.md`'s post-follow-up update. The contribution that
survives this pass is smaller than the one the original design docs
described before either experiment ran — that is the correct, expected
outcome of taking this review seriously, not a failure of it.

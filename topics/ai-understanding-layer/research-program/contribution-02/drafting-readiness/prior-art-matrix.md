---
id: note-contribution-02-drafting-prior-art-matrix
title: "Contribution 2 Drafting Readiness — Prior-Art Collision Matrix"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, prior-art]
refs: [../prior-art-audit.md, ../collision-tests.md, novelty-review.md]
---

## Prior-Art Collision Matrix

Restructures `../prior-art-audit.md`'s matrix around the columns this
review requires, adds mechanisms not separately broken out there
(ordinary version control, ML model registries as a distinct row from
MLflow's tracking half, XACML/PDP-PEP), and adds one column
(**ambiguity behavior**) the original audit did not need but the Case 10
follow-up makes directly relevant: does the mechanism, when the record
is genuinely insufficient, fail silently/confidently, or does it (or can
it) honestly signal insufficiency?

Where a mechanism, correctly and fully populated, already provides the
required property, this is stated plainly — per the authorizing
instruction, this does not by itself kill the article; see
`contribution-definition.md`'s "Contribution" section for how the
surviving claim is scoped instead.

| Mechanism / literature | Preserves artifact versions | Preserves valid time | Preserves transaction time | Preserves event order | Preserves causal relation (decision → consumed x) | Binds decision to consumed context | Supports historical reconstruction | Ambiguity behavior | Relation to Contribution 2 | Citation |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ordinary version control (git)** | Yes, for code | No native valid-time (commit time only) | Yes (commit time is a transaction-time-like fact) | Yes, causally (commit DAG) | No — records code history, not which commit a specific *decision* consumed | No | For code/execution (sub-problem B) only | N/A — not decision-facing | Baseline positive control: shows history preservation alone (for code) does not, by itself, address decision-context binding | Git documentation; standard practice |
| **Audit logs (NIST SP 800-92)** | No, unless schema-specific | No | Event-timestamp only | Yes, by log order | No, unless organization adds it | No, by the standard's own baseline fields | Whatever fields the org's logging policy specifies — not policy/evidence/authority validity by default | Typically fails silently: a missing field is simply absent, not flagged as "insufficient for reconstruction" | Confirms integrity ≠ completeness (Objection 3) | NIST SP 800-92 |
| **EU AI Act, Article 12** | Partial (one system class's minimum content) | No | Event-timestamp (period of use) | Yes | No, not in specified minimum | No | Execution/outcome-scoped only | Silent — the Article specifies minimum content, not a signal for when that minimum is insufficient | Strongest regulatory anchor; still short of D/E/G | Regulation (EU) 2024/1689, Art. 12 |
| **Event sourcing (general)** | Yes, for internally modeled domain events | No native valid-time unless added | Event-timestamp = transaction time by construction | Yes, natively (this is the pattern's core property) | **Only if deliberately instrumented** to capture version identifiers, not raw values, at consultation time | Only if so instrumented | Full internal-state replay (A/B); C/D/E only if externally-sourced reads are modeled as events | If instrumented to capture identifiers: honest, unique answer. If capturing only values (typical): silently produces the confidently-wrong-or-ambiguous behavior tested by both experiments' Regime B | **F10-6 confirms**: an ordinary consumption event, not framed as "binding," fully closes the gap when present | Fowler, "Event Sourcing," 2005 |
| **Bitemporal databases (Snodgrass; SQL:2011)** | Yes, natively | **Yes, natively — this is the mechanism's purpose** | Yes, natively | N/A (not an ordering mechanism) | No — bitemporal completeness answers "what was valid then," not "which slice this decision consumed" | No, not by itself | D and E completely, in theory, wherever applied — **but see ambiguity behavior** | **Confidently wrong under retroactive correction** (primary experiment, Cases 3/8/9: a correct valid-time query, run after a backdated correction, returns a different, wrong answer with no signal that this occurred) | **Primary experiment's central empirical result**: necessary, not sufficient | Snodgrass (TSQL2); SQL:2011; primary experiment `../experiment/RESULT.md` |
| **Distributed tracing (OpenTelemetry)** | Only via undifferentiated span attributes | No | Span start/end only | Yes, causally (span parent/child) | Only if attributes happen to encode version identifiers, with no schema guarantee | No native concept | B (execution) with high fidelity; C/D/E only informally | No structured signal — attributes are freeform key-value, so absence of the needed field is indistinguishable from its presence to an automated reconstructor | Same "values vs. identifiers" gap as event sourcing, plus a retention-horizon mismatch | OpenTelemetry Specification |
| **Data/model lineage (e.g., MLflow dataset lineage, catalog lineage graphs)** | Yes, for training-time inputs | No | Run-timestamp only | Yes, for the training DAG | Training-time only: which data produced which model — not runtime decision consumption | No — lineage stops at model registration, not per-decision use | Training pipeline provenance only | N/A for runtime decisions — lineage tools are not typically queried for "did decision D use model version X under policy Y" at all | Right graph shape, wrong life-cycle stage (see novelty-review.md Objection 9) | MLflow docs; general data-catalog lineage practice |
| **ML model registries (MLflow Model Registry, Vertex AI Model Registry, Unity Catalog)** | Yes, for model artifacts | No (registry "stage" is current-state, not valid-time) | Registration timestamp only | N/A | No — registry answers "what is the current/staged model," not "which version this decision consumed" | No | B (which model version exists/is staged) | Silent — a registry query returns the current stage regardless of whether that matches what a past decision actually used | Solves model versioning; has nothing to say about prompts, retrieval, or per-decision policy/authority binding | `../prior-art-audit.md`'s MLflow entry |
| **W3C PROV (PROV-DM)** | If Entities are version-identified (not required by the model) | **No — point-in-time only** (generatedAtTime/usedAtTime/invalidatedAtTime), no valid-time interval | Not modeled | Yes, via Generation/Usage temporal ordering | **Yes, structurally** — Usage/Association/Delegation relations are exactly a causal decision→context relation, once populated | Yes, if populated with version-identified Entities | Lineage reconstruction, once populated | If Entities are values rather than version identifiers: same silent gap as event sourcing/tracing. If version-identified: honest, structural answer, but with no valid-time containment check | **Closes the follow-up's precision-ambiguity mechanism if populated correctly; does not close the primary experiment's retroactive-correction mechanism without a valid-time extension** | W3C, PROV-DM, 2013 |
| **in-toto Attestation Framework / SLSA / Sigstore (Rekor)** | Yes, per signed Statement | No — existence-before-time only | Yes, via Rekor inclusion time | Via Merkle-tree log order | Yes, if the Predicate schema includes version references — no AI-decision predicate exists today | Yes, if so designed — not by default (no such predicate type is standardized) | Strong integrity; content only as complete as the (undefined) predicate schema | Existence-integrity is strong (tamper-evidence); validity-interval semantics are absent, so the same retroactive-correction risk as bitemporal-without-binding applies if the predicate references live rather than version-pinned facts | Closest production-grade container mechanism; the AI-decision predicate type is genuinely undone design work | in-toto spec; slsa.dev v1.0; Sigstore/Rekor docs |
| **XACML / PDP-PEP architecture** | No native versioning of policy sets | No native valid-time | No | N/A | No — a PDP evaluates the *current* policy set against a request; it does not, by the standard, retain which policy-set version produced a specific past decision | No | Not designed for later reconstruction at all — it is a request-time authorization mechanism, not a preservation mechanism | Silent by design — a PDP's job ends at the decision response; nothing in the architecture flags that a later query about "what policy applied to decision D" cannot be answered from the PDP alone | Structurally the authority/policy analogue of "an output, not a decision record" — confirms the audit's finding that authorization architectures are evaluation-time, not preservation-time, by default | OASIS XACML 3.0 specification |

## Reading the matrix

**No cell in this table is forced.** Where a mechanism, correctly and
fully populated (bitemporal databases; PROV with version-identified
Entities; event sourcing capturing identifiers; an in-toto predicate
designed to include version references), already supplies the needed
property, the matrix says so directly — consistent with
`../prior-art-audit.md`'s own explicit statement that "if the answer had
been 'yes, [X] alone resolves it,' this would directly weaken the
contribution... this is precisely why the brief requires testing it head
on."

**What the matrix shows the contribution actually is**, reading down the
"ambiguity behavior" column: every mechanism surveyed either (a) has no
structured signal for its own insufficiency (audit logs, tracing, model
registries, XACML) — meaning a caller cannot distinguish "this answer is
reliable" from "this answer is a guess" — or (b) achieves the required
property only *conditionally*, dependent on a deliberate instrumentation
choice (event sourcing, PROV, in-toto) that current tooling does not make
by default (per the prior-art audit's own repeated finding that
prompt/retrieval/policy stores are "essentially never built this way").
Only bitemporal databases achieve the property unconditionally within
their own scope (D, E) — and the primary experiment shows that scope
itself has a specific, measured limit (retroactive correction).

**The contribution, restated once more against this matrix:** not a new
row in this table, but the empirically demonstrated claim that (1) no
existing row's *default* configuration closes the gap for the AI-specific
dependency set, (2) the gap has at least two independently measurable
failure modes (retroactive correction; precision-loss ambiguity), and (3)
closing it requires a *causal relation*, which several existing rows can
supply if deliberately configured to do so — this is a narrower, more
defensible claim than "none of these mechanisms can solve it," which the
matrix does not support and the contribution does not make.

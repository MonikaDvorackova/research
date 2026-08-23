---
id: note-contribution-02-collision-tests
title: "Contribution 2 — Collision Tests Against the Strongest Objections"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, collision-tests, adversarial-audit]
refs: [prior-art-audit.md, problem-formalization.md]
---

## Contribution 2 — Collision Tests

Scope: Task 5 (the nine named objections) and Task 6 (replay vs.
reconstruction). Instruction is explicit: do not protect the thesis. Each
objection is formulated in its strongest form, credited for what it gets
right, and only then tested for what survives.

---

### Objection 1 — "This is just provenance" (W3C PROV)

**Strongest version:** PROV-DM's Entity/Activity/Agent model, with
Generation, Usage, Derivation, Attribution, Association, and Delegation,
already gives you exactly "which evidence (Entity) was used by which process
(Activity), performed under whose authority (Agent, via Association and
Delegation)." That is evidence and authority reconstruction, fully
formalized, as a W3C Recommendation since 2013.

**What it gets right:** This is a genuine, structural match for representing
C (evidence) and E (authority) relationships, once the relevant entities are
captured. It is not a straw man — PROV is exactly the right shape of graph
for a decision's lineage.

**Does the contribution survive?** Yes, narrowly, for two confirmed reasons
(verified by direct inspection of the PROV-DM specification, not inferred):

1. **No valid-time semantics.** PROV-DM's temporal properties are
   instantaneous markers (`generatedAtTime`, `usedAtTime`,
   `invalidatedAtTime`) — points, not intervals. It cannot natively express
   "policy P was the operative version from t_a to t_b," which is exactly
   what sub-problem D requires. A PROV graph can tell you *when* a Usage
   event occurred; it cannot, without an added extension, tell you whether
   the Entity used was still the *valid* one under a separately time-varying
   policy.
2. **No normative vocabulary.** PROV models "who did what to what," not
   "was this evidence sufficient" or "was this agent authorized under the
   rule in force at the time." Reconstructing G requires a normative
   judgment PROV has no predicate for.

**Remaining difference:** PROV would need a bitemporal extension plus a
requirements/adequacy predicate to close sub-problems D and G. This is a
real, buildable extension — not a deep theoretical gap — but it does not
exist today as a named, ready-made solution.

**Evidence that would demonstrate the difference:** A real PROV graph for a
decision whose evidence and policy both later changed, where a query for
"was the evidence used still valid under the policy in force at t0" cannot
be answered from the graph alone without externally supplied valid-time
metadata.

---

### Objection 2 — "This is just event sourcing"

**Strongest version:** If every state transition is captured as an immutable
event in an append-only log, replaying to t0 reconstructs the exact state at
t0. Nothing is lost, by construction.

**What it gets right:** For internal application state (sub-problems A and
B), this is close to fully true, and event sourcing is arguably the
strongest existing mechanism for that specific claim.

**Does the contribution survive?** Yes. Event sourcing captures the
system's *own* domain events. It does not, by default, capture **externally
sourced, mutable reads** — a retrieval call's response, a live policy
service's answer, a prompt template resolved at request time — unless the
architecture deliberately emits an event for each such read at the moment of
consultation. This is precisely Source A's own example ("a retrieval result
that has since changed"): the retrieval call happens outside the local event
log's boundary by default. Event sourcing is a necessary *implementation
technique* for capturing decision-time bindings once you know what to
capture; it does not tell you which external reads need to become events in
the first place.

**Remaining difference:** The AI-specific inventory of which external,
mutable dependencies must be turned into first-class, captured events is
exactly the design question this contribution raises — event sourcing
theory is silent on it.

---

### Objection 3 — "This is just an audit log"

**Strongest version:** Regulatory logging is already mandated (EU AI Act
Article 12: automatic recording of events over the system's lifetime, 6
months minimum retention) and audit-log integrity is a mature discipline
(NIST SP 800-92, tamper-evident hashing). A compliant system already
produces exactly the durable record this contribution is asking for.

**What it gets right:** Audit logging is real, legally mandated for
high-risk AI systems, and tamper-evidence is a solved integrity problem.

**Does the contribution survive?** Yes, and this objection reveals a
specific, checkable conflation. Article 12's own specified minimum content
(for the one system class the Act enumerates in detail, Annex III point
1(a)) is: period of use, the reference database checked, the input data
causing a match, and the identity of the persons who verified it. This is
**execution/outcome-oriented content** — it does not require recording which
policy version applied, whether the evidence satisfied a stated requirement,
or who had authority to approve a deviation. A system can be fully Article
12-compliant, and fully tamper-evident per NIST SP 800-92, while still
failing sub-problems D, E, and G entirely. NIST SP 800-92's tamper-evidence
property answers "was this record altered after the fact" — a question
about **integrity** — not "does this record contain what's needed" — a
question about **completeness**. The objection conflates the two.

**Remaining difference:** Legal/security audit-log minimums are calibrated
to a different purpose (detecting tampering and monitoring for risk
indicators) than decision-justification reconstruction, and nothing in
either standard requires closing that gap.

---

### Objection 4 — "This is just bitemporal data"

**Strongest version:** If policy documents and authority/role assignments
are stored in a bitemporal schema (valid-time + transaction-time, per
Snodgrass and SQL:2011 — a standard older than most of the AI stack), then
"what policy/authority was valid at t0" is a solved, decades-old query
problem.

**What it gets right:** This is the single strongest objection in the
audit. Bitemporal modeling is **exactly** the correct technical answer to
sub-problems D and E, and it requires no new theory whatsoever — this
question was solved in the 1980s and standardized in SQL:2011.

**Does the contribution survive?** Yes, but only barely, and the surviving
claim is narrow: bitemporal theory answers D and E completely **wherever it
is applied**, but it does not answer *what should be modeled bitemporally in
an AI system*, and — checked directly — prompt stores, vector databases /
retrieval corpora, and policy-as-config services in the current AI/ML stack
are essentially never built with valid-time semantics by default. The gap is
**adoption of a 40-year-old idea to a new set of objects**, not a missing
technical capability. Separately, bitemporal theory says nothing about
sub-problem C (was this specific piece of evidence an accurate
representation of ground truth when consulted, as opposed to merely
"recorded then") or sub-problem G (the normative synthesis).

**Remaining difference:** An AI-specific enumeration of which dependencies
need bitemporal treatment, plus the binding step connecting a specific
decision to specific valid-time slices — neither of which bitemporal theory
supplies on its own.

---

### Objection 5 — "This is just reproducible ML"

**Strongest version:** Version code, data, and model; run a deterministic
pipeline; get the same output. Reproducibility research (data leakage,
versioning discipline, the "five pillars" of ML reproducibility) already
covers this extensively.

**What it gets right:** Reproducibility fully answers sub-problem B
(execution reconstruction) — same inputs, same code, same output,
mechanically verified.

**Does the contribution survive? Yes — this is the cleanest surviving
distinction in the entire audit, and it is explicitly formalized in Task 6
below.** Reproducing output = 0.87 tells you nothing about which threshold
applied to that 0.87, why that threshold was the applicable one, which
policy version set it, or who was authorized to approve an exception. Also
worth noting directly: much production LLM inference is not even reliably
replayable in the traditional-ML sense (sampling, non-deterministic GPU
kernels, silent provider-side model updates), which makes reproducibility an
even weaker foundation for AI decisions than for classical ML — the premise
of this objection is harder to satisfy in the AI case than the objection
assumes.

**Remaining difference:** Replay and reconstruction are different
properties, formalized in the section below. This objection does not
collide with reconstruction at all; it only closes B.

---

### Objection 6 — "This is just observability/tracing"

**Strongest version:** OpenTelemetry captures the complete execution path,
timing, attributes, and status across every service a request touched.
Doesn't that already show "why" a decision happened?

**What it gets right:** Tracing gives excellent fidelity on sub-problem B —
which service, which function, what parameters, in what order, with what
latency and error status.

**Does the contribution survive?** Yes. Two independent reasons, one
conceptual and one operational. Conceptually: OpenTelemetry span attributes
are undifferentiated key-value pairs chosen by whoever instrumented the
code — there is no schema distinction in the spec between "this attribute
is evidence," "this attribute is the applicable policy version," and "this
attribute is incidental debug context." A trace shows *how* execution
proceeded; it has no native vocabulary for *why*, normatively, that
execution was authorized. Operationally: most tracing backends retain spans
for a bounded window (days to weeks) for cost reasons — this is standard
practice, not a spec requirement, but it means tracing infrastructure is
frequently not even architected as a long-horizon store, which matters
because the reconstruction problem is defined to arise months later.

**Remaining difference:** Tracing answers HOW; reconstruction requires WHY
(a normative claim), and tracing's typical operational retention horizon is
mismatched with the reconstruction problem's time horizon even where the
conceptual gap could in principle be closed.

---

### Objection 7 — "This is just SLSA/in-toto applied to AI"

**Strongest version:** in-toto's Statement/Predicate/Subject model plus
Sigstore's Rekor transparency log already give you exactly a durable,
signed, tamper-evident, timestamped structured-evidence container — which is
what a decision record needs to be. Just define an AI-decision predicate
type and you're done.

**What it gets right:** This is the closest existing production-grade
mechanism to what Contribution 2 needs, and it is more concretely available
than the general access-control prior art already conceded for Contribution
1. Confirmed by direct inspection of the in-toto and Sigstore
specifications: the Statement/Predicate structure is generic and
extensible, and Rekor's append-only Merkle-tree log gives strong tamper
resistance and existence-before-time proof.

**Does the contribution survive?** Yes, narrowly, for three checkable
reasons: (1) no AI-decision predicate type is standardized today — defining
one is real, undone design work, not an application of an existing
standard; (2) in-toto/SLSA's object of attestation is fundamentally a
**build** (how an artifact came to exist) — applying the same mechanism to a
**runtime decision** (an agent's tool call, a per-request authorization
using an already-built model) stretches the framework beyond its stated
design intent, and no primary source reviewed describes this extension;
(3) Rekor gives existence-integrity ("this attestation existed before time
T"), not validity-interval semantics ("this was the applicable policy at
time T") — the same bitemporal gap identified in Objection 1 and Objection
4 recurs here.

**Remaining difference:** This is the strongest surviving collision in the
whole audit and should be named as such in any future publication of
Contribution 2 — in-toto + Sigstore supplies the durable-signed-container
mechanism; it does not supply the AI-specific predicate schema or the
runtime (rather than build-time) object of attestation.

---

### Objection 8 — "If you version code, model, dataset, prompt, configuration, and policy, there is no reconstruction problem"

**Strongest version:** Comprehensive versioning of every mutable dependency
eliminates the gap by construction — reconstruction becomes a pure retrieval
problem once nothing is silently overwritten.

**What it gets right:** For the components that are actually versioned,
this is correct. If every dependency is versioned, if the decision record
explicitly pins the exact version-id of each dependency consulted at t0, and
if those versioned artifacts are retained, then C, D, E, and F reduce to
retrieval, not knowledge.

**Does the contribution survive? Yes — this is the single most important
finding of the whole audit, and the sharpest formulation of the
contribution's actual claim.** Two gaps remain even under the objection's
own generous premise:

1. **The binding problem.** Having version history for the policy document
   *elsewhere in the system* does not tell you *which version applied to
   this decision* unless the decision record itself pins that reference at
   t0. Systems routinely version their own artifacts (git-versioned code,
   registry-versioned models) without ever recording, per decision, which
   version was consulted. This is Source A's own six-months-later scenario
   restated precisely: the model, the retrieval corpus, and the policy could
   each be independently, perfectly versioned elsewhere, and the decision
   could still be unreconstructable, because nothing bound this decision to
   those specific versions at the moment it was made.
2. **The completeness-of-enumeration problem.** The objection assumes
   someone correctly identified, in advance, every mutable dependency worth
   versioning. In practice this enumeration is incomplete by default — an
   LLM provider can silently change model behavior without a version bump a
   consumer can see, or a "live" feature flag is never treated as a
   versioned artifact at all — placing such cases outside the objection's
   own premise without anyone having decided so deliberately.

**Remaining difference:** Versioning infrastructure existing is not the
same as a per-decision binding being recorded. **The objection's own "if" is
this contribution's actual thesis, not a refutation of it** — it just
restates, as an assumption, the discipline this contribution argues is
currently absent by default.

---

### Objection 9 — "A sufficiently complete event log contains everything, so the distinction is artificial"

**Strongest version:** Define "sufficiently complete" as literally logging
every read and every write, including every external call's exact response,
forever. By definition, nothing is then missing.

**What it gets right:** Tautologically true. If a system logs everything
with perfect fidelity in perpetuity, there is no reconstruction problem, by
construction.

**Does the contribution survive?** Yes, and this objection is the weakest of
the nine for a specific reason: it is **unfalsifiable by definition** and
**practically vacuous**. No real system logs "everything" — for cost,
privacy, and epistemic reasons alike. The epistemic reason is the sharpest:
some inputs to a decision are never data at all — Source A's own example of
"a human approval whose rationale was never recorded" is not a logging
failure, it is information that never existed as a loggable artifact in the
first place. The interesting question was never "would total completeness
solve it" (trivially yes) but "does anything in current standard practice
approach that completeness for the AI-specific transient dependencies
without deliberate design" — and the prior-art audit answers this directly:
no. PROV lacks the normative/temporal vocabulary; event sourcing is blind to
unmodeled external reads; tracing has both a semantic gap and an
operational retention mismatch; the strongest regulatory minimum (EU AI Act
Art. 12) is execution-scoped by its own text.

**Remaining difference:** The objection wins only as a logical triviality
and loses as an engineering claim about default practice. The genuinely
open question it deflects from is "what is the minimal necessary and
sufficient content, and does anything capture it by default" — answered in
`minimal-decision-record.md`.

---

## Task 6 — Replay vs. Reconstruction, and whether the distinction is novel

**REPLAY:** Can the same computation/output be reproduced, given the same
versioned code, data, and model?

**RECONSTRUCTION:** Can it be determined why the decision was valid or
authorized under the conditions that applied at t0 — which threshold
applied, why that threshold applied, which policy version established it,
which evidence satisfied the requirement, and whether that evidence was
itself valid at t0?

**Prior-art check for this exact distinction:** The closest existing
formalization is the ACM Artifact Review and Badging taxonomy
(Repeatability / Reproducibility / Replicability / Results Replicated,
v1.1, 2020) — but this taxonomy, verified directly, is entirely about
whether the **same measurement/result** can be obtained by the same or a
different team under the same or different setup. It has no term, and no
apparent intention to have a term, for whether a *result, once obtained, was
normatively justified*. No source encountered in this audit formalizes a
distinction matching REPLAY vs. RECONSTRUCTION as defined here. **This
distinction is not found named this way in the prior art surveyed — it
appears to be a genuine, if modest, contribution specific to this
programme**, not a rediscovery of an existing formal dichotomy. It should be
introduced explicitly as such, with the ACM taxonomy cited as the nearest
adjacent (but non-overlapping) formalization for the REPLAY half only.

**Caveat required by the brief's own instruction not to assume novelty:**
"replay ≠ reconstruction" as an informal engineering intuition is almost
certainly familiar to practitioners in ML observability and MLOps without
ever having been named this way in a citable source — this audit can
confirm an absence in the literature surveyed, not prove the idea has never
been stated informally elsewhere. The claim of novelty here should be scoped
to "not found as a named, formalized distinction in the prior art surveyed,"
not "the first time anyone has ever thought this."

---

## Summary table

| Objection | Survives Contribution 2's claim? | Strongest surviving gap |
|---|---|---|
| 1. Just provenance (PROV) | Yes, narrowly | No valid-time semantics; no normative vocabulary |
| 2. Just event sourcing | Yes | Blind to unmodeled external reads by default |
| 3. Just an audit log | Yes | Legal/security minimums are execution-scoped, not justification-scoped; conflates integrity with completeness |
| 4. Just bitemporal data | Yes, barely — closest theoretical collision | Theory is sufficient; AI-specific adoption is absent; doesn't address evidence content-validity or the binding step |
| 5. Just reproducible ML | Yes, cleanly | Replay ≠ reconstruction (see Task 6) |
| 6. Just observability/tracing | Yes | Answers how, not why; retention-horizon mismatch |
| 7. Just SLSA/in-toto for AI | Yes, narrowly — closest production-mechanism collision | No AI-decision predicate type; built for build-time, not runtime; existence-integrity ≠ validity-interval |
| 8. Comprehensive versioning solves it | Yes — sharpens the thesis rather than refuting it | Versioning existing ≠ binding recorded, per-decision |
| 9. Sufficiently complete logging solves it | Yes, trivially — the objection is unfalsifiable and vacuous | Real systems never approach this; the useful question is minimal sufficient content |

**No objection defeats Contribution 2 outright.** The pattern across all
nine is consistent: every individual primitive needed already exists in a
mature, separate literature (PROV for lineage, bitemporal databases for
validity intervals, in-toto/Sigstore for durable signed evidence, event
sourcing for internal-state history), but **no existing mechanism combines
valid-time semantics, structured signed evidence, and an explicit
per-decision binding into one applied pattern for the AI-specific set of
transient dependencies**, and none is applied to those dependencies by
default in current AI/ML tooling. This is the basis for the Verdict B
("narrowed survival") reached in `novelty-verdict.md`.

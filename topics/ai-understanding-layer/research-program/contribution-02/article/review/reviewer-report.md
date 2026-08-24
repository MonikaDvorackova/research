---
id: note-contribution-02-article-review-reviewer-report
title: "Contribution 2 Article — Adversarial Reviewer Report"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, review, adversarial]
refs: [../draft-v1.md, ../draft-v1-audit.md, claim-review.md, VERDICT.md]
---

## Adversarial Reviewer Report

Independent review of `../draft-v1.md`. Draft-v1's own self-audit
(`../draft-v1-audit.md`) is treated as a starting hypothesis, not a
verified conclusion — every claim it scored PASS is re-checked here
against the raw committed data and the reasoning independently
reconstructed, not re-run.

**Headline finding, stated up front because it changes how the rest of
this report should be read:** independent inspection of the primary
experiment's actual query implementation
(`../../experiment/src/reconstruction.py::_as_of_valid_time_latest_transaction`)
found that Regime B's bitemporal query uses "as of the latest known
transaction state" semantics (the greatest `recorded_at` across *all*
retained rows, unbounded by t0), not "as of transaction time t0"
semantics (`recorded_at <= t0`, then latest). A standard SQL:2011
`SYSTEM_TIME AS OF t0` query — using only data Regime B already
retains, and t0, which every regime already knows from its own outcome
log — would return the pre-correction value (v1) on Cases 3, 8, and 9,
because the backdated correction's `recorded_at` (after t0) would be
excluded from consideration entirely. **This means Regime B, as
implemented, does not represent the best possible use of its own
retained data on the retroactive-correction cases**, which is exactly
the internal-validity failure mode the experiment design's own
`validity-and-confounders.md` explicitly worried about and believed it
had avoided. This is treated as the review's central technical finding
and threaded through the relevant sections below.

---

## Three reviewers

### Reviewer A — senior distributed-systems / data-systems engineer

**Primary attack:** "Isn't this just provenance, event sourcing, temporal
databases, tracing, or causal metadata?"

**Verdict after independent inspection:** Draft-v1's "This Is Not a New
Provenance System" section answers this credibly for four of five
mechanisms (PROV, event sourcing, distributed tracing, audit logs/
lineage) — it concedes ground precisely, states the conditional under
which each mechanism already solves the problem, and does not overstate
non-overlap. **Bitemporal databases are the one mechanism where the
article's answer does not survive independent inspection**, for the
reason stated in the headline finding above: the article claims
bitemporal databases solve the problem "for exactly the cases without
retroactive correction," but this reviewer's inspection shows a
correctly-used bitemporal database (with `SYSTEM_TIME AS OF t0`) also
solves the retroactive-correction case, using no additional artifact.
This is Reviewer A's strongest objection and it lands.

### Reviewer B — ML systems / MLOps engineer

**Primary attack:** "Is this actually an AI systems contribution, or a
generic systems observation wrapped around an AI example?"

**Verdict:** Largely correct, and draft-v1 does not fully defend against
it. The synthetic testbed's "model" is a fixed, two-parameter weighted
sum with a threshold rule — there is no learned behavior, no
stochasticity, no inference step distinguishable from an ordinary
rules engine. Swap "model version" for "pricing-rule version" and the
experiment is unchanged in every particular (see the AI-removal test
below). The article's title and opening frame this as being about "an
AI decision" specifically; the actual mechanism tested is about any
system with versioned, time-varying dependencies and no per-decision
causal record. This does not defeat the article, but it does mean the
current framing oversells AI-specificity relative to what was tested,
and the "AI-mediated" language should either be justified more directly
or narrowed.

### Reviewer C — skeptical technical editor

**Primary attack:** "Even if technically correct, is there enough here
for an independent article, and will a sophisticated reader learn
something non-obvious?"

**Verdict:** Yes, conditional on Reviewer A's objection being addressed.
The retained-vs-consumed distinction, the honest-ambiguity-vs-confident-
wrongness distinction, and the negative control are all genuinely
non-obvious and well-earned by the follow-up experiment specifically. The
primary experiment's retroactive-correction result, as currently framed,
is the weakest of the article's three empirical pillars once Reviewer A's
finding is taken into account — it needs either a defense or a
significant down-weighting in the article's overall argument, because as
written it reads as the article's *lead* empirical result, and it is now
the most vulnerable one.

---

## First-principles argument test

Reconstructing the argument without its prose:

- **P1.** An artifact (policy, evidence, authority, model, config) can
  exist in a retained history at t1 (definitional/observational).
- **P2.** A decision D, made at t0, used exactly one version of each
  relevant artifact (definitional — this is what "consumed" means).
- **P3.** A later query against retained history, asking "which version
  was valid at t0," may return a version other than the one D actually
  used. (**Empirical claim**, requires evidence — supplied by the primary
  experiment for the retroactive-correction sub-case, *conditional on the
  headline finding above being addressed*.)
- **P4.** A later query against retained history may, under some
  conditions, be unable to return a unique version at all. (**Empirical
  claim**, supplied by the follow-up experiment for the observational-
  precision-loss sub-case — this transition is well-supported and
  independent of P3's vulnerability.)
- **P5.** An explicit, decision-time-authored record avoids both P3 and
  P4's failure, by construction, in the tested cases. (**Empirical
  claim**, supported directly — Regime C's FHC=0.00 and TC=1.00 across
  both experiments, no exception.)
- **P6.** A non-binding, ordinary causal-consumption event *also* avoids
  P4's failure. (**Empirical claim**, supported directly by F10-6 —
  applies only to the mechanism P4 covers, not tested against P3's
  mechanism.)
- **Conclusion (C).** The required property is a preserved causal
  relation between D and its consumed context, not specifically an
  explicit binding schema. (**Synthesis** of P5+P6, an interpretation,
  not itself a single data point — correctly labeled as such throughout
  draft-v1.)

**Weakest transition:** P3. It is stated as a clean empirical fact in the
article, but the reviewer's independent inspection shows P3 is true only
of the *specific query algorithm implemented*, not of "retained bitemporal
history" as a general category — a more sophisticated, still-binding-free
query defeats P3 on the same data. **This is the transition that, if
corrected, would require the most revision** (see `claim-review.md` and
`revision-plan-v2.md`, both P0).

**Does removing P3 collapse the article?** No, but it changes its center
of gravity substantially. P4, P5 (for the P4 mechanism), and P6 are
independently sound and, together, already carry the article's strongest
and most novel content (the honest-ambiguity finding and the negative
control). P3, if it cannot be adequately defended, should be reframed
from "Regime B fails" to "a naively-queried Regime B fails; a
transaction-time-sophisticated query does not, and this itself is
informative" — which is a smaller but still legitimate and interesting
claim (see `revision-plan-v2.md` P0-1).

---

## Central claim attack

Article's core claim: *retaining artifact versions is not equivalent to
preserving enough causal structure to identify which versions a decision
actually consumed.*

### Objection 1 — Isn't ordinary temporal querying enough, given valid-time intervals and a decision timestamp?

**Strongest form:** if every dependency has a valid-time interval and the
decision has a timestamp, "what was valid at t0" is a complete, standard
bitemporal query — SQL:2011 solved this in the 1980s/90s.

**Does draft-v1 currently answer it?** Partially. It answers the
*valid-time* half correctly (a naive valid-time-only query is defeated by
retroactive correction — true and well-explained). It does **not**
address the *transaction-time* half — that a `SYSTEM_TIME AS OF t0` query
also uses only retained data and is not defeated by the same mechanism.
This is the review's central finding, restated.

**Technically sufficient?** No, as currently written.

**Revision needed:** Either (a) add 1-2 sentences explaining why
transaction-time-anchored querying is not "free" in the sense that
matters (it requires the investigator to know, in advance, to pin the
cutoff to *decision* time rather than *query* time — a non-default
choice that ordinary bitemporal tooling does not make automatically,
and which Regime C removes the need for entirely), or (b) reframe the
retroactive-correction result as being about default/naive query
practice specifically, not about bitemporal completeness as a category.
See `revision-plan-v2.md` P0-1 for the exact required change.

**Threatens publishability?** Not fatally, but it is the single most
important required fix before v2. Left unaddressed, a sophisticated
Reviewer-A-type reader will identify this independently and it will read
as either a mistake or an omission.

### Objection 2 — If event sourcing records the causal event stream correctly, isn't the problem already solved?

**Strongest form:** a complete, append-only event log, replayed to t0,
gives exact historical state — including, if instrumented richly enough,
which version was consulted.

**Does draft-v1 answer it?** Yes, directly and well — "Event sourcing...
is exactly the negative control's mechanism," immediately qualified by
the values-vs-identifiers distinction. This is one of the article's best
passages: it concedes the objection's strongest form (via F10-6) rather
than resisting it.

**Technically sufficient?** Yes.

**Revision needed:** None.

**Threatens publishability?** No — this is a strength, not a weakness.

### Objection 3 — If W3C PROV can encode `used` relationships, isn't this literally provenance?

**Strongest form:** PROV's Usage relation between an Activity and an
Entity is exactly "D used x" — the causal relation the article claims is
missing.

**Does draft-v1 answer it?** Yes, and correctly: PROV's Usage relation is
conceded as structurally the right shape, with the specific, narrow gap
named (no native valid-time interval on the Entity). This matches the
prior-art audit's own finding and is not overstated.

**Technically sufficient?** Yes.

**Revision needed:** None required for correctness. Optional: could be
slightly more explicit that a PROV graph populated with version
identifiers (not raw values) as Entities would, in fact, close the
retroactive-correction case too — the current text only says PROV closes
"the second" (precision-loss) failure, but a version-identified PROV
Usage relation is functionally identical to Regime C's binding and would
also survive Objection 1's mechanism. Minor, not required.

### Objection 4 — If distributed tracing preserves causal relationships, what is left?

**Strongest form:** OpenTelemetry spans are explicitly causally linked
(parent/child); doesn't that already capture "why"?

**Does draft-v1 answer it?** Yes, briefly but adequately, grouped with
audit logs and lineage tools in one paragraph. The answer (undifferentiated
attributes, no schema distinction) is correct and matches the prior-art
audit.

**Technically sufficient?** Yes, though thin relative to how central
tracing is to Reviewer A's mental model — a one-sentence example (a trace
attribute storing a raw threshold value vs. a version ID) would
strengthen this without adding length. Optional, not required.

### Objection 5 — Is "decision-context identifiability" merely a new name for an established property?

**Strongest form:** this sounds like a restatement of "referential
integrity" or "foreign-key completeness" — standard database concepts,
not a new property.

**Does draft-v1 answer it?** Not explicitly — the term is defined once
(`## What a Historical Decision Actually Depends On`) and not defended
against this specific framing.

**Technically sufficient?** The definition itself is fine; the *omission*
of this objection is the issue. A sophisticated reader familiar with
referential integrity will draw this comparison unprompted, and the
article currently has no answer ready. The honest answer is available and
should be added: referential integrity guarantees a reference *resolves*
to something that exists; it says nothing about whether the reference
was *authored correctly at the time it mattered* (a foreign key can point
to the wrong row and still be "valid" in the referential-integrity
sense). This is close to, but not identical to, the concern — worth one
sentence.

**Threatens publishability?** No, but leaving it unaddressed is a missed
opportunity a technical editor (Reviewer C) will flag.

### Objection 6 — Is "retained vs. consumed" too obvious to be a meaningful contribution?

**Strongest form:** any engineer who has debugged a "why did this happen
three months ago" incident already knows intuitively that having the
data isn't the same as being able to use it.

**Does draft-v1 answer it?** Implicitly, via the empirical demonstration
— but not explicitly. `novelty-review.md` Objection 5 and Objection 10
(in the drafting-readiness package) directly address this and concede it
partially ("the mechanism is not novel; the diagnostic/empirical
demonstration is"), but this concession does not appear in draft-v1
itself.

**Technically sufficient?** The experiments themselves answer this well
— an intuition and a measured, reproducible demonstration with named
failure modes and a negative control are different things, and the
article's job is to make that difference visible. Currently implicit
rather than stated.

**Revision needed:** One sentence near the opening or in "This Is Not a
New Provenance System," conceding the intuition is not new and stating
plainly that the contribution is measuring it, not discovering it. Low
priority (P2).

**Threatens publishability?** No.

---

## Is this really about AI?

Running the substitution test: replace "AI-mediated decision" with
"deployment configuration decision," "financial transaction
authorization," or "any automated workflow decision using versioned
policy, evidence, and role data." Every mechanism, every metric, every
result in both experiments is unchanged by this substitution — the
"model version" dimension in the testbed is a fixed two-weight linear
function, not a trained or stochastic model in any sense that
distinguishes it from a versioned configuration parameter.

**Say so explicitly: yes, the core argument is substrate-independent.**
This is not fatal — most genuinely useful systems findings are
substrate-independent at their core — but the article's title and framing
currently claim more AI-specificity than the evidence supports.

**What legitimate AI-specific framing remains, honestly stated:**

- AI-mediated systems characteristically combine model version, retrieved
  evidence, policy-as-config, and delegated authority in one decision path
  more routinely than many other automated-decision categories — this is
  a *packaging* observation, not a claim that the underlying failure mode
  is AI-specific.
- The experiments are instantiated in an AI-decision-shaped testbed
  because that is Contribution 2's stated scope
  (`../../problem-formalization.md`), not because the mechanism requires
  AI.
- MLOps/ML-platform tooling conventionally emphasizes artifact/model
  versioning (registries, experiment tracking) while treating the
  decision-to-version relation as an afterthought — this is a real,
  citable pattern (`../../prior-art-audit.md`'s MLflow entry) and is the
  most defensible AI-specific framing available.

**Does the title/body oversell AI specificity? Yes, mildly.** "Why
Keeping Every Version Still Isn't Enough to Explain an AI Decision" reads
as a claim about AI decisions specifically; the honest claim is about
versioned automated-decision systems generally, illustrated in an
AI-shaped testbed. See `title-review.md` for the recommended correction
and `revision-plan-v2.md` P1 for the exact text change.

---

## Experiments as evidence

**Manipulation validity (did B and C differ only in the tested
property)?** Yes for both experiments — machine-checked
(`verify_b_c_equivalence`, run for every case in both experiments,
confirmed in this review by re-reading the check's assertions, not merely
trusting its name) and independently verifiable from the raw code. This
holds regardless of the headline finding above (which is about B's
*query algorithm*, not about B-vs-C data equivalence).

**Construct validity (does Temporal Correctness measure the claimed
property)?** Yes, as defined (does the named version's interval actually
contain t0 per ground truth) — but the primary experiment's TC result on
retroactive cases measures "did *this specific query algorithm* get it
right," which is a narrower construct than "does Regime B's *retained
data* support getting it right" — exactly the gap the headline finding
identifies. The metric is fine; the algorithm under test is what needs
qualification.

**Case construction — were cases built so C was guaranteed to win?**
No evidence of this. Four of ten primary cases (2, 4, 6, 7) were
deliberately built as cases where B was expected to, and did, succeed —
a real, checkable control against this specific risk, confirmed in the
raw results (`aggregate_by_category.csv`: B and C both 1.00 on
forward-drift). The follow-up's F10-1 control and F10-6 negative control
serve the same function. This objection does not survive inspection.

**Deterministic investigator — does this trivialize the result?** No,
for the reason `../../drafting-readiness/evidence-review.md` and the
experiment design already state: using a fixed, best-possible algorithm
establishes an *upper bound* on what a regime's information supports,
isolating information availability from investigator skill. This is
methodologically sound. The headline finding is not an objection to using
a deterministic investigator — it is an objection to whether *this*
deterministic investigator was actually the best-possible one for Regime
B, which is a different and more specific concern.

**Synthetic environment — what generalizes?** Only the mechanism itself
(demonstrated to be real and measurable in a controlled setting), not its
prevalence or severity elsewhere — draft-v1 already states this
correctly and repeatedly.

**Sample/case count — "33 + 12 case-regime rows."** These are executions
of hand-constructed scenarios, not an independent statistical sample, and
draft-v1's body **does not** use the row count rhetorically anywhere —
good discipline, confirmed by inspection. (The number appears only in the
git commit message and prior turn summaries, not in the article body
itself.) No revision needed on this point, but flag as a **required
constraint on v2**: if a future revision adds any language like "N cases
tested" or "across dozens of scenarios," it must not imply statistical
sampling. See `revision-plan-v2.md` P3 (preventive, not corrective).

---

## Primary experiment result — deep inspection

Restating the headline finding in the terms the authorizing brief asked
for:

- **Was B using the best historical query available?** No. See above.
- **Was retroactive correction represented fairly?** Yes, on its own
  terms — the correction scenario itself (a backdated policy correction,
  `recorded_at` after `valid_from`) is realistic and not strawmanned.
  The *unfairness*, such as it is, is in the query algorithm chosen to
  represent "the best available reconstruction from Regime B's data,"
  not in the scenario construction.
- **Is the failure a property of "versioned but unbound" or of the
  specific temporal semantics chosen?** Primarily the latter, per this
  review's inspection. A regime that is "versioned but unbound" and
  queried with `SYSTEM_TIME AS OF t0` semantics would succeed on Cases 3,
  8, 9 using no binding at all.
- **Could a competent bitemporal design avoid the failure?** Yes — see
  above.
- **Does that effectively preserve the causal relation claimed to be
  required?** This is the subtle part, and it is where a defensible
  narrower claim survives: `SYSTEM_TIME AS OF t0` querying does not add
  or preserve any *new* relation — it uses exactly the data Regime B
  already has. What it requires is that the *investigator* deliberately
  choose to anchor the transaction-time cutoff to the decision's own
  timestamp rather than to query time — a non-default, non-obvious
  choice most real bitemporal usage does not make automatically (ordinary
  "as of" queries default to "as of now"). Regime C removes the need for
  this investigator sophistication entirely — the binding record is
  looked up directly, with no query design decision required at all. This
  is a real, defensible, but *narrower* distinction than "Regime B
  fails."

**Verdict: draft-v1 currently does not explain this nuance, and it must
before v2.** This is the report's single highest-priority required
change.

---

## False Historical Confidence

**Well-defined?** Yes — a concrete, single-value answer to a
version-bearing question that is wrong, as distinct from an honestly
unresolved answer. The definition survives inspection.

**Genuinely measured, not an artifact of a badly-designed algorithm that
should have abstained?** This is the crux question, and it connects
directly to the headline finding: Regime B's confident-wrong answer on
Cases 3/8/9 is not a case where the algorithm *should have* abstained and
didn't (the query returns exactly one matching row under its own
"latest known state" semantics — it is not ambiguous by that algorithm's
own criteria, so there was no missed opportunity to return
`UNDETERMINED`). The correct diagnosis is not "the algorithm should have
abstained" but "the algorithm used the wrong transaction-time cutoff and
therefore wasn't ambiguous when it should have been unresolvable or
correct." This is a variant of the headline finding, not a new,
independent problem with the FHC metric itself.

**Distinguish architecture/information failure from reconstruction-
algorithm failure:** Per the above, this specific result is better
described as an **algorithm-choice failure operating on sufficient
information**, not an information-architecture failure. This changes
what the article can honestly claim FHC demonstrates for the primary
experiment specifically — see `claim-review.md`.

**Intuitively explained in the draft?** Yes, well — "The More Dangerous
Failure" section is one of the strongest-written sections regardless of
this issue.

**Overclaimed?** The metric itself is not overclaimed. The *example*
used to introduce it (the retroactive-correction case) is the one this
report flags throughout.

---

## Case 10 follow-up — isolation check

**Timestamp truncation mechanism:** confirmed by inspection
(`../../experiment/followup-case10/src/domain.py::observed_t0`) —
microsecond-precision `true_t0` truncated to whole seconds, matching the
article's description exactly.

**Candidate versions / what B can observe / what C can observe:**
confirmed via `verify_b_c_equivalence` and direct code inspection — B
sees the full policy/authority/model history and the observable
(truncated) timestamp only; C additionally sees a binding authored from
the true, untruncated timestamp. No transaction-time dimension exists
anywhere in this experiment's code (confirmed above) — the headline
finding above does **not** apply to this experiment.

**Ground truth isolation:** confirmed — ground truth is computed from
`true_t0` before any regime view is constructed, and neither view type
carries a `ground_truth` field (checked directly against
`RegimeBView`/`RegimeCView`'s dataclass fields).

**Is "B returns AMBIGUOUS, C returns correct unique" evidence of
failure, or of B behaving correctly?** **This is exactly right, and
draft-v1 gets it right too** — "Experiment 2" states plainly that B's
`AMBIGUOUS` result is "epistemically different" from a wrong answer and
explicitly declines to call it a failure of the dangerous kind. The more
precise interpretation the authorizing brief asks for — "version history
is insufficient for unique historical identification under the tested
conditions" — is what the article actually says, almost verbatim
("Both are failures of unique reconstruction — but only one of them is
dangerous"). **No revision required here; this is a strength.**

---

## F10-6 negative control

**What did it falsify?** Confirmed: "explicit decision-time binding is
uniquely necessary" — the draft states this precisely and correctly.

**What survives?** Confirmed: "some preserved causal relation is
required" — stated correctly, with the implementation-vs-property
distinction made explicit ("the property, not the implementation, is
what the evidence supports").

**Is it prominent enough?** Yes — it has its own section, placed
immediately after the second experiment and before the prior-art
revisit, matching the authorizing brief's explicit requirement not to
bury it. A reader finishing the article could not reasonably conclude
the author invented a proprietary binding architecture — the section's
own language actively forecloses that reading ("does not establish a
new, proprietary reconstruction mechanism").

**No revision required.** This is the strongest-executed section in the
draft.

---

## Prior-art fairness — independent classification

| Mechanism | A/B/C/D | Matches draft-v1's treatment? |
|---|---|---|
| W3C PROV | **B** (solves if configured — version-identified Entities) | Yes, matches exactly |
| Event sourcing | **B** (solves if configured — identifiers not values) | Yes, matches exactly |
| Bitemporal databases | **B**, but broader than draft-v1 currently states — solves *both* tested mechanisms if `SYSTEM_TIME AS OF t0` is used, not only the non-retroactive cases | **No — draft-v1 currently under-credits this mechanism**, per the headline finding |
| Distributed tracing | **C** (neighboring — captures execution, not decision-context identity by default) | Yes |
| Audit logs | **D** (not materially relevant to the causal-relation claim — orthogonal integrity/completeness concern) | Yes, matches `../../collision-tests.md` Objection 3 |
| Version control (git) | **C** (solves code history, not decision-context binding) | Not mentioned in draft-v1 at all — acceptable omission, git is not central to this problem, no revision required |
| Lineage tools | **C** (training-time, not runtime-decision-scoped) | Yes |
| Attestations (in-toto/SLSA) | **B**, conditionally (if a decision-predicate type existed) | Not mentioned in draft-v1 — acceptable scope cut for length; optional addition, not required |

**The one required correction:** bitemporal databases' classification
must move from "solves the non-retroactive cases only" to "solves both
tested mechanisms if the transaction-time cutoff is anchored to decision
time" — see `revision-plan-v2.md` P0.

---

## Terminology attack

- **"Retained" / "consumed"** — clear, well-established informal usage,
  no confusion risk. Keep.
- **"Causal relation" / "causal linkage"** — the term most likely to
  mislead a statistically literate reader into thinking of causal
  inference (confounders, counterfactuals, do-calculus). The relation
  actually being described is closer to a **reference** or
  **consumption record** than a causal-inference object. `consumption
  relation` is more precise and lower-risk; draft-v1 uses "causal" nine
  times across the body. Recommend auditing each occurrence in v2 and
  replacing at least the first, definitional occurrence with
  "consumption relation," keeping "causal" only where it reads naturally
  and low-risk (e.g., "causal trail" in the closing line, which is
  idiomatic enough not to trigger the statistical-inference reading).
  See `revision-plan-v2.md` P1.
- **"Decision context"** — correctly avoided in the body (confirmed by
  grep in the prior self-audit and re-confirmed here); "consumed
  context" used consistently instead. Keep.
- **"Decision-context identifiability"** — precise and scoped, used once
  as a formal definition and not overused afterward. Keep, but note it
  is never referenced again after its introduction — either use it at
  least once more (e.g., in "The Property to Design For," which
  currently restates the same idea in different words without the term)
  or consider whether introducing it added value proportional to the
  risk of an unused technical term. Low priority (P2/P3).
- **"Historical reconstruction" / "temporal correctness" / "false
  historical confidence"** — used consistently with their experimental
  definitions, no drift detected.
- **"Binding"** — consistently reserved for naming Regime C's mechanism
  specifically, never used as the name of the general property (checked
  by grep, confirmed in `../draft-v1-audit.md` and independently
  re-verified here). No revision needed.

---

## Opening review (first ~300 words)

- **Establishes the paradox quickly?** Yes, by the fourth paragraph
  ("And there may still be no way to answer the question").
- **Implies a prevalence claim?** No — the opening is deliberately
  singular ("a production system," "call it D"), not "most systems" or
  "AI systems commonly." Good discipline.
- **Is "consequential" necessary?** Marginal — it does light framing work
  (signals stakes) but is not load-bearing; could be cut without loss.
  P3.
- **Is the example concrete enough?** Borderline. "A specific model
  version, a specific policy, specific evidence... a specific authority
  to approve it, and specific configuration" is a list, not a scenario —
  more concrete than an abstract claim, less concrete than a named
  example with actual values (contrast with Article 1's opening, which
  gives a specific accuracy number, `0.913`). A single illustrative
  number or named policy ("policy P7, threshold 0.50") in the opening
  would strengthen concreteness without adding length. P2.
- **Does the reader know whether this is about model inference,
  deployment decisions, or AI-mediated system decisions generally?** No
  — deliberately generic ("an ordinary automated approval, or an agent's
  tool call, or a deployment gate passing"), which is honest given the
  AI-specificity finding above, but means the opening does not yet
  justify the title's AI-specific framing. This should be resolved
  together with the title decision (`title-review.md`), not
  independently.
- **Is the distinction visible before jargon appears?** Yes — "retained"
  vs. "consumed" appears in the first section without any prior formal
  terminology, which is good sequencing.

---

## Summary of section-level findings

Carried into `section-review.md` in full; the load-bearing conclusion for
this report is that **exactly one substantive technical gap** was found
(the transaction-time query sophistication issue, affecting the primary
experiment's framing and the bitemporal-databases prior-art
classification), everything else the draft claims about the follow-up
experiment and the negative control survives independent adversarial
inspection without modification, and the AI-specificity framing is
mildly oversold relative to the evidence and should be narrowed rather
than defended.

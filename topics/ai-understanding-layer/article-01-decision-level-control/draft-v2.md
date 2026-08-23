# Model Outputs Are Not Decisions: Building Evidence-Gated AI Systems

### A concrete architecture pattern for the gap between what a model says and what a system is allowed to do

---

A model finishes an evaluation run. The dashboard shows accuracy: 0.913, latency within budget, no obvious regressions against the previous version. Someone opens the deployment pipeline. Nothing technical stops them from promoting the new model to production right now.

What, exactly, makes that promotion justified?

Not "is the model good" — the metrics answer that, more or less. The harder question is architectural: what has to be true, and be checked, before the system is allowed to change what it does in production? Training and evaluation typically get real architectural attention: pipelines, harnesses, versioned datasets, dashboards. The transition from an evaluation result to a production authorization can be as thin as a single conditional, or a person clicking "deploy" after reading a dashboard, with nothing else checking it.

That thinness is the subject of this article: not whether the model is good, but what stands between a model saying something and a system acting on it.

## Outputs are not decisions

Two things happened in that scenario, and it's worth naming them separately.

An output is information produced by the system. A decision is an authorized state transition.

The model produced an **output**: `accuracy = 0.913`. It describes something — how well the model performed against a test set, what label it assigned, what text it generated, what action it recommends. An output does not, by itself, authorize anything; it's a claim, not a change.

The system then made — or was about to make — a **decision**: `promote model v17 to production`. Before the decision, production traffic is served by v16. After, it's served by v17. Something that could not previously happen is now permitted — that's what makes it a decision rather than an output.

The architectural problem starts exactly where these two get treated as equivalent, where the existence of a good output is allowed to stand in for the decision to act on it. In the scenario above, nothing separates "the evaluation looks acceptable" from "production changes." The output flows straight through.

This gap is what a **decision boundary** is for: an explicit point in the architecture where the system stops treating an output as self-authorizing and asks whether the conditions for the corresponding decision have actually been met. This article calls what sits at that boundary a **decision layer** — not an established industry term, but a useful name for the architecture proposed here. Its shape is simple to state: an output becomes a proposed decision; a proposed decision needs evidence; evidence gets checked against requirements and authority; and only what passes becomes an actual system transition.

## What a production decision needs

If an output doesn't automatically authorize a decision, something else has to close the gap. That something is evidence — but evidence here means something narrower than documentation attached to a decision after the fact. In this pattern, evidence is structured input into authorization: the architecture has to be able to evaluate, not just store, whether evidence

- exists at all;
- belongs to the correct artifact and version — not "a recent evaluation," but the specific model and dataset pairing actually being proposed for promotion;
- satisfies the relevant requirement, rather than merely being present; and
- comes from a source authorized to produce it, where that matters — a self-reported number is not the same as one produced by an independent evaluation harness.

Evidence isn't the whole picture, and the surrounding concepts are worth keeping separate rather than folding into one bundle.

**Decision requirements** are the conditions that must hold before the transition is permitted — a minimum accuracy threshold, a required test, a policy reference and its version. Requirements don't do anything by themselves; they're what evidence gets checked against.

**Authority** is who or what is permitted to authorize this particular transition — an automated rule for routine cases, a named role for higher-risk ones. Authority answers a different question than evidence does: not "does the evidence satisfy the requirement," but "is this the party allowed to say yes here."

Evidence, requirements, and authority are related but distinct — the pattern only holds together if the architecture keeps them that way. None of this implies a single universal schema, either for evidence or for requirements: a low-risk internal tool and a customer-facing pricing model don't need the same bar. What they need is the same underlying architecture — evidence, requirements, and authority attached to the *decision*, and evaluated the same way regardless of which specific ones apply.

Once these exist and are attached to a proposed decision, a further problem appears immediately: none of this, by itself, stops anything from happening.

## Recording is not enforcing

There's a difference between "the organization has a policy that says X" and "the production architecture will not proceed unless X is true." Documenting a requirement and enforcing it are not the same act, and treating them as equivalent is where control quietly disappears.

Take the missing-evidence case from the previous section. Suppose policy requires a robustness evaluation before any promotion, and for this particular model, that evaluation was never run — maybe the harness didn't cover the new architecture yet, maybe someone skipped a step under deadline pressure. The requirement is documented: it's in the model card template, the governance wiki, possibly a compliance checklist someone signs. The deployment pipeline still lets the promotion through, because nothing in the pipeline reads that requirement and checks whether it was satisfied.

The organization has a policy. The system does not enforce it. A fully documented system can still execute a decision that violates its own stated requirements, because documentation describes intended behavior and doesn't constrain actual behavior.

This isn't an argument against documentation, model cards, or approval records — they do something else, and something valuable: communicating intent, supporting review, creating a record people can consult. The point is narrower: documentation and enforcement solve different problems, and only one of them can stop a decision from happening. If a requirement matters enough to write down, it's worth asking whether anything in the architecture would actually catch its absence.

## The evidence-gated pattern

The pattern that closes this gap — call it an **evidence-gated decision**, a proposed term rather than an established one — is simple to state: put a gate at the decision boundary, and require every proposed decision to pass through it before it can take effect.

```
PROPOSED DECISION
        +
EVIDENCE BUNDLE
        +
DECISION REQUIREMENTS
        │
        ▼
       GATE
        │
   ┌────┼────┐
   ▼    ▼    ▼
ALLOW BLOCK ESCALATE
```

[FIGURE 1: Evidence-gated decision architecture — see diagram-spec.md]

A **proposed decision** names the transition being requested — "promote model v17 to production" — without assuming it will happen. An **evidence bundle** attaches what the previous section described: evaluation results, artifact/dataset identifiers, the source each result came from. **Decision requirements** state the conditions this class of decision must satisfy — a threshold, a required test, a policy reference and its version.

The gate's job is to bring these together with authority: check the evidence against the requirements, confirm whether the decision falls within what the gate itself is authorized to approve automatically, and return exactly one of three outcomes.

**ALLOW** — the evidence satisfies the requirements, and the decision is within the gate's own authority; the transition proceeds automatically.

**BLOCK** — a required condition is not satisfied, or required evidence is missing entirely; the decision does not proceed, and this is recorded as a failed decision, not silently dropped.

**ESCALATE** — the automated gate cannot authorize the transition under its current conditions, but policy permits the decision to move to a separate, explicitly authorized review path. This is not an exception to the architecture; it's a second authorization path, with its own defined authority and evidence trail — who approved, on what basis, against which policy version.

A minimal version of this is easy to sketch:

```python
decision = propose_promotion(model_version)

evidence = collect_evidence(
    evaluation_report=...,
    dataset_version=...,
    required_tests=...,
)

result = gate.evaluate(decision, evidence)

if result == ALLOW:
    deploy(model_version)
elif result == ESCALATE:
    request_approval(decision, evidence)
else:
    block_deployment()
```

The architectural contribution here is the decision boundary and the evidence-gate pattern, not any particular place to run it. CI/CD is a natural fit for deployment-time decisions like this one: it already mediates the transition from candidate artifact to production state, the same way a pipeline runs tests before a merge. It isn't the only fit — a decision made at runtime, by an agent or a live policy check rather than at deployment time, needs its enforcement point in the request path, not the pipeline. The gate is the same pattern either way; only where it's installed changes.

These ideas took shape partly while designing AIGov Core, where governance decisions were treated as engineering artifacts rather than reporting artifacts — evidence, authority, policy context, and the assumptions behind a decision, attached directly to it.

## What this architecture buys you — and what it doesn't

What does this actually buy you? An explicit decision boundary instead of an implicit one. Evidence and requirements that can be inspected rather than inferred from someone's memory of the policy. Deterministic enforcement for the classes of decision where that's appropriate. Clear authority — a record of who or what was allowed to say yes. And, when the inputs and the rules are fixed, a gate outcome that's reproducible rather than a judgment call that might go differently on a different day. It also removes the specific failure mode this article opened with: the informal, unchecked transition from "evaluation finished" to "production changed."

It's worth being equally clear about what this doesn't buy. This architecture governs authorization at decision time. It does not, by itself, solve every problem of explainability, auditability, safety, or compliance. It doesn't guarantee regulatory compliance, general trustworthiness, or the absence of AI risk. And it isn't the right amount of machinery for every AI application — a low-stakes internal experiment doesn't need the same gate a customer-facing production model does. The claim here is narrower: for decisions with real production consequences, evidence and enforcement work better as architecture than as documentation.

## The question that matters

AI engineering has spent the last several years getting very good at producing better outputs — more accurate models, better-calibrated scores, more capable agents. Production engineering has to answer a different question: what is a system allowed to do because of what a model said?

The useful move is architectural, not procedural: stop letting the transition from output to consequential action happen implicitly, and put an explicit, evidence-gated boundary in its place. Not because outputs can't be trusted, but because "trusted enough to act on" is itself a decision, and decisions deserve a place in the architecture where they're actually made — not assumed.

The question is not only whether the model produced a good output. The question is whether the system has enough evidence to authorize what happens next.

---

## Editorial notes

*(Not part of the article. For internal review before publication.)*

**Material changes from v1:**
- Removed the unsupported prevalence claim "Most ML architecture diagrams are dense on the left side..." Replaced with a claim about what training/evaluation typically get architecturally (a much weaker, more defensible generalization) plus a possibility-framed description of the gap ("can be as thin as...") rather than a claim about what most or many pipelines actually look like.
- Deleted "Most governance failures live in that gap" outright, per instruction. Replaced with a direct statement of the conceptual difference between documenting and enforcing a requirement, with no prevalence claim attached.
- Rewrote the evidence section to distinguish four concepts — evidence, decision requirements, authority, and the gate — that v1 partially conflated (v1 listed "who can authorize this" as one bullet among evidence properties; v2 treats authority as its own concept, answering a different question than evidence does).
- Rewrote ESCALATE: v1's "meets the conditions for automated handling but falls into a category that requires..." was internally inconsistent (met conditions, yet needs escalation?). v2 states it as the gate lacking authority to approve under current conditions, with policy routing the decision to a separate, explicitly authorized path.
- Renamed the diagram's gate box from "DETERMINISTIC GATE" to "GATE" to match the requested flow exactly; "deterministic" is preserved as a descriptor in the surrounding prose instead.
- Added one explicit sentence at the end of the "Outputs are not decisions" section previewing the full architectural flow (output → proposed decision → evidence → requirements/authority → gate → transition), so the architecture is shown to follow from the central distinction rather than being introduced later without connective tissue.
- Rewrote the CI/CD paragraph's closing to state explicitly that the decision-boundary/gate pattern is the contribution and CI/CD is one implementation location, not the theory itself.
- Rewrote the AIGov Core paragraph to match Source A §7 more faithfully — "engineering artifacts rather than reporting artifacts," with evidence/authority/policy context/assumptions attached to the decision — removing the more enforcement-forward v1 framing ("making governance decisions enforceable within AI delivery infrastructure"). Kept, not removed: it reinforces the evidence/authority/requirements vocabulary just defined, at low length cost, and is now closer to what Source A actually documents.
- Removed the explicit reconstructability discussion from "What this architecture buys you — and what it doesn't" ("doesn't make every past decision reconstructable... related but different problems"). Replaced with the narrower, Article-2-silent sentence supplied for this revision: "This architecture governs authorization at decision time. It does not, by itself, solve every problem of explainability, auditability, safety, or compliance."
- General tightening pass: shorter sentences in the "recording is not enforcing" section, removed a few redundant clauses, compacted the disclaimer paragraph.
- Ending preserved verbatim, as instructed — no new thesis introduced in the conclusion.

**AIGov Core: retained, not removed.** Reason: after rewriting it to track Source A §7 directly (engineering artifacts vs. reporting artifacts; evidence/authority/policy/assumptions attached to the decision), it no longer overclaims enforcement functionality the source doesn't document, costs only two sentences, and reinforces the article's own evidence/authority/requirements/gate vocabulary rather than reading as an aside. It does not claim AIGov Core empirically validates the pattern.

**Claims still requiring external sourcing:**
- None of the article's substantive claims rely on unverified prevalence or causal statistics; v2 removes both instances flagged in v1's editorial notes (the "most diagrams" claim and the "most governance failures" claim).
- "Training and evaluation typically get real architectural attention" (opening section) is a mild generalization about common ML engineering practice, not a governance claim — low risk, but worth a sanity check at copy-edit rather than being asserted as measured fact.
- The fairness/safety/robustness examples used for "how it was evaluated" remain illustrative only, not tied to a named regulation — same open question as v1 if this piece is meant to avoid implying a specific regulatory context.

**Boundary scan (Article 2 / Article 3 reserved material):** none found. Confirmed by direct text scan for: state is not knowledge, historical reconstruction, preservation of decision context, prompt/policy/retrieval drift, Git/transaction-log/tracing analogies, capability vs. understanding, epistemological gap, understanding layer, and explainability/observability/governance fragmentation. The v1 boundary-bridge sentence about later explainability was removed entirely in this revision rather than merely softened, since Section 9's instruction was to protect Article 2 harder — the replacement sentence stays entirely at decision time.

**Word count (article body, title through closing line, excluding this Editorial notes section):** 1,848 words total (including the ASCII diagram and Python pseudocode blocks); 1,798 words of running prose/headings if the diagram and code block are excluded — inside the 1,600–1,850 target and tighter than v1's 1,814 prose words, as requested.

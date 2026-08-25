# What Your AI Audit Trail Is Missing: The Relations, Not the Records

*Why approving an AI decision and explaining it later are two different engineering problems.*

## The Gap Between Approved and Explainable

A candidate model passes every required check. The evaluation report clears the bar. The dataset version is pinned. The deployment policy in effect that week requires two approvals for a model touching this pipeline, and it gets them. The gate opens. The model goes to production.

Nothing about this was informal. There was an evaluation, a policy, an approval, a gate. By any reasonable definition, the decision to promote this model was authorized.

Four months later, an incident review needs to answer a narrower question: what, exactly, authorized this specific deployment, and what exact state — which evaluation run, which dataset snapshot, which policy version, which approver — did that decision actually rely on? The deployment record still exists. So does the model registry. So do the logs. But the model has since been retrained twice, the evaluation pipeline has been updated, the policy document has been revised, and nobody thought to record which specific version of any of these the original decision consumed, as opposed to which versions merely existed at the time. The team can reconstruct that *a* valid-looking evaluation, policy, and approval existed around that date. They cannot establish, uniquely, that this deployment consumed *these specific ones* rather than a nearly-identical set from the week before or after.

The decision was approved. It is not explainable.

One clarification before going further, because the word invites a specific misreading: "explainable" here does not mean interpreting a model's internal reasoning — that is the job of interpretability and explainable-AI (XAI) research, and it is not what this article is about. Here, to *explain* a decision means something narrower and more mundane: to reconstruct it after the fact — to establish what authorized it, what state it actually consumed, and what action followed. A model can be maximally interpretable and the decision built on top of it can still be impossible to reconstruct months later, because interpretability and reconstructability are answers to different questions.

This gap — approved now, not explainable later — is not a logging failure in the usual sense. Nothing was deleted. Nothing crashed. The system simply never distinguished between *what existed* and *what this decision used*, and those turn out to be different engineering properties. Confusing them is easy, because most systems are architected as if solving one solves the other. It does not. Authorizing a decision and later explaining it are two separate problems, and this article is about why that's true, what causes it, and what to actually build so it stops being true for your own systems.

## The Decision Is the Unit — Not Only the Model

Start with a distinction that sounds pedantic and isn't: a model produces information. A decision authorizes a consequential change of state.

A model scoring a transaction, generating a recommendation, or evaluating a candidate for promotion is doing inference — producing an output. Nothing about that output, by itself, causes anything to happen in production. Something else has to decide that this particular output, in this particular context, is allowed to become an action: promote this model, approve this transaction, send this message, execute this tool call. That something is a decision, and it is a distinct object from the model output that fed it.

This is not a claim that models don't need auditing. Model evaluation, interpretability, and monitoring are real, necessary, well-developed disciplines, and nothing here argues otherwise. The claim is narrower: model-level auditability answers "is this a good model," not "was this specific production action authorized, and can we later establish why." Those are different questions, evaluated against different evidence, and a system can score well on the first while having no answer at all for the second.

Once you separate the two, a practical consequence follows immediately: the thing you need to track, gate, and later reconstruct is not only the model. It's the decision — the specific act of turning a model's output into a change in production state. A single model can participate in many decisions with different requirements: a fraud-scoring model's output might authorize an automatic block above one threshold, trigger a human review below it, and do nothing at all outside a certain transaction category — three different decisions, three different requirement sets, three different approving authorities, one model. Tracking auditability at the model level flattens all three into "was the model good," which is a real question but not the one an incident review actually needs answered.

This is also why model-level artifacts — a model card, an evaluation report, a registry entry — are not a substitute for decision-level records, even when they're done well. A model card describes the model in general; it doesn't say which specific decision relied on which specific version of it, under which specific policy, approved by whom. The decision — not only the model — is the operational unit this article follows from here on, because it's the level at which both of the article's central questions ("was this allowed?" and "what did it use?") actually have precise answers.

## Authorizing a Decision

Back to the model-promotion example, now at the moment it matters: the instant before the gate opens.

For that promotion decision to be genuinely authorized — not just informally agreed on in a chat thread — four things need to be explicit and checkable, not implicit and assumed:

**Evidence.** The specific artifacts the decision is based on: this evaluation run, against this dataset version, producing these metrics. Not "the model was evaluated" — *this* evaluation, identifiable and retrievable.

**Requirements.** What the evidence needs to satisfy before promotion is even eligible: minimum accuracy on a held-out set, no regression on a protected slice, latency under a threshold. Requirements make "good enough" a checkable condition instead of a judgment call made fresh each time.

**Authority.** Who — or what role, or what automated system — is actually permitted to approve this class of decision. Not "someone approved it," but a specific, checkable authority: this model class requires sign-off from a named role, and the deployment record shows that role's approval, not merely *an* approval from *someone*.

**A gate.** A mechanical checkpoint that actually blocks the transition to production if evidence, requirements, or authority are missing or don't check out — not a document describing what should happen, but code or infrastructure that enforces it. Documentation is not enforcement. A policy that says "models must be evaluated before promotion" changes nothing about what actually happens if nobody reads it that week; a gate that refuses to open without a passing evaluation attached changes exactly that.

Together these four give the gate exactly three possible outcomes, not an open-ended range of informal judgment calls: **allow** the promotion, **block** it outright, or **escalate** it to a human decision-maker when the automated check can't resolve it alone. That third outcome matters as much as the first two — an escalation path that itself has no evidence, requirement, or authority structure (a human "just looks at it and decides") is not actually a fourth safe option; it's the same gap wearing a human face. A well-formed escalation still needs the same evidence bundle the automated check would have used, a clear statement of which requirement it failed to satisfy automatically, and a named authority whose approval is then itself recorded as part of the decision — not a Slack thread standing in for all three at once. Skipping this is how organizations end up with gates that are rigorous for the easy cases and completely undocumented for exactly the edge cases most likely to matter later.

None of this is a new invention, and it shouldn't be presented as one. Admission controllers in Kubernetes block a pod from starting until policy checks pass. Policy decision points and policy enforcement points (the PDP/PEP pattern from access-control systems) separate "is this allowed" from "make it happen" in exactly the shape described above. Software supply-chain frameworks like in-toto and SLSA gate a build's promotion on signed, checkable attestations rather than trust. CI/CD deployment gates block a release until required checks pass. What's being described here is not a new enforcement mechanism — it's the same, well-understood pattern (evidence, requirements, authority, a mechanical gate) applied specifically to the point where a model's output is about to become a production-consequential decision, which is a boundary most ML pipelines don't yet treat as a distinct, enforced checkpoint at all. The synthesis is in the application, not the mechanism.

## Explaining a Decision, Later

Suppose the gate above worked exactly as designed. The promotion was genuinely authorized: real evidence, real requirements, a real approving authority, a real gate that would have blocked it otherwise. Does that mean the decision is now explainable, months later, if someone needs to ask what it actually relied on?

No — and this is the part that surprises people, because it seems like it should follow automatically.

Say the model registry retains model v17 and v18. The evaluation store retains evaluation run A and evaluation run B, both from around the promotion date. The policy repository retains three successive versions of the deployment policy, each a plausible candidate for "the one in effect that week." All of this is real, retained, and genuinely present in the system. It tells you what *existed*. It does not, by itself, tell you what *this specific decision consumed*.

That's the distinction this article calls **retained ≠ consumed**, and it's easy to walk past because retention feels like it should be sufficient. It isn't, for a precise reason: a version history records that a thing existed at a point in time. It does not, by default, record that a *specific later event* used *that specific version* rather than a different one that also existed nearby in time. If model v17 and v18 were both available around the promotion date, and nothing recorded which one the promotion decision actually bound to, then an investigator looking at the retained history later has two candidates that are both consistent with everything that was kept — and no way to choose between them from the retained record alone. The gap isn't that information was lost. It's that the specific fact an investigator needs — *this* decision consumed *that* version, not a nearby one — was never captured as its own fact in the first place. It was implicit in the moment, and moments don't get retained; only their artifacts do.

The same gap shows up in an even more ordinary shape: retroactive correction. Suppose the deployment policy is revised on Tuesday, and the promotion decision happened sometime that same week. A system that retains "current policy" plus a change history can usually tell you what the policy said on any given date — but if the policy record was updated in place rather than versioned with the specific timestamp the decision actually queried, an investigator six months later may only be able to narrow the candidate policy down to "one of the two or three versions active that week," not identify the one the gate actually evaluated against. Nothing was lost or overwritten maliciously; the system just never treated "which version did this decision see" as a fact worth keeping separately from "what did the policy eventually settle into."

The property that closes this gap is what can be called a **consumption relation**: an explicit record, made at decision time, that this decision bound to this specific evaluation run, this specific policy version, this specific approving authority — not "a" version consistent with the timeframe, but the one actually used. Retention gives you the pool of candidates. A consumption relation tells you which one from the pool was actually drawn.

It's worth being precise about what this claim is not. It is not a claim that bitemporal databases — systems that track both when a fact was true and when it was recorded — can't solve this. They can, and they're a mature, well-engineered way to represent exactly this kind of history precisely. The claim is mechanism-neutral: whatever storage technology is underneath, *some* mechanism has to actually record the consumption relation, at decision time, as a first-class fact — not be assembled after the fact by guessing which nearby version is "probably" the right one. A perfectly good bitemporal database that never captures "this decision consumed this row" has the identical gap as a plain log file that never captures it; the sophistication of the storage layer doesn't substitute for the presence of that one specific fact.

## When the Record Can't Decide

Here's a harder case than the one above, and it's worth sitting with because the honest answer is not "reconstruction succeeded" or "reconstruction failed" — it's a third thing.

Suppose the promotion decision consumed a metric that two different evaluation runs both happened to produce identically — a coincidence, not a bug, but a real possibility when evaluation runs are frequent and metrics are coarse. Now the retained record genuinely cannot tell you, from the evidence alone, which of the two evaluation runs the decision actually used. Both are equally consistent with everything that was kept.

This is not the same failure as the missing-consumption-relation case above. There, the information was simply never captured. Here, even a well-built reconstruction procedure, looking carefully at everything retained, runs into a record that is *genuinely underdetermined* — two candidates, equally supported, no tiebreaker available. The correct behavior in that situation is not to guess and report one of them as fact. It's to say so: this decision's history is **ambiguous**, and here are the candidates it could be. A reconstruction mechanism that instead picks one arbitrarily and reports it with confidence has produced something worse than no answer — a wrong answer that looks exactly like a right one, which is the one failure mode nobody wants from an audit process. Honest ambiguity and false confidence are not the same outcome, and treating them as interchangeable is where a lot of the trust in "we can audit this" quietly goes to die.

This same distinction — a record that determines a unique answer, versus one that genuinely doesn't and should say so — recurs one level up, when decisions form a sequence rather than standing alone: did this deployment decision depend on the output of an earlier decision in the same workflow, or a different one that produced a similar-looking result? The same principle applies, and the same mechanisms already used for single decisions — an explicit, preserved relation connecting one decision to the one it depended on — close the gap here too, the way distributed tracing already preserves parent-span relationships and workflow-provenance systems already preserve which upstream step produced which input. Nothing new is required architecturally; what's required is making sure that relation is actually captured, the same discipline as before, one level up.

## This Isn't a New Mechanism

It's worth stating plainly, because the alternative is easy to slide into by accident: none of the mechanisms this article describes are new.

Policy decision points and policy enforcement points have separated "is this allowed" from "make it happen" in access-control systems for decades. W3C's own provenance data model (PROV-DM) already distinguishes an entity's own attributes from the `used` relation connecting it to what it was derived from — structurally, exactly the consumption relation described above [1]. Workflow-provenance systems in scientific computing have modeled activity-to-entity dependency graphs since before most current ML tooling existed. Distributed tracing systems capture parent-span relationships specifically so a request's causal path across services can be reconstructed later, not just observed at the moment it happens [2]. Event-sourcing architectures already have the option to record which prior event a later one consumed, when they're instrumented to do so, rather than only recording what the later event itself did [3]. And in safety engineering, dynamic and continuous assurance cases go further than any of the above: they explicitly link a system's authorization claims to ongoing, in-operation evidence, treating "is this still justified" as something that has to be actively maintained over time rather than settled once at deployment — including, in recent work, applied specifically to frontier AI systems, where the case that a system is safe to operate is treated as something requiring continuous evidence rather than a one-time sign-off [4].

Every mechanism this article needs — an authorization gate, a consumption relation, honest handling of ambiguity, a cross-decision dependency link — already exists in some field adjacent to AI/ML engineering. What doesn't already exist, in most production AI systems today, is the discipline of connecting them around the AI-mediated decision specifically. ML engineering culture has, understandably, organized itself around the model: model registries, model cards, model evaluation reports, model versioning. That's not wrong, but it leaves the decision — the actual point where a model's output becomes a production action — as the thing nobody built dedicated tracking around, even though every piece needed to track it already exists somewhere else in the stack.

This is worth saying explicitly too: none of this is unique to AI. The distinction between authorizing something and later explaining it, and the distinction between what was retained and what was actually used, are old problems in systems engineering generally — the version-control, transaction-log, and tracing lineage above predates modern AI by decades. What AI-mediated systems add is not a new kind of problem; it's more of the same problem, more often, with more heterogeneous inputs (a model version, a prompt, a retrieval result, a tool's state, a policy version, sometimes a human approval) feeding into decisions that increasingly happen with less direct human mediation than a lot of the systems these mechanisms were originally built for. That's a reason the discipline matters more now, not a reason to claim it was invented now.

## What to Actually Build

```
                    evidence
                       |
                       v
model output --> proposed decision --> authorization gate --> action
                       |
                       |
                 decision record
                       |
          +------------+-------------+
          |                          |
authorization relation      consumption relation
          |                          |
          v                          v
 why was it allowed?        what did it actually use?
```

Translate the above into a concrete checklist. For every production-consequential AI-mediated decision, aim to preserve at least the following, as explicit fields the decision record actually carries — not implicit facts a future investigator has to reconstruct by inference:

- **Decision ID** — a stable identifier for this specific decision, distinct from any model version or run ID.
- **Proposed action** — what change of production state this decision would authorize if allowed.
- **Authorization relation** — the evidence used, the requirements evaluated against it, the policy version in force, the approving authority, and the gate's outcome (allow / block / escalate). This answers *why was it allowed*.
- **Consumption relation** — the specific model version, data/evaluation version, prompt or configuration state, retrieved or contextual inputs, and any relevant tool or policy state, that this decision actually bound to at the moment it was made — not merely what versions existed nearby in time. This answers *what did it actually use*.
- **Action relation** — the resulting production action or state transition that actually followed, distinct from the proposal (a decision can be authorized and still not executed, for independent operational reasons).
- **Dependency relations** — where decisions form a workflow, an explicit link from this decision to whichever prior decision's output it depended on, when such a dependency exists.
- **Reconstruction outcome** — when someone later asks what this decision relied on, the honest answer available from the record: **identified** (a unique answer exists), **ambiguous** (multiple candidates remain equally consistent with the record — list them), or **unavailable** (the relation was never captured).

Two things about this list matter as much as its contents. First, it is not a mandatory universal schema — the right field names, storage shape, and enforcement points will differ by system, and nothing here should be read as "implement exactly these seven fields or you've done it wrong." Some organizations will fold the authorization and consumption relations into one decision-record table; others will keep them in entirely separate systems (an approval workflow tool for the first, a data-lineage system for the second) and simply ensure both are queryable by the same decision ID. Either is fine. What matters is that both relations exist *somewhere*, addressable from a shared identifier, not that they live in any particular schema.

Second, the reconstruction-outcome field is doing real work by existing at all. A system that has no way to represent "ambiguous" as a legitimate outcome will, sooner or later, produce a confident wrong answer instead of an honest uncertain one, simply because nothing in the design gives it permission to say "I don't know, and here's why." That's the same failure mode described in the previous section, made concrete as a schema decision rather than an abstract principle: if your reconstruction tooling only has two possible outputs — a specific answer, or an error — it will eventually be asked a question the record genuinely can't resolve, and it will produce a specific answer anyway, because that's the only shape of output it knows how to give. Building "ambiguous, and here are the candidates" in as a first-class outcome from the start is considerably cheaper than discovering its absence during an incident review, when the wrong confident answer has already been acted on.

## What This Doesn't Claim

To be precise about scope: this is not a new provenance mechanism, not a new policy engine, and not a new enforcement architecture — every mechanism above already exists, credited above, in an adjacent field. It is not a compliance guarantee, and it does not constitute a complete AI governance framework; regulatory frameworks, safety cases beyond the authorization/reconstruction split described here, and organizational governance processes are all real and are all out of scope. It is not a claim that models don't require their own auditing — interpretability, evaluation, and monitoring remain necessary and are not replaced by anything here. It is not a claim that every AI-mediated action needs identical ceremony; a low-stakes internal recommendation and a production deployment decision don't need the same rigor, and this article takes no position on where exactly that line should sit for your system. And it makes no claim about system-level "understanding," about capability scaling outpacing anything, or about any dedicated new architectural layer — the mechanisms described here are ordinary engineering discipline applied at a specific boundary, not a new abstraction sitting above it.

What it does claim is narrower and, hopefully, more useful for having stayed narrow: logging more artifacts is not the same as being able to answer the two questions that actually matter when a decision is questioned later. *Why was this decision allowed?* and *what did this decision actually use?* are separate questions, answered by separate relations, and a system that has carefully built enforcement for the first has told you nothing about whether it can answer the second. Both have to be engineered, deliberately, around the decision — not assumed to follow from having approved it, and not assumed to follow from having kept the logs.

---

## References

[1] W3C, "PROV-DM: The PROV Data Model," W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-dm/

[2] OpenTelemetry, "Traces," OpenTelemetry Documentation. https://opentelemetry.io/docs/concepts/signals/traces/

[3] Fowler, M., "Event Sourcing," 2005. https://martinfowler.com/eaaDev/EventSourcing.html

[4] Carlan, C. et al., "Dynamic Safety Cases for Frontier AI," arXiv:2412.17618, 2024.

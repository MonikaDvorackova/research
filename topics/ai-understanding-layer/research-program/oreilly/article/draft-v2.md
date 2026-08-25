# Authorized Now, Reconstructable Later

*Why approving a production AI decision and reconstructing it later require different evidence and different system relationships.*

## The Gap Between Authorized and Reconstructable

A candidate model passes every required check. The evaluation report clears the bar. The dataset version is pinned. The deployment policy in effect that week requires two approvals for a model touching this pipeline, and it gets them. The gate opens. The model goes to production.

Nothing about this was informal. There was an evaluation, a policy, an approval, a gate. By any reasonable definition, the decision to promote this model was authorized.

Four months later, an incident review needs to answer a narrower question: what, exactly, authorized this specific deployment, and what exact state — which evaluation run, which dataset snapshot, which policy version, which approver — did that decision actually rely on? The deployment record still exists. So does the model registry. So do the logs. But the model has since been retrained twice, the evaluation pipeline has been updated, the policy document has been revised, and nobody preserved which specific version of any of these the original decision consumed, as opposed to which versions merely existed at the time. The team can establish that *a* valid-looking evaluation, policy, and approval existed around that date. They cannot establish, uniquely, that this deployment consumed *these specific ones* rather than a nearly identical set from the week before or after.

The decision was authorized. It is not reconstructable.

A quick note on that word, because it's easy to misread: reconstructing a decision here does not mean interpreting a model's internal reasoning — that is the job of interpretability and explainable-AI (XAI) research, and it is not what this article is about. To *reconstruct* a decision means something narrower and more mundane: to establish, after the fact, what authorized it, what state it actually consumed, and what action followed. A model can be maximally interpretable and the decision built on top of it can still be impossible to reconstruct months later, because interpretability and reconstructability answer different questions. Where "explain" appears below, it's shorthand for this — reconstruction, not model interpretation.

This gap — authorized now, not reconstructable later — is not a logging failure in the usual sense. Nothing was deleted. Nothing crashed. The system simply never distinguished between *what existed* and *what this decision used*, and those turn out to be different engineering properties. It's easy to architect a system as if solving one solves the other. It doesn't. Authorizing a decision and later reconstructing it are two separate problems, and this article is about why that's true, what causes it, and what to build so it stops being true for your own systems.

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

**A gate.** A mechanical checkpoint that actually blocks the transition to production if evidence, requirements, or authority are missing or don't check out — not a document describing what should happen, but code or infrastructure that enforces it. Documentation is not enforcement. A policy that says models must be evaluated before promotion changes nothing about what actually happens if nobody reads it that week; a gate that refuses to open without a passing evaluation attached changes exactly that.

Together, these four let a useful gate expose three operational outcomes, rather than an open-ended range of informal judgment calls: **allow** the promotion, **block** it outright, or **escalate** it to a human decision-maker when the automated check can't resolve it alone. Escalation matters as much as the other two — an escalation path with no evidence, requirement, or authority structure of its own (a human "just looks at it and decides") isn't a fourth safe option; it's the same gap wearing a human face. A well-formed escalation still needs the same evidence bundle the automated check would have used, a clear statement of which requirement it couldn't verify automatically, and a named authority whose approval is itself recorded as part of the decision. Skipping this is how organizations end up with gates that are rigorous for the easy cases and undocumented for exactly the edge cases most likely to matter later.

None of this is a new invention, and it shouldn't be presented as one. Kubernetes admission controllers block a pod from starting until policy checks pass [1]. Policy decision points and policy enforcement points — the PDP/PEP pattern formalized in access-control standards like XACML — separate "is this allowed" from "make it happen" in exactly the shape described above [2]. Software supply-chain frameworks like in-toto [3] and SLSA [4] gate a build's promotion on signed, checkable attestations rather than trust. CI/CD deployment gates block a release until required checks pass. What's being described here is not a new enforcement mechanism — it's the same, well-understood pattern (evidence, requirements, authority, a mechanical gate) applied specifically to the point where a model's output is about to become a production-consequential decision, a boundary that doesn't map cleanly onto model registries, model cards, or evaluation reports — the artifacts ML tooling already centers. The synthesis is in the application, not the mechanism.

## Reconstructing a Decision Later

Suppose the gate above worked exactly as designed. The promotion was genuinely authorized: real evidence, real requirements, a real approving authority, a real gate that would have blocked it otherwise. Does that mean the decision is now reconstructable, months later, if someone needs to establish what it actually relied on?

No — and this is the pivot the rest of the article turns on. Authorization and reconstruction ask different questions of different evidence. **Authorization** asks whether the system had enough evidence and authority to permit the transition, evaluated at the moment the decision was made. **Reconstruction** asks whether the retained record, examined later, contains enough information to establish what the transition actually depended on. A system can satisfy either property while failing the other — passing the gate says nothing about whether the record left behind will later determine a unique answer.

Say the model registry retains model v17 and v18. The evaluation store retains evaluation run A and evaluation run B, both from around the promotion date. All of this is real, retained, and genuinely present in the system. It tells you what *existed*. It does not, by itself, tell you what *this specific decision consumed*. A version history records that a thing existed at a point in time; it does not, by default, record that a specific later event used that specific version rather than a different one that also existed nearby in time. If v17 and v18 were both available around the promotion date and nothing distinguishes which one this decision actually depended on, an investigator later has two candidates equally consistent with everything retained — and no way to choose between them from the record alone. The gap isn't that information was lost. It's that the one fact an investigator needs — *this* decision consumed *that* version, not a nearby one — was never established as its own fact, whether at the time or afterward.

The requirement this points to is informational, not representational: **the retained system record must preserve enough evidence to identify the consumed context uniquely.** That evidence may be captured directly, as an explicit binding authored when the decision is made. Or it may be reliably derivable afterward, from provenance edges, event records, execution traces, or a sufficiently precise temporal history — as long as the derivation actually narrows to one answer, not several. Explicit decision-time recording is one way to guarantee this property holds. It is not the only way, and this article does not claim it's required. A correctly designed bitemporal database or a well-instrumented event log can already preserve everything needed, if it's instrumented to capture the right relationship — the failure isn't about which storage technology sits underneath; it's about whether the retained record, whatever form it takes, leaves multiple candidate histories equally consistent with what's known.

That failure is worth naming precisely, because it can happen even in careful systems. If a policy document is updated in place rather than preserving its own history at the exact moment a decision queried it, a later investigation may only narrow the candidate policy down to "one of a few versions active that week" — not identify the one the gate actually evaluated against. Nothing was lost maliciously; the system simply never treated "which version did this decision see" as a fact worth keeping distinct from "what did the policy eventually become." When that happens, the honest answer is that the consumed context is ambiguous — not unreconstructable, and not something to guess at with false confidence. The next section is about exactly that distinction.

## When the Record Can't Decide

A reconstruction attempt against any decision record can land in one of three places, and it's worth naming all three, because conflating them is where trust in "we can audit this" quietly erodes.

**Identified.** The retained record determines a unique answer: this decision consumed this evaluation run, this policy version, this approving authority. No other candidate is consistent with what's known.

**Ambiguous.** More than one candidate remains equally consistent with the retained record — two evaluation runs that happened to produce an identical metric, two policy versions active in the same window with no way to tell which one the decision actually queried. The record genuinely underdetermines the answer.

**Unavailable.** The information needed to reconstruct the decision was never retained, or is no longer accessible, and no candidate can even be proposed from what remains.

Ambiguous is not the same failure as wrong, and it's worth being precise about where the actual engineering failure sits. If a system reports "ambiguous" honestly — here are the two candidates, and the record can't distinguish them — it has not failed. It has correctly reported the limits of what was preserved. The failure, if there is one, happened earlier: whatever engineering decision left the record underdetermined in the first place, when unique reconstruction was actually a requirement. A reconstruction mechanism that instead picks one candidate arbitrarily and reports it with confidence has produced something worse than an honest "I don't know" — a wrong answer that looks exactly like a right one, and that's the one outcome that should never be acceptable from an audit process.

This same three-way distinction recurs one level up, when decisions form a sequence rather than standing alone: did this deployment decision depend on the output of an earlier decision in the same workflow, or a different one that produced a similar-looking result? The same principle applies, and the same mechanisms already used for single decisions — a preserved relation connecting one decision to the one it depended on — close the gap here too, the way distributed tracing already preserves parent-span relationships and workflow-provenance systems already preserve which upstream step produced which input. Nothing new is required architecturally; what's required is making sure that relation is actually captured, or reliably derivable, one level up from a single decision.

## This Isn't a New Mechanism

It's worth stating plainly, because the alternative is easy to slide into by accident: none of the mechanisms this article describes are new.

Policy decision points and policy enforcement points have separated "is this allowed" from "make it happen" in access-control systems for decades [2]. Database-provenance theory formalized the distinction between an entity's own attributes and the relations connecting it to what it was derived from over a decade before general-purpose provenance standards existed [5], and W3C's own provenance data model (PROV-DM) represents structurally the same relationship this article calls a consumption relation [6]. Distributed tracing systems capture parent-span relationships specifically so a request's causal path across services can be reconstructed later, not just observed at the moment it happens [7]. Event-sourcing architectures already have the option to record which prior event a later one consumed, when they're instrumented to do so, rather than only recording what the later event itself did [8]. And in safety engineering, dynamic and continuous assurance cases go further than any of the above: they explicitly link a system's authorization claims to ongoing, in-operation evidence, treating "is this still justified" as something that has to be actively maintained rather than settled once at deployment — including, in recent work, applied specifically to frontier AI systems, where the case that a system is safe to operate is treated as requiring continuous evidence rather than a one-time sign-off [9]. Of everything cited here, dynamic and continuous assurance cases come closest to this article's own combined concern — linking a prospective authorization claim to ongoing, retrospective evidence is exactly the shape of the authorization/reconstruction duality this piece describes, and it wasn't invented here.

Every mechanism this article needs — an authorization gate, a consumption relation, honest handling of ambiguity, a cross-decision dependency link — already exists in some field adjacent to AI/ML engineering. What this article contributes is narrower: a practitioner translation, centered specifically on the AI-mediated production decision, that separates authorization from reconstruction explicitly and connects each to the mechanisms that already exist to satisfy it. ML engineering culture has, understandably, organized itself around the model: model registries, model cards, model evaluation reports, model versioning. That's not wrong, but it leaves the decision — the actual point where a model's output becomes a production action — as the thing nobody built dedicated tracking around, even though every piece needed to track it already exists somewhere else in the stack.

This is worth saying explicitly too: none of this is unique to AI. The distinction between authorizing something and later reconstructing it, and the distinction between what was retained and what was actually used, are old problems in systems engineering generally — the access-control, provenance, and tracing lineage above predates modern AI by decades. What AI-mediated systems add is not a new kind of problem; it's the same problem with more heterogeneous inputs than the systems these mechanisms were originally built for typically carry — a decision's consumed context can be distributed across a model version, a prompt or configuration state, a retrieval result, a tool's state, an underlying dataset, a policy version, and a human or service authority, all at once, feeding decisions that increasingly happen with less direct human mediation than before. That heterogeneity is the reason the discipline matters more now, not a reason to claim it was invented now.

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

Split the practical checklist into two different moments, because they come from two different processes and mixing them is a real source of confusion.

**What to preserve around the decision**, populated as the decision happens:

- *Decision identity* — a stable decision ID, distinct from any model or run ID; the proposed action; the resulting production action or state transition that actually followed (a decision can be authorized and still not executed, for independent operational reasons).
- *Authorization evidence* — the evidence used, the requirements evaluated against it, the policy version in force, the approving authority, and the gate's outcome (allow / block / escalate). This answers *why was it allowed*.
- *Execution and consumed-context evidence* — the specific model version, data/evaluation version, prompt or configuration state, retrieved or contextual inputs, and any relevant tool or policy state the decision actually bound to — captured directly, or backed by provenance, event, or trace data precise enough to derive it uniquely later. This answers *what did it actually use*.
- *Cross-decision relations* — where decisions form a workflow, a link from this decision to whichever prior decision's output it depended on, when such a dependency exists.

**What a reconstruction process should be able to return**, evaluated whenever someone later asks the question — not persisted at decision time, because it isn't known at decision time:

- **Identified**, **ambiguous** (with the candidates named), or **unavailable** — the three outcomes from the previous section, applied here as the honest output any reconstruction tooling should be capable of producing.

Two things about this split matter as much as its contents. First, it is not a mandatory universal schema — the right field names, storage shape, and enforcement points will differ by system. Some organizations will fold authorization and consumption evidence into one decision-record table; others will keep them in entirely separate systems (an approval workflow tool for the first, a data-lineage system for the second) and simply ensure both are queryable by the same decision ID. Either is fine, as long as both kinds of evidence exist somewhere, addressable from a shared identifier.

Second, the reconstruction outcome deserves to be a first-class *possible answer*, not an afterthought. If a reconstruction interface can only return a specific answer or an error, it has no honest way to represent a genuinely underdetermined record — that design creates pressure to collapse ambiguity into a specific answer that looks the same as a determined one, simply because nothing in the design permits reporting the alternative. Building "ambiguous, and here are the candidates" in as a legitimate output from the start costs little; discovering its absence during an incident review, after a wrong confident answer has already been acted on, costs a great deal more.

## What This Doesn't Claim

To be precise about scope: this is not a new provenance mechanism, not a new policy engine, and not a new enforcement architecture — every mechanism above already exists, credited above, in an adjacent field. It is not a compliance guarantee, and it does not constitute a complete AI governance framework; regulatory frameworks, safety cases beyond the authorization/reconstruction split described here, and organizational governance processes are all real and are all out of scope. It is not a claim that models don't require their own auditing — interpretability, evaluation, and monitoring remain necessary and are not replaced by anything here. It is not a claim that every AI-mediated action needs identical ceremony; a low-stakes internal recommendation and a production deployment decision don't need the same rigor, and this article takes no position on where exactly that line should sit for your system. And it makes no claim about system-level "understanding," about capability scaling outpacing anything, or about any dedicated new architectural layer — the mechanisms described here are ordinary engineering discipline applied at a specific boundary, not a new abstraction sitting above it.

What it does claim is narrower, and hopefully more useful for having stayed narrow. Authorization and reconstruction are separate engineering properties, and both depend on preserving enough information about the relationships around a decision — what permitted it, and what it consumed — to answer those questions when they matter, whether that information is captured explicitly at the time or reliably established afterward. A system that has carefully built enforcement for the first has told you nothing about whether it can answer the second. Both have to be engineered, deliberately, around the decision — not assumed to follow from having approved it, and not assumed to follow from having kept the logs.

---

## References

[1] Kubernetes, "Admission Controllers Reference," Kubernetes Documentation. https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/

[2] OASIS, "eXtensible Access Control Markup Language (XACML) Version 3.0," OASIS Standard, 22 January 2013. https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html

[3] in-toto, "in-toto: A Framework to Secure the Integrity of Software Supply Chains." https://in-toto.io/

[4] SLSA, "Supply-chain Levels for Software Artifacts." https://slsa.dev/

[5] Buneman, P., Khanna, S., Tan, W.C., "Why and Where: A Characterization of Data Provenance," International Conference on Database Theory (ICDT), 2001.

[6] W3C, "PROV-DM: The PROV Data Model," W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-dm/

[7] OpenTelemetry, "Traces," OpenTelemetry Documentation. https://opentelemetry.io/docs/concepts/signals/traces/

[8] Fowler, M., "Event Sourcing," 2005. https://martinfowler.com/eaaDev/EventSourcing.html

[9] Carlan, C. et al., "Dynamic Safety Cases for Frontier AI," arXiv:2412.17618, 2024.

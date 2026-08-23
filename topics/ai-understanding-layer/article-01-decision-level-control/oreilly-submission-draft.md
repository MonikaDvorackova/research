# Model Outputs Are Not Decisions: Building Evidence-Gated AI Systems

### A practitioner pattern for the boundary where a model's output becomes a production action — borrowed from ideas access control and supply-chain security already solved

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

This gap is what this article calls a **decision boundary** — a proposed term for this framing, not an established one — an explicit point in the architecture where the system stops treating an output as self-authorizing and asks whether the conditions for the corresponding decision have actually been met. What sits at that boundary, this article calls a **decision layer** — again, a name proposed here, not an industry standard. Its shape is simple to state: an output becomes a proposed decision; a proposed decision needs evidence; evidence gets checked against requirements and authority; and only what passes becomes an actual system transition.

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

Where you install this gate depends on when the decision happens. For a deployment-time decision like this one, CI/CD is a natural fit, since it already mediates the transition from candidate artifact to production state. A decision made at runtime — by an agent, or a live policy check rather than a deployment step — needs its enforcement point in the request path instead, not the pipeline. The gate is the same pattern either way; only where it runs changes.

## The mechanism isn't new. The boundary is the point.

None of this is new mechanism. Software engineering already has mature, well-established answers for exactly this shape of problem — just not usually applied at the point where a model's output becomes a production action.

**Access control** has never treated a request as self-authorizing. Architectures like XACML separate the request itself from the policy that governs it, the attributes needed to evaluate that policy, and the point that actually enforces the decision. That's the same separation — evidence kept apart from requirements, kept apart from the gate that checks them — just applied here to a proposed promotion instead of an access request.

**Software supply-chain security** already assumes a technically valid artifact isn't automatically an admitted one. Kubernetes admission controllers, and tools like Sigstore's policy-controller checking in-toto attestations, won't let a container image through — however well built — without the evidence a policy requires. A model with acceptable metrics is in a similar position to an image with a clean build: fine on one axis, not yet authorized on the one that matters.

**Deployment pipelines** already treat "technically deployable" and "approved to deploy" as different things — a required-reviewer rule on a protected environment is a human authorization path formalized into the pipeline, not an informal exception bolted onto it.

None of these ideas were invented for AI. The useful move is applying them at a boundary AI/ML pipelines don't usually make explicit: what evidence has to exist before this model's output is allowed to cause this system transition?

## What this architecture buys you — and what it doesn't

What does this actually buy you? An explicit decision boundary instead of an implicit one. Evidence and requirements that can be inspected rather than inferred from someone's memory of the policy. Deterministic enforcement for the classes of decision where that's appropriate. Clear authority — a record of who or what was allowed to say yes. And, when the inputs and the rules are fixed, a gate outcome that's reproducible rather than a judgment call that might go differently on a different day. It also removes the specific failure mode this article opened with: the informal, unchecked transition from "evaluation finished" to "production changed."

It's worth being equally clear about what this doesn't buy. This architecture governs authorization at decision time. It does not, by itself, solve every problem of explainability, auditability, safety, or compliance. It doesn't guarantee regulatory compliance, general trustworthiness, or the absence of AI risk. And it isn't the right amount of machinery for every AI application — a low-stakes internal experiment doesn't need the same gate a customer-facing production model does. The claim here is narrower: for decisions with real production consequences, evidence and enforcement work better as architecture than as documentation.

## The question that matters

AI engineering has spent the last several years getting very good at producing better outputs — more accurate models, better-calibrated scores, more capable agents. Production engineering has to answer a different question: what is a system allowed to do because of what a model said?

The useful move is architectural, not procedural: stop letting the transition from output to consequential action happen implicitly, and put an explicit, evidence-gated boundary in its place. Not because outputs can't be trusted, but because "trusted enough to act on" is itself a decision, and decisions deserve a place in the architecture where they're actually made — not assumed.

The question is not only whether the model produced a good output. The question is whether the system has enough evidence to authorize what happens next.

---

## Further reading

- OASIS, *eXtensible Access Control Markup Language (XACML) Version 3.0* — the PEP/PDP/PIP/PAP model referenced above. docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html
- Kubernetes, *Admission Control* — kubernetes.io/docs/reference/access-authn-authz/admission-controllers/
- Sigstore, *Policy Controller* — docs.sigstore.dev/policy-controller/overview/; in-toto Attestation Framework — github.com/in-toto/attestation
- GitHub, *Deployment protection rules* — docs.github.com/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules

---

## Editorial notes

*(Not part of the article. For internal review before publication.)*

**Exact prose word count:** 2,016 words — title through the end of "The question that matters," i.e. the article proper, excluding the "Further reading" list (per the instruction to target length "excluding references") and excluding this Editorial notes section; the ASCII diagram and Python pseudocode blocks are also excluded, consistent with prior drafts' methodology. This is within the 1,800–2,100 target and under the 2,200 ceiling. (Including "Further reading," total body length is 2,061 prose words / 2,111 words counting the diagram and code blocks.)

**Sources introduced (all verified in `novelty-audit.md` / `sourcing-audit.md`, none invented):**
- OASIS XACML 3.0 specification (docs.oasis-open.org) — access-control analogy.
- Kubernetes admission control documentation (kubernetes.io) — supply-chain/admission analogy.
- Sigstore policy-controller documentation (docs.sigstore.dev) and the in-toto attestation framework (github.com/in-toto/attestation) — supply-chain/admission analogy, evidence-bundle precedent.
- GitHub Actions deployment protection rules documentation (docs.github.com) — deployment-protection analogy; also supports the existing CI/CD placement paragraph.

Four sources were selected from the audit's larger set, per instruction to choose approximately 2–4 rather than everything researched. OPA/Rego, Cedar, ML model registries (MLflow/Databricks/Vertex), NIST AI RMF, Model Cards, Guardrails AI, AI gateways, MCP, and the Deontic Policies paper were all considered and deliberately left out of the article body — either redundant with the four chosen (OPA/Cedar largely restate the XACML point), too narrow to the running example in a way that would undercut generality (ML registries — see "novelty claims deliberately avoided" below), or reserved for Articles 2/3 (Deontic Policies, NIST AI RMF).

**Novelty claims deliberately avoided:**
- The article never claims to have invented gating, policy enforcement, evidence-based authorization, ALLOW/BLOCK-style decision logic, CI/CD enforcement, or authorization architectures generally — this is now stated explicitly and prominently, not just implied by hedged terminology.
- "Decision boundary" and "decision layer" are both explicitly flagged at first use as proposed, non-established terms for this article's framing (previously only "decision layer" carried this flag).
- "Evidence-gated decision" and "evidence gate" are used only as lowercase descriptive phrases in the body. The title's "Evidence-Gated AI Systems" is title-case styling of the working title (describing a category of systems, "AI systems that are evidence-gated") and was explicitly permitted by the audit; "Evidence-Gated AI" does not appear anywhere as a standalone branded framework name or proper noun within the article body.
- The title was reconsidered against two alternatives (a title foregrounding "access control" directly, and a punchier "the gate your pipeline doesn't have" framing) and the original title was retained: it states a distinction and a construction task ("Building... Systems," in the ordinary practitioner-book sense of building something in your own systems), not an invention claim, and this reading is now directly reinforced by the new dek and the prior-art section.
- One specific omission was deliberately made and is worth flagging for human review: ML model registries (MLflow, Databricks Unity Catalog, Vertex AI Model Registry) are the closest existing prior art to the running example specifically (see `novelty-audit.md`, Objection 4) — closer than any of the four sources actually cited. They were left out of the article body because naming them would require acknowledging that the running example's core transition is close to an existing, off-the-shelf capability, which would either require a longer treatment than the word budget allows or risk undercutting the running example's illustrative value. This omission is a real editorial choice, not an oversight, and a human reviewer may reasonably decide it should be disclosed.

**AIGov Core: removed.** Per the instruction that the final article does not need a product mention for credibility, and given the new prior-art section already carries the intellectual-honesty work the AIGov Core paragraph was partly doing in v2, keeping a proprietary-system mention immediately after a "we didn't invent this" argument risked reading as promotional exactly where the article is trying to sound most disinterested. Removing it also kept the article inside the tighter word budget without cutting substantive material.

**Statements still requiring human factual verification:**
- The "training and evaluation typically get real architectural attention" line remains uncited in-body (per instruction to keep the piece from becoming citation-heavy); Sculley et al., "Hidden Technical Debt in Machine Learning Systems" (NeurIPS 2015), was identified in `sourcing-audit.md` as a desirable-not-required supporting source, and its existence was confirmed via search but its full text was not read this session — verify before any direct quotation.
- The four Further Reading URLs were retrieved via live search and appear to be the correct canonical documentation pages, but were not independently re-verified by a second fetch in this session; spot-check links before publication.
- The fairness/safety/robustness examples used earlier in the article remain illustrative only, not tied to any named regulation — unchanged open question from prior drafts.

**Article 2 / Article 3 boundary scan:** confirmed clean by direct review. The prior-art section discusses supply-chain attestations (SLSA/in-toto family) strictly as evidence-bundle precedent for decision-time gating — it does not develop provenance-as-durable-historical-record, reconstructability, or drift-over-time arguments, all of which are reserved for Article 2. No mention of Git, transaction logs, distributed tracing, capability-vs-understanding, epistemological framing, an "understanding layer," or the fragmentation-of-explainability/observability/governance thesis — all reserved for Article 3. The article's closing does not introduce any claim beyond what the article itself argued.

**Self-review checklist (all pass):**
1. Could a reader think we're claiming to have invented policy gates? No — the article now says so explicitly and prominently, with named prior art, before the benefits section.
2. Is output-vs-decision obvious by the first third? Yes — stated as a definition pair within the first section after the opening scenario.
3. Does prior art strengthen rather than derail the argument? Yes — it resolves the credibility risk the novelty audit flagged (silent omission) without turning the piece into a literature review; the section is ~230 words and ends by pointing back at the article's own question.
4. Is there a concrete, implementable pattern? Yes — unchanged from v2: named components, three-way outcome semantics, working pseudocode, and explicit guidance on where to install the gate.
5. Does the article still have a distinctive thesis after novelty claims are narrowed? Yes — the thesis is now explicitly the synthesis/application move itself ("applying them at a boundary AI/ML pipelines don't usually make explicit"), which is a real, narrower, and more defensible claim than v2's implicit framing.
6. Does it consume Article 2 or Article 3? No — see boundary scan above.

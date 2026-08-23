# Model Outputs Are Not Decisions: Building Evidence-Gated AI Systems

### Production ML architecture is organized around models. Once outputs can cause consequential actions, the model stops being the right unit of control — the decision is.

---

A model finishes an evaluation run. The dashboard shows accuracy: 0.913, latency within budget, no obvious regressions against the previous version. Someone opens the deployment pipeline. Nothing technical stops them from promoting the new model to production right now.

What, exactly, makes that promotion justified?

Not "is the model good" — the metrics answer that, more or less. The harder question is architectural: what has to be true, and be checked, before the system is allowed to change what it does in production? Training and evaluation typically get real architectural attention: pipelines, harnesses, versioned datasets, dashboards. The transition from an evaluation result to a production authorization can be as thin as a single conditional, or a person clicking "deploy" after reading a dashboard, with nothing else checking it.

That thinness is the subject of this article — and, underneath it, a bigger assumption worth questioning: that a good model is most of what production AI architecture needs.

## Outputs are not decisions

Two things happened in that scenario, and it's worth naming them separately.

An output is information produced by the system. A decision is an authorized state transition.

The model produced an **output**: `accuracy = 0.913`. It describes something — how well the model performed against a test set, what label it assigned, what text it generated, what action it recommends. An output does not, by itself, authorize anything; it's a claim, not a change.

The system then made — or was about to make — a **decision**: `promote model v17 to production`. Before the decision, production traffic is served by v16. After, it's served by v17. Something that could not previously happen is now permitted — that's what makes it a decision rather than an output.

The architectural problem starts exactly where these two get treated as equivalent — where a good output stands in for the decision to act on it. This is what this article calls a **decision boundary** — a proposed term for this framing, not an established one: the point where the system stops treating an output as self-authorizing and asks whether the conditions for the corresponding decision have actually been met.

## The model is not the unit of control

Production ML architecture is organized around a familiar shape: data becomes training, training becomes a model, a model gets evaluated, an evaluated model gets deployed. Model registries, versioning, evaluation harnesses, CI/CD for ML — almost all of it exists to answer one question: *how do we build, evaluate, version, and deploy models?*

That's a good question, and nothing here argues otherwise. It stops being the only one that matters once a model's output can cause something to happen — trigger a refund, change a price, deny a transaction, call a tool. At that point a second question becomes unavoidable, and the model lifecycle doesn't answer it: *under what conditions is an AI-derived output allowed to change the state of a real system?* The model lifecycle isn't wrong; it's just answering "how do we build a good model," not "what is this system allowed to do because of what the model said" — and treating the second as automatically settled by the first is exactly the gap the opening scenario showed.

The architecture that answers the second question doesn't replace the model lifecycle — it cuts across it. Call it the **decision layer**: the set of decision boundaries — output → proposed decision → evidence → authorization → state transition — that sit wherever an AI-derived output is about to cause something consequential. A boundary can exist at deployment time, the scenario this article keeps returning to. It can just as easily exist at inference time, before a recommendation changes a downstream workflow, before an agent calls a tool, or before an automated system executes an external action — none of which are "the model lifecycle" in the data-to-deployment sense.

Put sharply: evaluation tells you whether an output is good. Authorization tells you whether the system may act on it. Those are different engineering problems, and a good model has never been proof that either one was answered.

## What a production decision needs

Wherever a decision boundary sits — deployment, a runtime recommendation, an agent's next tool call — the same architecture closes the output/decision gap. Call it evidence: the structured basis for a decision, not the informal signal a human glances at before clicking deploy.

For a promotion decision, evidence has to establish that the model version and dataset are correctly identified, that it passed the required tests, and that the results actually exist rather than being assumed present.

Evidence isn't the whole picture. **Decision requirements** are the conditions that must hold before the transition is permitted — a threshold, a required test, a policy version; they're what evidence gets checked against, not something that acts on its own. **Authority** is who or what may authorize this particular transition — an automated rule for routine cases, a named role for higher-risk ones; it answers a different question than evidence does: not "does the evidence satisfy the requirement," but "is this the party allowed to say yes."

None of this implies one universal schema — a low-risk internal tool and a customer-facing pricing model don't need the same bar, only the same underlying architecture. And once evidence, requirements, and authority exist and are attached to a proposed decision, a further problem appears immediately: none of this, by itself, stops anything from happening.

## Recording is not enforcing

There's a difference between "the organization has a policy that says X" and "the production architecture won't proceed unless X is true." Documenting a requirement and enforcing it are not the same act — treating them as equivalent is where control quietly disappears.

Suppose policy requires a robustness evaluation before any promotion, and for this model it was never run. The requirement is documented — a model card, a governance wiki, a compliance checklist someone signs — but the pipeline still lets the promotion through, because nothing in it reads that requirement and checks whether it was satisfied.

The organization has a policy. The system does not enforce it. A fully documented system can still execute a decision that violates its own stated requirements, because documentation describes intended behavior and doesn't constrain actual behavior. This isn't an argument against documentation — model cards and approval records do something else, valuable in its own right. The point is narrower: documentation and enforcement solve different problems, and only one of them can stop a decision from happening.

## The evidence-gated pattern

The pattern that closes this gap — call it an **evidence-gated decision**, a proposed term rather than an established one — applies at any decision boundary, not only deployment: put a gate at the boundary, and require every proposed decision to pass through it before it can take effect.

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

A **proposed decision** names the transition being requested — "promote model v17 to production" — without assuming it will happen. An **evidence bundle** attaches evaluation results, artifact/dataset identifiers, and the source each result came from. **Decision requirements** state the conditions this class of decision must satisfy.

The gate's job: bring these together with authority, and return one of three outcomes.

**ALLOW** — the evidence satisfies the requirements, and the decision is within the gate's own authority; the transition proceeds automatically.

**BLOCK** — a required condition isn't satisfied, or evidence is missing entirely; the decision doesn't proceed, and is recorded as a failed decision, not silently dropped.

**ESCALATE** — the gate can't authorize the transition under current conditions, but policy allows the decision to move to a separate, explicitly authorized review path — a second authorization path, not an exception to the architecture.

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

Where you install the gate depends on when the decision happens: CI/CD for deployment-time decisions, since it already mediates candidate-to-production transitions; the request path for runtime decisions instead. The gate is the same pattern either way — only where it runs changes.

## The mechanism isn't new. The placement is.

None of this is new mechanism. Software engineering has repeatedly separated "this was computed" from "this is now authorized to happen" — just not usually inside AI pipelines.

**Access control** never treats a request as self-authorizing: XACML separates the request from the policy, the evidence needed to evaluate it, and the point that enforces the decision. **Databases** draw the same line inside a single system — computing a value and committing a transaction are different operations, and a merely-computed value has no effect until something explicitly commits it. **Kubernetes admission control** won't treat a technically valid object as an admitted one without a separate check. **Software supply-chain security** — Sigstore's policy-controller checking in-toto attestations — won't admit a cleanly built container image without the evidence a policy requires. **CI/CD** treats "deployable" and "approved to deploy" as different states, with required-reviewer rules formalizing the second as a real path, not an exception. **Model registries** like MLflow's and Databricks Unity Catalog's already provide staged promotion and approval for model versions — this isn't unfamiliar territory inside ML either.

What's missing isn't the mechanism. It's where the discipline gets attached. A model registry gates a model's *stage*. None of the examples above gates an arbitrary *decision*, wherever one occurs, regardless of which model is involved. The mechanisms are old. The placement is the argument.

## One model, many decisions

This matters more than "add a gate to your pipeline." The same large language model can summarize an internal document, recommend denying a transaction, draft an external email, and generate a database mutation. The model is identical in all four cases. The decisions are not — different evidence is relevant, different people or rules have authority, different consequences follow from being wrong.

Model-level governance — approving a model version, documenting its evaluation, granting it a deployment sign-off — cannot express any of that. A single approval, attached to the model, has no way to say this model may summarize documents but not deny transactions, or that denying a transaction needs a compliance reviewer while summarizing a document needs no one. The model isn't the wrong thing to govern; it's an *insufficient* one — the object with consequences is the decision the output feeds into, and one model participates in many.

This gets sharpest with agents. A model's output might be the text *"Refund the customer."* A system decision is `issue_refund(customer_id, amount)`. Generating that tool call is still just an output — a proposed action, not an authorized one — and it shouldn't become authorized merely because a capable model produced it fluently. The gate belongs between the proposal and the effect, exactly as for a model promotion — only where it sits changes.

It also exposes a gap in how "human-in-the-loop" gets used: a person present in a workflow is not, by itself, a control architecture. Ask, of any human-in-the-loop step: what evidence do they see? What, specifically, are they authorized to approve? If they say no, is that refusal enforced, or does the system proceed anyway on a timeout? An approval step that can't answer those questions isn't an authorization path; it's a person standing near a button — a weaker version of the informal transition this article opened with.

## What this buys you — and what it doesn't

A decision boundary that's explicit instead of assumed. Evidence and requirements that can be inspected rather than inferred from memory. A real second authorization path, not a bypass, where automated enforcement isn't appropriate. And because the boundary is attached to the decision rather than the model, it generalizes — the same pattern that gates a promotion gates a tool call.

It's equally worth being clear about what this doesn't buy: regulatory compliance, general trustworthiness, or the absence of AI risk — and it isn't the right amount of machinery for every application. The claim is narrower: for decisions with real consequences, evidence and enforcement work better as architecture, attached to the decision, than as documentation attached to the model.

## The question that matters

AI engineering has spent the last several years getting very good at producing better outputs — more accurate models, better-calibrated scores, more capable agents. Production engineering has to answer a different question: what is a system allowed to do because of what a model said?

The useful move isn't procedural. It's a change in what gets governed: stop organizing control around the model, and organize it around the decision — the point where an output threatens to become an effect. Evaluation tells you whether an output is good. Authorization tells you whether the system may act on it. A good model has never been proof that either one was answered.

The question is not only whether the model produced a good output. The question is whether the system has enough evidence to authorize what happens next.

---

## Further reading

- OASIS, *eXtensible Access Control Markup Language (XACML) Version 3.0* — docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html
- Kubernetes, *Admission Control* — kubernetes.io/docs/reference/access-authn-authz/admission-controllers/
- Sigstore, *Policy Controller* — docs.sigstore.dev/policy-controller/overview/; in-toto Attestation Framework — github.com/in-toto/attestation
- GitHub, *Deployment protection rules* — docs.github.com/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules
- MLflow, *Model Registry* — mlflow.org/docs/latest/ml/model-registry/; Databricks, *Manage model lifecycle in Unity Catalog* — docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/

---

## Editorial notes

*(Not part of the article. For internal review before publication.)*

**What changed from `oreilly-submission-draft.md`:** this version is a structural strengthening pass, not a correction pass. It adds one new section ("The model is not the unit of control") that states the central inversion thesis directly, generalizes the evidence/requirements/authority section and the evidence-gated pattern to apply beyond model promotion, expands the prior-art section from four analogies to six (adding databases/transactions and, honestly, ML model registries), and adds a new "One model, many decisions" section carrying the strongest new argument plus the agent example and the human-in-the-loop critique. The opening scenario, output/decision definitions, evidence/requirements/authority distinction, recording-vs-enforcing section, evidence-gated pattern, ALLOW/BLOCK/ESCALATE, prior-art honesty, implementation guidance, and closing question are all preserved, per instruction.

**Word count:** 2,197 prose words — title through "The question is whether the system has enough evidence to authorize what happens next," excluding "Further reading" and this Editorial notes section, and excluding the ASCII diagram and Python pseudocode blocks. Within the 1,900–2,200 target.

**Adversarial self-review:**

1. *What established ML assumption does this article actually challenge?* That the model — its version, its evaluation, its approval — is the correct object to attach production control to. The article argues the decision (the authorized state transition an output feeds into) is the right unit instead, and that this generalizes past deployment to any point where an output threatens to become an effect.
2. *Reducible to "use policy-as-code"?* No — policy-as-code is one possible implementation of the gate (acknowledged directly in the prior-art section), but the article's claim is about what gets governed (the decision, not the model), which is a positioning question policy-as-code tooling doesn't itself answer.
3. *Reducible to "use MLflow approval workflows"?* No, and this is now handled honestly rather than by omission: the prior-art section explicitly names MLflow and Databricks Unity Catalog as already providing staged model promotion. The article's distinct claim is that a decision boundary is not tied to a model's registry entry — the same pattern has to gate a runtime recommendation or an agent's tool call, where no model registry is involved at all.
4. *Is the model-lifecycle vs. decision-lifecycle distinction explicit?* Yes — it is the subject of an entire section ("The model is not the unit of control"), stated as two different questions with two different architectures, and it is explicitly said not to replace but to "cut across" the model lifecycle.
5. *Does the same-model/different-decisions example prove why decision-level control matters?* Yes — "One model, many decisions" shows a single LLM used for summarization, transaction denial, external email, and a database mutation, and argues a model-level approval has no way to express the different evidence/authority/consequences each decision needs.
6. *Does the agent example generalize the abstraction beyond deployment?* Yes — the refund example (`"Refund the customer."` → `issue_refund(customer_id, amount)`) explicitly relocates the same gate pattern to a runtime, non-deployment decision boundary, reinforcing the "cuts across the lifecycle" claim with a concrete case that has no model-registry equivalent.
7. *Are we still honest about prior art?* Yes, more so than the previous draft — six analogies now appear in-body (access control, databases/transactions, Kubernetes admission control, software supply-chain security, CI/CD, and model registries), with the model-registry acknowledgment specifically added per instruction, and the section still ends on an explicit non-invention statement.
8. *Have we accidentally claimed mechanism novelty?* No — every named mechanism (XACML-style authorization, transactional commit, admission control, attestation-checked admission, deployment protection rules, staged model promotion) is presented as pre-existing; the only claim of originality is about what object gets governed and where the boundary is placed, stated explicitly as "the mechanisms are old, the placement is the argument."
9. *Have Articles 2/3 remained untouched?* Yes — confirmed by direct text scan for state-is-not-knowledge, reconstructability, drift, preservation-over-time, Git/transaction-log-as-history, capability-vs-understanding, epistemological framing, understanding layer, and the fragmentation thesis; none appear. The database/transaction analogy is used only for the single-point-in-time compute-vs-commit distinction, not for transaction *logs* or history, per the explicit constraint.

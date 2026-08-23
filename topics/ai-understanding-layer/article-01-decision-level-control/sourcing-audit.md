---
id: note-article-01-decision-level-control-sourcing-audit
title: "Article 1 Claim-by-Claim Sourcing Audit"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [article-planning, sourcing-audit, decision-level-control]
refs: []
---

## Article 1 Claim-by-Claim Sourcing Audit

Every externally contestable claim in `draft-v2.md`, classified per the five required categories. No citations are inserted into `draft-v2.md` at this stage — this is a pre-sourcing audit only. Section references follow the article's own headings.

**Classification key:** conceptual argument (no citation required) · illustrative example (no citation required) · established technical fact (citation desirable) · external factual claim (citation required) · author-proposed terminology (identified as such, not cited).

---

### Opening ("The gap")

| Claim | Classification | Best source if cited |
|---|---|---|
| The model-promotion scenario (accuracy 0.913, dashboard, deploy button) | Illustrative example | None needed |
| "Training and evaluation typically get real architectural attention: pipelines, harnesses, versioned datasets, dashboards." | Established technical fact — citation desirable, not required | Sculley et al., "Hidden Technical Debt in Machine Learning Systems," NeurIPS 2015 — documents that ML pipeline/eval infrastructure is a well-recognized engineering investment area (papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems; research.google/pubs/hidden-technical-debt-in-machine-learning-systems/). Confirmed to exist via live search; not yet read in full — verify before inserting as a citation. |
| "The transition from an evaluation result to a production authorization can be as thin as a single conditional... with nothing else checking it." | Conceptual argument (possibility claim, not a prevalence claim) — no citation required | — |

### "Outputs are not decisions"

| Claim | Classification | Best source if cited |
|---|---|---|
| "An output is information produced by the system. A decision is an authorized state transition." | Conceptual argument (the article's own proposed distinction) | No citation required; this is the article's central claim, not an external fact |
| "**decision boundary**" / "**decision layer**" | Author-proposed terminology | Already correctly flagged in-article as "not an established industry term" |
| Architecture-flow preview sentence (output → proposed decision → evidence → requirements/authority → gate → transition) | Conceptual argument | No citation required |

### "What a production decision needs"

| Claim | Classification | Best source if cited |
|---|---|---|
| Evidence must exist, belong to the correct artifact/version, satisfy the requirement, and come from an authorized source | Conceptual argument, though it parallels a well-documented external structure | Citation *desirable* if this section is ever expanded: this four-property list closely parallels in-toto's attestation model (subject binding, typed predicate, signed source) — github.com/in-toto/attestation. Not required for the practitioner piece as written, since the article presents this as its own reasoning, not as a citation of in-toto. |
| "**Decision requirements**" / "**Authority**" definitions | Author-proposed terminology | No external citation required; these are the article's own vocabulary, though the underlying concepts parallel XACML's PDP/PAP separation (docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html) — see `novelty-audit.md` for the full comparison |
| "a low-risk internal tool and a customer-facing pricing model don't need the same bar" | Illustrative example | No citation required |

### "Recording is not enforcing"

| Claim | Classification | Best source if cited |
|---|---|---|
| "Documenting a requirement and enforcing it are not the same act, and treating them as equivalent is where control quietly disappears." | Conceptual argument | No citation required — this is the article's own reasoned claim, not a claim about how often it happens in the world (the v1→v2 revision specifically removed the earlier prevalence version of this claim) |
| Missing-evaluation scenario (model card template, governance wiki, compliance checklist) | Illustrative example | No citation required |
| "A fully documented system can still execute a decision that violates its own stated requirements, because documentation describes intended behavior and doesn't constrain actual behavior." | Conceptual argument | No citation required, though Model Cards / Datasheets for Datasets are real-world evidence that documentation-only responsible-AI practice is well established and does not itself enforce anything: Mitchell et al., "Model Cards for Model Reporting," FAT* 2019; Gebru et al., "Datasheets for Datasets," 2021. Citation desirable if this claim is ever challenged, not required as written. |

### "The evidence-gated pattern"

| Claim | Classification | Best source if cited |
|---|---|---|
| "**evidence-gated decision**" | Author-proposed terminology | Already correctly flagged in-article as "a proposed term rather than an established one" |
| The gate diagram and ALLOW/BLOCK/ESCALATE definitions | Conceptual argument / author-proposed pattern | No citation required for the piece as written; see `novelty-audit.md` Task D, Objection 6 — this outcome shape is standard in access control (XACML Permit/Deny/Indeterminate/NotApplicable) and should never be described as novel if the article is extended |
| Python pseudocode | Illustrative example | No citation required |
| "CI/CD is a natural fit for deployment-time decisions like this one: it already mediates the transition from candidate artifact to production state, the same way a pipeline runs tests before a merge." | Established technical fact — citation desirable | GitHub Actions deployment protection rules documentation: docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments; docs.github.com/actions/deployment/protecting-deployments/configuring-custom-deployment-protection-rules |
| "a decision made at runtime, by an agent or a live policy check rather than at deployment time, needs its enforcement point in the request path, not the pipeline" | Conceptual/architectural argument | No citation required for the claim as stated; if expanded, could reference AI-gateway pattern sources (mlflow.org/blog/gateway-guardrails/ — vendor-adjacent, treat as illustrative not authoritative) |
| "These ideas took shape partly while designing AIGov Core, where governance decisions were treated as engineering artifacts rather than reporting artifacts — evidence, authority, policy context, and the assumptions behind a decision, attached directly to it." | **External factual claim — citation required.** This is a factual claim about what AIGov Core's design does. | Source: `topics/ai-understanding-layer/sources/source-a-missing-layer.md`, §7 ("AIGov Core as an Architectural Experiment"). This is an **internal, private source** (the author's own prior draft) — there is no public specification or documentation to cite externally, and none should be fabricated. The claim is already faithful to that source per the prior revision task; no further external sourcing exists to attach. |

### "What this architecture buys you — and what it doesn't"

| Claim | Classification | Best source if cited |
|---|---|---|
| Benefits list (explicit boundary, inspectable evidence, deterministic enforcement, clear authority, reproducible outcomes) | Conceptual argument — these are claims about the proposed pattern itself, not about the external world | No citation required |
| "when the inputs and the rules are fixed, a gate outcome that's reproducible" | Established technical fact (determinism of pure functions) — citation not required, general CS knowledge | — |
| "This architecture governs authorization at decision time. It does not, by itself, solve every problem of explainability, auditability, safety, or compliance." | Conceptual argument / scope disclaimer | No citation required |
| "It doesn't guarantee regulatory compliance, general trustworthiness, or the absence of AI risk." | Conceptual argument / scope disclaimer | No citation required |

### "The question that matters" (closing)

| Claim | Classification | Best source if cited |
|---|---|---|
| "AI engineering has spent the last several years getting very good at producing better outputs" | Conceptual/framing claim, not a specific factual assertion | No citation required — deliberately general, not quantified |
| Closing thesis restatement | Conceptual argument | No citation required — this is the article's own conclusion, not an external claim |

---

### Summary

**Claims requiring citation before publication:** one — the AIGov Core paragraph, which is already satisfied by an internal source (`sources/source-a-missing-layer.md` §7); no external public citation exists or should be invented, since AIGov Core has no public specification.

**Claims where citation is desirable but not required:** the "training and evaluation get architectural attention" line (Sculley et al. 2015), the CI/CD-as-natural-enforcement-point line (GitHub Actions documentation), and the evidence-structure parallel to in-toto/XACML if the evidence/requirements/authority section is ever expanded for a more technical audience.

**No fabricated, invented, or unverified sources were used.** Every URL and paper referenced in this document and in `novelty-audit.md` was retrieved via live search on 2026-08-21 and corresponds to a real, checkable primary source (an official specification, official documentation, or a real peer-reviewed/preprint paper with a verifiable identifier). The Sculley et al. 2015 paper's existence was independently confirmed via search before being listed here; its full text has not been read in this session, so its exact wording should be checked before any direct quotation is added to the article.

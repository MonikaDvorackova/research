---
id: pub-jair-paper-v1
title: "A Knowledge Representation Framework for Historical AI Decision Reconstruction"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [jair, manuscript, knowledge-representation, decision-reconstruction, knowledge-continuity, AI-systems]
source_topics: [ai-infrastructure-gap]
target_venue: Journal of Artificial Intelligence Research (JAIR)
venue_format: journal
publish: false
checklist_version: "0.1.0"
version: v1-jair-submission-package
authors: ["Monika Dvořáčková"]
affiliations: ["*[affiliation to be filled]*"]
orcid: ["https://orcid.org/0009-0009-0879-1605"]
acknowledgements: "[Author confirmation required]"
note: >
  JAIR submission-ready prep: citations, tables, figures, KR related work,
  reference composition, KCM evaluation reframing. Evaluation markers unchanged.
---

## A Knowledge Representation Framework for Historical AI Decision Reconstruction

**Authors:** Monika Dvořáčková
**Affiliations:** *[affiliation to be filled — author confirmation required]*
**ORCID:** [0009-0009-0879-1605](https://orcid.org/0009-0009-0879-1605)
**Corresponding author:** Monika Dvořáčková (*[email to be filled — author confirmation required]*)

**Acknowledgements.** *[Author confirmation required]* No acknowledgements text is recorded in the repository.

**Funding.** No specific external funding is recorded for this work in the repository. *[Author confirmation required before submission.]*

**Competing interests.** The author declares that she has no competing interests of which the repository provides contrary evidence. *[Author confirmation required before submission.]*

**Author contributions.** Conceptualization, investigation, formal analysis, writing — Monika Dvořáčková.

**Data and artefact availability.** Evaluation artefacts (unit reviews, coverage audit, scenarios, composition analysis, checklist, Knowledge Continuity Model, and conformance specification) are maintained in the research repository associated with this manuscript (`topics/ai-infrastructure-gap/`). No separate experimental dataset was collected.

**Code availability.** No software implementation is claimed or evaluated in this manuscript. Mermaid/Graphviz figure sources are included with the submission package.

**Use of generative AI.** *[Author confirmation required]* Any use of AI tools in manuscript preparation must be disclosed by the author in accordance with JAIR policy; AI systems are not authors.

---

## Abstract

Contemporary AI systems preserve abundant **execution** artefacts—traces, logs, provenance graphs, model metadata, policy evaluations, and interaction records—yet often fail to preserve the **decision knowledge** required to reconstruct, as of decision time, why an AI-assisted outcome was justified, authorized, and valid. We present a refined formulation of this gap as a **knowledge-representation and AI-systems** problem: the historical decision reconstruction problem. In this specific representational and compositional form, the problem has been previously under-characterized. It is independent of law, regulation, and compliance regimes; those domains merely expose a deficiency that arises whenever AI systems commit to outcomes whose interpretive basis must remain recoverable after models, criteria, evidence stores, and agents change.

We characterize historical decision knowledge by distinguishing execution artefacts from decision knowledge and by formalizing faithful reconstruction over a base triad of justification, authorization, and temporal validity, together with reliance distinctions and durable semantic bindings. We derive technology-neutral reconstruction requirements (a Reconstruction Checklist) that specify the representational completeness needed for reconstructability. Applying the checklist across thirteen representative AI-systems infrastructure sources, and evaluating reconstructability through adversarial scenarios and composition analysis, we find that existing families are often capable for their native purposes but do not jointly preserve sufficient decision knowledge without durable bindings to a shared decision identity and to decision-time versions of criteria, evidence, models, and human acts.

From that analysis we derive an engineering response—the Knowledge Continuity Model—centred on the **Decision Episode** as a representational abstraction for historically meaningful AI decisions, together with a Conformance Specification for evaluating reconstruction capability. Under stated retention and population assumptions an internal coverage analysis finds that the derived response instantiates the stated requirements for base-triad reconstructability; this is not independent empirical confirmation. Adoption limits, evidence deletion, and several conditional categories remain. Contributions are ordered as: refined problem formulation; representational requirements; unit and compositional evaluation of contemporary AI infrastructure; identification of residual semantic-binding and shared-identity gaps; the derived KCM and conformance response; and a reference implementation (AIGov) that instantiates selected representational objects to demonstrate implementation feasibility—not independent validation of the theory. Provenance, observability, policy, and explanation components remain complementary substrates rather than complete substitutes for Decision Episode representation.

**Keywords:** historical decision reconstruction · knowledge representation · decision knowledge · temporal knowledge · semantic bindings · AI systems · autonomous agents · Decision Episode · reconstructability · compositional evaluation

---

## 1 Introduction

### 1.1 The AI problem: historical reconstruction of decision knowledge

AI systems increasingly participate in decisions whose meaning depends on more than a final output label. An AI-assisted decision is typically the result of interacting components: model inference, input evidence, thresholds or rules, optional human acceptance or override, and the criteria treated as applicable at the moment of commitment. Months later—during debugging of decision quality, analysis of model drift, multi-agent handoff review, long-lived assistant audit trails, or operational incident analysis—a fundamental AI-systems question arises:

> Can we reconstruct, from retained structure alone, *what decision knowledge held at decision time*—not what the live system would compute now?

In practice, AI deployments retain abundant **execution artefacts**: traces of how computation proceeded, logs that events occurred, provenance of how artefacts were derived, lineage of datasets and pipelines, and documentation of released models. These artefacts answer important questions about execution and derivation. They do not, by themselves, answer whether the system preserved a coherent **representation of the decision**: its identity, outcome, temporal anchor, governing criteria versions, relied-upon evidence, model participation, human interventions, and authority under which the outcome was committed.

The result is a characteristic failure mode of contemporary AI stacks. Policies, prompts, models, and features drift; live stores overwrite decision-time inputs; human overrides may leave only a final business state; explanations may be regenerated after the fact from a different model version. A reconstructor who consults “what the system says now” risks substituting present computational narrative for historical decision knowledge. This is a problem of **representation, semantic binding, and temporal persistence**—core concerns of knowledge representation, AI systems, autonomous agents, multi-agent systems, decision support, reasoning over historical state, explainability infrastructure, and long-lived AI systems—before it is a problem of any particular application domain.

### 1.2 Why execution artefacts are not enough

We distinguish *execution artefacts* from *decision knowledge*. Execution artefacts record paths, events, and derivations. Decision knowledge, for reconstructability, must represent at least: the decision as an identifiable episode; the outcome; the time and versioned context; the justification structure (evidence available versus relied upon, and participating AI outputs); the authorization structure (actors and authority relative to applicable criteria); and the validity structure (constraints and rules treated as in force, without silent latest-only substitution).

Adjacent AI capabilities are routinely mistaken for this representational target. Replay restores computational paths without necessarily restoring normative decision structure. Provenance can encode portions of historical decision knowledge and is a relevant representational substrate, yet provenance alone does not guarantee reconstruction of justification, authorization, temporal validity, actual reliance, or cross-component semantic bindings. Explainability often yields contemporaneous or regenerable accounts. Model reproducibility recreates outputs without reconstructing the criteria and authority under which an output became a committed decision. The research gap we pursue is therefore not the claim that logging, provenance, or explanation mechanisms are absent or that prior work ignored decisions. It is that heterogeneous AI-system components still lack a durable, compositional **representation of decision episodes** that binds those components into historically interpretable decision knowledge—an aspect previously under-characterized in this specific representational and compositional form.

### 1.3 Problem statement: historical decision reconstruction

We refine and formalize the **historical decision reconstruction problem** for Artificial Intelligence systems:

> Given only retained structured information and a stated reconstruction procedure, recover—deterministically and as of decision time—the decision knowledge that identifies an AI-assisted decision episode and restates its justification, authorization, and temporal validity, without substituting current execution state for historical decision state.

The problem is a **knowledge-representation and AI-systems** problem. It exists whenever AI components participate in committed outcomes whose basis must remain interpretable after drift, update, or redistribution of system state. It does **not** depend on law, regulation, governance, or compliance. Those regimes are application settings in which the same representational deficiency becomes externally visible; they do not define the problem.

### 1.4 Related diagnostic work and differentiation from DEMM

Prior work already addresses provenance of automated decisions, accountable decision pipelines, structured records of entities, activities, agents, and derivations, and explanations generated from retained provenance [@singh2019decisionProvenance; @huynh2021provenanceExplanations; @moreau2013provDm]. Governance-oriented evidence assessment likewise shares a diagnostic concern with our evaluation. The Decision Evidence Maturity Model (DEMM) [@solozobov2026demm] operationalises governance-evidence sufficiency through property-level reconstructability assessment. DEMM evaluates evidence produced by existing upstream systems and identifies the *container fallacy*: the presence of evidence containers does not establish reconstructability. We share that diagnostic concern. Our primary research question differs: we characterize the **representational capability** that AI systems must preserve for faithful historical reconstruction. Our scientific object is historical decision knowledge represented through **Decision Episodes**; we derive decision-time preservation and binding requirements; we treat justification, authorization, and temporal validity as distinct reconstruction targets; we distinguish relied-upon evidence from merely available evidence; and we evaluate compositional sufficiency across heterogeneous infrastructure families. DEMM and this manuscript are related; neither subsumes the other. Section 2 expands this comparison.

### 1.5 Motivating application domains

The problem appears in long-lived decision-support systems; AI assistants that accumulate commitments; orchestrated multi-step AI workflows; autonomous systems whose acts must remain interpretable after model or criteria updates; and multi-agent systems in which evidence and authority cross agent boundaries. External scrutiny in regulated deployments—including record-keeping practices discussed under instruments such as the EU AI Act [@eu2024aiAct]—stress-tests the same deficiency. These domains motivate and illustrate; they are not the scientific object of the paper. The manuscript remains coherent if legal references are set aside.

### 1.6 Research question and contributions

This paper asks:

> Can existing AI systems infrastructure for provenance, observability, metadata, policy, documentation, explanation, and human–AI interaction—alone or in composition—support deterministic faithful reconstruction of justification, authorization, and temporal validity for historically situated AI-assisted decisions; and if not, how should the missing representational capability be characterized and what minimum structures and semantic bindings does that characterization imply?

We structure the answer so that engineering artefacts remain consequences of problem characterization:

1. **Refine** the historical decision reconstruction problem as a knowledge-representation and AI-systems formulation, with an explicit distinction between execution artefacts and decision knowledge.
2. **Characterize** representational requirements for historical decision knowledge (justification, authorization, temporal validity, reliance, and semantic bindings).
3. **Evaluate** contemporary AI infrastructure families at unit level against those requirements.
4. **Evaluate** compositional sufficiency across heterogeneous families (scenarios and composition analysis).
5. **Identify** the residual gap: missing durable semantic bindings and shared decision identity.
6. **Derive** an engineering response—the Knowledge Continuity Model (KCM) and a Conformance Specification—as consequences of that analysis; then evaluate the derived response on the same bar (internal coverage).
7. **Instantiate** selected representational objects in a reference implementation (AIGov) as a feasibility demonstration—not as independent validation of KCM or the checklist.

**Principal scientific contribution.** A refined formulation and systematic characterization of the historical decision reconstruction problem—previously under-characterized in this specific representational and compositional form—including representational requirements and compositional evaluation of reconstructability.

**Derived engineering contribution.** The Decision Episode abstraction, KCM objects and semantic bindings, and conformance classes—as *one* solution implied by the characterization, not as the paper’s primary claim.

**What this paper is not.** It is not a new logging system, not a provenance serialization format, not a workflow engine, and not an explainability method. Nor is its principal contribution an architecture proposal for its own sake. Those mechanisms remain components; the characterized problem is whether AI systems represent historically reconstructable decisions with the bindings needed for compositional sufficiency.

We do not claim that reconstruction is metaphysically impossible everywhere, nor that only a branded product can succeed. We claim, on the basis of the completed evaluation, that the reviewed composition of AI-systems standards and frameworks does not guarantee deterministic faithful reconstruction without durable episode-centric representational bindings, and that the derived KCM information requirements appear sufficient for the base triad when those bindings are populated under stated assumptions.

Figure 1 summarizes the scientific narrative: execution preservation is widespread; decision-knowledge preservation remains under-characterized compositionally; requirements formalize the gap; evaluation diagnoses composition failure; KCM is derived as an engineering response and checked for internal requirement coverage on the same bar.

![Figure 1. Scientific argument from execution artefacts to derived KCM.](../figures/fig1-scientific-argument.pdf)

**Figure 1.** Scientific argument: execution artefacts reveal missing decision knowledge; reconstruction requirements drive unit and compositional evaluation; the Knowledge Continuity Model is a *derived* response, not the starting contribution. (Source: `figures/fig1-scientific-argument.pdf`.)

The remainder of the paper follows that narrative. Section 2 synthesizes related infrastructure, adjacent KR traditions, and differentiates DEMM and decision-provenance work. Section 3 formalizes reconstruction requirements. Section 4 describes evaluation methodology. Section 5 reports results on existing approaches and a reference composition, then a reference implementation feasibility demonstration. Section 6 derives the Knowledge Continuity Model. Section 7 summarizes the derived Conformance Specification. Section 8 evaluates the derived solution. Sections 9–11 discuss implications, threats, and conclusions.

---

## 2 Related Work

We organize related work by capability families evaluated in our unit reviews, then differentiate the strongest related diagnostic framing (DEMM) and clarify decision-provenance positioning. Each family contributes real AI-systems infrastructure. None—individually or by unspecified composition—defines a complete, durable **decision-episode representation** for base-triad reconstruction as characterized here. Table 1 summarizes the families; detailed checklist scores live in the unit reviews and are not repeated here.

**Table 1.** Evaluated infrastructure families (unit corpus). Native strengths and alone-limitations follow unit reviews and coverage audit.

| Family | Representative sources | Native strength | Reconstruction contribution | Principal limitation alone |
|---|---|---|---|---|
| Provenance | W3C PROV-DM | Entities, activities, agents, derivation | Derivation and responsibility graphs | Not a shared Decision ID / reliance / policy-version episode model |
| Observability | OpenTelemetry | Traces, metrics, logs | Execution-path reconstructability | Paths ≠ normative decision structure; no standard Decision Episode semantic |
| ML metadata | Google ML Metadata | Artefacts, executions, contexts | Model/run heritage | Pipeline-centric; unbound to business Decision ID |
| Data lineage | OpenLineage | Job/dataset lineage | Feature/training heritage | Unbound to decision identity and reliance subset |
| Policy / authz | OPA; Cedar | Allow/deny eval; optional decision logs | Authorization *islands* (esp. OPA bundle revision) | Cross-component episode binding absent; Cedar durability not mandated |
| Documentation | Model Cards; Datasheets; System Cards | Release-time transparency | Version/background knowledge | Cards describe releases, not sealed episode associations |
| Risk guidance | NIST AI RMF 1.0 | Organizational oversight processes | Process context | Process docs ≠ decision-time reconstruction schema |
| Explainability | NISTIR 8312 | Explanation quality principles | Clarifies explanation goals | Quality ≠ retained decision-bound justification package |
| Regulated logging | EU AI Act logging duties (motivating) | Retention-backed operational events | Monitoring stress-test | Not a cross-component Decision Episode contract |
| Human–AI workflow | OASIS WS-HumanTask | Task lifecycle, roles, history API | Human-gate acts | No mandated retention/rationale or shared Decision ID |

### 2.1 Provenance and decision provenance

W3C PROV-DM provides a normative vocabulary for entities, activities, agents, usage, generation, and derivation [@moreau2013provDm]. It systematically supports responsibility relations and time-stamped process graphs. Prior work already addresses provenance of automated decisions, accountable decision pipelines, structured records of entities, activities, agents, and derivations, and explanations generated from retained provenance—including decision-provenance and provenance-backed explanation lines of research [@singh2019decisionProvenance; @huynh2021provenanceExplanations]. Provenance is therefore a **relevant representational substrate** and can encode portions of historical decision knowledge. We do not claim that provenance research ignored decisions.

Our narrower distinction is compositional and reconstructive. Provenance alone does not guarantee reconstruction of justification (including relied-upon versus merely available evidence), authorization under then-applicable criteria, temporal validity without latest-only substitution, actual reliance, or durable cross-component semantic bindings to a shared decision identity. For reconstructability of AI-assisted decisions as formalized in Section 3, provenance answers “from what / by whom derived” more directly than “under which criteria and authority was this outcome valid as a committed decision.” Policy identity and version, reliance distinctions, and first-class decision-episode identity spanning heterogeneous stores are not native guarantees of PROV or of provenance-backed explanations. PROV strengthens lineage when composed with other stores, but does not by itself constitute a complete decision-knowledge representation for the base triad. This manuscript evaluates whether heterogeneous capabilities compose into faithful historical reconstruction—not whether provenance mechanisms exist.

### 2.2 Observability

OpenTelemetry specifies traces, metrics, and logs for distributed execution [@openTelemetry2026specification]. Observability is essential for understanding *how* AI-serving computation proceeded. It does not encode governing criteria versions, authority, or reliance distinctions as decision structure. Attribute bags can *carry* a decision identifier if applications invent one; the specification does not define a Decision Episode representation. Runtime correlation is therefore easy to confuse with historical reconstruction of decision knowledge.

### 2.3 ML metadata and data lineage

ML Metadata and OpenLineage record artefacts, executions, jobs, and dataset lineage [@google2026mlMetadata; @openLineage2026specification]. They are strong for pipeline and training heritage—important background for interpreting model behaviour. They are typically not centred on a decision identity, nor on the subset of evidence *relied upon* for a particular committed outcome. Lineage of a training run is not automatically an evidence snapshot of an inference that later entered a human-gated or policy-gated decision.

### 2.4 Policy, rules, and authorization components

Open Policy Agent decision logs can retain allow/deny results with bundle revision identifiers [@openPolicyAgent2026]. Cedar provides a principled authorization language and diagnostics [@cedarPolicyLanguage2026]. These systems can support authorization *islands* when logging and retention are enabled, and they contribute rule-evaluation structure relevant to validity and authorization representations. They do not, by themselves, bind policy evaluation to AI inference outputs, relied-upon evidence, human override rationales, or later contestation under a shared episode key. Cedar’s language also does not mandate durable decision logging. Policy engines are necessary components of many AI decision architectures; they are not a complete decision-knowledge composition.

### 2.5 Model and dataset documentation

Model Cards, Datasheets for Datasets, and System Cards improve release-time transparency of AI artefacts [@mitchell2019modelCards; @gebru2021datasheets; @procope2022systemCards]. Documentation of model version, intended use, and dataset lifecycle is valuable background knowledge. It is not a substitute for episode representations: cards describe releases, not the sealed association of a specific model version, input snapshot, and human or policy act to one historical decision. Current documentation easily substitutes for historical documentation at query time—an instance of latest-only temporal failure.

### 2.6 Organizational guidance and explainability

NIST AI RMF 1.0 frames organizational risk management and oversight processes [@nist2023aiRmf]. NISTIR 8312 articulates principles for explainable AI [@nist2021ir8312]. Both strengthen practice and explanation *quality*. Neither defines a durable, decision-bound representation that retains authorization, justification structure, and validity constraints as of decision time. Explanation quality properties must not be conflated with retained historical justification knowledge.

### 2.7 Human–AI interaction records and regulated logging

OASIS WS-HumanTask defines a rich human-task lifecycle with roles, completion semantics, and history APIs [@oasis2010wsHumanTask]—relevant wherever humans remain in the loop of AI-assisted decisions. HumanTask can record who completed a task and optional comments, but it does not mandate reconstruction-grade retention, required override rationales, or a shared Decision ID across model and policy stores. Regulated logging practices, including duties discussed in the EU AI Act [@eu2024aiAct], illustrate externally imposed retention of operational events. Such logging supports monitoring of system functioning; it does not, in general, prescribe a cross-component decision representation spanning inference, criteria versions, reliance, and later correction. Data-minimization constraints may further delete inputs needed for justification reconstruction—an application pressure on any temporal decision representation, not a definition of the representation problem itself.

### 2.8 Temporal, event, and case-oriented knowledge representation

Classical KR traditions already represent change, episodes, and reusable decision records. Interval-based temporal logics support qualitative relations among time intervals [@allen1983temporalIntervals]. The situation calculus provides a formal account of actions and changing world state [@mccarthy1969situationCalculus]. The event calculus treats events as primitives for updating historical narratives and reasoning about periods for which fluents hold [@kowalski1986eventCalculus]. Case-based reasoning stores and reuses decision or problem-solving cases [@aamodt1994caseBasedReasoning]. These traditions represent historical state, event structure, and case identity *well* within a coherent knowledge base, and they are directly relevant to Decision Episodes as temporally indexed, identity-bearing units of decision knowledge.

They do not, by themselves, establish the cross-component preservation requirements this paper evaluates for contemporary AI infrastructure. A situation- or event-calculus theory, an interval ontology, or a case base can encode justification-like and temporal content when an authoring system writes that content into one store. They do not automatically supply durable shared Decision IDs across heterogeneous runtime components; sealed decision-time policy and model versions spanning policy engines, model registries, and workflow systems; separation of actual reliance from merely available evidence under live feature stores; or authorization artefacts distinct from transient execution roles. We do not claim these traditions ignored historical decisions, nor that Decision Episode is an entirely new KR primitive. The contribution lies in the **specific representational and compositional requirements** imposed on contemporary AI infrastructure so that decision knowledge remains reconstructable when components are independently owned, versioned, and retained.

### 2.9 Decision Evidence Maturity Model (DEMM)

The Decision Evidence Maturity Model (DEMM) [@solozobov2026demm] is the strongest related diagnostic framing for reconstructability of decision-related evidence. DEMM operationalises governance-evidence sufficiency through property-level reconstructability assessment. It evaluates evidence produced by existing upstream systems and identifies the container fallacy: the presence of evidence containers does not establish reconstructability. We share that diagnostic concern and treat DEMM as complementary related work, not as irrelevant or superseded.

The primary research questions differ. DEMM asks how to score whether retained evidence suffices for stated governance properties. This manuscript asks what representational capability AI systems must preserve so that historical decision knowledge remains faithfully reconstructable. Our scientific object is historical decision knowledge represented through Decision Episodes; we derive decision-time preservation and binding requirements; we treat justification, authorization, and temporal validity as distinct reconstruction targets; we distinguish relied-upon evidence from merely available evidence; and we evaluate compositional sufficiency across heterogeneous infrastructure families (unit reviews plus composition and scenarios). Overlap exists in the shared observation that containers and logs are insufficient without reconstructable content and relationships. Neither approach subsumes the other: DEMM does not replace a Decision Episode representation or our compositional binding analysis, and our formulation does not replace DEMM’s property-level maturity scoring of upstream evidence.

### 2.10 Why no complete decision-knowledge composition emerges

Across the infrastructure families in §§2.1–2.7 and relative to the KR traditions in §2.8, local identities and version pins exist inside islands (for example, a policy decision identifier within policy logs, or a task identifier within a workflow engine). What is missing as a shared durable contract is a **compositional representation** that makes one historically situated AI-assisted decision reconstructable: a stable decision identity spanning inference, criteria evaluation, evidence snapshot, human review or override, and later correction; decision-time seals for criteria, model, and evidence versions; separation of relied-upon from merely available evidence; authority distinct from transient role labels; and aligned persistence of semantic relationships.

Two further observations follow from the unit corpus. First, optional features systematically inflate *capability ceilings* without creating reconstruction *guarantees*: optional comments, external log sinks, and open telemetry attributes may carry correlation keys—yet none is mandated as a Decision Episode representation. Second, process guidance and external duties often specify intended behaviours without specifying the durable technical representation needed to preserve decision knowledge over time. Related work therefore supplies components of a future composition. It does not, on the evidence of our evaluation, already specify that composition. DEMM’s container-fallacy diagnosis aligns with this residual; our contribution is the systematic characterization of representational and compositional reconstructability requirements for Decision Episodes, not a competing maturity scorecard.

---

## 3 Reconstruction Requirements as Representational Completeness

Having identified the historical decision reconstruction problem, we next **characterize** what representational completeness would have to provide. The requirements below are derived as a formalization of the problem—not as features of a particular product architecture.

### 3.1 Faithful reconstruction

We adopt an engineering definition of **faithful reconstruction**. A competent reconstructor, given only retained structured information and a publicly stated reconstruction procedure for the system under test, must be able to: identify the decision episode unambiguously; state the outcome; locate the episode in time and applicable versioned contexts; restate **authorization** (who or what was authorized to decide, under which governing criteria version, with what permit/deny or equivalent result); restate **justification** (which evidence and criteria were treated as supporting the outcome, including what was relied upon versus merely available); restate **validity** (which constraints and rules were treated as in force, and whether the outcome was represented as conforming); and distinguish contemporaneous system narrative from decision-time structure—avoiding silent substitution of current policies, models, or explanations for historical ones.

Faithfulness in this sense does **not** require bit-exact replay of all internal compute, full weight reproducibility, or recovery of every discarded intermediate token. It requires recovery of the normative and evidential *basis* of the decision as retained representational structure—i.e., persistent decision knowledge.

### 3.2 What reconstruction is not

Several adjacent AI capabilities are routinely mistaken for reconstruction. **Replay** may restore computational paths without restoring authorization or justification structure. **Audit logging** records that events occurred without necessarily retaining governing criteria versions or relied-upon evidence. **Provenance and lineage** explain derivation more readily than validity under then-applicable rules. **Explainability** often produces contemporaneous or regenerable accounts unbound to authorization and validity. **Reasoning traces** may reconstruct tool or token paths without criteria or authority binding. **Model reproducibility** recreates outputs without reconstructing permission or conformity. Passing the native success criteria of any of these capabilities does not, by itself, establish faithful reconstruction of decision knowledge.

### 3.3 The Reconstruction Checklist and base triad

The Reconstruction Checklist (v0.1.0) defines technology-neutral information categories (IC-01–IC-24), requirement classes (Required, Conditionally required, Optional), and binding criteria. Categories cover identity and outcome; actors and authority; policy and rules; evidence and reliance; model and tool context; assumptions and temporal or jurisdictional context; and integrity or derivation metadata. Critically, required and conditionally required items must be recoverable **as bound to the same decision identity** and, where versioning is in scope, to decision-time version axes. Unbound “latest criteria” stores do not satisfy versioned items. Table 2 summarizes the checklist structure and triad roll-up.

**Table 2.** Reconstruction requirements (checklist v0.1.0, selected). Binding criteria apply to all Required/Conditionally required items: same Decision ID and decision-time version axes where versioning is in scope.

| ID | Requirement | Reconstruction target | Failure consequence | Focus |
|---|---|---|---|---|
| IC-01 | Decision identity | Episode identification | Ambiguous correlation; non-determinism | Identity / binding |
| IC-02 | Decision outcome | What was decided | Incomplete reconstruction | Identity |
| IC-03 | Decision time | As-of temporal anchor | Latest-only substitution risk | Temporal validity |
| IC-04 | Actor(s) | Who participated | Attribution gap | Authorization |
| IC-05 | Authority | Mandate under which actor decided | Role≠authority confusion | Authorization |
| IC-06 | Governing policy | Criteria identity | Authorization/validity fail | Authorization / temporal validity |
| IC-07 | Policy version | Decision-time criteria | Current-policy substitution | Temporal validity / binding |
| IC-08 | Applicable rules / path | Fine-grained authorization/validity | Opaque allow/deny | Authorization / temporal validity |
| IC-09 | Constraints | Conformity constraints | Validity incomplete | Temporal validity |
| IC-10 | Evidence available | Evidential field | Justification incomplete | Justification |
| IC-11 | Evidence relied upon | Actual reliance | Available≠relied-upon fallacy | Justification / reliance |
| IC-13 | Model version | Participating model artefact | Drift falsifies historical account | Justification / binding |
| Binding | Same-identity + decision-time | Compositional sufficiency | Islands without episode | Binding |

Interpreted as knowledge representation requirements, the checklist asks whether an AI system (or composition) preserves:

- a **representation of the decision** (identity, outcome, time);
- a **representation of justification** (evidence field and reliance distinction; participating inference);
- a **representation of authority** (actors and mandates distinct from transient execution roles);
- a **representation of historical context** (versioned criteria, models, and as-of evidence);
- a **representation of temporal validity** (intervals and decision-time applicability without latest-only substitution).

Together these elements constitute a **representation problem**: the system must encode decision knowledge as structured, bindable, temporally indexed state. They are not reducible to an auditing problem, which may succeed by retaining high-volume events without encoding those semantic relationships.

The **base triad** treats justification, authorization, and temporal validity as separable reconstruction targets. An abstraction may satisfy one without satisfying the others. Base faithful reconstruction requires all three triad rows to pass under the declared completeness profile. This separation matters for AI systems: a policy allow/deny log may partially support authorization while leaving justification (reliance) and historical validity (then-applicable rules and evidence) unresolved.

### 3.4 Why observability is insufficient

Runtime observability answers how a request traversed AI-serving infrastructure. Deterministic historical reconstruction additionally requires sealed references to the criteria and evidence that *normatively* grounded the committed outcome. Traces degrade into non-determinism for reconstruction when identities are ambiguous, when retention is uneven across stores, or when the reconstructor must guess which current model or criteria apply. The checklist therefore judges **representational completeness**, not the presence of a telemetry product.

---

## 4 Evaluation Methodology

Our methodology is analytical rather than implementation-based. It tests whether candidate infrastructures preserve the decision knowledge required for reconstruction along five evaluation claims: representational completeness; historical reconstructability; semantic-relationship preservation; decision-time validity; and compositional sufficiency. Criteria are derived from the problem characterization in Section 3. Conclusions are conditional on the evaluated standards, versions, and stated assumptions. Figure 1 situates the steps; this section states them operationally.

### 4.1 Unit reviews

For each system under test (SUT)—one publication, framework, standard, or engineering approach—we: read the primary source; identify information the source preserves or defines as retainable; map that information to checklist categories; assign marks; and record strengths, limitations, and missing reconstruction capabilities. High-level capability rows use a 0–3 scale (not addressed; mentioned or partially supported; substantially supported; explicitly and systematically supported). Checklist categories use `PASS`, `PARTIAL`, `FAIL`, or `N/A`, with PARTIAL requiring a stated missing element. Evidence must come from the source; implementation generosity beyond what the source mandates is not credited. Thirteen unit reviews were completed, covering the families summarized in Section 2 and Table 1.

In representational terms, unit reviews evaluate whether each source **defines structures capable of encoding** the required decision-knowledge categories.

### 4.2 Coverage audit

After unit reviews, a coverage audit assessed whether further unit-source expansion was needed before composition. The audit concluded that minimum family coverage for synthesis was satisfied across provenance, observability, lineage/ML metadata, policy/authorization, documentation, risk-management guidance, explainability, regulated logging practices, and human–AI workflow records, and that remaining residuals were compositional rather than missing peer families. Unit-source expansion was therefore stopped in favour of scenarios and composition analysis.

### 4.3 Scenario analysis

Six adversarial scenarios test **reconstructability** of decision knowledge under realistic failure pressures:

1. **Model-assisted eligibility denial** — AI recommendation accepted by a human reviewer; later challenge.
2. **Criteria change after decision** — historical criteria bundle `P1` versus current `P2` at review time.
3. **Human override without preserved rationale** — final outcome retained; original recommendation and reasons missing.
4. **Model or dataset update** — challenge after retraining and reference-data refresh.
5. **Logging without shared identity** — rich per-system logs; only approximate timestamps and user identifiers for correlation.
6. **Challenge after partial evidence deletion** — contestation after minimization deletes raw input features (an application pressure also visible under data-protection and regulated-logging regimes [@eu2024aiAct]).

For each scenario we assess available unit capabilities, missing bindings, retention, identities, authority and version evidence, base-triad outcome, and whether reconstruction is deterministic, partial, or impossible under default composition. Scenarios evaluate whether retained structures still support reconstruction when AI-system state evolves.

### 4.4 Composition analysis

Composition analysis treats unit reviews as evidence of *component* capability. Joint sufficiency requires checklist binding criteria: same-identity binding and decision-time binding. Two components that each pass native criteria are not jointly sufficient unless their outputs are stably and durably bound to the same decision episode. The analysis enumerates minimum episode components, required cross-component bindings, temporal composition failures, and base-triad roll-up for the composed ecosystem.

In representational terms, composition analysis evaluates **preservation of semantic relationships** among decision-knowledge elements across heterogeneous AI components—not merely co-presence of logs.

### 4.5 Consistent scoring of the proposal

The Knowledge Continuity Model is later evaluated with the **same** checklist, marks, scenarios, and triad rules (Section 8). No new scoring rules are introduced. KCM is scored as model expressiveness and normative information requirements—analogous to scoring PROV-DM on what the model can express if followed—not as a field deployment census. This validates the proposed representation framework against the same completeness bar used for existing infrastructure.

---

## 5 Evaluation Results

### 5.1 Coverage findings

The reviewed corpus provides substantial native capabilities: derivation (PROV, ML Metadata, OpenLineage); execution observability (OpenTelemetry); authorization evaluation and logging (OPA, Cedar); release documentation (Model Cards, Datasheets, System Cards); organizational risk guidance (AI RMF); explanation quality principles (NISTIR 8312); retention-backed operational logging practices (including those discussed for regulated AI systems); and human-task lifecycle records (WS-HumanTask). Coverage is therefore not “empty.” The residual problem for reconstruction is not the absence of these families but the absence of a durable cross-component **decision-knowledge representation** that preserves one decision episode across them.

### 5.2 Scenario findings

Under default composition—components present without a jointly defined binding contract—the scenarios largely fail deterministic reconstruction. Scenario 1 fails the base triad without a shared Decision ID across inference, criteria evaluation, human task, notice, and later challenge records. Scenario 2 may leave a partial authorization island inside retained OPA decision logs, but full-episode justification and validity still fail when evidence and human acts are unbound and current criteria stores are consulted. Scenario 3 fails under outcome-only retention. Scenario 4 fails historical justification when inference inputs and model hashes are not snapshotted to a decision identity; bit-exact reproduction is not required for faithfulness, but unbound drift still falsifies historical accounts. Scenario 5 fails by identity fragmentation: ambiguous correlation is an explicit faithfulness failure mode. Scenario 6 fails justification and validity when relied-upon evidence is deleted, even if aggregated logs and a task completion record remain; authorization may survive only as a narrow unbound island. Table 3 summarizes ecosystem versus later KCM outcomes.

**Table 3.** Scenario results. Ecosystem marks are for default composition without a jointly defined binding contract. KCM marks assume conformant population of mandatory objects and bindings (internal coverage), not field deployment.

| Scenario | Principal failure mode (ecosystem) | Ecosystem | KCM (under assumptions) | Key assumption | Residual limitation |
|---|---|---|---|---|---|
| 1 Eligibility denial | No shared Decision ID across inference, policy, human task, notice | FAIL (impossible) | Complete PASS | Decision ID propagated; snapshot before mutation | Fairness of denial out of scope |
| 2 Criteria change | Latest policy store consulted; unbound evidence/human acts | FAIL triad (PARTIAL OPA island) | Complete PASS | Historical Policy Version resolvable | Non-registration → non-conformant FAIL |
| 3 Override sans rationale | Outcome-only retention | FAIL | Complete if gated; else Failed | Commitment gate requires rationale | Rationale *quality* out of scope |
| 4 Model/dataset update | Unbound drift of model/inputs | FAIL | Complete for basis (not bit-replay) | Version artefacts resolvable | Faithfulness ≠ compute-identical replay |
| 5 No shared identity | Timestamp/user correlation only | FAIL | Complete if ID attached | Instrumentation attaches Decision ID | Legacy stitching may remain PARTIAL |
| 6 Evidence deletion | Relied-upon inputs destroyed | FAIL (narrow authz island possible) | Complete / Partial / Failed by retention | Declared retention vs deletion law | Model does not override deletion constraints |

### 5.3 Composition findings

Figure 2 depicts fragmented AI-systems infrastructure: strong capability islands without a shared episode key, contrasted with a bound Decision Episode.

![Figure 2. Fragmented islands versus bound Decision Episode.](../figures/fig2-fragmented-islands.pdf)

**Figure 2.** Left/default: provenance, observability, lineage, policy, documentation, and human-workflow islands without a shared Decision ID yield ambiguous correlation and reconstruction FAIL. Right: the same families contribute objects under a shared Decision ID with decision-time seals. (Source: `figures/fig2-fragmented-islands.pdf`.)

Composition analysis identifies the principal limitation as **missing durable cross-component composition of decision knowledge**, not missing individual logging, provenance, explainability, or human–AI workflow support. Critical missing bindings include:

1. decision ID ↔ model inference event (model version, inputs, outputs);
2. decision ID ↔ criteria/policy evaluation (identity + version/bundle revision + result/path);
3. decision ID ↔ human task (actor, action, timestamps, override semantics);
4. human task ↔ actor authority (mandate distinct from task role);
5. decision ID ↔ evidence snapshot (relied-upon subset, not live store);
6. decision ID ↔ notification and challenge/appeal records where applicable;
7. decision ID ↔ later correction/remediation;
8. model version ↔ dataset and feature pipeline versions;
9. criteria version ↔ effective-date interval and decision timestamp.

None of these bindings is jointly defined as a normative, durable cross-standard contract by the unit sources reviewed. Table 4 contrasts required composition with ecosystem provision.

**Table 4.** Required semantic bindings (from composition analysis). Absence yields non-deterministic or impossible faithful reconstruction under default composition.

| Source object | Target object | Required relationship | Temporal / identity constraint | If absent |
|---|---|---|---|---|
| Decision ID | Model inference event | Episode membership | Same ID; model version sealed | Justification FAIL |
| Decision ID | Criteria/policy evaluation | Governing criteria link | Bundle/version at decision time | Authorization/Validity FAIL |
| Decision ID | Human task / review | Human-gate link | Actor + timestamps | Authorization/Justification FAIL |
| Human task | Actor authority | Mandate ≠ task role | Authority validity covers act time | Authorization FAIL |
| Decision ID | Evidence snapshot | As-of inputs | Relied-upon ⊂ available; capture time | Justification FAIL |
| Decision ID | Notification / appeal | Contestability link | Same ID across systems | Contestation path unbound |
| Decision ID | Correction / remediation | Append-only history | No rewrite of sealed commitment | Historical integrity FAIL |
| Model version | Dataset / feature pipeline | Heritage link | Versions resolvable | Drift interpretation FAIL |
| Criteria version | Effective interval + decision time | Temporal coverage | Interval covers decision/effective time | Validity FAIL (latest-only) |

### 5.4 Base-triad findings (ecosystem)

For full-episode reconstruction under the scenario set:

- **Authorization:** FAIL compositionally; PARTIAL only for narrow policy-log islands.
- **Justification:** FAIL (reliance accounting and decision-bound evidence/reasons absent or unbound).
- **Validity:** FAIL (historical criteria and evidence as-of binding absent).
- **Faithful reconstruction (base):** FAIL.

Architecturally, the failures cluster into identity fragmentation; version unbound from episode; authority and human-gate gaps; semantic thinness of purpose-based logs; explanations detached from decision-time packages; provenance without decision context; and challenge pathways that do not key technical episode artefacts. Temporal composition is especially fragile: criteria changes, model replacement, dataset and feature evolution, role changes, personnel turnover, deleted evidence, and regenerable explanations each incentivize latest-only substitution unless decision-time seals exist.

This is an architectural interpretation of the evaluation, not a claim that no organization can invent private integration schemas. Undocumented custom bindings fall outside what the reviewed sources guarantee and outside what the checklist permits as faithful reconstruction without a declared composition.

### 5.5 Reference composition (worked systems profile)

The compositional FAIL above diagnoses missing *bindings*, not missing *components*. To show that the residual is architecturally actionable, we state a **reference composition**—a feasibility-oriented systems profile for Scenario 1 (model-assisted eligibility denial). It is **not** a deployed implementation, **not** an empirical evaluation, and **not** evidence that real systems already satisfy the requirements. It answers whether one Decision Episode can be populated from existing families under explicit integration conventions.

**Narrative.** An eligibility recommendation is produced by a model runtime; a human reviewer accepts it in a workflow system; a policy engine evaluates governing criteria; months later a reconstructor asks for justification, authorization, and temporal validity.

| Component | Contributes object | Populates Decision Episode field | Required binding | If binding omitted | Native vs integration convention |
|---|---|---|---|---|---|
| Inference runtime | AI Inference + outputs | Inference; outcome contribution | Decision ID ↔ inference event | Justification FAIL | Native inference; **convention** for Decision ID attribute |
| Model registry / MLMD | Model Version (+ optional dataset/pipeline) | Model/dataset/pipeline versions | Inference ↔ Model Version; Decision ID ↔ versions | Drift falsifies historical justification | Native version ids; **convention** to attach Decision ID |
| Provenance / lineage (PROV or OpenLineage) | Derivation graph / job lineage | Provenance/lineage context | Decision ID ↔ PROV/lineage root | Derivation unbound to episode | Native graphs; **convention** for Decision ID as entity/attribute |
| Policy engine (OPA) | Evaluation result + bundle revision | Policy Version; evaluation | Decision ID ↔ policy decision / bundle revision | Authorization/Validity island only or FAIL | Native decision logs; **convention** to key by Decision ID |
| Identity / authority source | Human Actor; Authority intervals | Actors; Authority | Review ↔ Authority; Decision ID ↔ actors | Authorization FAIL (role≠mandate) | Org IAM native; **convention** to record authority object at act time |
| Evidence store + snapshotter | Evidence Snapshot | available / relied-upon refs | Decision ID ↔ snapshot; capture-before-mutation | Justification FAIL | Live store native; **snapshot+reliance** is integration |
| WS-HumanTask (or equivalent) | Human Review / Override | Review action; optional rationale | Decision ID ↔ task; task input ↔ inference hash | Human gate unbound | Native task IDs; **convention** for Decision ID + required rationale |
| Append-only / immutable episode store | Decision record; sealed bindings | Decision object; seal | All mandatory associations retained | Reconstruction non-deterministic | Not supplied as shared standard; **composition profile** store |
| Decision ID service | Immutable Decision ID | IC-01 join key | Propagated to all emitters at/before commitment | Scenario 5 FAIL | Application-level convention |
| Reconstruction query API | Published procedure | Triad statements + gaps | Read-only resolve by Decision ID | Heuristic correlation | Profile-defined; fail-closed |

**Decision ID propagation.** Mint Decision ID at commitment (or earlier at recommendation acceptance); write it into inference attributes, OPA decision log external key, HumanTask input, evidence snapshot metadata, and PROV entity attributes.

**Decision-time version bindings.** Seal OPA bundle revision, model hash/version, and evidence snapshot content hashes to the Decision record at commitment; forbid latest-only reads at reconstruction.

**Reconstruction query.** Given Decision ID, retrieve Decision, Evidence Snapshot, Policy Version+evaluation, Inference+Model Version, Human Review+Authority; evaluate triad; emit explicit gaps if any mandatory binding is missing.

This profile uses only families already reviewed. The residual gap is therefore **representational and contractual** (shared identity + seals + reliance), not the absence of logging, provenance, policy, or workflow products.

### 5.6 Reference implementation in AIGov

Section 5.5 argued that the residual gap is architecturally actionable under explicit integration conventions. We next report a **reference implementation**—AIGov—that *instantiates* selected representational objects from that profile in a real AI-governance infrastructure. AIGov is an audit-backed backend for AI deployments: typed evidence ingest, write-time policy enforcement, append-only hash-chained storage, deterministic compliance projections, and exportable audit artefacts, with an optional parallel AI decision flight recorder.

**Purpose (exclusive).** The implementation has one purpose only: to demonstrate that heterogeneous infrastructure *can preserve* representational objects of the kind required for historical decision reconstructability. It is **not** intended as independent validation of the Knowledge Continuity Model, **not** a proof of checklist completeness, and **not** empirical confirmation of superiority over alternative representations. It demonstrates **implementation feasibility**, not correctness of the theory. External validation remains future work.

#### 5.6.1 Architecture overview and concept mapping

AIGov does not use the product vocabulary “Decision Episode” or “KCM.” We therefore map paper concepts onto AIGov’s existing terminology honestly. The primary unit of decision-bound retention is an evidence **`run_id`**. Authoritative decision-state projection for a run is `GET /compliance-summary?run_id=…`, yielding `VALID`, `INVALID`, or `BLOCKED`. Historical retention is realized by an append-only, hash-chained evidence ledger (with optional object-lock anchors) plus export and integrity-check procedures (`GET /api/export/:run_id`, evidence-pack verify). A parallel AI decision flight recorder (`/api/ai-decision-traces`, Functions 2.0 flight-pack) retains operational trace structure (including model version and prompt *hash*, not raw prompts); it is complementary and does not replace the compliance-summary projection.

**Table 6.** Mapping from paper concepts to AIGov instantiation (feasibility mapping, not completeness claim).

| Concept (paper) | AIGov realization | Persisted object | Historical purpose | Reconstruction consequence if absent |
|---|---|---|---|---|
| Decision Episode | Evidence run as decision-bound unit | `run_id` + associated event sequence | Bound one historically situated decision process | No stable join key; correlation heuristics |
| Shared Decision ID | `run_id` (plus optional runtime `decision_id` metadata) | Run identity in ledger / traces | Cross-event membership | Identity fragmentation (Scenario 5 mode) |
| Decision knowledge | Typed evidence events + projected summary | `EvidenceEvent` sequence; compliance-summary projection | Retain process-relevant facts and derived state | Projection incomplete or `BLOCKED` |
| Justification structure | Required justification strings on human/risk review events; recorded evaluation evidence | `risk_reviewed` / `human_approved` payloads; evaluation events | Retain stated grounds for human/risk gates | Gate incomplete; verdict cannot become `VALID` |
| Authorization snapshot | Write-time policy evaluation against configured policy; approver fields on human approval | Policy engine decision at ingest; `human_approved.approver` | Retain that required acts occurred under policy | Missing required approvals → `BLOCKED` |
| Temporal / version context | Deployment `policy_version` / runtime `policy_bundle_version`; model version identifiers | Version fields on server/runtime and events | Anchor evaluation to known policy/model pins | Latest-only ambiguity for policy/model interpretation |
| Evidence bindings | All events keyed by `run_id`; hash-chained append order | Ledger entries under `run_id` | Same-identity evidence membership | Incomplete chain; verify/export fail or `BLOCKED` |
| Policy bindings | Policy modules → required evidence; evaluation at write time | Policy store + per-run evaluation state | Decision-time rule application | Missing required evidence classes → `BLOCKED` |
| Model bindings | `model_version_id` / flight `model_version` | Event and trace fields | Which model artefact participated | Model participation unbound |
| Prompt/version bindings | Flight recorder `prompt_hash` (hash only) | Trace `trace_started` payload | Integrity tip without retaining raw prompts | Prompt content not reconstructable as text (by design) |
| Human decision events | `human_approved`, `risk_reviewed`, flight `human_gate` | Typed events | Human-gate acts and justifications | Human participation missing → `BLOCKED` when required |
| Immutable historical preservation | Append-only hash-chained JSONL ledger; optional S3 Object Lock; append-only Postgres traces | Ledger files; `govai_ai_decision_trace_events` | Tamper-evident retention | Broken chain / missing export |
| Reconstruction procedure | Export + verify + compliance-summary (and optional flight-pack) | Audit export; evidence pack; summary JSON | Later recovery of retained decision state | No dedicated `/reconstruct` product route; procedure is export/verify/project |
| Fail-closed behaviour | Incomplete required evidence ⇒ `BLOCKED` (not success) | `missing_evidence` / `blocked_reasons` in summary | Refuse silent success under gaps | Attempted “success” without required objects is rejected |

Gaps relative to full KCM expressiveness are explicit: AIGov does not implement OPA/Cedar as external PDPs; reliance is not a first-class separate object beyond event payloads; overrides are constrained metadata and do not bypass fail-closed verdicts; and reconstruction is operationalized as **export / integrity-check / project**, not a single reconstruct endpoint. The mapping therefore shows *partial but real* instantiation of the representational requirements—not a complete KCM product.

#### 5.6.2 Decision lifecycle (one run)

A representative lifecycle for one historically retained decision process is:

1. **Decision request / activity begins** — a CI or runtime activity obtains or creates a `run_id`.
2. **Identity establishment** — `run_id` becomes the join key for subsequent evidence.
3. **Policy resolution** — configured policy modules determine required evidence classes for the run under the active `policy_version`.
4. **Authorization / gate resolution** — human approval and risk-review requirements are enforced as required event types (not optional comments).
5. **Model selection / recording** — model participation is recorded via model-version fields on events or flight-trace start.
6. **Evidence collection** — typed events are submitted via `POST /evidence` and appended under write-time policy checks.
7. **Decision execution / projection** — `GET /compliance-summary` projects `VALID` / `INVALID` / `BLOCKED` from the retained chain.
8. **Sealing / historical storage** — accepted events remain append-only and hash-chained; exports capture a stable audit artefact.
9. **Later reconstruction procedure** — a reconstructor uses `run_id` to export and integrity-check the pack and re-read the compliance projection (and optionally the flight-pack), without consulting live “latest” dashboards as authoritative substitutes.

#### 5.6.3 Reconstruction walkthrough

Consider a model-promotion gate analogous to Scenario 1’s human-accepted AI-assisted commitment, scoped to AIGov’s deployment-governance setting.

1. **Request.** An auditor asks: for `run_id=R`, what decision knowledge is retained for the promotion decision?
2. **Lookup.** Resolve `R` in the tenant ledger.
3. **Retrieve preserved artefacts.** Obtain the append-only event sequence and/or `GET /api/export/R`; optionally load the Functions 2.0 flight-pack for operational trace context.
4. **Resolve versions.** Read recorded `policy_version` / policy-bundle pins and `model_version` / `model_version_id` fields from retained artefacts.
5. **Resolve bindings.** Confirm all required events share `run_id=R` and that the hash-chain integrity check succeeds.
6. **Reconstruct justification structure.** Recover evaluation and human/risk justification fields from retained events (process grounds), not a regenerated post-hoc narrative.
7. **Check authorization-related acts.** Check that required `human_approved` / risk-review events exist with recorded approver/justification where mandated.
8. **Check temporal/version context.** Use sealed version pins from the export rather than the currently deployed policy bundle alone.
9. **Return historical decision state.** Return the compliance-summary projection and supporting exported events for `R`.

No latency, storage-cost, or accuracy metrics are claimed. The walkthrough shows procedural recoverability of *retained* objects.

#### 5.6.4 Fail-closed example

Suppose the policy requires `human_approved` for promotion, but only model and evaluation events were appended for `run_id=R`.

- `GET /compliance-summary?run_id=R` yields **`BLOCKED`**, with structured `missing_evidence` / `blocked_reasons` identifying the absent human-approval class.
- Export/integrity-check may still return the partial chain, but the authoritative decision projection does **not** become `VALID`.
- The system therefore surfaces **historical reconstruction of a successful authorized decision as unavailable** for the missing authorization component, rather than silently fabricating an approval or downgrading `BLOCKED` to success.

This behaviour follows the paper’s representational requirements: absence of a mandatory binding or required object yields fail-closed non-success, not heuristic completion. AIGov’s trust model likewise states that `VALID` is a statement about process compliance under retained evidence—not about model-output correctness—and that missing required evidence blocks success.

#### 5.6.5 Implementation versus evaluation

Three claims remain distinct:

1. **Analytical evaluation (Sections 4–5).** Reviewed infrastructure families do not compose by default into faithful historical decision reconstruction (ecosystem base triad: **FAIL**).
2. **Construction / internal coverage (Sections 6–8).** KCM was derived to cover the identified requirements and satisfies them under stated population assumptions (**PASS under assumptions**)—not independent empirical confirmation.
3. **Implementation feasibility (this subsection).** AIGov *instantiates* selected representational objects (shared run identity, append-only retention, version pins, human-gate justifications, export/integrity-check, fail-closed `BLOCKED`) in a working system.

The AIGov implementation does **not** independently validate completeness of the checklist, correctness of KCM, or superiority over alternative representations. It reduces only the concern that the residual is merely descriptive and non-implementable. Independent implementations and deployment studies remain future work.

The results motivate an engineering derivation: if the missing capability is durable decision-knowledge representation with semantic bindings, then a solution must reify decision episodes and seal decision-time relationships. Section 6 presents that derived solution. Section 5.6 shows that related objects can already be *operationalized* in one reference system without treating that system as theory confirmation.

---

## 6 Derived Solution: Knowledge Continuity Model

The preceding sections identify a missing AI representational capability and evaluate existing approaches against requirements derived from that problem. We now **derive** an engineering solution implied by the formalization. The Knowledge Continuity Model (KCM) is presented as a consequence of the analysis—not as an independently motivated headline architecture.

KCM elevates the **Decision Episode** as a representational abstraction for preserving historically meaningful AI decisions. It is a technology-neutral knowledge-representation and composition proposal: persistent objects, semantic bindings, and a reconstruction procedure over historical decision state. It does not mandate a store, ledger, graph database, message bus, or vendor stack. Existing AI-systems components remain valuable; KCM specifies how their outputs can be bound into reconstructable decision knowledge. Alternative compositions that realize the same representational requirements would address the same problem; KCM is one explicit derivation.

### 6.1 Design principles

The design principles follow from the evaluation diagnosis rather than from a prior product concept: the Decision Episode is the unit of representation; every episode has a stable semantic identity usable across systems; cross-component associations must be explicit and retained, not inferred; reconstruction uses historical structure rather than runtime or latest-only truth; criteria, authorities, models, and evidence carry temporal validity relative to decision time; references point to immutable version identifiers or content hashes; human actors, authority, review acts, overrides, and reasons are first-class decision knowledge; reconstruction preserves the minimal sufficient normative and evidential basis rather than requiring bit-exact replay; the model remains technology-neutral; and adoption can be incremental by binding existing AI components into episodes without replacing them.

### 6.2 Decision Episode as representational abstraction

![Figure 3. Decision Episode lifecycle.](../figures/fig3-decision-episode-lifecycle.pdf)

**Figure 3.** Decision Episode lifecycle: open → bind evidence/policy → acts → commitment → seal → reconstruction, with fail-closed outcomes when mandatory knowledge is missing. (Source: `figures/fig3-decision-episode-lifecycle.pdf`.)

A **Decision Episode** is the bounded set of facts, versions, bindings, and acts associated with one decision identity at decision time, plus subsequent review, challenge, and correction acts that refer to that identity. It is a **representational abstraction** for historically meaningful AI decisions—not a governance workflow construct. In boundary are the commit to an action or controlled outcome in which AI outputs materially participated; the evidence and criteria then treated as applicable; human interventions that produced or altered the outcome; and notices, challenges, and corrections referencing the episode. Out of boundary are unrelated telemetry, later training runs not referenced by the episode, organization-wide criteria repositories except via versioned references, and live feature stores except via evidence snapshots.

Each episode has a single immutable **Decision ID**, minted at or before commitment, never reused, used as the join key for all bindings, and stable across later correction. Mutable business keys may alias the Decision ID but must not replace it. Lifecycle phases include formation, commitment, disclosure, contest, correction, and retention under a declared profile.

As a KR construct, the Decision Episode is the reified decision state over which later reasoning—explanation retrieval, drift analysis, responsibility attribution, multi-agent handoff review—can operate without recomputing from live models.

### 6.3 Persistent objects as decision knowledge

![Figure 4. KCM objects and bindings.](../figures/fig4-kcm-objects-bindings.pdf)

**Figure 4.** Principal KCM objects and mandatory relationships: shared Decision ID; relied-upon evidence; authorization with validity intervals; decision-time policy and model version bindings. (Source: `figures/fig4-kcm-objects-bindings.pdf`.)

KCM defines conceptual persistent objects (attributes are information requirements, not schemas), including: **Decision** (identity, outcome, decision time, clock domain, status, profile); **Subject**; **Human Actor** and **Organization**; **Authority** with validity intervals; **AI Inference**; **Model Version**, **Dataset Version**, and **Feature Pipeline Version**; **Evidence Snapshot** distinguishing available, relied-upon, and optionally excluded evidence; **Policy** and **Policy Version** with validity intervals and evaluation results; **Explanation** as a decision-time account that is never the sole justification record; **Human Review** and **Override** (with required rationale when humans affect the outcome); **Notification**, **Appeal**, and **Remediation**; and optional **Audit Record** objects for integrity-elevated profiles.

These objects jointly encode representations of decisions, justification, authority, historical context, and temporal validity. Their co-presence without bindings is insufficient; their bound co-presence is the representational claim of KCM.

### 6.4 Semantic bindings

Bindings are defined exactly once and associate episode objects to the Decision ID (and selected intra-episode associations such as Review ↔ Authority and Inference ↔ Model Version). After commitment, associations and referenced version identifiers are immutable; corrections append new objects rather than rewriting history. Absence of a mandatory binding yields reconstruction failure rather than silent guesswork—the operational counterpart of checklist binding criteria, and the mechanism that preserves **semantic relationships** among decision-knowledge elements.

### 6.5 Temporal model

KCM distinguishes decision time, effective time, inference time, review time, notification time, appeal time, remediation time, and reconstruction time. Policy versions and authorities carry validity intervals that must cover the relevant act times. Evidence snapshots record capture/as-of time. Correction history is append-only: the original Decision remains, and remediation or a superseding Decision references the original identity. Retaining only current criteria, model, features, explanations, or roles as the sole source of truth is treated as a reconstruction failure mode. This is a model of **temporal decision knowledge**, not of bi-temporal databases as such—any storage technology may implement the intervals.

### 6.6 Reconstruction procedure

![Figure 5. Historical reconstruction process.](../figures/fig5-reconstruction-process.pdf)

**Figure 5.** Reconstruction request resolves a Decision ID, retrieves sealed objects, checks versions and temporal validity, then emits complete, partial, or unavailable triad results—never inventing missing mandatory evidence. (Source: `figures/fig5-reconstruction-process.pdf`.)

Given a Decision ID, reconstruction resolves the Decision; recovers evidence, criteria version and evaluation, inference, model/dataset/pipeline versions, human acts, authorities, optional explanation, and ordered notification/appeal/remediation records; then evaluates the triad, emitting explicit gaps if mandatory bindings are missing. The procedure is logical rather than executable code; conforming implementations must preserve fail-closed behaviour on missing mandatory bindings. Conceptually, reconstruction is **reasoning over retained historical decision state**, not re-inference against live models.

### 6.7 How the proposal addresses the gap

Where the ecosystem fails by unbound islands, KCM requires a shared Decision ID and sealed bindings. Where Scenario 2 fails by latest criteria substitution, KCM seals Policy Version. Where Scenario 3 fails by outcome-only retention, KCM requires Override records with rationale and authority. Where Scenario 4 fails by drift, KCM seals model/dataset/pipeline versions and evidence snapshots. Where Scenario 5 fails by correlation heuristics, KCM forbids reconstruction by undocumented identity guessing. Where Scenario 6 collides with deletion, KCM does not override external deletion constraints; it makes retention and redaction semantics explicit and allows partial reconstruction when only digests or categories remain.

---

## 7 Derived Conformance Specification

A problem formalization that cannot be tested invites purely rhetorical adoption claims. From the reconstruction requirements and Decision Episode representation we derive a Conformance Specification: how an independent evaluator determines whether an implementation preserves sufficient decision knowledge for deterministic faithful reconstruction. The specification is technology-neutral: it mandates neither storage engines, cryptography, schemas, serialization formats, network protocols, vendor APIs, nor deployment topologies. Normative keywords follow RFC 2119. Conformance evaluates reconstruction capability of a representation; it is not presented as a regulatory certification scheme.

### 7.1 Conformance classes

**KC Core** is the minimum class for claiming Knowledge Continuity reconstruction capability for the base triad profile. **KC Extended** requires Core conformance plus additional requirements that improve robustness, contestability linkage, and integrity-oriented reconstruction. Conformity claims must name the class and declared checklist profile. Vendor-specific profile names are out of scope. Future conformance classes are reserved but not defined. Table 5 summarizes classes and requirement themes.

**Table 5.** Conformance overview (derived Conformance Specification). Guarantees are representational/reconstruction capability claims under stated assumptions—not regulatory certification or empirical field proof.

| Class | Mandatory capabilities | Optional / Extended | Reconstruction guarantee | Explicit non-guarantees |
|---|---|---|---|---|
| KC Core | Decision ID/Episode; outcome/time; historical evidence + reliance distinction; policy version linkage + evaluation; inference/model(/pipeline) linkage; human review/override + authority when applicable; temporal validity; fail-closed published procedure; cross-system bindings (KC-01… applicable Core) | Integrity/signatures; excluded-evidence accounting; contestability extras | Base-triad reconstructability *if* mandatory objects populated and retained | Decision quality/fairness; adoption; bit-exact replay; override of deletion law |
| KC Extended | All Core | Contestability linkage; integrity-oriented Audit Records; additional robustness obligations | Core guarantee plus Extended profile obligations when claimed | Same non-guarantees; Extended does not imply universal completeness |

### 7.2 Normative requirements (summary)

The specification assigns stable identifiers KC-01 through KC-34. Requirements cover, among other themes: Decision identity and Episode existence; stable semantic identity; historical evidence and criteria preservation; criteria version and AI inference linkage; model, dataset, and feature-pipeline version linkage; human review and override linkage; authority preservation; temporal validity; explanation, notification, appeal, and remediation linkage; correction history; immutable historical references; cross-system bindings; minimal reconstruction completeness; technology neutrality; published reconstruction procedure; fail-closed behaviour; and subject linkage. Extended-class requirements address additional contestability and integrity-oriented obligations (including audit-oriented records and excluded-evidence accounting where claimed). We do not reproduce all thirty-four requirement blocks here; each block in the authoritative specification states a normative clause, rationale, related checklist items, related KCM principles, conformance class, and verification method (for example document inspection, metadata inspection, historical reconstruction, record traceability, version validation, temporal validation, or graph consistency).

### 7.3 Reconstruction verification

Successful reconstruction is defined with required inputs (Decision ID, published procedure, retained stores), minimum expected outputs (identity/outcome/time, triad statements, bound object identifiers, explicit gaps), acceptable uncertainty bounds, failure conditions, and historical consistency constraints. The specification distinguishes **complete**, **partial**, and **failed** reconstruction. Missing mandatory bindings yield failure rather than heuristic completion.

### 7.4 Base-triad verification

Objective pass criteria are stated for Authorization, Justification, and Validity. Authorization requires recoverable actor (as applicable), temporally valid authority, and criteria version/evaluation bound to the same Decision ID. Justification requires evidence snapshot with reliance distinction, inference/model (and pipeline when applicable) linkage, and human rationales when humans affect the outcome; unbound post-hoc explanation is insufficient as sole basis. Validity requires criteria temporal coverage, evaluation/outcome consistency, and prohibition of latest-only substitution. Base faithful reconstruction passes only if all three pass.

### 7.5 Relationship to the checklist and existing infrastructure

Requirements trace to KCM principles and to checklist categories. The specification complements provenance, observability, lineage, metadata, policy engines, authorization, documentation, explainability, human–AI workflow records, and organizational AI guidance. It does not replace them. Conformance evaluates **reconstruction capability of a representation**, not regulatory certification.

---

## 8 Evaluation of the Derived Solution

We evaluate the derived Knowledge Continuity Model analytically with the same checklist marks, base-triad roll-up, and six scenarios used for existing sources. Scoring credits objects and bindings the model defines; it does not credit hypothetical extras, organizational willingness to adopt, or bit-exact replay.

Four claims must be kept distinct:

1. **Ecosystem finding.** Reviewed infrastructure families do not compose by default into faithful historical decision reconstruction (Section 5; triad **FAIL**).
2. **Construction finding.** KCM was derived to cover the representational requirements identified from that analysis (Sections 3 and 6).
3. **Internal coverage finding.** Under stated population and preservation assumptions, KCM instantiates those requirements (triad **PASS** under assumptions). This is an **internal consistency and requirement-coverage** analysis—evidence that the derived model covers the requirements from which it was constructed—not independent empirical confirmation of sufficiency, not proof of operational feasibility, not proof that the checklist is complete, and not comparative superiority over all alternative models.
4. **Unresolved external-validation question.** Whether the model is sufficient and practical in deployed systems remains open.

KCM remains PASS only under its stated assumptions; the ecosystem triad remains FAIL.

### 8.1 Checklist evaluation

Under the base triad profile, KCM systematically supports decision identity, outcome, and time; actors; authority with validity intervals; governing criteria and criteria version; applicable-rule/evaluation path digests when multi-rule policies are in scope; evidence used and evidence relied upon; model version and confidence gates; temporal context; and decision-bound provenance/lineage via versioned bindings. These are the categories on which unit SUTs most often failed compositionally—especially shared identity, criteria-version sealing, and reliance distinction.

Remaining **PARTIAL** marks arise where the model provides expressibility without a first-class dedicated object, or where the checklist class is optional/conditional: constraints as distinct from criteria/evaluation content; excluded evidence unless elevated; prompts, tools, and external services via snapshot payloads rather than dedicated objects; explicit assumptions structure; jurisdictional frame objects; and integrity/signatures for elevated profiles. These partials are limitations of systematic coverage, not hidden passes.

### 8.2 Base triad

Under conformant population of mandatory objects and bindings:

- **Authorization:** PASS — actors, temporally valid authority, and sealed criteria version/evaluation on the same Decision ID.
- **Justification:** PASS — evidence snapshot with reliance distinction, bound inference/model context, and human rationales when applicable; post-hoc unbound explanations excluded as sole basis.
- **Validity:** PASS — historical criteria interval coverage and evaluation/outcome consistency without latest-only substitution.
- **Faithful reconstruction (base):** PASS under stated assumptions (internal coverage; not external validation).
- **Elevated integrity profiles:** PARTIAL until integrity/signature objects are populated.

### 8.3 Scenario evaluation

Table 3 contrasts prior ecosystem results with KCM under conformance. Scenarios 1–5 yield complete base reconstruction when mandatory objects are populated and Decision IDs are propagated; Scenarios 3 and 5 fail if organizations retain outcome-only records or refuse shared identity—those deployments are non-conformant rather than counterexamples to the model’s information requirements. Scenario 4 passes for historical justification context without claiming compute-identical replay. Scenario 6 is complete, partial, or failed depending on whether relied-upon evidence remains retained (possibly redacted): redacted snapshots with explicit reliance semantics may preserve partial justification; wholesale destruction of relied-upon evidence without a substitute representation fails justification.

Reconstruction is deterministic under the model’s assumptions when bindings are present: the procedure does not rely on undocumented correlation. Determinism here refers to structural triad statements from retained bindings, not to identical floating-point model internals.

### 8.4 Strengths and remaining limitations

**Strengths (coverage).** Relative to the gap characterized in Section 5, the derived model *expresses* Decision Episode identity, sealed versions, reliance distinction, human-act/rationale records, authority intervals, and fail-closed reconstruction as first-class decision knowledge. Section 5.5 shows an architectural path to populate those objects from existing components; Section 5.6 shows a partial instantiation in AIGov. Neither point is independent validation of KCM.

**Remaining limitations.** The model does not solve organizational adoption; incomplete retention; external deletion constraints; evidence never captured; implementation defects; or the substantive quality or optimality of decisions. Category thinness remains for constraints as first-class objects, excluded-evidence accounting, prompt/tool/external-service objects, systematic assumptions structure, jurisdictional-context objects, and integrity/signature elevation. Retroactive stitching of pre-adoption logs without Decision IDs remains non-deterministic. Rationale *quality* is out of scope even when rationale fields are mandatory. Universal completeness is not claimed. Sufficiency is relative to checklist base triad under stated assumptions: mandatory objects populated at commitment, historical version artefacts resolvable, retention horizon honoured, and reconstruction fail-closed on gaps.

---

## 9 Discussion

### 9.1 The scientific object is the problem

The central result of this paper is not that a particular model exists, but a refined formulation and systematic characterization of a representational deficiency of contemporary AI systems: they preserve execution while under-preserving the decision knowledge required for faithful historical reconstruction (Figure 1; Tables 1–4). Characterizing that deficiency—its distinction between execution artefacts and decision knowledge; its base triad of justification, authorization, and temporal validity; its reliance and binding conditions; and its compositional evaluation across infrastructure families—is the principal AI contribution. Adjacent KR traditions (§2.8) motivate episode and temporal structure without substituting for cross-component bindings. The reference composition (§5.5; Figure 2) shows architectural actionability without claiming deployment proof. The AIGov reference implementation (§5.6) further shows that selected representational objects can be *instantiated* in a working system; that demonstration addresses practical implementability and does **not** eliminate the need for external validation, comparative evaluation, or empirical deployment studies. Engineering artefacts (checklist, KCM, conformance; Figures 3–5; Table 5) remain instruments of the characterization and one derived response, evaluated only for internal coverage (Section 8).

### 9.2 Why the problem grows with future AI systems

As AI systems become longer-lived, more compositional, and more entangled with other agents and tools, the interpretive distance between *current execution state* and *past committed decisions* increases. Assistants accumulate commitments; orchestrators chain tools; multi-agent systems redistribute evidence and authority; autonomous systems update controllers while past acts remain consequential. None of these trends was experimentally measured here. They indicate, without speculation about particular products, that the historical decision reconstruction problem is unlikely to shrink as AI systems scale in duration and composition. Governance and regulated settings will continue to expose the deficiency; they do not exhaust it.

### 9.3 Implications for AI systems and knowledge representation

For knowledge representation, AI systems, agents, multi-agent systems, decision support, and long-lived deployments that commit to outcomes with lasting interpretive significance, preserving decision knowledge—identity, justification structure, authority, temporal validity, and semantic bindings—belongs among first-order representation requirements, not among optional telemetry hygiene. The analytical evaluation suggests that investing solely in more logs, richer provenance graphs, or better explanation interfaces will not reliably produce historical reconstruction if those artefacts remain unbound to a decision identity and to decision-time versions. **Decision knowledge** is a distinct representational layer relative to execution knowledge; provenance remains a relevant substrate that can encode portions of that knowledge without guaranteeing compositional reconstructability.

### 9.4 Potential application domains

We did **not** experimentally validate the following domains; we identify them as natural settings in which the formalized problem is likely to arise:

- **Decision-support systems**, where recommendations become commitments and must remain interpretable after model updates.
- **AI assistants and long-lived agents**, where cumulative commitments, tool uses, and user confirmations form an evolving decision history.
- **AI orchestration and multi-step workflows**, where bindings must span planners, tools, and downstream actuators.
- **Multi-agent systems**, where justification and authority cross agent boundaries and informal correlation of messages is insufficient.
- **Autonomous systems**, where post-incident reconstruction must recover decision-time criteria and evidence rather than current controller parameters.
- **Human–AI collaborative systems**, where overrides and rationales are part of the decision representation, not optional comments.

Regulated eligibility and oversight settings remain important *stress tests* of the same representational requirements.

### 9.5 Incremental adoption of the derived solution

Where organizations choose to address the formalized gap using KCM’s derivation, an adoption path begins by minting and propagating a Decision ID at the commitment point; wrapping existing policy-engine results, model-registry versions, and workflow completions as bound objects; adding evidence snapshotting beside live feature access; enforcing commitment gates that reject incomplete mandatory bindings; and extending to notification and challenge systems where applicable. Early steps do not require replacing OPA, OpenTelemetry, HumanTask processors, or model registries. AIGov (§5.6) illustrates one such path using `run_id`-keyed append-only evidence and fail-closed projections, without claiming that path is the only or complete realization of KCM.

### 9.6 Relationship to existing AI tooling

The formalized requirements complement provenance, observability, lineage/metadata, policy engines, authorization languages, documentation, explainability, and human–AI workflow records. Those components continue to provide derivation, paths, pipeline versions, evaluation semantics, release descriptions, explanation quality, and task lifecycle. What they do not jointly define—and what the problem statement demands—is episode membership with sealed decision-time semantic relationships and fail-closed reconstruction over historical decision state.

### 9.7 Trade-offs

Evidence snapshots cost storage and raise tension with data minimization; Scenario 6 shows that deletion of relied-upon inputs can force partial or failed justification even when other logs survive. Commitment gates increase operational friction but prevent silent non-conformance. Minimal sufficient reconstruction deliberately excludes bit-exact replay, which lowers forensic ambition while matching the checklist’s adequacy threshold. Elevated integrity (checksums, signatures) strengthens trustworthiness of retained records but is not required for base content faithfulness.

### 9.8 Scope and generality

The historical decision reconstruction problem, as formalized here, concerns reconstruction capability of decision knowledge. It does not assess decision quality, fairness, security hardening, or organizational process maturity. It is stated at a level of generality independent of law and compliance. Domain profiles may elevate optional checklist categories without weakening Required items.

What would count as addressing the problem without adopting KCM as a product is any declared composition that realizes the same Decision Episode representational requirements, publishes a reconstruction procedure, and fails closed on missing mandatory associations. Such a composition would confirm the *problem formalization*; it would not erase the finding that the reviewed sources do not already define those bindings.

### 9.9 What the reference implementation does and does not settle

AIGov reduces one practical concern raised by systems readers: whether the residual semantic-binding gap is merely descriptive. By operationalizing shared run identity, append-only retention, version pins, human-gate justifications, export/integrity-check procedures, and fail-closed `BLOCKED` outcomes, the reference implementation shows implementability of selected requirements. It does **not** settle external validation of the checklist, comparative evaluation against alternative episode models, or empirical studies of deployment frequency and cost. Those remain open.

---

## 10 Threats to Validity

**Conceptual evaluation.** Ecosystem and KCM scores assess specified information models and analytical scenarios, not measured frequencies in industry deployments. Adoption claims are accordingly constrained.

**Implementation dependence.** Optional features in sources (for example optional HumanTask comments, Cedar without a log sink) widen capability ceilings but not guarantees. Similarly, KCM triad PASS depends on commitment gates and retention; implementation failure falsifies a deployment, not the checklist alignment of the specification text.

**Publication and corpus bias.** The corpus privileges published primary sources selected for family coverage. Unpublished organizational schemas might already realize episode bindings. Such a schema would be a successful *composition profile* realizing KCM-like requirements; it would not show that the reviewed standards already define those bindings.

**Domain dependence.** Narrow application-specific logging fields must not be generalized into a complete decision representation. Profiles may need domain adaptation.

**Future standards.** Future AI-systems standards or profiles may later standardize the same bindings under other names. The finding concerns the reviewed ecosystem at the evaluation’s source pins, not perpetual impossibility.

**Alternative composition mechanisms.** The evaluation does not assert that only a branded new product layer can succeed. A composition profile over existing stores that realizes the same objects and bindings would also satisfy the information requirements. Authoring bias is a further threat because KCM was derived to answer composition failures; mitigation consists in using the same checklist and scenarios, and in recording PARTIAL marks and Scenario 6 limits explicitly.

**Absence of deployment measurements.** Scenarios are adversarial structural tests. They show failure modes consistent with unit boundaries; they do not estimate how often organizations already invent adequate private integrations.

**Circular evaluation risk.** Because KCM was designed against the checklist, Section 8 is an internal coverage check under conformance assumptions, not independent field efficacy and not external validation of sufficiency. We treat that limitation as intrinsic to conceptual KR evaluation at this stage and state it as claim (3) versus unresolved claim (4) in Section 8.

**Author-developed reference implementation.** AIGov is developed by the authors. It therefore cannot constitute independent validation of the theory, the checklist, or KCM. Its reported role is solely to demonstrate that selected representational requirements are *implementable* in a working AI-governance infrastructure. Independent third-party implementations, blinded replications of the analytical marks, and deployment measurements remain future work.

---

## 11 Conclusion

Contemporary AI systems preserve execution. They do not, on the evidence of our analytical evaluation of representative infrastructure, adequately preserve the decision knowledge required for deterministic faithful historical reconstruction of justification, authorization, and temporal validity. We refined and characterized that gap as the **historical decision reconstruction problem**—an Artificial Intelligence knowledge-representation and systems problem that exists independently of law, regulation, governance, and compliance.

Contributions follow a fixed hierarchy: (1) refined problem formulation; (2) representational requirements for historical decision knowledge; (3) unit and compositional evaluation of contemporary AI infrastructure; (4) identification of the residual semantic-binding and shared-identity gap; (5) the derived Knowledge Continuity Model and Conformance Specification centred on the Decision Episode abstraction; and (6) a reference implementation (AIGov) demonstrating that selected representational objects can be instantiated in a working system. Under stated assumptions an internal coverage analysis finds that the derived model satisfies base-triad requirements (PASS under assumptions)—not empirical proof of deployment sufficiency. The reviewed ecosystem composition remains FAIL for the base triad; adoption, retention, evidence deletion, and several conditional categories remain limiting. The AIGov demonstration addresses implementability only; it does not independently validate the theory.

The principal scientific contribution remains refined problem formulation and systematic characterization—previously under-characterized in this specific representational and compositional form—and distinguishable from logging, provenance formats, workflow engines, and explainability methods, while acknowledging provenance and DEMM as related but non-subsuming work. The engineering model and the reference implementation are derived instruments of that contribution, complementary to existing AI infrastructure and replaceable by any composition that realizes the same representational requirements.

Future work includes independent implementations; comparative evaluation of alternative episode representations; domain-specific profile elevations; studies of reconstructability in multi-agent and long-lived assistant settings; deployment measurements; and integrity-elevated reconstructions. Those steps should reuse the Reconstruction Checklist rather than weaken the problem characterization.

---

## Figure and table sources

Figures are Mermaid specifications under `publications/01-jair/figures/` (render with any Mermaid-compatible toolchain for journal production):

| Figure | File | Point |
|---|---|---|
| 1 | `fig1-scientific-argument.mmd` | KCM is derived after compositional failure |
| 2 | `fig2-fragmented-islands.mmd` | Islands without Decision ID vs bound episode |
| 3 | `fig3-decision-episode-lifecycle.mmd` | Lifecycle with fail-closed outcomes |
| 4 | `fig4-kcm-objects-bindings.mmd` | Objects, reliance, authority, version bindings |
| 5 | `fig5-reconstruction-process.mmd` | Complete / partial / unavailable reconstruction |

Tables 1–5 are embedded in the body from checklist, coverage, scenarios, composition analysis, KCM evaluation, and conformance specification artefacts. Table 6 maps paper concepts to the AIGov reference implementation (§5.6). Evaluation markers are unchanged.

---

## References

References are drawn from the repository BibTeX library (`references/bib/library.bib`). Keys used in this manuscript:

- `@moreau2013provDm`
- `@singh2019decisionProvenance`
- `@huynh2021provenanceExplanations`
- `@solozobov2026demm`
- `@allen1983temporalIntervals`
- `@kowalski1986eventCalculus`
- `@mccarthy1969situationCalculus`
- `@aamodt1994caseBasedReasoning`
- `@openTelemetry2026specification`
- `@google2026mlMetadata`
- `@openLineage2026specification`
- `@openPolicyAgent2026`
- `@cedarPolicyLanguage2026`
- `@mitchell2019modelCards`
- `@gebru2021datasheets`
- `@procope2022systemCards`
- `@nist2023aiRmf`
- `@nist2021ir8312`
- `@eu2024aiAct`
- `@oasis2010wsHumanTask`

*[Formatted reference list to be generated from BibTeX at journal export.]*

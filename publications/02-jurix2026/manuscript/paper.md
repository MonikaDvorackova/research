---
id: pub-02-jurix2026-paper-draft
title: "Preserving decision knowledge in legally relevant AI systems"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-30
tags: [jurix, manuscript-draft, publication-02]
target_venue: JURIX 2026
venue_format: Springer LNCS
submission_type: Full paper
review: Double-blind
language: English
source: planning/jurix-specification.md
publish: false
authors:
 - Monika Dvořáčková
 - Štěpánka Havlíková
 - Jakub Harašta
draft_sections_complete: [1, 2, 3, 4, 5, 6, 7, 8]

---

## Preserving decision knowledge in legally relevant AI systems

**Status:** First complete prose draft of Sections 1–8 with compiled References. Abstract remains outstanding. Figure assets are planned but not yet created.

**Source of truth:** `../planning/jurix-specification.md`

**Venue (specification):** JURIX 2026 · Full paper · Springer LNCS · English · Double-blind

**Authors (to anonymise before submission):** Monika Dvořáčková; Štěpánka Havlíková; Jakub Harašta

---

### Abstract

*[Not yet written. Skeleton only.]*

---

### 1. Introduction

#### 1.1 Motivation

Legally relevant AI systems increasingly participate in decisions that outlive the software version that produced them. Benefit determinations, eligibility screens, risk rankings, content-moderation outcomes, investigative triage and similar AI-assisted commits are reviewed, audited, appealed or investigated weeks, months or years later. In the same interval, engineering practice continues: prompts are rewritten, retrieval indices refreshed, tools and vendors replaced, models upgraded, and policy bundles revised. Those changes are ordinary success criteria of modern AI delivery. They are also ordinary threats to the reconstructability of past decisions.

Organisations already invest in operational logging, monitoring, model registries and governance documentation. Those investments answer a different question from the one later forums ask. Live systems and current documents show how the organisation operates *now*. Audit, appeal and oversight ask what was known, used, constrained and authorised *when a particular decision was made*. Where that decision-time basis was never retained as structured, decision-bound information, long-lived AI systems become difficult to govern precisely because they remain easy to change.

#### 1.2 Problem

This paper distinguishes *system state* from *Decision Knowledge*. System state is the mutable configuration and runtime content through which a system presently operates—current prompts, indices, tools, models, policies and recent operational records. Decision Knowledge, defined fully in Section 4, is the structured set of information required to explain, justify, review or contest a specific AI-assisted decision after it has been made.

The practical problem is that state can be healthy while Decision Knowledge is gone. Overwritten prompts, changed retrieval results, altered tools, model updates, human approvals without retained rationale, missing policy versions and disappearing legal context routinely erase or unbind what later reconstruction needs (Section 2). The result is not only a philosophical worry about “understanding AI.” It creates concrete difficulties for:

- **audit**, when auditors can inspect current controls but cannot recover the basis of a contested past outcome;
- **review**, when meaningful review of automated decision-making requires process records that mutable state does not stably supply;
- **appeal and contestation**, when subjects or oversight actors lack the materials that contestation procedures presuppose;
- **governance**, when compliance artefacts and dashboards coexist with reconstruction failure;
- **long-lived AI systems**, whose operational lifetime is designed to exceed any single model or prompt version.

In short: engineering that preserves only system state under-serves institutions that must reason legally about decisions across time.

#### 1.3 Research gap

Neighbouring research addresses parts of this landscape without closing the engineering gap. Explainable AI illuminates model behaviour, typically at prediction time, but does not organise retention of decision-time context under deployment change. Legal explainability clarifies what reason-giving should achieve, while often assuming that relevant facts and reasons remain available when review arrives. Reviewability frameworks (notably Cobbe, Lee and Singh, 2021) establish socio-technical record-keeping for meaningful review—the closest neighbour—yet leave room for an explicit engineering artifact and system property focused on technical mutability in contemporary AI stacks. Provenance and decision-provenance work trace derivation and flow; they do not, without further design, guarantee legal criteria, human rationale, policy constraints or review context bound to one decision. Governance frameworks and regulatory logging duties raise retention pressure without specifying Decision Knowledge as defined here.

Section 3 develops this comparison systematically and summarises it in Table 1. The gap statement used throughout is deliberately modest: existing approaches explain outputs, trace data or audit behaviour, but they do not—without further design—preserve the structured knowledge required for future legal reasoning about a specific AI-assisted decision.

#### 1.4 Research question

The paper therefore asks:

> How should AI systems preserve decision knowledge so that legally relevant decisions remain explainable, reviewable, contestable and justifiable over time?

The question is answered at a conceptual level: by diagnosing loss mechanisms (Section 2), differentiating neighbours (Section 3), defining Decision Knowledge and Knowledge Continuity (Section 4), and proposing preservation principles and concepts (Section 5). Implications for AI & Law follow in Section 6; discussion and conclusion in Sections 7–8. The paper does not claim an implemented evaluation.

#### 1.5 Contributions

The contributions correspond to material developed in the body:

1. **Problem formulation.** An engineering diagnosis of legally relevant AI systems that preserve mutable system state while losing decision-time knowledge under ordinary change (Section 2), including why post-hoc explanation cannot recover unretained context.
2. **Decision Knowledge as an engineering artifact.** A definition, working component inventory, temporal properties and lifecycle for the structured information required to explain, justify, review or contest a specific AI-assisted decision after it has been made (Section 4).
3. **Knowledge Continuity as a system property.** A definition of the capacity to preserve Decision Knowledge across time, system changes and institutional contexts, disambiguated from organisational knowledge-management and business-continuity uses of “continuity” (Section 4).
4. **Conceptual preservation framework.** Design principles, logical layering, capture/binding/retention mechanisms and integration guidance for engineering Knowledge Continuity without prescribing a product architecture (Section 5).
5. **Implications for AI & Law.** An account of how the framework bears on legal explainability, accountability, reviewability, contestability and evidentiary reconstruction, including the claim that explainability is not only a model property but also depends on preserved decision-time knowledge (Section 6).

Contribution 1 is a problem characterisation, not a proof that no existing deployment ever retains sufficient records. Contributions 2–4 are conceptual; they invite formalisation and empirical evaluation rather than asserting measured superiority over reviewability or provenance. Contribution 5 states enabling conditions for legal functions, not satisfaction of particular statutory articles.

#### 1.6 Roadmap

Section 2 details the missing engineering problem. Section 3 positions the paper among neighbouring approaches (Table 1). Section 4 defines Decision Knowledge and Knowledge Continuity. Section 5 develops the conceptual framework for preserving Decision Knowledge across the AI lifecycle. Section 6 discusses engineering, legal/governance and regulatory implications. Section 7 discusses positioning, strengths, limitations and future work. Section 8 concludes.

---

### 2. The Missing Engineering Problem

Legally relevant AI systems are typically engineered to remain available, observable and updatable. In that engineering culture, what is retained is primarily *system state*: the live configuration, stores and runtime artefacts through which the system presently operates. System state may include current prompts and templates, the active retrieval index, connected tools and external services, the deployed model version, current policy bundles, and recent operational logs. Such artefacts are indispensable for operation. They are not, however, identical to the structured information required later to explain, justify, review or contest a *particular* AI-assisted decision.

The difficulty is temporal. Legal and institutional review characteristically occurs after the decision, often after the system has changed. Accountability, contestability and administrative review therefore depend on reconstructing the decision as it was situated at decision time, not on inspecting whatever the system happens to contain at review time. Where engineering practice preserves only mutable state, the information needed for later legal reasoning can disappear even though the organisation continues to “have logs,” “have monitoring,” and “have a model in production.” This section makes that gap precise by examining what current systems tend to preserve, what they lose under ordinary change, why the resulting deficit is an engineering problem, why post-hoc explainability does not close it, and why the deficit creates legal and governance risk.

#### 2.1 What current systems preserve

Contemporary AI deployments, especially those that combine generative models with retrieval, tools and human gates, typically preserve several classes of operational information.

First, they preserve *execution and observability data*: request logs, traces, latency metrics, error rates and related telemetry. These records support reliability engineering and incident response. Second, they often preserve *derivation-oriented artefacts* associated with data and model pipelines—training-set references, model registry entries, deployment tags—or more general provenance records in the sense of lineage and derivation graphs. Third, many regulated or governed deployments retain *policy and access artefacts*: the current authorisation configuration, allow/deny decision logs from policy engines, and organisational documentation such as model cards or system descriptions. Fourth, conversational and agentic systems may retain *session transcripts* or partial tool-call histories for product or safety review.

None of these preservations is negligible. Collectively they show that the field already invests heavily in recording behaviour, lineage and control. The claim of this paper is narrower: preserving operational and lineage artefacts does not automatically preserve the structured decision-time knowledge later required for legal reasoning about a specific decision. System state answers, in large part, what the system *is* and how it *behaves now*. Legal review asks what was known, used, constrained and authorised *then*.

#### 2.2 What is lost over time

The loss mechanisms that matter for legally relevant AI systems are ordinary engineering events, not exotic failures. Each mutates or erases information that later explanation, justification, review or contestation may need.

**Overwritten prompts.** Prompt templates and instance prompts often encode task framing, implicit criteria and safety instructions. When templates are edited for product improvement, the live system no longer contains the prompt that shaped a past decision. Unless that prompt context was retained as bound to the decision, later reconstruction must guess which instructions were in force.

**Changing retrieval results.** Retrieval-augmented systems ground outputs in an evolving corpus or index. Re-running the same query later can return different passages. If the passages actually retrieved—and, where selection occurred, those relied upon—were not retained with the decision, a reviewer cannot recover the evidential field that supported the outcome.

**Changing external tools.** Tool schemas, APIs and downstream services change. A tool result that was decisive at decision time may be irreproducible, or may be replaced by a differently versioned service. Operational logs may show that “a tool was called” without preserving the versioned result that entered the decision.

**Model updates.** Models are routinely swapped, quantised, fine-tuned or reconfigured. Reproducing an output under a later model does not recover the decision-time model’s contribution. Where model identity and version are not bound to the decision, later explanations risk describing a different computational participant than the one that acted.

**Human approvals without rationale.** Many legally sensitive pipelines insert a human gate. Systems frequently record that an approval occurred (actor, timestamp, allow/deny) while omitting the rationale, the criteria applied, or the materials the human treated as decisive. The approval event remains; the justificatory content does not.

**Missing policy constraints.** Authorisation and validity often depend on policy bundles and constraints that change independently of the model. Retaining only the current policy, or only a boolean allow/deny without the governing policy version and applicable rule path, leaves later review unable to state under which constraints the decision was permitted.

**Disappearing legal context.** Jurisdiction, procedural posture, applicable legal criteria and institutional mandate are frequently kept outside the technical system—in tickets, emails or unspoken role knowledge. When that context is not bound to the decision as retained structure, later legal reasoning must re-import it from unstable institutional memory.

These mechanisms can co-occur. A single contested decision may be separated from review by a prompt rewrite, an index refresh, a model upgrade, a policy bump and staff turnover. The live system at review time can be healthy and well logged while the decision-time knowledge is gone.

#### 2.3 Why this is an engineering problem

The deficit is not merely that organisations sometimes forget to archive files. It is a mismatch between (i) what continuous AI engineering optimises for—freshness, replaceability and operational visibility—and (ii) what later legal reasoning requires—stable, decision-bound structure across change.

Three properties make the mismatch engineering-shaped. First, the relevant information is often *transient*: prompts, retrieved passages, tool outputs and human rationales exist briefly in the decision path and are not first-class persistent objects. Second, the relevant bindings are *cross-cutting*: a later reviewer needs the association among outcome, evidence, model version, policy version, rationale and legal criteria for *one* decision identity, not unbound global stores of “latest prompts” and “latest policies.” Third, change is *normal*: model and tool updates are success metrics of AI product organisations; they are also erasure events for decision-time context unless preservation is designed.

Accordingly, treating the problem as only organisational negligence understates it. A system can follow common MLOps and observability practice and still fail to retain Decision Knowledge. Closing the gap requires explicit preservation design—what later sections call *Knowledge Continuity*—rather than hoping that residual logs will suffice.

#### 2.4 Why explainability approaches do not solve it

Post-hoc explainable AI (XAI) methods typically aim to illuminate model behaviour at prediction time: which features mattered, what counterfactual changes would alter the output, or how an interpretable surrogate approximates the model. That research programme is important for understanding models. It does not, by itself, guarantee that the decision-time context needed for later legal reasoning has been retained.

Legal explainability scholarship has long distinguished technical accounts of model behaviour from legally meaningful reason-giving and from the institutional conditions under which explanations can be used (see, among others, Wachter, Mittelstadt and Russell, 2017; Edwards and Veale, 2017). Counterfactual and related explanation methods may support contestation when the underlying facts and decision setting remain available; they cannot recover prompts, retrieved evidence, tool results, policy versions or human rationales that were never preserved. Likewise, process-centric explanation proposals aimed at contestability (Yurrita, Balayn and Gadiraju, 2023) presuppose access to process-relevant information. If that information has been overwritten by ordinary system change, explanation methods operate on an incomplete or anachronistic basis.

The engineering point is simple: an explanation generated at review time is not a substitute for Decision Knowledge captured at decision time. Where the system no longer retains what was used, constrained and authorised then, explainability techniques can at best narrate the present system or an incomplete trace. They cannot manufacture missing historical bindings. Section 3 and Table 1 locate this limit among neighbouring approaches; the present subsection states only the engineering dependence.

#### 2.5 Legal and governance risks

When decision knowledge is not preserved, several legal and governance functions degrade together.

*Explanation and justification* become speculative: institutions may be able to describe current practice while being unable to reconstruct the basis of a past decision. *Reviewability*—understood following Cobbe, Lee and Singh (2021) as the possibility of meaningful review supported by systematic records of automated decision-making—depends on more than mutable system state. *Contestability* presupposes that a decision subject or oversight actor can scrutinise relevant materials; if those materials no longer exist in structured form, contestation rights are procedurally hollow even when formally recognised (cf. Alfrink et al., 2023, on contestable AI by design as consuming process-relevant information). *Accountability* relations require that forums can obtain answers about what was done and on what basis (cf. Wieringa, 2020); state dumps and current configurations do not reliably supply those answers after change. *Evidentiary reconstruction* for disputes or investigations faces the same deficit: lineage and logs may show activity without recovering the normative and evidential basis of the outcome.

Governance instruments intensify the practical stakes without dissolving the engineering problem. Documentation regimes, risk-management frameworks and regulatory record-keeping duties (including, in the European setting, logging and transparency obligations under Regulation (EU) 2024/1689) create pressure to retain information. They do not, by themselves, specify the structured Decision Knowledge required for later legal reasoning about a specific AI-assisted decision. Compliance artefacts and live system state can therefore coexist with reconstruction failure. Section 6 returns to this point when relating the framework to governance and the AI Act.

Having stated the loss mechanisms, we next ask how existing research programmes relate to the gap—and where they stop.

*[Figure 1 — System State vs Decision Knowledge: planned; assets not yet created.]*

---

### 3. Existing Approaches and Their Limits

Section 2 diagnosed a preservation gap under ordinary AI-system change. Section 1 summarised why explainability, reviewability, provenance and governance leave an engineering residue; this section makes that comparison explicit. The aim is not a comprehensive survey. It is a structured comparison: for each neighbour, what problem it addresses, what it preserves, what it typically does not preserve, and how that relates to *Decision Knowledge* and *Knowledge Continuity* as defined in Section 4. Table 1 compresses the result.

The shared research gap, stated in the manuscript specification and used as the evaluation criterion below, is as follows: existing approaches explain outputs, trace data or audit behaviour, but they do not—without further design—preserve the structured knowledge required for future legal reasoning about a specific AI-assisted decision.

Throughout, “supports reconstruction” means support for reconstructing decision-time justification, authorisation-relevant constraints and review context after system change—not merely replaying logs or regenerating a model commentary.

#### 3.1 Explainable AI

**Primary objective.** Make model behaviour intelligible: which features mattered, how a prediction was produced, or how an interpretable surrogate approximates a complex model (Doshi-Velez and Kim, 2017; Lipton, 2018; Guidotti et al., 2018).

**Problem solved.** Opacity of learned predictors at prediction or analysis time; scientific and practical demands for interpretability.

**What it preserves.** Often little as a durable decision artifact. Methods typically *compute* explanations from a model and inputs when asked. Some deployments store explanation outputs, but retention of decision-time context (prompts, retrieved evidence, tool results, policy versions, human rationale) is not the organising goal of the XAI research programme.

**What it does not preserve.** By default, the cross-cutting bindings that Section 2 showed are erased by prompt, retrieval, tool and model change. NIST’s explanation principles (Phillips et al., 2021) articulate qualities of explanations; they do not specify a retention contract for legally relevant decision episodes under continuous deployment change.

**Temporal scope.** Predominantly contemporaneous with prediction or post-hoc analysis of a fixed model snapshot.

**Engineering scope.** Model- and method-centric (feature attribution, surrogates, counterfactual generators, attention analyses).

**Relation to Decision Knowledge.** An explanation text may become *one component* of Decision Knowledge if captured and bound to a decision. XAI does not define Decision Knowledge as an engineering artifact.

**Relation to Knowledge Continuity.** Weak unless explanations and their supporting context are intentionally retained across change. Generating a new explanation later is not Knowledge Continuity.

#### 3.2 Legal explainability

**Primary objective.** Clarify what legally meaningful reason-giving and “explanation” require of automated decisions, as distinct from technical interpretability (Wachter, Mittelstadt and Russell, 2017; Edwards and Veale, 2017; Selbst and Powles, 2017). In the AI & Law tradition, justification is further tied to legally structured argument rather than prediction alone (e.g. Atkinson and Bench-Capon, 2005; Mumford, Atkinson and Bench-Capon, 2022).

**Problem solved.** Misalignment between ML explainability discourse and legal or regulatory expectations of reasons, contestation and meaningful information.

**What it preserves.** Primarily conceptual and doctrinal requirements—what kinds of reasons or counterfactuals should be available to subjects, decision-makers or ecosystems—not an engineering schema for retention.

**What it does not preserve.** The literature often *assumes* that relevant facts and reasons remain accessible at review time. It under-theorises the engineering disappearance of prompts, retrievals, tools and policy versions described in Section 2.

**Temporal scope.** Oriented to legal processes that unfold after the decision, but typically without an explicit model of technical mutability in LLM/tool-augmented stacks.

**Engineering scope.** Normative and socio-legal; implementation is usually left open.

**Relation to Decision Knowledge.** Legal explainability names *consumers and standards* for reason-giving. Decision Knowledge names the *structured artifact* those consumers need. The present paper treats the former as motivating the latter.

**Relation to Knowledge Continuity.** Legal explainability articulates why continuity matters; it does not, by itself, engineer continuity as a system property.

#### 3.3 Reviewability

**Primary objective.** Make automated decision-making amenable to meaningful review through systematic socio-technical record-keeping across the decision process (Cobbe, Lee and Singh, 2021).

**Problem solved.** Accountability and administrative-law-inspired oversight of ADM where opacity and organisational fragmentation block review.

**What it preserves.** Process-relevant records sufficient for review—policies, roles, interventions, and related organisational documentation—as a reviewability programme.

**What it does not preserve (relative to this paper’s focus).** Reviewability is the strongest adjacent framework. Overlap is real and must not be denied. Differentiation is narrower: Cobbe et al. establish *reviewability* as a socio-technical property of ADM systems and organisations. This paper isolates *Decision Knowledge* as a named engineering artifact and *Knowledge Continuity* as a system property centred on structured preservation under *technical change* characteristic of contemporary AI stacks (prompt overwrite, retrieval drift, tool churn, model swap). The claim is not that reviewability “does not care about records,” but that an engineering layer—what must remain bound to a decision after MLOps-style change so that later legal reasoning remains possible—still needs explicit articulation.

**Temporal scope.** Across the ADM process and subsequent review; organisational time as well as technical time.

**Engineering scope.** Socio-technical: organisational practices plus technical logging/records.

**Relation to Decision Knowledge.** Reviewability records are a major *supplier and consumer* of Decision Knowledge. Decision Knowledge is a more specific artifact type oriented to explain/justify/review/contest functions under the loss modes of Section 2.

**Relation to Knowledge Continuity.** Closely related. Knowledge Continuity can be read as an engineering refinement emphasising persistence of Decision Knowledge across model/tool/prompt change, not as a rival that replaces reviewability.

#### 3.4 Decision provenance

**Primary objective.** Trace how decisions are produced and flow across systems, services and organisational boundaries (Singh, Cobbe and Norval, 2019).

**Problem solved.** Fragmented decision pipelines in which accountability fails because no one can follow how an outcome was assembled across components.

**What it preserves.** Flows, dependencies and provenance relations among decision-relevant events and systems.

**What it does not preserve.** Derivation and flow tracing do not guarantee retention of legal criteria, human rationale, policy constraints, prompt context or review context as a bound package for later contestation. A complete flow graph can coexist with missing justificatory content.

**Temporal scope.** Across distributed processing over time; strong on causal/derivation history.

**Engineering scope.** Cross-system tracing and provenance instrumentation.

**Relation to Decision Knowledge.** Decision provenance is a valuable *substrate* for assembling Decision Knowledge. It is not identical to Decision Knowledge unless extended to capture the component inventory in Section 4.2.

**Relation to Knowledge Continuity.** Supports continuity of *trace*; does not automatically ensure continuity of *decision-time normative and evidential content* under change.

#### 3.5 Provenance models

**Primary objective.** Represent how entities, activities and agents produce data products and other artefacts—canonically in W3C PROV-DM (Moreau and Missier, 2013) and in data-lineage practice. Provenance-based explanation work (Huynh et al., 2021) uses such graphs to support explanatory accounts.

**Problem solved.** Auditability of derivation; reproducibility of data products; accountability for “where did this come from?”

**What it preserves.** Derivation structure: used, wasGeneratedBy, associated agents, and related relations.

**What it does not preserve.** Legal criteria, human rationales, governing policy versions and review context are not entailed by a derivation graph. They can be modelled in PROV only if designers add them; the standard does not make them mandatory for legally relevant AI decisions.

**Temporal scope.** Historical derivation; excellent for past entity versions when recorded.

**Engineering scope.** Metadata and graph infrastructure for lineage.

**Relation to Decision Knowledge.** Necessary but insufficient substrate. Decision Knowledge may *use* PROV-style links among evidence objects; it additionally requires decision-bound justificatory and normative structure.

**Relation to Knowledge Continuity.** Lineage continuity ≠ Knowledge Continuity. A pristine lineage store can still fail Section 2’s reconstruction needs.

#### 3.6 Contestable AI

**Primary objective.** Design systems so that decisions can be challenged, scrutinised and corrected through human and institutional mechanisms (Almada, 2019; Lyons, Velloso and Miller, 2021; Alfrink et al., 2023). Process-centric explanation for contestability (Yurrita, Balayn and Gadiraju, 2023) emphasises process information as input to contestation.

**Problem solved.** Power asymmetry and closed automation that leave subjects without effective means to contest.

**What it preserves.** Design features, interfaces and practices that enable scrutiny—appeals, human review channels, explanatory affordances—when the underlying process information remains available.

**What it does not preserve.** Contestable-AI frameworks specify what contestation *needs* and how to *organise* it. They less often specify the retention contract for prompts, retrievals, tools and policy versions that must still exist when a contest arrives weeks later after a model upgrade.

**Temporal scope.** From decision through contestation windows; depends on retained process materials.

**Engineering scope.** Interaction design, organisational process and explanatory tooling.

**Relation to Decision Knowledge.** Contestability is a primary *consumer* of Decision Knowledge. Without preserved Decision Knowledge, contestability features risk operating on anachronistic system state.

**Relation to Knowledge Continuity.** Complementary: contestability designs the forum and affordances; Knowledge Continuity designs persistence of what the forum must inspect.

#### 3.7 Knowledge Representation

**Primary objective.** Provide structured, often logic-based, representations of situations, events, norms and cases—including temporal formalisms (McCarthy and Hayes, 1969; Kowalski and Sergot, 1986; Allen, 1983) and case-based reasoning (Aamodt and Plaza, 1994), as well as legal ontologies and normative systems in AI & Law.

**Problem solved.** Explicit, manipulable representations for reasoning, explanation of legal structure and knowledge-based decision support.

**What it preserves.** Symbolic knowledge bases, case representations and normative models—when those are the system’s primary artefacts.

**What it does not preserve.** Classical KR rarely specifies *retention contracts* for legally relevant decisions in continuously updated LLM/tool deployments. Hybrid symbolic–ML explanation research (Mumford, Atkinson and Bench-Capon, 2022) advances explaining legal reasoning structure; it does not, by itself, solve lifecycle preservation of decision-time context in production AI stacks.

**Temporal scope.** Strong conceptual tools for time and situations; weak default engineering link to MLOps change.

**Engineering scope.** Representation languages, ontologies and reasoners.

**Relation to Decision Knowledge.** KR supplies motivation and vocabulary for treating Decision Knowledge as a structured artifact (Contribution 2). This paper does not yet offer a formal KR theory of Decision Knowledge (future work).

**Relation to Knowledge Continuity.** Temporal KR motivates why anchoring matters; Knowledge Continuity states the system-property demand under deployment change.

#### 3.8 AI governance frameworks

**Primary objective.** Organise organisational duties for trustworthy AI—principles, risk management, documentation and oversight (OECD, 2019; NIST, 2023). Related documentation artefacts include model cards (Mitchell et al., 2019) and datasheets (Gebru et al., 2021). Regulatory instruments such as Regulation (EU) 2024/1689 impose logging, record-keeping and transparency duties that raise the stakes for retention without fully specifying Decision Knowledge as defined here.

**Problem solved.** Institutional control of AI risk, compliance and accountability at programme level.

**What it preserves.** Policies, risk registers, system documentation, and often operational logs required for compliance.

**What it does not preserve.** Governance checklists and model/system cards describe systems and controls. They are not decision-episode packages binding prompt context, relied-upon evidence, human rationale and policy versions for a single contested outcome. Audit trails preserve *behavioural events*; they do not automatically preserve Decision Knowledge (Section 2).

**Temporal scope.** Programme lifecycle and compliance periods; often misaligned with decision-episode reconstruction after rapid model change.

**Engineering scope.** Process, documentation and control frameworks; variable technical depth.

**Relation to Decision Knowledge.** Governance creates *demand* and sometimes *raw materials* for Decision Knowledge. It does not define the artifact.

**Relation to Knowledge Continuity.** Governance may require continuity-like outcomes; Knowledge Continuity names the engineering property that makes those outcomes feasible for specific decisions.

#### 3.9 Comparative summary

Table 1 compresses the comparison already previewed in Section 1.3. “Supports reconstruction?” is assessed against the Section 2/4 criterion: recovery of decision-time structured knowledge for explain, justify, review and contest after technical change. Entries of “partial” mean the neighbour can contribute substantially when extended or composed, not that it already solves the problem by default.

| Concept | Primary objective | Unit of preservation | Temporal perspective | Engineering focus | Supports reconstruction? | Relation to Decision Knowledge |
|---|---|---|---|---|---|---|
| Explainable AI | Interpret model behaviour | Explanation outputs (often ephemeral) | Prediction / analysis time | Models and XAI methods | Usually no (unless retained & bound) | Possible component, not the artifact |
| Legal explainability | Specify legally meaningful reason-giving | Requirements and doctrines | Post-decision legal process | Normative / socio-legal | Indirect (assumes access) | Motivates the artifact |
| Reviewability | Enable meaningful ADM review | Process records across ADM | Process + review time | Socio-technical records | Partial (strongest neighbour) | Supplier/consumer; broader frame |
| Decision provenance | Trace decision flows across systems | Events and cross-system links | Distributed processing history | Tracing / instrumentation | Partial (flow ≠ justification package) | Substrate for assembly |
| Provenance models (e.g. PROV) | Record derivation of entities | Lineage graphs | Historical derivation | Metadata / lineage infra | Partial (derivation ≠ legal basis) | Substrate; insufficient alone |
| Contestable AI | Enable challenge and scrutiny | Affordances and process features | Decision → contest window | HCI + organisational design | Partial (needs retained materials) | Primary consumer |
| Knowledge Representation | Structure situations, norms, cases | Knowledge bases / formal models | Logical / situational time | Representation & reasoning | Indirect (motivates structure) | Vocabulary for artifact design |
| AI governance frameworks | Manage AI risk and compliance | Policies, docs, programme logs | Programme / compliance lifecycle | Process & documentation | Usually no at decision-episode grain | Creates demand; not the artifact |
| **This paper** | Preserve decision-time knowledge for later legal reasoning | **Decision Knowledge** artifact | Decision time → later review under change | Capture, binding, retention as system property (**Knowledge Continuity**) | **Target capability** | **Defines the artifact and property** |

#### 3.10 What this paper is not

The differentiation can be stated negatively with explicit reasons.

**Not another provenance framework.** Provenance models and decision provenance address derivation and flow. This paper’s object is a decision-bound package for later legal reasoning, including components provenance does not entail (legal criteria, human rationale, policy constraints, review context). Provenance remains a likely implementation substrate (Section 5).

**Not another explainability paper.** XAI and legal explainability address how to generate or demand reasons. This paper addresses whether the information those reasons depend on still exists after ordinary AI-system change. An explanation method cannot recover unretained Decision Knowledge (Section 2.4).

**Not another reviewability framework.** Reviewability (Cobbe et al., 2021) is acknowledged as the closest socio-technical neighbour. The contribution claimed here is narrower and engineering-shaped: naming Decision Knowledge as artifact and Knowledge Continuity as system property under technical mutability. Novelty is not “first to value records.”

**Not another governance checklist.** OECD/NIST-style governance (OECD, 2019; NIST, 2023) and AI Act duties create institutional pressure and documentation obligations. They do not specify the structured decision-episode artifact argued in Sections 4–5. Compliance documentation can coexist with reconstruction failure (Section 2.5).

**Not another audit-logging proposal.** Audit trails preserve operational behaviour. Behavioural completeness does not imply justificatory or normative completeness for a specific decision after prompts, tools and models change.

#### 3.11 Synthesis

Across these programmes, a pattern recurs: each preserves something important—interpretability, legal standards, review records, derivation, contestability affordances, symbolic structure, or governance documentation—yet none, taken as standardly formulated, coincides with Decision Knowledge plus Knowledge Continuity as defined in this paper (Table 1). The constructive task is therefore not to displace these neighbours but to specify the missing engineering layer they implicitly rely on when later legal reasoning must succeed under continuous AI-system change. Sections 4 and 5 develop that layer conceptually.

---

### 4. From State to Decision Knowledge

Section 2 argued that preserving mutable system state is not the same as preserving what later legal reasoning needs; Section 3 and Table 1 showed that neighbouring programmes leave that residue. This section supplies the positive vocabulary. It defines *Decision Knowledge* as an engineering artifact, defines *Knowledge Continuity* as a system property, and relates both to decisions, system state, temporal structure and engineering practice. The definitions follow the manuscript specification; the surrounding exposition is interpretive synthesis for JURIX readers and should not be read as empirical measurement.

#### 4.1 Decision Knowledge: definition

e: definition

**Decision Knowledge** is the structured set of information required to explain, justify, review or contest a specific AI-assisted decision after the decision has been made.

Several constraints are built into this definition. Decision Knowledge is *decision-specific*: it is indexed to an identifiable decision episode, not to the system as a whole. It is *structured*: unstructured transcript dumps may contribute material, but the artifact is the organised set of information and bindings needed for the four functions named in the research question. It is *post-decisional in use*: its primary purpose is future explanation, justification, review and contestation, even though it must be captured at or around decision time. Finally, Decision Knowledge is not identical to a model explanation text, a provenance graph fragment, or an audit log line. Those artefacts may supply parts of Decision Knowledge; none of them is, without further design, the whole.

In knowledge-representation terms, Decision Knowledge is best understood as a designed representational object—an engineering artifact—rather than as residual exhaust of computation. Treating it as an artifact makes retention, binding and lifecycle responsibilities assignable. Treating it only as whatever happens to remain in logs leaves those responsibilities implicit and routinely unmet.

#### 4.2 Components

No claim is made that the following inventory is ontologically complete. It is a working component set derived from the legal functions in the research question (explain, justify, review, contest) and from the loss mechanisms in Section 2. Components may be merged in an implementation if their semantics are preserved; evaluators should ask whether the *information* is recoverable, not whether every label appears as a separate table.

| Component | Role in later legal reasoning |
|---|---|
| Input data | What entered the decision process as base facts or case materials |
| Prompt context | Task framing and instructions that shaped model participation |
| Retrieved evidence | Passages or items retrieved into the decision context |
| Model version | Which model(s) materially participated |
| Tool outputs | Results of tools or services relied on in the episode |
| Policy constraints | Governing constraints and authorisation conditions then applicable |
| Legal criteria | Legal or institutional criteria treated as applicable |
| Human rationale | Reasons recorded for human approvals, overrides or rejections |
| Uncertainty | Scores, thresholds or uncertainty representations that gated the outcome |
| Links between evidence, reasoning and output | Bindings that connect supporting materials to the outcome |

Two distinctions are essential when reading the inventory. First, *available* evidence is not the same as *relied-upon* evidence: retrieval context can be wide while justification depends on a narrower subset. Second, *policy identity* is not the same as *policy version and applicable path*: knowing that “a policy engine ran” does not reconstruct which constraints were in force. Section 2’s failure modes map onto these distinctions: overwritten prompts delete prompt context; index refresh deletes or falsifies retrieved evidence; model updates break model-version binding; approvals without rationale delete human rationale; missing policy constraints delete normative basis; disappearing legal context deletes legal criteria.

#### 4.3 Relationship to decisions and to system state

A *decision*, for this paper, is an identifiable AI-assisted commit to an action, classification, recommendation acceptance, or controlled outcome. Decision Knowledge is the structured informational basis associated with that commit for later legal reasoning. The decision outcome is necessary but not sufficient: an archived final answer without bindings to evidence, constraints and rationale is not Decision Knowledge in the sense defined above.

*System state* is the mutable contents and configuration through which the system presently operates. Relation to Decision Knowledge is asymmetrical:

1. At decision time, Decision Knowledge is *drawn from* elements that may also appear in system state (the then-current prompt, model, evidence, policies).
2. After change, system state and Decision Knowledge *diverge*: state reflects the present; Decision Knowledge must continue to reflect the decision-time situation.
3. Therefore, copying live state into cold storage is not automatically Knowledge Continuity. What must persist is decision-bound structure, including versions and links, not merely a snapshot of whatever is newest.

This contrast is the conceptual core of Contribution 1 and the terminological basis of Contributions 2 and 3.

#### 4.4 Temporal properties

Decision

Knowledge is historically situated. At least three temporal properties follow.

**Decision-time anchoring.** Components must be interpretable relative to the time of the decision (and, where relevant, to business time versus system time). Substituting current policies or models at review time falsifies reconstruction.

**Version persistence.** Where prompts, models, tools, indices or policies are versioned in operation, Decision Knowledge must retain the versions that applied, not only symbolic names such as “production model.”

**Stability under later change.** The artifact must remain intelligible across subsequent system changes and, often, across institutional hand-offs (different reviewers, forums or organisations). Continuity across institutional contexts is part of the definition of Knowledge Continuity below; it is already implicit in the temporal demand that Decision Knowledge survive beyond the originating team’s memory.

These properties connect Decision Knowledge to classical motivations in knowledge representation for temporally situated events and situations. The present paper does not adopt a formal temporal calculus; it insists only that any adequate engineering representation be capable of expressing decision-time binding under change.

#### 4.5 Lifecycle of Decision Knowledge

Decision

Knowledge has a lifecycle distinct from the lifecycle of the model alone:

1. **Formation.** During the decision episode, transient context (prompts, retrievals, tool results, human rationale, applicable constraints) is captured and structured.
2. **Binding.** Captured elements are associated with a stable decision identity and outcome.
3. **Retention.** The bound artifact is stored under retention, access and integrity rules appropriate to the legal and institutional setting.
4. **Use.** Later actors employ the artifact to explain, justify, review or contest.
5. **Evolution of the *system*.** Models, tools and policies may change without rewriting the retained artifact’s decision-time content.
6. **Closure or transfer.** Retention ends, or the artifact is transferred under institutional rules—without silently equating deletion policies with “the decision never needed knowledge.”

Formation and binding are the points at which ordinary AI engineering most often fails: the system optimises for the next deployment, not for the later forum.

#### 4.6 Knowledge Continuity

**Knowledge Continuity** is the ability of an AI system to preserve the decision knowledge necessary for future explanation, accountability, contestation and legal review across time, system changes and institutional contexts.

As used here, Knowledge Continuity is a *system property of legally relevant AI systems concerning Decision Knowledge*. It is not organisational “knowledge continuity” in the knowledge-management sense of staff succession, nor business continuity in the sense of service uptime. Disambiguation matters because the phrase appears in those neighbouring discourses with different referents.

Knowledge Continuity relates to Decision Knowledge as persistence relates to an artifact type: Decision Knowledge names what must be preserved; Knowledge Continuity names the system’s capacity to preserve it under the conditions that Section 2 showed are normal. A system may produce excellent real-time explanations and still lack Knowledge Continuity if those explanations—and their supporting context—are not retained as decision-bound structure.

#### 4.7 Why Knowledge Continuity matters

The importance of Knowledge

Continuity follows directly from the temporal structure of legal and institutional oversight:

- legal review occurs later than the decision;
- accountability requires reconstruction of basis, not only of outcome;
- contestability requires preserved context that can be scrutinised;
- legal justification requires more than the final output;
- explainability, in legally relevant settings, depends on preserved knowledge rather than only on the possibility of generating a new model commentary at review time.

These points are design motivations, not doctrinal conclusions about any one statute. They state conditions under which the legal functions named in the research question remain *possible* as epistemic tasks for human institutions.

#### 4.8 Engineering implications

If Decision Knowledge is an engineering artifact and Knowledge

Continuity a system property, several engineering implications follow before any particular architecture is chosen.

First, preservation must be *intentional*: Decision Knowledge should be a designed output of the decision path, not an accidental residue. Second, capture must target *transient* context at the moment it exists. Third, *bindings* among components and the decision identity are part of the artifact, not optional metadata. Fourth, retention must be planned jointly with privacy, proportionality and purpose limitation—Knowledge Continuity is not a licence for unbounded surveillance archives (Section 6). Fifth, evaluation of legally relevant AI systems should ask not only whether explanations can be generated, but whether Decision Knowledge for past decisions remains reconstructable after change.

Section 5 turns these implications into a conceptual framework of principles and concepts for engineering Knowledge Continuity across the AI lifecycle.

---

### 5. Engineering Knowledge Continuity

This section describes, at a conceptual level, how legally relevant AI systems could preserve Decision Knowledge so that Knowledge Continuity becomes an engineered property rather than an accidental one. The framework is a design sketch (Contribution 4). It does not present an implemented architecture, a formal ontology, or an empirical evaluation; those are future work. Conceptual vocabulary is introduced to make preservation responsibilities discussable in AI & Law terms, not to prescribe a product stack.

#### 5.1 Design stance

Three stances follow from

Sections 2 and 4.

1. **Preservation is a first-class design concern.** If Decision Knowledge is required after change, capture and binding must be designed before deployment, not added only when a dispute arrives.
2. **Logging is not the framework.** Operational logs, provenance graphs and policy decision records may serve as *substrates*. Knowledge Continuity additionally requires that the substrates be sufficient, bound to a decision identity, and retained for the legal functions at issue.
3. **Composition is allowed; substitution is not assumed.** Existing mechanisms may jointly realise parts of Decision Knowledge. The framework asks whether the composed whole meets the preservation need, not whether a single new store replaces all prior tooling.

#### 5.2 Architecture as conceptual layering

Architecturally, the proposal isa

*logical* layering over AI systems that already perform inference, retrieval, tool use, policy checks and human gating:

- **Decision path (existing).** The operational flow that produces an AI-assisted decision.
- **Capture points.** Interfaces at which transient context is recorded (prompt instantiation, retrieval results, tool returns, policy evaluation, human gate, outcome emission).
- **Decision Knowledge artifact.** The bound structured object (or equivalent structured collection) that constitutes Decision Knowledge for that decision.
- **Continuity services.** Retention, integrity, access control, and retrieval for later explanation, review, contestation and justification.
- **Change plane (existing).** Model, index, tool and policy updates that must *not* silently rewrite retained Decision Knowledge.

This layering is deliberately non-proprietary. It can be realised through extensions to existing platforms, through organisational record systems integrated with AI services, or through specialised stores—provided the information and bindings of Section 4 are preserved. Figure 3 (planned) will summarise the conceptual model; Figure 2 (planned) will show continuity across lifecycle stages.

#### 5.3 Principles

The specification’s principles are restated here as design requirements for Knowledge Continuity.

| Principle | Engineering meaning |
|---|---|
| Preserve Decision Knowledge as a persistent engineering artifact | Treat the Section 4 object as a designed, retainable artifact with identity and lifecycle |
| Capture transient context | Record prompts, retrievals, tool outputs, rationales and related ephemeral inputs while they exist |
| Connect evidence to decisions | Maintain explicit links from relied-upon evidence (and relevant exclusions, where required) to the decision outcome |
| Preserve reviewability | Ensure retained structure supports meaningful later review, not only operational replay |
| Record rationale for approvals | Persist human gate reasons, not only allow/deny events |
| Preserve governance constraints | Retain applicable policy/legal constraints and their decision-time versions |
| Design preservation before deployment | Allocate capture, binding and retention in system design, not solely in post-incident practice |

These principles are jointly aimed at the four functions in the research question. A deployment may satisfy observability metrics while violating several principles at once—for example, by logging tool calls without retaining versioned tool outputs bound to the decision.

#### 5.4 Conceptual vocabulary

The following concepts are a shared vocabulary for discussing implementations. They are not an ontology commitment and may be reduced if page limits require.

- **Decision object.** The identifiable unit representing the decision episode and its outcome, to which other elements bind.
- **Evidence object.** Structured representation of inputs, retrieved items, tool outputs or other materials entering the evidential field; distinguishable, where needed, from the subset relied upon.
- **Knowledge dependency.** An explicit link expressing that an element (evidence, policy, model version, rationale) supported or constrained the decision object.
- **Review context.** Information retained to make later review intelligible (forum-relevant identifiers, procedural posture, pointers to legal criteria), without pretending to store an entire legal file.
- **Governance primitive.** A retained representation of authorisation or constraint evaluation applicable at decision time (for example, policy identity, version and result).
- **Lifecycle model.** The stages through which Decision Knowledge is formed, bound, retained, used and closed (Section 4.5).
- **Audit chain.** An integrity-preserving sequence or attestation path over retained artifacts, where the institutional setting requires tamper-evident history. Integrity supports trustworthy reconstruction; it does not by itself supply missing justificatory content.
- **Decision knowledge graph.** An optional graph-shaped organisation of decision objects, evidence objects and dependencies. Useful where relations are many; not mandatory if equivalent structure is expressed otherwise.

Closest neighbours in the literature—reviewability frameworks, decision provenance, contestable-AI design features, and PROV-style derivation records—supply practices and substrates that can realise parts of this vocabulary. The present framework’s distinctive demand is that the vocabulary be satisfied *as preserved Decision Knowledge under technical change*, for later legal reasoning about a specific decision.

#### 5.5 Preservation mechanisms

At the mechanism level, Knowledge

Continuity requires three complementary operations.

**Capture.** At defined points in the decision path, write Decision Knowledge components from transient state into durable structured form. Capture policies should state what is mandatory for a given class of legally relevant decision, mindful of proportionality.

**Binding.** Associate captured elements with the decision object and with decision-time version anchors. Binding fails when materials exist only in unbound global stores (“current prompt repository”) without decision identity.

**Retention and disclosure control.** Keep the bound artifact available for authorised later use under retention schedules, access rules and redaction regimes. Knowledge Continuity without access control is operationally incomplete; Knowledge Continuity without retention limits is legally and ethically incomplete.

Replay, bit-exact model reproducibility and post-hoc explanation generation may assist some investigations. They are not the primary preservation mechanisms for Decision Knowledge: replay can restore computational paths without restoring normative basis; reproducibility may be impossible after model retirement; post-hoc explanation cannot recreate unretained context.

#### 5.6 Reconstruction process

Reconstruction is the later use of retained Decision

Knowledge to support explanation, justification, review or contestation. Conceptually:

1. Identify the decision object.
2. Retrieve the bound Decision Knowledge artifact.
3. Read outcome, decision-time anchors and components.
4. Separate decision-time content from current system state.
5. Produce the account required by the forum (technical, administrative or legal), without silently substituting live configuration for retained structure.

Faithful reconstruction, in this conceptual sense, fails when required components or bindings are missing, when only current state is available, or when the reconstructor must rely on undocumented personal memory. As Section 3 and Table 1 showed, XAI, provenance and audit trails do not, by default, prevent those failures. Section 6 relates successful reconstruction conditions to legal and governance functions.

#### 5.7 Evolution over time

I systems evolve continuously. Knowledge Continuity requires that evolution of the *system* not entail silent evolution of *past Decision Knowledge*. Practically:

- model, index, tool and policy updates create new decision-time contexts for *future* decisions;
- retained artifacts for *past* decisions remain anchored to their original versions and bindings;
- migrations of storage or format must preserve semantics of components and links;
- institutional transfers (vendor change, agency hand-off) must export Decision Knowledge as structure, not only as opaque operational images.

Figure 2 (planned) is intended to show this continuity thread across lifecycle stages and break points corresponding to Section 2’s loss mechanisms.

#### 5.8 Integration with existing AI systems

Integration should prefer extension points over green

-field replacement:

- observability pipelines can emit candidates for capture, but schemas must be enriched for Decision Knowledge components and bindings;
- model registries can supply model-version identifiers to be bound into the decision object;
- policy engines can contribute governance primitives if decision logs include policy version and applicable path, not only allow/deny;
- provenance systems can contribute derivation substrate for evidence and data products;
- human-workflow tools can capture rationale at approval gates;
- case-management or records systems can provide retention and access control aligned with institutional review.

The integration test is functional: after realistic change (prompt, retrieval, tool, model, policy), can authorised reviewers still reconstruct Decision Knowledge for a past decision? If not, Knowledge Continuity is absent regardless of how many adjacent tools are deployed.

#### 5.9 Scope of the claim

This section claims only that legally relevant AI systems

*can be designed* so that Decision Knowledge is preserved as an engineered artifact and Knowledge Continuity becomes an explicit system property. It does not claim that one graph database, one audit vendor, or one governance product is required. It does not claim that preservation alone makes decisions lawful or correct. It supplies conditions under which later legal reasoning remains epistemically possible. Section 6 develops the corresponding implications for AI & Law without treating the framework as a compliance certificate.

*[Figures 2–4 — planned; assets not yet created.]*

---

### 6. Implications for AI and Law

Sections 2–5 argued that legally relevant AI systems need an engineered capacity to preserve Decision Knowledge under change. This section draws implications. The central claim is modest and cumulative: explainability is not only a model property; it also depends on whether the system preserved the knowledge necessary for future legal reasoning. The same dependence holds, with different institutional textures, for review, contestation, accountability and evidentiary reconstruction.

#### 6.1 Engineering implications

If Decision Knowledge is treated as a first-class engineering artifact, several practice shifts follow from

Sections 4–5.

**Design-time allocation.** Capture points, bindings and retention rules become design deliverables alongside model quality and latency. Preservation is scheduled before deployment, not improvised after a dispute.

**Schemas beyond observability.** Telemetry that records that a tool was called is insufficient unless versioned tool outputs, relied-upon evidence, prompt context and policy versions can be bound to a decision object. Model registries, policy engines, provenance stores and workflow tools remain valuable, but as substrates that must jointly satisfy Decision Knowledge components (Table 1; Section 5.8).

**Change management.** Model, index, tool and policy updates are treated as events that create new decision-time contexts for *future* decisions without rewriting retained artifacts for *past* decisions. Release engineering gains an explicit non-goal: do not silently invalidate reconstructability.

**Evaluation.** Acceptance tests for legally relevant systems include a reconstruction probe: after realistic change, can authorised reviewers recover Decision Knowledge for sampled past decisions? Passing XAI demos or dashboard reviews does not substitute for that probe.

**Proportionality by design.** Because retention has privacy and cost implications, engineering must classify which decisions require which Decision Knowledge components, rather than archiving all context indiscriminately. Knowledge Continuity is a capacity, not a mandate to retain everything forever.

None of these shifts requires a single vendor stack. They require that preservation responsibilities be assignable—the point of treating Decision Knowledge as an artifact.

#### 6.2 Legal and governance implications

Knowledge

Continuity complements existing governance approaches. It does not replace reviewability programmes, contestability design, accountability frameworks or compliance documentation. Those programmes name duties, forums and affordances; Decision Knowledge names structured material those forums often need after technical change (Section 3; Table 1).

For **legal explainability**, the implication is conditional: reason-giving standards can be met in practice only if decision-time inputs, constraints and rationales remain available. Technical XAI methods remain useful for understanding models; they do not discharge the preservation condition.

For **reviewability**, Knowledge Continuity supplies an engineering refinement focused on MLOps-style mutability. Organisations pursuing reviewable ADM still need socio-technical records; this paper argues they also need decision-bound Decision Knowledge that survives prompt, retrieval, tool and model change.

For **contestability**, affordances for challenge presuppose inspectable materials. Without Knowledge Continuity, contestation interfaces risk presenting current system behaviour as if it were the historical basis of the contested decision.

For **accountability** and **institutional responsibility**, forums can demand answers only if reconstructable bases exist (Wieringa, 2020). State dumps and current policy text are weak answers when the decision pre-dates the dump.

For **evidentiary reconstruction**, lineage and logs may establish that processing occurred; Decision Knowledge aims at the normative and evidential basis of the outcome. The paper does not claim that retained Decision Knowledge is always admissible evidence in any jurisdiction—only that without some such structure, reconstruction is epistemically impoverished.

Governance checklists and risk registers remain necessary for programme control. They are not substitutes for decision-episode artifacts.

#### 6.3 Relationship to the EU AI Act

Regulation (EU) 2024/1689 imposes, among other things, logging, record-keeping and transparency-related duties for certain AI systems, and has prompted debate on explanation rights (including discussions around Article 86 in the emerging commentary). This paper does **not** claim that the AI Act expressly requires “Decision Knowledge” or “Knowledge Continuity” as defined here. Those terms are analytical constructs of this manuscript, not statutory terms.

The relationship claimed is instrumental and cautious. Where the Act (or similar regimes) requires durable records, logging or information that supports oversight and explanation, organisations still face an engineering design choice: retain unbound operational state and generic logs, or retain decision-bound structured knowledge adequate for later review. The framework in Sections 4–5 is offered as a way to strengthen long-term *reviewability and reconstructability* in systems that must already satisfy record-keeping pressure. Whether a particular retention design meets a particular legal obligation is a compliance determination outside the scope of this conceptual paper.

In short: the AI Act raises the stakes for preservation; it does not by itself specify the Decision Knowledge artifact argued here.

#### 6.4 Bridge to discussion

Section 6 has stated implications under the assumption that the conceptual argument of

Sections 2–5 is accepted. Open questions of maturity, alternative framings, institutional adoption and staged validation are taken up in Section 7, which also separates conceptual, engineering, empirical and legal next steps. Section 8 then answers the research question directly.

---

### 7. Discussion

The preceding sections stated a problem, differentiated neighbours, defined terms, proposed a conceptual preservation framework and drew implications. This section situates that argument without enlarging it into a paradigm claim, and states strengths, limitations and realistic next steps.

#### 7.1 Positioning in AI & Law and in engineering practice

Within AI & Law, the paper sits at the junction of legal explainability, reviewability, contestability, provenance and knowledge representation (Table 1). It does not displace those programmes. It argues that they share an often implicit dependence on decision-time information remaining available after ordinary AI-system change, and that this dependence should be named and engineered as Decision Knowledge under a system property of Knowledge Continuity.

Relative to JURIX concerns with justification and structured legal reasoning, the contribution is infrastructural rather than doctrinal: it asks what must be retained so that later legal reasoning about a *deployed* AI-assisted decision remains possible. Relative to hybrid symbolic–ML explanation research, it shifts attention from explaining legal structure in a reasoning system to preserving decision-time context in continuously updated production stacks.

Relative to engineering practice, the framework is intentionally compositional. It assumes MLOps, observability, model registries, policy engines, provenance tooling and records systems already exist, and asks how they must be bound and retained to support later reconstruction (Section 5.8). The proposal is therefore closer to a missing design concern—or engineering layer in the narrow sense of assignable preservation responsibility—than to a call to replace current platforms. Readers seeking a new socio-technical paradigm will not find one; readers seeking a sharper artifact for long-lived, legally relevant AI systems may.

#### 7.2 Strengths

Four features of the argument are offered as its main scientific value.

**Conceptual clarity.** Distinguishing system state from Decision Knowledge makes a common operational confusion discussable. Many deployments are rich in live configuration and poor in decision-bound structure; the vocabulary makes that diagnosis precise enough to evaluate (Sections 2 and 4).

**Engineering perspective.** By treating Decision Knowledge as an artifact with capture, binding and retention responsibilities, the paper converts a governance aspiration into design questions that release engineering and records management can own (Sections 4–5).

**Temporal perspective.** Knowledge Continuity centres time and change—prompt overwrite, retrieval drift, tool churn, model swap, policy bump—as first-class threats, not as edge cases. That matches how contemporary AI systems are actually operated.

**Integration with existing approaches.** Table 1 frames neighbours as complements and substrates. The framework can absorb provenance links, policy decision logs, reviewability records and contestability affordances without requiring that any one of them already be sufficient.

These strengths are conceptual. They do not establish empirical superiority.

#### 7.3 Limitations

Several limitations should constrain how the paper is cited.

**Conceptual nature.** The work offers definitions, a working inventory, principles and a logical layering. It provides neither formal semantics nor a reference implementation.

**Absence of empirical evaluation.** No reconstruction probe has been executed on a real deployment; no user study with auditors, reviewers or decision subjects is reported. Claims about practical difficulty are reasoned from engineering mechanisms (Section 2), not measured failure rates.

**Preliminary artifact inventory.** The component list in Section 4.2 is derived from the research question’s legal functions and from observed loss modes. Alternative inventories—narrower minimal cores, or broader evidentiary packages—are possible. The list should not be read as a standard.

**Alternative conceptualisations.** One may argue that an enriched reviewability programme, an extended decision-provenance profile, or a carefully composed PROV-plus-policy-log schema already answers the research question without new terms. The paper’s reply is comparative (Section 3), not experimental: as standardly formulated, those neighbours do not coincide with Decision Knowledge plus Knowledge Continuity. Composition may close much of the gap in practice; that is an empirical question left open.

**Restricted scope.** The analysis targets legally relevant AI-supported decisions for which later explanation, justification, review or contestation is institutionally plausible. It does not address all AI products, all logging problems, or all organisational knowledge-management issues.

**Trade-offs not solved.** Over-documentation, storage cost, privacy, data minimisation, purpose limitation and access control are acknowledged (Sections 5–6) but not given a complete governance design. Knowledge Continuity can conflict with retention limits; proportionality is required, not optional. Institutional adoption faces incentives that favour shipping model improvements over investing in reconstructability.

**Limits of reconstruction.** Even with preservation, reconstruction can fail: capture may be incomplete; rationales may be thin or contested; redaction may remove needed material; forums may disagree on what “relied upon” meant. Preserving Decision Knowledge is a necessary condition for many later legal-reasoning tasks, not a sufficient condition for correct, lawful or fair decisions.

#### 7.4 Future work

Next steps should be staged and modest.

**Conceptual research.** Formalise Decision Knowledge (temporal binding, identity, minimal versus extended component sets) and relate it explicitly to PROV and to reviewability record types. Clarify success criteria for “faithful reconstruction” relative to different forums (engineering audit, administrative review, contestation).

**Engineering implementation.** Build reference compositions—observability plus policy logs plus records systems—implementing capture, binding and retention without a green-field platform. Publish schemas and failure-injection tests for prompt, retrieval, tool, model and policy change.

**Empirical validation.** Apply the reconstruction probe of Section 5.8 to sampled decisions before and after realistic change. Compare compositions against unaugmented logging baselines. Include qualitative study of what reviewers actually need.

**Legal evaluation.** Map Decision Knowledge components to concrete review and appeal procedures in chosen domains. Assess interaction with data-protection retention rules. Keep the AI Act (and similar regimes) as a stress-test for record-keeping pressure, not as a claim that the statute already defines Decision Knowledge (Section 6.3).

Until such work exists, Knowledge Continuity should be treated as a proposed system property and research programme, not as a mature standard.

---

### 8. Conclusion

This paper asked how AI systems should preserve decision knowledge so that legally relevant decisions remain explainable, reviewable, contestable and justifiable over time.

The answer developed here is conceptual. Systems should treat *Decision Knowledge*—the structured, decision-bound information required for those four functions—as an engineering artifact, and should engineer *Knowledge Continuity* as the system property of preserving that artifact across time, technical change and institutional contexts. Ordinary AI delivery preserves mutable *system state*; legal and governance forums need decision-time basis. Neighbouring approaches in explainability, reviewability, provenance and governance address important adjacent problems but, as standardly formulated, do not coincide with that artifact and property (Table 1). A compositional framework of capture, binding and retention can extend existing stacks without replacing them (Section 5).

The contribution is accordingly narrow: a problem diagnosis under technical mutability; definitions and a working inventory; a system-property framing; a conceptual preservation framework; and implications that treat explainability and related legal functions as dependent on preserved decision-time knowledge, not only on model-centric methods. The paper does not claim empirical proof, statutory identity with the AI Act, or a paradigm shift in AI & Law.

Future research should formalise the artifact, implement and test compositional retention under change, and evaluate legal adequacy in concrete institutional settings. The forward-looking stake is practical: as legally relevant AI systems become longer-lived and more frequently updated, institutions will need reconstructable decision-time knowledge—or will discover, too late, that they retained only the present.

---

### Planned figures (from specification)

- Figure 1 – System State vs Decision Knowledge

- Figure 2 – Knowledge Continuity across the AI lifecycle
- Figure 3 – Conceptual model of decision knowledge preservation
- Figure 4 – Relationship between decision, evidence, rationale, policy constraints and review context

*[Figure assets not yet created; see `figures/`.]*

---

### Assumptions (internal drafting notes; remove before camera-ready)

The drafted sections rely on the following assumptions. They are not empirical findings.

1. **Scope assumption.** The analysis concerns *legally relevant* AI-assisted decisions—those for which later explanation, justification, review or contestation is institutionally plausible—not all AI products.
2. **Temporal-review assumption.** Material review often occurs after technical change (prompts, retrieval, tools, models, policies). Where review is always contemporaneous with an immutable system, some loss mechanisms weaken.
3. **Working inventory assumption.** The Decision Knowledge component list is a working inventory derived from the research question’s legal functions and from Section 2 loss modes; it is not a final ontology.
4. **Neighbour-complement assumption.** Section 3 treats reviewability, decision provenance, contestable-AI design, PROV/lineage, XAI, KR and governance as complementary neighbours that do not, as standardly formulated, coincide with Decision Knowledge plus Knowledge Continuity; compositions may narrow the gap without erasing the conceptual distinction.
5. **Non-evaluation assumption.** Sections 1–8 are conceptual; no implementation or user study is claimed. Contribution language is correspondingly modest.
6. **Citation status.** In-text citations and the References list below are compiled from `planning/literature-map.md` and the shared workspace BibTeX (`references/bib/library.bib`). Regulatory reference: Regulation (EU) 2024/1689 is cited as primary law for governance pressure, not as proof that the Act requires Decision Knowledge.
7. **Contribution mapping.** C1↔§2; C2–C3↔§4; C4↔§5; C5↔§6. No contribution beyond the specification list is claimed.

---

### References

Aamodt, A. and Plaza, E. (1994). Case-Based Reasoning: Foundational Issues, Methodological Variations, and System Approaches. *AI Communications* 7(1): 39–59. doi:10.3233/AIC-1994-7104.

Alfrink, K., Keller, I., Kortuem, G. and Doorn, N. (2023). Contestable AI by Design: Towards a Framework. *Minds and Machines* 33(4): 613–639. doi:10.1007/s11023-022-09611-z. (First published online 2022.)

Allen, J. F. (1983). Maintaining Knowledge about Temporal Intervals. *Communications of the ACM* 26(11): 832–843. doi:10.1145/182.358434.

Almada, M. (2019). Human Intervention in Automated Decision-Making: Toward the Construction of Contestable Systems. In *Proceedings of the Seventeenth International Conference on Artificial Intelligence and Law (ICAIL ’19)*, pp. 2–11. ACM. doi:10.1145/3322640.3326699.

Atkinson, K. and Bench-Capon, T. (2005). Legal Case-Based Reasoning as Practical Reasoning. *Artificial Intelligence and Law* 13(1): 93–131. doi:10.1007/s10506-006-9003-3.

Cobbe, J., Lee, M. S. A. and Singh, J. (2021). Reviewable Automated Decision-Making: A Framework for Accountable Algorithmic Systems. In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’21)*, pp. 598–609. ACM. doi:10.1145/3442188.3445921.

Doshi-Velez, F. and Kim, B. (2017). Towards a Rigorous Science of Interpretable Machine Learning. arXiv:1702.08608.

Edwards, L. and Veale, M. (2017). Slave to the Algorithm? Why a ‘Right to an Explanation’ Is Probably Not the Remedy You Are Looking For. *Duke Law & Technology Review* 16(1): 18–84.

European Parliament and Council of the European Union (2024). Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). *Official Journal of the European Union* L 2024/1689. <https://eur-lex.europa.eu/eli/reg/2024/1689/oj.>

Gebru, T., Morgenstern, J., Vecchione, B., Wortman Vaughan, J., Wallach, H., Daumé III, H. and Crawford, K. (2021). Datasheets for Datasets. *Communications of the ACM* 64(12): 86–92. doi:10.1145/3458723.

Guidotti, R., Monreale, A., Ruggieri, S., Turini, F., Giannotti, F. and Pedreschi, D. (2018). A Survey of Methods for Explaining Black Box Models. *ACM Computing Surveys* 51(5): 93:1–93:42. doi:10.1145/3236009.

Huynh, T. D., Tsakalakis, N., Helal, A., Stalla-Bourdillon, S. and Moreau, L. (2021). Addressing Regulatory Requirements on Explanations for Automated Decisions with Provenance—A Case Study. *Digital Government: Research and Practice* 2(2): 1–14. doi:10.1145/3436897.

Kowalski, R. and Sergot, M. (1986). A Logic-based Calculus of Events. *New Generation Computing* 4(1): 67–95. doi:10.1007/BF03037383.

Lipton, Z. C. (2018). The Mythos of Model Interpretability. *Communications of the ACM* 61(10): 36–43. doi:10.1145/3233231.

Lyons, H., Velloso, E. and Miller, T. (2021). Conceptualising Contestability: Perspectives on Contesting Algorithmic Decisions. *Proceedings of the ACM on Human-Computer Interaction* 5(CSCW1): 106:1–106:25. doi:10.1145/3449180.

McCarthy, J. and Hayes, P. J. (1969). Some Philosophical Problems from the Standpoint of Artificial Intelligence. In Meltzer, B. and Michie, D. (eds), *Machine Intelligence 4*, pp. 463–502. Edinburgh University Press.

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D. and Gebru, T. (2019). Model Cards for Model Reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* ’19)*. ACM. doi:10.1145/3287560.3287596.

Moreau, L. and Missier, P. (eds) (2013). *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. <https://www.w3.org/TR/2013/REC-prov-dm-20130430/.>

Mumford, J., Atkinson, K. and Bench-Capon, T. (2022). Reasoning with Legal Cases: A Hybrid ADF-ML Approach. In *Legal Knowledge and Information Systems: JURIX 2022* (FAIA 362), pp. 93–102. IOS Press. doi:10.3233/FAIA220452.

National Institute of Standards and Technology (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. doi:10.6028/NIST.AI.100-1. (Cited in text as NIST, 2023.)

OECD (2019). Recommendation of the Council on Artificial Intelligence. OECD/LEGAL/0449. <https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449.>

Phillips, P. J., Hahn, C. A., Fontana, P. C., Yates, A. N., Greene, K., Broniatowski, D. A. and Przybocki, M. A. (2021). *Four Principles of Explainable Artificial Intelligence*. NISTIR 8312. doi:10.6028/NIST.IR.8312.

Selbst, A. D. and Powles, J. (2017). Meaningful Information and the Right to Explanation. *International Data Privacy Law* 7(4): 233–242. doi:10.1093/idpl/ipx022.

Singh, J., Cobbe, J. and Norval, C. (2019). Decision Provenance: Harnessing Data Flow for Accountable Systems. *IEEE Access* 7: 6562–6574. doi:10.1109/ACCESS.2018.2887201.

Wachter, S., Mittelstadt, B. and Russell, C. (2017). Counterfactual Explanations Without Opening the Black Box: Automated Decisions and the GDPR. *Harvard Journal of Law & Technology* 31(2): 841–887 (journal issue 2018; widely cited as 2017).

Wieringa, M. (2020). What to Account for When Accounting for Algorithms: A Systematic Literature Review on Algorithmic Accountability. In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (FAT* ’20)*, pp. 1–18. ACM. doi:10.1145/3351095.3372833.

Yurrita, M., Balayn, A. and Gadiraju, U. (2023). Generating Process-Centric Explanations to Enable Contestability in Algorithmic Decision-Making: Challenges and Opportunities. arXiv:2305.00739.

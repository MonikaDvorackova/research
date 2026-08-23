---
id: source-missing-layer-in-ai-stack
title: "SOURCE A — The Missing Layer in the AI Stack (verbatim)"
topic: ai-understanding-layer
type: literature
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [source-material, verbatim, capability-vs-understanding, primary-source]
source_kind: primary-verbatim
---

> **Verbatim capture — do not edit, correct, or reword.**
> This file preserves Source A exactly as supplied by the author, including any
> typographical irregularities and the embedded Czech-language working notes
> that appear near the end of the original text. It is historical source
> material for the `ai-understanding-layer` topic, not a polished draft.
> Analysis lives in `../notes/`.

---

## SOURCE A — Missing Layer / Capability vs Understanding

# The Missing Layer in the AI Stack: Why Capability Is Advancing Faster Than Understanding

### 1. The Success of Modern Artificial Intelligence

The artificial intelligence industry has become exceptionally good at measuring capability.

We measure benchmark performance, inference quality, reasoning accuracy, code generation, agent execution, retrieval effectiveness, tool orchestration, workflow completion, latency, cost, and increasingly complex evaluation pipelines. Whether in research labs or production engineering, success is increasingly defined by a single question: *What can these systems do?*

This focus has produced extraordinary progress. Models now solve problems that seemed out of reach only a few years ago. Agents can reason across multiple steps, coordinate specialized tools, interact with external systems, and execute increasingly complex workflows with minimal human intervention. Yet our definition of progress has become increasingly one-dimensional. We have become exceptionally good at measuring what artificial intelligence systems can accomplish. We have become far less systematic at measuring what we continue to understand about how those accomplishments emerge. Capability has become one of the most carefully measured properties in modern engineering. However the information required to reconstruct why a system behaved as it did is often treated as a secondary concern.

Capability is becoming easier to demonstrate, it has almost become a routine. It is less obvious that decisions are becoming easier to explain. Preserving the information needed to explain consequential decisions has not. When a decision is questioned months later, the relevant context may already be gone: prompts have changed, retrieval sources have evolved, policies have been updated, and the original justification may no longer be reconstructable. This is often discussed as auditability. I think the underlying issue is broader.

---

### 2. The Hidden Pattern in Software Engineering

Software engineering has a recurring habit. Whenever systems become too complex to understand directly, new abstractions emerge to preserve what would otherwise be lost. Many of the technologies that define modern software engineering were introduced to solve immediate engineering problems. Version control enabled collaborative software development. Transaction logs improved database reliability. Distributed tracing simplified debugging across microservices. Observability platforms improved production operations.

Over time, however, they acquired another role. Each preserves information that cannot be recovered reliably from the current state of a system alone.

A Git repository contains not only the latest version of the code, but the sequence of changes that produced it. A transaction log records not only the current database state, but the operations that led to that state. A distributed trace captures not only the outcome of a request, but the path it followed across services. Observability systems retain execution data long after the process itself has finished.

These mechanisms differ in purpose and implementation, but they share an architectural property: they preserve information that would otherwise disappear during system evolution or execution.

As software systems became larger, more distributed, and more dynamic, reconstructing the past became an engineering capability in its own right.

Without that preservation, systems eventually become impossible to debug, operate, modify, or trust. Software engineering has repeatedly responded to increasing complexity by creating new mechanisms for preserving the information required to understand systems later. This pattern appears throughout the history of the discipline.

---

### 3. Artificial Intelligence Field May Be Breaking the Pattern

Modern artificial intelligence frameworks expose native abstractions for almost every aspect of intelligent execution. Models encapsulate inference. Retrieval systems expose external information. Memory extends interaction beyond a single session. Planning framworks decompose objectives into executable steps. Agent runtimes coordinate tools, workflows, and external services.

These abstractions have transformed what artificial systems can accomplish. They have not evolved equally sophisticated abstractions for explaining why consequential decisions were considered justified. A modern artificial intelligence system can often report which model produced an output, which tools were invoked, which documents were retrieved, and even which intermediate reasoning steps were executed. Far fewer systems can answer a different class of questions. What evidence ultimately justified the decisions? Which assumptions did that justification depend on? Would the same decision still be considered valid after the underlying policies, retrieval corpus, or execution environment have changed?

*This is not simply a missing feature.* It reflects an architectural asymmetry. The modern AI stack contains mature abstractions for producing behaviour. It contains comparatively few abstractions whose primary purpose is to preserve the decision context needed to reconstruct, investigate, or challenge that behaviour later.

5. State Is Not Knowledge

Traditional software systems implicitly rely on an important assumption. Although the current state of a system rarely explains how that state was reached, the missing information can usually be reconstructed from other engineering artifacts. Version history, transaction logs, execution traces, audit records, and operational telemetry together provide a historical account of how the system evolved.

Artificial intelligence systems increasingly violate that assumption.

The information required to explain a consequential decision may never become part of the system's persistent state. It may depend on a prompt that was overwritten, a retrieval result that has since changed, an external tool that now behaves differently, a model that has been updated, or a human approval whose rationale was never recorded.

In these cases, the problem is not that information has been lost from the current system state. The problem is that the information required to reconstruct the decision was never treated as a persistent engineering artifact in the first place.

This changes the relationship between state and knowledge.

For many artificial intelligence systems, the current state is no longer sufficient to support future explanation, investigation, or justification. Those activities increasingly depend on information that was transient by design.

This is why the problem is merely optional. It is rather epistemological.

Consider a production AI system six months after an important deployment decision. An auditor asks why the system was allowed to perform a particular action. The deployment record still exists. The model, however, has since been updated. The retrieval corpus has changed. The prompt template has been modified several times. An external policy service now returns different guidance. The approval remains recorded, but the reasoning behind it does not. Nothing has failed. The system simply never treated that decision context as something that needed to be preserved.

This is where AI systems differ from many traditional software systems. The difficulty is not recovering the current state. The difficulty is reconstructing the conditions under which the original decision was considered valid.Once that information has disappeared, the remaining system state is no longer sufficient to explain, investigate, or justify the decision.

6. The Missing Layer

The modern artificial intelligence stack provides abstractions for building intelligent behavior. Models perform inference. Retrieval systems provide external context. Agent runtimes coordinate execution. Memory extends interaction across sessions. Workflow engines orchestrate increasingly complex tasks.

What it does not provide is an equivalent abstraction for the lifecycle of decision. Once a consequential decision has been made, the engineering support for preserving its justification, supporting evidence, applicable policies, delegated authority, and decision context is often fragmented across independent systems or missing entirely. This is the architectural gap.

The missing layer is not another inference engine or orchestration framework. It is a layer that treats decision provenance as a first-class engineering concern rather than an afterthought assembled from logs, prompts, databases, and human memory.

Such a layer would not replace governance.

It would provide the architectural primitives on which governance, auditability, and operational trust could be built.

7. AIGov Core as an Architectural Experiment

These observations did not originate as a theoretical exercise. They emerged while designing AIGov Core, originally conceived as an AI governance and auditability runtime.

A recurring engineering problem quickly became apparent.

Determining whether a deployment had been justified at the time it was made was often far more difficult than determining whether the decision complied with current policies. The necessary information was scattered across deployment records, evaluation results, prompts, external polic documents, approval workflows, and operational logs. In many cases, parts of that context had already changed or disappeared.

This shifted the design objective.

Instead of treating governance as a reporting problem, AIGov Core treats governance decisions themselves as engineering artifacts. The objective is to preserve not only the outcome of a decision, but also the evidence, authority, policy context, and assumptions that made the decision valid when it was taken.

Whether this approach represents the right abstraction remains an open question.

More importantly, it suggests that preserving decision context may deserve to become a first-class concern of AI system architecture rather than a collection of artifacts reconstructed after the fact.

8. The Next Decade of AI Engineering

The last decade of AI was defined by a single question:

What can these systems do?

The next decade may be defined by a different one.

What information must be preserved so that we continue to know what they are doing?

If previous generations of software engineering were shaped by mechanisms that preserved knowledge about code, state, and execution, future AI engineering may require mechanisms that preserve knowledge about decisions.

The challenge is not merely building intelligent systems.

It is ensuring that intelligence does not outpace understanding.

## Why capability is advancing faster than understanding

Most discussions of progress in AI focus on capability. This is understandable. Capability is relatively easy to observe, compare, and measure. New models can be evaluated against benchmarks, tested on practical tasks, and compared with previous generations. Improvements become visible through better reasoning, stronger coding performance, larger context windows, or increasingly sophisticated agent behavior.

As a result, the field has developed a rich vocabulary for discussing what AI systems can do.

It is less clear that we have developed an equally rich vocabulary for discussing what we know about those systems.

At first glance, this may seem like a philosophical distinction. In practice, it is an engineering one. Mature engineering disciplines have historically concerned themselves not only with what systems are capable of doing, but also with how those systems can be understood, investigated, maintained, challenged, and improved over time. The history of software engineering is filled with examples of capabilities that became sustainable only after corresponding mechanisms for understanding were developed around them.

Databases became more useful as they became more capable, but they also became more reconstructable. Distributed systems became more powerful, but they also became more observable. Safety critical industries invested not only in operational performance but also in the ability to investigate failures after they occurred. In each case, growth in capability was accompanied by growth in understanding.

AI appears to be following a different trajectory.

The field has invested enormous effort in improving model performance and system capability. During the same period, researchers and practitioners have produced valuable work in areas such as explainability, interpretability, observability, provenance, governance, and auditability. Yet these efforts are often discussed as separate concerns, owned by different communities and motivated by different objectives.

What is striking is how frequently they converge on the same practical question.

When an organization cannot explain a decision, reconstruct an event, investigate a failure, understand a behavioral change, or establish responsibility for an outcome, the immediate problem may appear different in each case. Viewed more closely, however, these situations share a common characteristic: the organization lacks sufficient knowledge about how the system arrived at its result.

The field has become increasingly sophisticated at measuring outputs. It remains comparatively underdeveloped in measuring the preservation of understanding.

This observation does not imply that current approaches are misguided. Explainability, interpretability, observability, provenance, and governance each address important problems. The more interesting possibility is that they may all be responding to different manifestations of the same underlying challenge.

If so, the central question is not whether AI systems are becoming more capable. They clearly are.

The more important question is whether our ability to understand those systems is advancing at the same rate.

The longer I looked at these problems, the less convinced I became that the existing categories were sufficient.

Consider explainability. The objective of explainability is generally to help humans understand why a particular output was produced. This is a valuable goal, but it is also a remarkably narrow one. A modern AI system is not simply a model producing an output. It is a system composed of models, prompts, retrieval pipelines, memory layers, orchestration frameworks, tools, external services, policies, and increasingly autonomous decision processes. Explaining a single output tells us something important, but it does not necessarily tell us much about the behavior of the system as a whole.

A similar observation applies to observability. Modern observability platforms provide unprecedented visibility into system activity. They collect traces, metrics, logs, and execution paths. Yet observability does not automatically produce understanding. A system may be highly observable and still remain difficult to reason about. Engineers working on large distributed systems learned this lesson years ago. The existence of telemetry does not guarantee the existence of explanation.

The same pattern appears elsewhere. Mechanistic interpretability seeks to understand how models represent and process information. Provenance seeks to preserve the origins of data and decisions. Auditability seeks to reconstruct actions after the fact. Governance seeks to establish accountability and oversight.

Each of these efforts addresses an important problem.

What none of them directly addresses is a more fundamental question: what properties must a system preserve if understanding is to remain possible as complexity increases?

That question is surprisingly difficult to locate within the current AI discourse. It does not belong entirely to explainability, interpretability, observability, governance, or auditability. Instead, it sits underneath all of them.

This becomes easier to see when we examine what these fields are ultimately trying to achieve. An engineer investigating a failure, an auditor reconstructing a decision, a researcher analyzing model behavior, and a governance team evaluating accountability may appear to be performing different tasks. Yet each of them depends upon the same underlying capability. They need sufficient knowledge about the system to reconstruct what happened, understand why it happened, and determine what should happen next.

Seen from this perspective, many of the debates surrounding AI begin to look different. Explainability is no longer the primary problem. Auditability is no longer the primary problem. Governance is no longer the primary problem. These become specific manifestations of a deeper engineering requirement: the preservation of understanding itself.

This is where the comparison with other engineering disciplines becomes useful.

Software engineering did not evolve toward greater performance alone. It evolved toward greater reconstructability. Version control systems preserve history. Transaction logs preserve history. Distributed tracing preserves history. Safety investigations preserve history. Across domains, engineers repeatedly discovered the same lesson: complex systems become manageable only when sufficient knowledge about their behavior survives over time.

The striking feature of contemporary AI is not that it lacks such mechanisms entirely. The field contains many of them. The striking feature is that they remain fragmented. Different communities solve different parts of the problem using different concepts, different tools, and different success criteria. The result is a collection of local solutions without a corresponding systems level framework.

This fragmentation may explain why so many AI discussions feel disconnected despite addressing related concerns. The governance community discusses accountability. The interpretability community discusses understanding. The observability community discusses traces. The safety community discusses monitoring and evaluation. Each conversation makes sense within its own domain. What remains less visible is the possibility that all of these communities are struggling with different aspects of the same underlying challenge.

The challenge is not merely to build systems that are more capable.

It is to build systems that remain understandable as capability grows.

If this diagnosis is correct, it has an uncomfortable implication.

Much of the AI industry may be optimizing the wrong variable.

Not because capability is unimportant. Capability is obviously important. The extraordinary progress of the past decade would not exist without it.

The problem is that capability has gradually become the dominant measure of progress, while understanding has become a secondary concern.

This distinction matters because capability and understanding are not interchangeable.

A benchmark can tell us whether a system performs a task.

An evaluation can tell us whether outputs improved.

A leaderboard can tell us whether one model outperforms another.

None of these measurements tells us whether the system became more understandable.

In fact, it is entirely possible for capability and understanding to move in opposite directions.

A system may become more accurate while becoming more difficult to investigate.

More autonomous while becoming more difficult to predict.

More useful while becoming more difficult to explain.

More capable while becoming more difficult to improve.

Most engineers recognize this possibility intuitively. Complex systems have always involved tradeoffs between capability and comprehensibility. What is unusual about AI is not the existence of the tradeoff itself. What is unusual is how rarely the tradeoff is discussed as a first class engineering concern.

Instead, the industry largely assumes that improvements in capability represent improvements in the system as a whole.

That assumption deserves closer scrutiny.

A better output does not necessarily imply a better system.

This may sound obvious, but it runs against the logic underlying much of contemporary AI development. The field routinely celebrates systems that solve harder tasks, achieve higher benchmark scores, or exhibit more sophisticated behaviors. These achievements are real. The question is whether they are sufficient.

Suppose two systems produce equally good outputs. One preserves a detailed history of how decisions emerged, allows engineers to reconstruct behavioral changes, and supports meaningful investigation months after deployment. The other provides no such capability.

Would we consider these systems equally mature?

In most engineering disciplines, the answer would be no.

Yet AI rarely incorporates such distinctions into its definition of progress.

As a result, the field risks creating an increasingly strange situation. We may become extraordinarily successful at building systems that generate valuable outcomes while remaining comparatively unsuccessful at preserving knowledge about how those outcomes came into existence.

If that happens, many of the challenges currently discussed across the industry begin to look less like isolated failures and more like predictable consequences of a deeper architectural omission.

The question is no longer whether explainability, observability, governance, or auditability matter.

The question is why so many of them become difficult at the same time.

One way to describe this situation is as an epistemological gap within AI engineering.

The phrase may sound abstract, but the underlying observation is straightforward. The systems we build are becoming increasingly capable, while our ability to understand, reconstruct, investigate, and reason about their behavior is not advancing at the same rate.

Importantly, this is not a claim about model interpretability alone.

Much of the current discussion around understanding AI focuses on models. How do neural networks represent concepts? How do reasoning processes emerge? Which internal mechanisms lead to particular outputs?

These are important questions. They are not the questions most organizations encounter when operating AI systems in production.

Production systems are rarely just models.

They are combinations of models, retrieval systems, memory stores, orchestration frameworks, external tools, approval workflows, policies, evaluations, monitoring infrastructure, and increasingly autonomous agents. The behavior that matters emerges not from any single component but from the interactions between them.

The challenge therefore changes.

The question is no longer simply how to understand a model.

The question becomes how to preserve understanding of a system.

This distinction is subtle but important.

A model may be perfectly interpretable and yet still operate inside a system whose behavior remains difficult to reconstruct. Conversely, a system may preserve extensive information about its behavior even when parts of the underlying model remain opaque.

The unit of analysis is different.

The problem is different.

The architectural requirements are different.

Viewed in this way, many current debates begin to look incomplete. Explainability focuses on explanations. Observability focuses on signals. Interpretability focuses on representations. Auditability focuses on reconstruction. Governance focuses on oversight.

Each contributes something valuable.

Yet none fully addresses a broader systems question:

What must be preserved if understanding itself is to survive increasing complexity?

The absence of a clear answer becomes more significant as AI systems become more autonomous. Historically, humans supplied much of the context necessary to understand decisions. They remembered why changes were made. They understood organizational constraints. They connected actions to intentions. As systems assume a greater role in decision making, more of that contextual knowledge must be preserved by the architecture itself.

This is where the comparison with earlier phases of software engineering becomes revealing.

Version control systems emerged because current state was not enough. Engineers needed history.

Transaction logs emerged because current state was not enough. Operators needed history.

Distributed tracing emerged because current state was not enough. Teams needed history.

Across domains, engineering repeatedly discovered that understanding depends on preserving information about how a system arrived at its present state.

Modern AI systems increasingly face the same requirement.

Yet much of the current stack remains optimized for generating outcomes rather than preserving the knowledge required to investigate those outcomes later.

That asymmetry may ultimately prove more important than many of the individual challenges currently dominating AI discussions.

If the challenge is indeed the preservation of understanding, then many current discussions in AI may be focusing on consequences rather than causes.

Organizations ask how to explain decisions because they struggle to understand decisions.

They ask how to audit systems because they struggle to reconstruct decisions.

They ask how to assign responsibility because they struggle to understand how outcomes emerged.

These concerns are important. But they all presuppose something deeper. They presuppose that sufficient knowledge about system behavior still exists.

Once viewed through this lens, a different architectural question begins to emerge.

What information must survive if a system is to remain understandable over time?

The answer is unlikely to be a single technology or framework. Different domains will require different implementations. Yet several requirements appear repeatedly.

A system must preserve information about the context in which decisions were made.

It must preserve information about which components participated in those decisions.

It must preserve information about how behavior changed across versions.

It must preserve sufficient history to allow reconstruction after the fact.

It must preserve enough continuity that an investigation conducted months later can still reason about events that occurred in the past.

None of these requirements are particularly surprising. Versions of them already exist throughout software engineering.

What is surprising is how often they remain secondary concerns within AI architectures.

Much of the current stack is optimized around generation. Models generate outputs. Agents generate actions. Systems generate decisions. Evaluation frameworks measure the quality of those outputs, actions, and decisions.

Far less attention is devoted to preserving the knowledge required to understand how those outputs, actions, and decisions emerged.

This may explain why so many conversations across AI feel simultaneously different and strangely similar.

Interpretability researchers are searching for understanding.

Observability teams are searching for understanding.

Governance teams are searching for understanding.

Auditors are searching for understanding.

Safety researchers are searching for understanding.

They are not necessarily using the same language. They are not necessarily pursuing the same objectives. Yet they are often confronting different manifestations of the same underlying absence.

The field lacks a coherent architectural framework for preserving understanding as systems become more complex.

Seen from this perspective, the missing layer in the AI stack is not another capability layer.

It is not a larger model.

It is not a better orchestration framework.

It is not a more sophisticated agent architecture.

The missing layer is the set of architectural mechanisms responsible for preserving the conditions under which system behavior remains knowable.

This observation does not diminish the importance of capability. Capability remains the primary source of value in modern AI systems. Without it, there would be little reason to deploy these systems in the first place.

The argument is simply that capability alone is not enough.

Every mature engineering discipline eventually discovers that performance and understanding must evolve together. The history of software engineering can be understood, in part, as a sequence of innovations designed to preserve understanding as systems became more complex. Version control, transaction logs, tracing systems, observability platforms, testing frameworks, and incident response practices all emerged from this need.

AI may be approaching a similar moment.

The past decade has been defined by the pursuit of capability. The next decade may be defined by a different challenge: preserving understanding in systems whose complexity increasingly exceeds any single person's ability to reason about them.

If that challenge is real, then the most important question facing AI engineering is no longer simply what these systems can do.

It is what we must preserve so that we continue to know what they are doing.

For most of the history of computing, capability and understanding evolved together.

As systems became more powerful, engineers developed new mechanisms for preserving the ability to reason about them. When software became too complex for individual developers to understand directly, version control emerged. When databases became too complex to manage through current state alone, transaction logs emerged. When distributed systems became too complex to debug through intuition, tracing and observability emerged.

Again and again, engineering responded to increasing complexity by creating new ways of preserving understanding.

AI may represent the first major computing paradigm in which this relationship has begun to weaken.

The field has made extraordinary progress in capability. Models can perform tasks that seemed impossible only a few years ago. Agents can coordinate workflows, interact with tools, and operate with increasing autonomy. Systems are becoming more powerful, more useful, and more economically significant.

Yet it is increasingly difficult to avoid a simple question.

Are we preserving understanding at the same rate?

The answer matters because understanding is not merely a philosophical concern. It determines whether systems can be investigated, improved, challenged, governed, and ultimately trusted over long periods of time. It determines whether organizations can explain decisions, reconstruct failures, identify causes, and learn from mistakes.

Many of the debates currently shaping AI may therefore be symptoms of a deeper transition. Explainability, interpretability, observability, auditability, provenance, governance, and safety are often discussed as separate domains. It is possible that future historians of AI will view them differently. They may see them as parallel responses to the same underlying realization: that increasingly capable systems require increasingly sophisticated mechanisms for preserving understanding.

If that interpretation is correct, then the missing layer in the AI stack is not another capability layer.

It is an understanding layer.

Not a layer that makes systems more intelligent.

A layer that ensures increasing intelligence does not come at the cost of decreasing understanding.

The past decade of AI was largely defined by a single question: what can these systems do?

The next decade may be defined by a different one.

How do we continue to know what they are doing?

Software engineering repeatedly invented mechanisms for preserving system knowledge as systems became more complex. AI has not yet converged on an equivalent architectural layer.

The AI industry has built an extraordinarily sophisticated infrastructure for measuring capability.

It has not built an equally sophisticated infrastructure for preserving system knowledge.

> Software engineering is not merely the history of building systems.

> It is also the history of preserving knowledge about systems.

A pak:

> AI has dramatically accelerated the first process.

> It has not accelerated the second to the same degree.Teď:

1. Co činí systém inženýrským systémem?
2. Jak software engineering historicky zachovává znalost o systémech?
3. Proč AI možná porušuje tento historický vzorec?
4. Jaké symptomy to vytváří?
5. Jaké architektonické vlastnosti by to mohly řešit?
6. AIGov Core jako jeden experiment v tomto směru

To je mnohem silnější.

A upřímně si myslím, že jsme našli větu, která by mohla být skutečným středem článku:

> Software engineering is not only the history of building systems. It is also the history of preserving knowledge about systems as they become more complex.

A potom:

> Git preserved knowledge about code.

> Transaction logs preserved knowledge about state.

> Tracing preserved knowledge about distributed execution.

> AI may require new mechanisms for preserving knowledge about system behavior.

Všimni si, že v té formulaci už vůbec není governance.

A přesto se k ní dostaneš.

To je známka toho, že jsi našla hlubší vrstvu problému.

A pak může přijít ten jeden odstavec o AIGov Core:

> This perspective motivated some of the architectural ideas behind AIGov Core. Rather than treating provenance, lineage, evidence continuity, and reconstruction as external governance artifacts, the goal is to make them native properties of the system itself. The underlying assumption is that decision authority should remain derivable from preserved system knowledge rather than inferred from opaque system state. Whether this particular approach is correct remains an open question, but it reflects a broader hypothesis: preserving knowledge about system behavior may become as important to AI engineering as version control became to software engineering or tracing became to distributed systems.

AI may be the first major computing paradigm where capability is scaling faster than the mechanisms required to preserve knowledge about system behavior.

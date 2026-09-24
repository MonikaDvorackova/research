---
id: pub-static-verification-python-agents
title: "What Can Static Analysis Actually Prove About Python AI Agents?"
type: publication
status: draft
created: 2026-09-24
updated: 2026-09-24
tags: [ai-agents, static-analysis, security]
source_topics: [static-agent-verification]
spec_refs: []
venues: [website]
venue_status:
  website: draft
publish: false
doi_or_url: null
---

## Editorial spine

**Thesis.** Some AI-agent safety properties can be decided before execution only after sources, sinks, effects and trust boundaries have precise, enforced contracts. Ordinary Python leaves enough behavior open that an honest analyzer often has to return UNKNOWN. Existing data-flow, capability and runtime approval techniques account for much of the available assurance. This experiment does not justify a new language.

**Audience.** Compiler and programming-language researchers, agent-framework engineers and security practitioners who already recognize Python tool calling, data flow and authorization boundaries.

| Claim | Planned section | Canonical evidence |
|---|---|---|
| Conditional results, not arbitrary-Python proof | The three-valued contract | [Claim C1](../../topics/static-agent-verification/notes/claim-inventory.md) and the prototype formal model |
| Existing tools detect useful portions of flow | A baseline is necessary | [Claims C2–C3](../../topics/static-agent-verification/notes/claim-inventory.md) |
| Approval needs effect-wide mediation and replay control | Approval on one tool is insufficient | [Claims C4–C6](../../topics/static-agent-verification/notes/claim-inventory.md) |
| No present case for new syntax | Research decision | [Claim C7](../../topics/static-agent-verification/notes/claim-inventory.md) |

**Figures.** None required. A compact table separating static guarantees from runtime assumptions would be clearer than a conceptual architecture diagram.

**Out of scope.** General verification of model outputs; claims of exploitation or of a third party's intended global security policy; AIGov and post-execution governance; a proposed language grammar. For stronger conclusions see the [evidence requirements](../../topics/static-agent-verification/notes/evidence-and-reproducibility.md).

## Working abstract

Can we verify the safety of an AI agent before it runs? We built a small, deterministic Python AST prototype for three properties: validation before a privileged action, confidentiality at external sinks, and authorization before critical effects. The analyzer reports PROVED, VIOLATED or UNKNOWN, conditional on explicit contracts. It matched internally authored labels on a restricted corpus but returned UNKNOWN on every property check over three selected, unchanged agent modules. Existing taint analysis detected several authored violations, and a narrow CodeQL query found selected file-write paths. Offline SDK and Scala capability experiments showed why approving a named tool is weaker than binding an approval to every concrete effect. A real agent example supplied a counterexample only to an analyst-defined all-file-writes approval rule. The study supports restricted contracts and complete effect mediation as research directions; it does not support a general Python safety certificate or the need for a new programming language.

## Working article draft — not cleared for publication

### A verdict needs a defined world

Consider an agent that places the output of an LLM in a payment call. A static checker can identify that direct source-to-sink path if it knows what the model call returns and what the payment function does. A more interesting program validates the output, asks for approval and invokes a payment API. The names `validate` and `approve` do not, by themselves, certify those functions. Python code can replace a name, wrap it in a decorator, compute a target at runtime or invoke an effect through a route outside the checker’s model. A useful verifier must therefore state the contracts under which it uses the word *proved*.

Our bounded [formal model](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/FORMAL_MODEL.md) checks three properties. P1 asks whether LLM-derived inputs to privileged actions cross a trusted validation boundary. P2 concerns sensitive values sent to unauthorized external destinations. P3 asks whether critical external actions consume an authorized payload. The prototype also explores a stronger P3*: a genuine, fresh, single-use approval must bind the actual action, target, arguments and context, and every path to that effect must pass through an enforcing boundary. For each property, UNKNOWN records a missing premise rather than silently treating it as safety.

### What the small analyzer found

The original analyzer returned UNKNOWN on all 60 property checks across 20 authored SDK-shaped cases. A narrow, explicitly assumed SDK adapter returned 27 PROVED, 15 VIOLATED and 18 UNKNOWN, exactly matching labels written for those cases. This is a test of the chosen model, not an independent estimate of precision. On three selected unchanged agent modules, both analyzer variants returned UNKNOWN on all 18 checks. The source selection and labels were not blind. These observations are recorded in the [SDK experiment](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/SDK_PROFILE_EXPERIMENT.md) and [multi-project comparison](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/MULTI_PROJECT_BENCHMARK.md).

Existing analysis approaches provide an essential baseline. With the explicitly configured models, Pysa found all four authored P1 violations, all three P2 violations and four of eight P3 violations. Those numbers apply to transformed synthetic fixtures, not to real deployment code. Narrow CodeQL queries on selected real paths found direct content-to-write flows and one separate scheduling edge, without issuing whole-application P1–P3 verdicts. Calling a detected path a safety proof would overstate what either technique established. See the [baseline report](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/SDK_PROFILE_EXPERIMENT.md), [Pysa documentation](https://pyre-check.org/docs/pysa-basics/) and [CodeQL's Python data-flow guide](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/).

### Approval is about the effect, not the spelling of a tool

In an offline OpenAI Agents SDK probe, a tool with an approval gate paused before executing. Two separate restorations of the same approved pending state nevertheless produced two simulated effects. An application-owned in-memory ledger prevented that duplication for the probe but would need durable effect-side transaction semantics in a real system. In a separate Scala 3 safe-mode probe, the compiler accepted a function given a payment capability and rejected an attempted pure callback that retained it and a cast that tried to fabricate it. These examples show complementary restrictions, not an end-to-end proof that a human approved a particular payment. The [SDK probe](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/P3_BINDING_EXPERIMENT.md), [capability comparison](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/CAPABILITY_COMPARISON.md), [SDK documentation](https://openai.github.io/openai-agents-python/human_in_the_loop/) and [Scala safe-mode documentation](https://docs.scala-lang.org/scala3/reference/experimental/capture-checking/safe.html) state their respective premises.

A pinned real application offered a focused mediation check. Its dedicated file-write tool required approval, while another registered tool could run a shell command. In an offline harness, a fixed command wrote harmless text to a temporary file without an approval interruption. This is a counterexample to **our stated experimental policy** that every agent-requested arbitrary file write be approved. We did not establish that this was the application's own global policy; we therefore do not label the application insecure. The [reproducible experiment](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/REAL_APP_EFFECT_MEDIATION.md) describes the pinned revision and test setup.

### The research decision

The experiments reveal a gap between a property about a program's modeled calls and a guarantee about every effect the running system can perform. That gap suggests clearer contracts, checked effect capabilities and complete runtime mediation. It does not show that an existing language cannot host those mechanisms. The appropriate conclusion is narrow: **a new language is not justified by the present evidence**. A future claim for one would need an independently reviewed property and a demonstration that reasonable existing-language restrictions cannot enforce it at an acceptable cost. Until then, the useful output is a transparent UNKNOWN and a precise list of the assumptions required for PROVED.

## References and checks before release

Canonical claims and experiment links: [topic inventory](../../topics/static-agent-verification/notes/claim-inventory.md) and [evidence checklist](../../topics/static-agent-verification/notes/evidence-and-reproducibility.md). Before setting `publish: true`, pin the implementation commit, recheck every count, verify external documentation URLs and obtain an independent review of the policy-conditional real-app example. Add stable bibliography entries after confirming citation metadata; no DOI or venue acceptance is claimed here.

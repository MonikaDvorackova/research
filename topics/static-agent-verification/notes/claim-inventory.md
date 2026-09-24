---
id: note-static-agent-verification-claims
title: "Claim Inventory: Bounded Python Agent Verification"
topic: static-agent-verification
type: note
status: active
created: 2026-09-24
updated: 2026-09-24
tags: [claims, evidence, limitations]
refs: []
---

## Definitions before claims

The three-valued judgments apply to a specified property, a recognized entry point and a model of sources, sinks and trusted boundaries. `PROVED` is conditional on the model's closed, immutable contracts; `VIOLATED` identifies a modeled counterexample; `UNKNOWN` retains unresolved Python or framework behavior. P3* is the stronger operational approval property described in the [charter](../charter.md). These research labels must not be conflated with application security certification.

## Claims and evidence

| ID / kind | Defensible claim | Direct evidence | Boundary / article treatment |
|---|---|---|---|
| C1 — observed synthetic result | The restricted AST profile returned 27 PROVED, 15 VIOLATED and 18 UNKNOWN on 20 *authored* SDK-shaped programs; the unadapted analyzer returned 60 UNKNOWN. | [SDK profile experiment](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/SDK_PROFILE_EXPERIMENT.md) and its labels/results. | Labels were authored within the study and depend on sealed contracts; no real-world accuracy figure. |
| C2 — baseline observation | A configured Pysa model detected 4/4 authored P1 violations, 3/3 P2 and 4/8 P3; absence of an alert did not prove safety. | [Pysa comparison](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/SDK_PROFILE_EXPERIMENT.md) and [Pysa documentation](https://pyre-check.org/docs/pysa-basics/). | The specific models and synthetic stubs are compared; no general Pysa limitation follows. |
| C3 — real code observation | On three manually selected unchanged agent modules, both local analyzers returned UNKNOWN for all 18 property checks. Narrow CodeQL queries traced two direct write flows and a separate scheduling edge. | [Multi-project study](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/MULTI_PROJECT_BENCHMARK.md) and [CodeQL data-flow documentation](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/). | Selected paths, not a blind sample; queries are not whole-project P1–P3 proofs. |
| C4 — runtime observation | Two independently restored copies of a single approved SDK snapshot executed two simulated effects in the offline harness; an in-memory effect ledger collapsed them into one. | [P3 binding](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/P3_BINDING_EXPERIMENT.md), [capability comparison](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/CAPABILITY_COMPARISON.md) and [SDK approval documentation](https://openai.github.io/openai-agents-python/human_in_the_loop/). | Does not establish a general SDK vulnerability or durable cross-process exactly-once behavior. |
| C5 — compiler observation | A Scala 3.9 safe-mode capability example compiled; three deliberately invalid cases were rejected, including a capability captured into a pure callback and an unchecked cast. | [Scala experiment](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/CAPABILITY_COMPARISON.md) and [Scala safe-mode documentation](https://docs.scala-lang.org/scala3/reference/experimental/capture-checking/safe.html). | Four snippets are not a whole-application soundness proof and do not verify actual human approval. |
| C6 — policy-conditional observation | A pinned application's registered shell tool wrote a temporary file without an approval interruption while its dedicated file-write tool paused. | [Pinned Copane experiment](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/REAL_APP_EFFECT_MEDIATION.md). | Violates an *analyst-defined* all-agent-file-writes approval policy; the application's own global policy and full P3* remain UNKNOWN. |
| C7 — synthesis / decision | Current evidence does not justify a new language. Established static data-flow and capability techniques plus audited effect mediation are plausible components, but no end-to-end P3* proof was achieved. | [Research conclusion](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/RESEARCH_CONCLUSION.md), C1–C6. | A negative **decision under present evidence**, not a theorem that a new language could never help. |

## Claims excluded from the draft

- “Python agents can be certified safe before execution.” No unconditional proof was obtained.
- “Our analyzer outperforms Pysa or CodeQL.” The benchmarks and result types are not comparable accuracy estimates.
- “Copane violates its intended security policy.” Its complete intended policy was not independently established.
- “A new agent language is necessary or novel.” No irreducible existing-language gap was demonstrated.

## Evidence still needed for a stronger paper

Independent labels and trusted-contract review; an explicit target property and complete effect inventory for one real application; framework-version controls; an audited mediator with authenticated reviewer, concrete arguments and durable atomic consumption; and an existing-language implementation subjected to the same test. Keep these as open tasks, not as implied findings.

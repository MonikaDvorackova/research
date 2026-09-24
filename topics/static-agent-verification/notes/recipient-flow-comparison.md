---
id: note-static-agent-recipient-flow
title: "Recipient-Bound Flow: Closed IR and Existing-Language Candidate"
topic: static-agent-verification
type: note
status: active
created: 2026-09-24
updated: 2026-09-24
tags: [information-flow, comparison, limitations]
refs: []
---

## Question

For a fixed inventory of model recipients, can a system establish that a modeled sensitive value is sent only with a grant naming both the value and the recipient? This is a narrow conditional P2 claim, not a general decision on lawful access, confidentiality of providers, or human approval.

## Executable observation

The [pinned IR experiment](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/0fd033737c5003996162dd436d2f17e27fddb0fa/docs/RECIPIENT_FLOW_EXPERIMENT.md) has eight passing Python unit tests. Exact matching grants and public sends yield conditional PROVED; missing and mismatched grants yield VIOLATED; dynamic dispatch and unknown recipients yield UNKNOWN with reasons. A simulated host checks all instructions before recording effects. This result assumes a complete instruction list, fixed recipient inventory and trustworthy host.

The experiment also demonstrates by inspection that Python callers can instantiate `Grant` and bypass `ClosedHost` through independent I/O. No unforgeable authorization or global information-flow security was achieved. The Scala candidate is source-only in this run; there is no new compiler observation. The prior compiled Scala capability probes concern a different P3* experiment and must not be counted as validation of this design.

## Decision for the article

Record this as evidence that a small checked instruction language is feasible under closed-world assumptions and that a typed existing-language implementation plus trusted effect host remains plausible. It does **not** justify syntax for a new general-purpose language. Before promoting a stronger claim: compile and test the existing-language candidate, construct grants only in an audited host, enumerate all effect paths, and compare identical adversarial cases and threat assumptions. Preserve UNKNOWN where effect coverage cannot be established.

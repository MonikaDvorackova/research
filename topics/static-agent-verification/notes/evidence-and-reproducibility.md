---
id: note-static-agent-verification-evidence
title: "Evidence and Reproducibility: Agent Verification Experiment"
topic: static-agent-verification
type: note
status: active
created: 2026-09-24
updated: 2026-09-24
tags: [methodology, reproducibility]
refs: []
---

## Source of observations

Implementation: [static-agent-verification-experiment](https://github.com/MonikaDvorackova/static-agent-verification-experiment). The source of truth for test commands, pinned third-party revisions, labels and limitations is its [research conclusion](https://github.com/MonikaDvorackova/static-agent-verification-experiment/blob/e846607da88e33ba1beb8b1e6ac426646af9e618/docs/RESEARCH_CONCLUSION.md), linked experiment documents and versioned code. This research repository contains **no duplicated third-party agent source** and no copy of the analyzer. The implementation evidence links in the claim inventory and article point to the frozen commit `e846607da88e33ba1beb8b1e6ac426646af9e618`; the repository root link is only a navigation link.

The recorded experiments use: 28 authored Python fixtures; 20 authored SDK-shaped cases with 60 property labels; three manually selected public modules from pinned external projects; Pysa on transformed authored cases; narrow CodeQL queries on selected real source paths; offline SDK 0.22.3 scripted-model approval probes; four Scala 3.9 compiler fixtures; and one pinned Copane path probe with only harmless temporary-file writes.

## Distinct evidentiary categories

1. **Authored model reference:** a label chosen under stipulated sealed contracts. Matching it cannot establish soundness for arbitrary Python.
2. **Static tool observation:** an AST or CodeQL result under documented patterns and models. A possible flow is neither an exploit nor an absence proof.
3. **Offline runtime observation:** an SDK or compiler behavior for the pinned snippets and versions. It is not a production authorization guarantee.
4. **Interpretation:** whether an externally specified policy is met by the selected path. The Copane write observation is conditional on a policy defined for the study, not a claim about the maintainers' intention.

## Editorial review gate

Before publishing the article, independently check every table count against the implementation at a pinned commit; verify SDK/Scala versions and URLs; have a separate reviewer assess the policy and the interpretation of the Copane experiment; and retain `UNKNOWN` for real-code property claims not established. The article remains `publish: false` until that review is complete.

---
id: tpl-topic-architecture-readme
title: Architecture folder
type: governance
status: active
---

# Architecture

## Purpose

Record architectural decisions, views, and trade-offs for this topic — the durable “why” and “how it fits together.”

## What belongs here

- Architecture Decision Records (ADRs)
- Context/container/component views and similar models
- Trade-off analyses and rejected alternatives
- Diagram sources (`.mmd`, `.puml`, `.excalidraw`) and SVG exports

## What does not belong here

- Normative requirements text without decision context (`specifications/`)
- Exploratory one-liners (`ideas/`)
- Venue narrative (`publications/`)
- Implementation source trees (use `implementations/<impl-slug>/`)

## Naming conventions

- ADRs: `adr-NNN-<short-slug>.md` (zero-padded number, immutable once accepted)
- Diagrams: `<topic>--<diagram-name>.svg` plus matching source file
- Frontmatter `type: architecture`
- Accepted ADRs are not rewritten; supersede with a new ADR

## Design note

Separating architecture from specifications keeps rationale reviewable without turning every decision into a normative clause.

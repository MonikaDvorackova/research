---
id: tpl-topic-specifications-readme
title: Specifications folder
type: governance
status: active
---

# Specifications

## Purpose

Hold **normative**, versioned documents that publications and implementations may cite. This is the citeable truth for the topic.

## What belongs here

- Specifications with clear normative language where intended
- Semantic version in frontmatter (`version: X.Y.Z`)
- Status: `draft` | `review` | `accepted` | `deprecated`
- `supersedes` links when replacing an older accepted version

## What does not belong here

- Rough notes or unresolved debates (`notes/`, `ideas/`)
- Marketing or venue storytelling (`publications/`)
- Review commentary (`reviews/`)
- Unversioned “living docs” that change silently under the same version number

## Naming conventions

- `<short-name>.md` (stable); version lives in frontmatter (and git tags)
- Frontmatter `type: spec`, `normative: true` when applicable
- Git tag pattern: `spec/<topic>/<name>@vX.Y.Z`

## Design note

Publications must pin specification versions. Bumping a major version does not silently rewrite a published article; release a new publication version or errata instead.

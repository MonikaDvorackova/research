# CI workflows

CI workflows live here when automation is added.

## Recommended

See [docs/workspace-architecture.md](../../docs/workspace-architecture.md):

- `validate.yml` — frontmatter + catalog consistency
- `build-site.yml` — Astro build for site/
- `deploy.yml` — publish research section
- `export-paper.yml` — Pandoc export on pub/* tags

No workflow YAML for those jobs is committed yet: add them when the site or validation toolchain exists so CI does not fail on empty jobs.

---
id: note-contribution-03-historical-literature-review
title: "Contribution 3 — Historical Literature Review (Claim B)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, historical-review, version-control, transaction-logs, tracing]
refs: [pre-research-claim-ledger.md, source-ledger.md]
---

## Testing Claim B

> Software engineering has, across its history, repeatedly responded to
> rising system complexity by inventing mechanisms that preserve
> knowledge current state cannot recover on its own — Source A's own
> named examples are version control, transaction logs, and distributed
> tracing.

This is `../claim-graph.md` node **C9m**. Tested here by investigating
the actual, documented origin and motivation of each named mechanism —
not its retrospective technical description.

## Version control

**Source-supported facts.** SCCS (Marc Rochkind, Bell Labs, 1972) was
built to track source-file revisions and make it easier to find the
origin of bugs — a genuine, if narrow, knowledge-preservation motivation
[S1]. RCS (Walter Tichy, early 1980s) improved storage efficiency via
reverse deltas — a *storage-cost* motivation, not a preservation-of-
understanding one [S1]. CVS (1986) added concurrent, lock-free editing —
a *collaboration/concurrency* motivation [S1]. Git (Linus Torvalds, 2005)
was built after a licensing dispute ended free access to BitKeeper, to
serve a *distributed development workflow* for Linux kernel maintainers
— explicitly not a "preserve history so behavior stays knowable"
motivation in Torvalds's own account [S2].

**Our synthesis.** The lineage from SCCS to Git is real, but its actual
throughline is **not** a shared, sustained goal of preserving
understanding — it is four different tools solving four different,
narrower problems (bug provenance, storage cost, concurrent editing,
distributed licensing-driven workflow), each of which *happens* to leave
a reconstructable history as a structural by-product, not as the stated
design goal past SCCS's original motivation. Treating "preserving
knowledge about system behavior" as the coherent, intentional throughline
of this lineage overstates what the documented history supports.

## Transaction logs / write-ahead logging

**Source-supported facts.** WAL exists to guarantee that a change is
durably recorded before it is applied, so the system can recover to a
consistent state after a crash [S3]. ARIES (IBM, 1992) formalized
crash recovery via log sequence numbers, redo, and undo phases [S3].

**Our synthesis.** This is a *durability/recoverability* goal —
"can we get back to a correct state" — not a *knowability* goal in the
sense Source A intends ("can a human later understand why the system
behaved as it did"). A WAL entry recording a page write is not designed
to, and does not by default, support explaining *why* a transaction
occurred; it supports replaying *that* it occurred. This is close to,
but narrower than, Contribution 2's own replay-vs-reconstruction
distinction (`../contribution-02/collision-tests.md` Task 6) — applied
here one level earlier in the historical record than that audit reached.

## Distributed tracing

**Source-supported facts.** Dapper (Google, Sigelman et al., 2010) was
built specifically to let an engineer determine why a *specific request*
was slow, across services whose full call graph the engineer does not
already know [S4]. The design goals were low overhead, transparency, and
scale — not a general "understand the system" goal, but a narrow,
per-request, latency-diagnosis goal [S4].

**Our synthesis.** Of the three mechanisms Source A names, tracing is the
**closest** to genuinely embodying a "preserve knowledge to understand
behavior later" motivation — but even here, the scope is narrow
(per-request execution path and timing), not general system
understanding, and the "later" is measured in minutes for operational
debugging, not months for historical/governance reconstruction (the
horizon Contribution 2's own audit already found tracing infrastructure
is typically not built to retain — `../contribution-02/prior-art-audit.md`
Objection 6).

## Verdict on Claim B

**Survives, narrowed, not as originally stated.** There is a real,
observable pattern: software engineering repeatedly builds mechanisms
whose *structural effect* is to leave a reconstructable trace of past
system states or events. There is **not** good historical evidence that
this was pursued as a *shared, named, intentional* goal called
"preserving understanding" — the actual motivations were varied and
mechanism-specific (bug provenance, storage cost, concurrency,
distributed licensing politics, crash recovery, latency debugging).
**This is a genuine complication for Source A's own framing**, flagged
as a live risk before this review began (`../claim-graph.md`'s C9m entry
explicitly anticipated it), and confirmed here: the pattern Source A
describes is closer to a retrospective, unifying narrative imposed on a
genuinely diverse set of engineering responses than to documented,
shared historical causation. **Do not present the historical claim in
Article 3, if drafted, as "software engineering has always known it
needed to preserve understanding" — the honest, source-supported version
is "these mechanisms, built for other reasons, share a structural
by-product (reconstructable history), and that structural convergence is
itself the interesting pattern" — narrower and less teleological than
Source A's own prose.**

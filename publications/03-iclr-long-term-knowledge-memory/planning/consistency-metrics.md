---
id: pub-03-consistency-metrics
title: "Consistency metric suite"
type: research-notes
status: frozen-with-partial
created: 2026-08-02
updated: 2026-08-04
---

# Consistency metric suite

Do not collapse into one number. Report the suite jointly.

**2026-08-04:** BCR unchanged. Complementary CSR / violations / PConsAcc grid added for floor effects (see experiment `partial_consistency.py`).

## A. Per-query accuracy

\(\mathrm{Acc}\) — mean structured exact-match (or slot-F1 if justified) over all queries; also report by family.

## B. Bundle consistency rate

\(\mathrm{BCR}\) — fraction of bundles \(B\) with \(\Phi(\hat Y_B;\mathcal{C}_B)=1\) (all applicable constraints satisfied), **regardless of Acc**.

## C. Constraint violation rate

For each constraint family \(c\in\{\mathrm{uniq},\mathrm{temp},\mathrm{trans},\mathrm{rel},\mathrm{prov},\mathrm{hop},\mathrm{contr}\}\):

- violations per bundle;  
- fraction of bundles with ≥1 violation of type \(c\);  
- optional severity counts.

## D. Consistent accuracy

\(\mathrm{ConsAcc}\) — fraction of bundles that are **both** fully accurate (\(\mathrm{Acc}_i=1\) for all \(i\in B\)) **and** consistent (\(\Phi=1\)).

## E. Accuracy–consistency gap

Primary gap (bundle-level):

\[
\mathrm{Gap}_{\mathrm{bundle}}
=
\mathrm{Acc}_{\mathrm{bundle}}
-
\mathrm{ConsAcc}
\]

where \(\mathrm{Acc}_{\mathrm{bundle}}\) is the fraction of bundles with all answers individually correct (ignoring \(\Phi\)).

Also report mean Acc vs BCR when useful.

**H1 predicts** \(\mathrm{Gap}_{\mathrm{bundle}}>0\) for strong baselines.

## F. Temporal consistency

Consistency restricted to constraints linking current, historical, and transition answers (subset of \(\mathcal{C}\)).

## G. Provenance consistency

Whether asserted facts and cited sources/events refer to the same valid world version / supporting event.

## Reporting protocol

- Main table: Acc (overall + by family), BCR, ConsAcc, Gap, temporal and provenance scores.  
- Appendix: violation heatmaps by system × constraint family.  
- Never claim “wins on consistency” from Acc alone.

## H. Constraint Satisfaction Rate (CSR) — complementary (2026-08-04)

\[\mathrm{CSR}_b = \frac{\#\{\text{satisfied applicable constraints}\}}{\#\{\text{applicable constraints}\}}\]

- Report mean/median CSR, distribution, by family and difficulty.  
- Violations per bundle (raw + normalized).  
- \(\mathrm{BCR}=1\) iff \(\mathrm{CSR}=1\).  
- **PConsAcc** grid: Acc \(\tau\in\{0.5,0.8\}\) × CSR \(\tau_c\in\{0.8,0.9\}\); report the full grid.  
- Do not invent one composite headline score or cherry-pick a grid cell.  
- Implementation: `experiments/worldconsistmem/src/worldconsistmem/partial_consistency.py`.

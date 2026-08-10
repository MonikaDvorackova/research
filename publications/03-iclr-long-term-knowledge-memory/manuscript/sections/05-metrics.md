---
id: pub-03-sec-05-metrics
title: "Evaluation Metrics"
type: chapter
status: camera-ready-pass
created: 2026-08-04
updated: 2026-08-04
---

# 5. Evaluation Metrics

Metrics are reported jointly. We do not collapse evaluation into a single headline score. Strict BCR remains the primary consistency rate; CSR and partial ConsAcc are complementary diagnostics, especially when BCR floors.

## 5.1 Per-query accuracy

For query \(q_i\) with gold \(y_i^*\) and prediction \(\hat y_i\),

\[
\mathrm{Acc}_i = \mathbf{1}[\hat y_i \equiv y_i^*]
\]

under structured equality (IDs, times, relation slots). Mean query accuracy \(\mathrm{Acc}\) averages \(\mathrm{Acc}_i\) over all scored queries. We also report accuracy by query family.

## 5.2 Bundle Consistency Rate (BCR)

Let \(B\) be the set of bundles. With \(\Phi\) as in Section 3,

\[
\mathrm{BCR}
=
\frac{1}{|B|}
\sum_{b\in B}
\mathbf{1}\bigl[\Phi(\hat Y_b;\mathcal{C}_b)=1\bigr].
\]

BCR is **strict**: a single violated applicable constraint yields \(\Phi=0\) for that bundle. Under weak readers, BCR can floor at zero even when systems differ in how many constraints they satisfy.

## 5.3 Constraint Satisfaction Rate (CSR)

For bundle \(b\),

\[
\mathrm{CSR}_b
=
\frac{\#\{\text{satisfied constraints in }b\}}
{\#\{\text{applicable constraints in }b\}},
\]

with \(\mathrm{CSR}_b=1\) when \(\mathcal{C}_b=\emptyset\). Equivalently, \(\mathrm{BCR}\) is the fraction of bundles with \(\mathrm{CSR}_b=1\). We report mean and median CSR, CSR distributions, CSR by constraint family, and CSR by difficulty/tier.

**Violations per bundle.** We report the mean/median number of violated constraints and normalized violations \(\mathrm{CSR}_b\)’s complement \(1-\mathrm{CSR}_b\) when \(|\mathcal{C}_b|>0\).

CSR does **not** replace BCR. It provides resolution when almost no bundle is fully consistent.

## 5.4 Consistency-aware accuracy

**Strict ConsAcc.** Fraction of bundles that are fully correct (\(\mathrm{Acc}_i=1\) for all \(i\in Q_b\)) **and** \(\Phi=1\).

**Relaxed / partial ConsAcc.** (i) Relaxed ConsAcc: mean query Acc on the bundle \(\ge \tau\) and \(\Phi=1\) (default \(\tau=0.8\)). (ii) Partial ConsAcc grid \(\mathrm{PConsAcc}_{\tau,\tau_c}\): fraction of bundles with mean query Acc \(\ge \tau\) and \(\mathrm{CSR}_b\ge \tau_c\), for predeclared \(\tau\in\{0.5,0.8\}\) and \(\tau_c\in\{0.8,0.9\}\). We report the **full grid**; we do not cherry-pick a favorable cell as a primary claim.

## 5.5 Accuracy–consistency gaps

**Primary gap (\(\mathrm{Gap}_{\mathrm{query}}\)):**

\[
\mathrm{Gap}_{\mathrm{query}} = \mathrm{Acc} - \mathrm{BCR}.
\]

**Secondary gap (\(\mathrm{Gap}_{\mathrm{bundle}}\)):**

\[
\mathrm{Gap}_{\mathrm{bundle}} = \mathrm{Acc}_{\mathrm{bundle}} - \mathrm{ConsAcc}_{\mathrm{strict}},
\]

where \(\mathrm{Acc}_{\mathrm{bundle}}\) is the fraction of bundles with all answers individually correct.

Large positive \(\mathrm{Gap}_{\mathrm{query}}\) indicates high per-query Acc relative to strict joint consistency.

## 5.6 Family diagnostics

- **Temporal consistency / temporal violation rate:** bundles with at least one failed temporal or transition constraint.  
- **Provenance consistency / provenance violation rate:** bundles with at least one failed provenance constraint.  
- **Constraint-family violation rates:** fraction of bundles with \(\ge 1\) failure in each family (uniqueness, temporal, transition, relational, provenance, multi-hop, contradiction).  
- **High-accuracy inconsistent rate:** fraction of bundles with mean Acc \(\ge 0.8\) and \(\Phi=0\).  
- **Abstention and malformed rates** (LLM readers): fraction of queries marked abstain or unparsable under the frozen parser.

## 5.7 Statistical protocol

Primary units for confidence intervals are **worlds**, not queries. We report world-level bootstrap 95% CIs for Acc, BCR, ConsAcc, and CSR where applicable. Queries within a bundle are not treated as independent samples.

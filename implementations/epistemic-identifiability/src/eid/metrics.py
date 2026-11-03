"""Detection statistics and evaluation metrics."""
from __future__ import annotations

import numpy as np
from scipy.stats import chi2
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


def prefix_stat(Z: np.ndarray, T: int):
    """Two-sided fit statistic on the first T steps. Under Q the squared residuals are chi-square.

    Returns (D, reject): D = |log mean z^2|; reject is the alpha=0.05 two-sided chi-square test.
    """
    n = 2 * T
    m2 = (Z[:, :T] ** 2).mean(axis=(1, 2))
    D = np.abs(np.log(np.maximum(m2, 1e-12)))
    reject = (m2 < chi2.ppf(0.025, n) / n) | (m2 > chi2.ppf(0.975, n) / n)
    return D, reject


def auroc(pos: np.ndarray, neg: np.ndarray) -> float:
    y = np.r_[np.ones(len(pos)), np.zeros(len(neg))]
    return float(roc_auc_score(y, np.r_[pos, neg]))


def ece(p: np.ndarray, y: np.ndarray, bins: int = 10) -> float:
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(p, edges[1:-1]), 0, bins - 1)
    return float(sum((idx == k).mean() * abs(p[idx == k].mean() - y[idx == k].mean()) for k in range(bins) if (idx == k).any()))


def platt_ece_brier(score_cal, y_cal, score_test, y_test):
    """Platt scaling fitted on a separate (experimenter-side) calibration batch."""
    clf = LogisticRegression(C=1e4, max_iter=1000).fit(score_cal[:, None], y_cal)
    p = clf.predict_proba(score_test[:, None])[:, 1]
    return ece(p, y_test), float(np.mean((p - y_test) ** 2))


def bootstrap_ci(values, n_boot: int = 2000, seed: int = 0):
    v = np.asarray(values, dtype=float)
    v = v[np.isfinite(v)]
    if len(v) == 0:
        return float("nan"), float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    means = rng.choice(v, (n_boot, len(v))).mean(1)
    return float(v.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))

"""Evaluation metrics, probes, baselines."""
from __future__ import annotations
import numpy as np, torch
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from . import gen


def feats_model(model, u, y, bs=1024):
    out = []
    with torch.no_grad():
        for i in range(0, u.shape[0], bs):
            out.append(model(u[i:i + bs].float(), y[i:i + bs].float(), sample=False)["feat"])
    return torch.cat(out).numpy()


def fit_probe(F, lab, C=0.3):
    sc = StandardScaler().fit(F)
    clf = LogisticRegression(C=C, max_iter=2000).fit(sc.transform(F), lab)
    return sc, clf


def probe_probs(probe, F):
    sc, clf = probe
    pr = clf.predict_proba(sc.transform(F))
    full = np.zeros((F.shape[0], gen.NCLS)); full[:, clf.classes_] = pr
    return full


def ece(probs, lab, bins=10):
    conf = probs.max(1); pred = probs.argmax(1); acc = (pred == lab).astype(float)
    e = 0.0
    for lo in np.linspace(0, 1, bins, endpoint=False):
        s = (conf > lo) & (conf <= lo + 1 / bins)
        if s.any(): e += s.mean() * abs(acc[s].mean() - conf[s].mean())
    return float(e)


def metrics_id(probs, lab):
    """Identifiable test set."""
    lab = np.asarray(lab); pred = probs.argmax(1)
    cm = np.zeros((gen.NCLS, gen.NCLS), int)
    for a, b in zip(lab, pred): cm[a, b] += 1
    return dict(acc=float((pred == lab).mean()), ece=ece(probs, lab),
                nll=float(-np.log(np.clip(probs[np.arange(len(lab)), lab], 1e-6, 1)).mean()), confusion=cm.tolist())


def metrics_eq(probs, thr=0.8):
    """Equivalent (non-identifiable) worlds: any confident claim is unsupported."""
    conf = probs.max(1)
    return dict(claim_rate=float((conf >= thr).mean()), mean_conf=float(conf.mean()))


def bootstrap_ci(values, n=1000, seed=0):
    v = np.asarray(values, float); rng = np.random.default_rng(seed)
    bs = [v[rng.integers(0, len(v), len(v))].mean() for _ in range(n)]
    return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def oracle_probs(inst, u, y, matched=False):
    out = torch.zeros(inst["K"].shape[0], gen.NCLS, dtype=torch.float64)
    for fam in (0, 1):
        idx = (inst["fam"] == fam).nonzero().squeeze(-1)
        if len(idx):
            sub = gen.take(inst, idx)
            out[idx] = (gen.oracle_class_posterior_matched if matched else gen.oracle_class_posterior)(sub, u[idx], y[idx], fam)
    return out.numpy()


def hand_features(u, y):
    """Strong non-neural summary features: lagged regression of dy on u, residual stats, extrema."""
    u = u.numpy(); y = y.numpy(); N, T = y.shape
    dy = np.diff(y, axis=1, prepend=0.0)
    feats = []
    for k in range(0, 9):
        uk = np.pad(u, ((0, 0), (k, 0)))[:, :T]
        feats.append((dy * uk).sum(1) / ((uk ** 2).sum(1) + 1e-6))
    for amp_lo, amp_hi in ((0, .1), (.1, .3), (.3, 1.01)):
        m = (np.abs(u) >= amp_lo) & (np.abs(u) < amp_hi)
        feats.append(((dy * np.sign(u)) * m).sum(1) / (m.sum(1) + 1))
    feats += [np.abs(y).max(1), y.std(1), np.abs(dy).mean(1)]
    for q in (T // 3, 2 * T // 3, T):
        feats.append(y[:, q - T // 3:q].mean(1)); feats.append(np.abs(y[:, q - T // 3:q]).mean(1))
    return np.stack(feats, 1)

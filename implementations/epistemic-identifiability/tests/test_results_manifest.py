"""Immutability guard: every result file frozen at the end of Phase 4 must still match its recorded SHA-256."""
import hashlib
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")


def test_phase4_results_are_unmodified():
    bad, missing = [], []
    for line in open(os.path.join(ROOT, "results", "MANIFEST_phase4.sha256")):
        h, path = line.rstrip("\n").split("  ", 1)
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            missing.append(path)
        else:
            # hashes are of LF-normalised bytes so that a checkout that rewrites line endings does not trip the guard
            data = open(full, "rb").read().replace(b"\r\n", b"\n")
            if hashlib.sha256(data).hexdigest() != h:
                bad.append(path)
    assert not missing, missing
    assert not bad, bad

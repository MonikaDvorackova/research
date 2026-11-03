"""Compare confirmatory decisions and estimates between run A (original) and run B (deterministic repeat).
Usage: PYTHONPATH=src python scripts/compare_runs.py 1 results/bayes1_confirm results/bayes1_confirm_runB"""
import re
import subprocess
import sys


def table(kind, d):
    out = f"{d}/confirmatory.md"
    subprocess.run([sys.executable, "-W", "ignore", "-m", f"eid.confirm_bayes{kind}", "--dir", d, "--out", out], check=True, capture_output=True)
    rows = {}
    for line in open(out):
        m = re.match(r"\| (\w+) \| .*?\| ([-+]?\d+\.\d+) \[([-+]?\d+\.\d+), ([-+]?\d+\.\d+)\].*?\| \*\*(yes|not established)\*\* \|$", line.strip())
        if m:
            rows[m.group(1)] = (float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5))
    return rows


if __name__ == "__main__":
    kind, a, b = sys.argv[1:4]
    A, B = table(kind, a), table(kind, b)
    print("| id | run A mean [95% CI] | run B mean [95% CI] | run A decision | run B decision | same decision |\n|---|---|---|---|---|---|")
    for k in A:
        ra, rb = A[k], B.get(k)
        print(f"| {k} | {ra[0]:+.3f} [{ra[1]:+.3f}, {ra[2]:+.3f}] | {rb[0]:+.3f} [{rb[1]:+.3f}, {rb[2]:+.3f}] | {ra[3]} | {rb[3]} | {'yes' if ra[3] == rb[3] else '**NO**'} |")

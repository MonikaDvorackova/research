"""Guards the immutability of the confirmatory X1 raw data (checksums recorded before analysis)."""
import hashlib, pathlib
D = pathlib.Path(__file__).resolve().parents[1] / "results" / "x1_confirm"


def test_raw_confirmatory_files_match_manifest():
    man = D / "MANIFEST_raw.sha256"
    assert man.exists()
    for line in man.read_text().splitlines():
        h, name = line.split()
        assert hashlib.sha256((D / name).read_bytes()).hexdigest() == h, name

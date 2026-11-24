"""
Run all Nepali spaCy experiments sequentially.
Usage: uv run python experiments/run_all.py
"""
import subprocess
import sys
import os

EXPERIMENTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(EXPERIMENTS_DIR)

scripts = sorted(
    f for f in os.listdir(EXPERIMENTS_DIR)
    if f.startswith("0") and f.endswith(".py")
)

print(f"Found {len(scripts)} experiments\n")

passed = 0
failed = 0

for script in scripts:
    path = os.path.join(EXPERIMENTS_DIR, script)
    print(f"{'─' * 60}")
    print(f"▶ Running: {script}")
    print(f"{'─' * 60}")
    result = subprocess.run(
        [sys.executable, path],
        cwd=PROJECT_ROOT,
        capture_output=False,
    )
    if result.returncode == 0:
        passed += 1
        print(f"✅ {script} PASSED\n")
    else:
        failed += 1
        print(f"❌ {script} FAILED (exit code {result.returncode})\n")

print(f"\n{'=' * 60}")
print(f"RESULTS: {passed} passed, {failed} failed, {len(scripts)} total")
print(f"{'=' * 60}")

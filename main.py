import subprocess
import sys
from pathlib import Path

# ============================================================
# LieFold-AI Main Runner
# ============================================================
# This script sequentially executes all three notebooks:
#
# 1. LieFold-AI.ipynb
# 2. liefold_ai_improved.ipynb
# 3. liefold_ai_improved_R2.ipynb
#
# Usage:
#     python main.py
#
# Requirements:
#     pip install -r requirements.txt
# ============================================================

NOTEBOOKS = [
    "LieFold-AI.ipynb",
    "liefold_ai_improved.ipynb",
    "liefold_ai_improved_R2.ipynb",
]


def run_notebook(notebook_path):
    """
    Execute a Jupyter notebook using nbconvert.
    """

    print("\n" + "=" * 70)
    print(f"Running notebook: {notebook_path}")
    print("=" * 70)

    command = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        notebook_path,
    ]

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"\n[ERROR] Failed to execute: {notebook_path}")
        sys.exit(result.returncode)

    print(f"\n[SUCCESS] Finished: {notebook_path}")


def main():

    print("=" * 70)
    print("LieFold-AI Unified Execution Pipeline")
    print("=" * 70)

    for notebook in NOTEBOOKS:

        notebook_file = Path(notebook)

        if not notebook_file.exists():
            print(f"\n[WARNING] Notebook not found: {notebook}")
            continue

        run_notebook(notebook)

    print("\n" + "=" * 70)
    print("All notebooks completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
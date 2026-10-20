from __future__ import annotations

import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.append(str(SRC))

from pipeline import Pipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    pipeline = Pipeline(str(ROOT))
    results = pipeline.run()
    print("Pipeline completado.")
    print(results)

if __name__ == "__main__":
    main()
from __future__ import annotations

from pathlib import Path
import json
import pandas as pd


def write_excel(rows: list[dict], output_path: str | Path, sheet_name: str = "results"):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(rows)
    df.to_excel(path, index=False, sheet_name=sheet_name)

    return path


def write_json(payload: dict, output_path: str | Path):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    return path
from __future__ import annotations

from pathlib import Path
import pandas as pd


def export_report(rows: list, file_name: str, output_dir: str):
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(rows)
    output_path = out_dir / file_name
    df.to_excel(output_path, index=False)
    return str(output_path)
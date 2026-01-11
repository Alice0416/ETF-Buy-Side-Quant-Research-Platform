from __future__ import annotations
from pathlib import Path
import pandas as pd

def build_universe(
    qc_csv: Path,
    min_rows: int = 750,
    max_zero_vol_frac: float = 0.01,
) -> pd.DataFrame:
    qc = pd.read_csv(qc_csv, parse_dates=["start_date", "end_date"])

    ok = (
        (qc["rows"] >= min_rows) &
        (qc["nonpos_price_rows"] == 0) &
        (qc["bad_high_rows"] == 0) &
        (qc["bad_low_rows"] == 0) &
        ((qc["zero_volume_rows"] / qc["rows"]) <= max_zero_vol_frac)
    )

    universe = qc.loc[ok].copy()
    universe = universe.sort_values(["start_date", "rows"], ascending=[True, False])

    return universe

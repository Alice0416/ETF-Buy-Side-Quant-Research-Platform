from pathlib import Path
from typing import List
import pandas as pd

def list_data_files(
    base_dir: Path,
    exts: List[str] = [".csv", ".txt"]
) -> List[Path]:
    """
    Recursively list data files under base_dir with given extensions.
    """
    files: List[Path] = []
    for ext in exts:
        files.extend(base_dir.rglob(f"*{ext}"))
    return sorted(files)

REQUIRED_COLS = ["Date", "Open", "High", "Low", "Close", "Volume"]

def read_one_ohlcv(fp: Path) -> pd.DataFrame:
    """
    Read one OHLCV file (csv/txt) and standardize:
    - Keep Date, Open, High, Low, Close, Volume
    - Date -> DatetimeIndex
    - Numeric coercion, drop bad rows
    - Sort by Date, drop duplicated Date
    """
    # 1) read
    df = pd.read_csv(fp, sep=",")  # your files are comma-separated

    # 2) column check
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"{fp.name}: missing columns {missing}")

    # 3) keep only required
    df = df[REQUIRED_COLS].copy()

    # 4) parse time + numeric
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for c in ["Open", "High", "Low", "Close", "Volume"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # 5) drop invalid rows
    df = df.dropna(subset=REQUIRED_COLS)

    # 6) set index + sort + dedupe
    df = df.sort_values("Date").drop_duplicates("Date").set_index("Date")

    return df

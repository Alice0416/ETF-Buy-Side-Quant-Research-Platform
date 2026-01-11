from pathlib import Path
from src.universe import build_universe

u = build_universe(Path("outputs/qc_summary.csv"))
print("Universe size:", len(u))
print(u[["ticker", "rows", "start_date", "end_date"]].head())
u.to_csv("outputs/universe_list.csv", index=False)

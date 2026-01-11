from pathlib import Path
import pandas as pd
from src.features import load_universe_prices
from src.backtest import backtest_long_only

prices = load_universe_prices(
    universe_csv=Path("outputs/universe_list.csv"),
    curated_dir=Path("data/curated/ETFs"),
)

signal = pd.read_parquet("outputs/signal_mom1m.parquet")

bt = backtest_long_only(
    prices=prices,
    signal=signal,
    top_n=10,
    cost_bps=10.0,
)

bt.to_csv("outputs/backtest_top10.csv")
print(bt.tail())

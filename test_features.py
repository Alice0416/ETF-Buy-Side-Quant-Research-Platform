from pathlib import Path
from src.features import load_universe_prices, momentum_1m

prices = load_universe_prices(
    universe_csv=Path("outputs/universe_list.csv"),
    curated_dir=Path("data/curated/ETFs"),
)

signal_mom1m = momentum_1m(prices, lookback=21)

print("prices shape:", prices.shape)
print("signal shape:", signal_mom1m.shape)
print(signal_mom1m.tail())
signal_mom1m.to_parquet("outputs/signal_mom1m.parquet")

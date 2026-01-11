from __future__ import annotations
import pandas as pd
import numpy as np

def monthly_rebalance_dates(prices: pd.DataFrame) -> pd.DatetimeIndex:
    return prices.resample("M").last().index

def compute_positions(signal: pd.DataFrame, rebalance_dates, top_n: int) -> pd.DataFrame:
    # On rebalance dates, rank cross-sectionally and pick top N (equal weight)
    pos = pd.DataFrame(0.0, index=signal.index, columns=signal.columns)
    for d in rebalance_dates:
        if d not in signal.index:
            continue
        scores = signal.loc[d].dropna()
        picks = scores.sort_values(ascending=False).head(top_n).index
        w = 1.0 / top_n if top_n > 0 else 0.0
        pos.loc[d, picks] = w
    # Forward-fill positions between rebalances
    pos = pos.ffill().fillna(0.0)
    return pos

def backtest_long_only(
    prices: pd.DataFrame,
    signal: pd.DataFrame,
    top_n: int = 10,
    cost_bps: float = 10.0,
) -> pd.DataFrame:
    # daily returns
    rets = prices.pct_change().fillna(0.0)

    # rebalance schedule
    rebal_dates = monthly_rebalance_dates(prices)

    # positions
    pos = compute_positions(signal, rebal_dates, top_n)

    # turnover & cost
    turnover = pos.diff().abs().sum(axis=1)
    cost = turnover * (cost_bps / 1e4)

    # portfolio return
    port_ret = (pos.shift(1) * rets).sum(axis=1) - cost

    equity = (1 + port_ret).cumprod()

    out = pd.DataFrame({
        "portfolio_return": port_ret,
        "equity": equity,
        "turnover": turnover,
        "cost": cost,
    })
    return out

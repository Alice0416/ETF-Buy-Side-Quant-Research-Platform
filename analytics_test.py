import pandas as pd
import matplotlib.pyplot as plt
from src.analytics import performance_metrics

bt = pd.read_csv("outputs/backtest_top10.csv", parse_dates=["Date"], index_col="Date")

metrics = performance_metrics(bt["portfolio_return"])
print(metrics)

# Equity curve
plt.figure(figsize=(10,4))
plt.plot(bt.index, bt["equity"])
plt.title("Equity Curve (Top-10 Momentum)")
plt.grid(True)
plt.savefig("outputs/equity_curve.png", dpi=150)
plt.close()

# Drawdown
running_max = bt["equity"].cummax()
drawdown = bt["equity"] / running_max - 1

plt.figure(figsize=(10,4))
plt.plot(bt.index, drawdown)
plt.title("Drawdown")
plt.grid(True)
plt.savefig("outputs/drawdown.png", dpi=150)
plt.close()

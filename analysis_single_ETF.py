import pandas as pd
import matplotlib.pyplot as plt



# ======================================
# Step 1: read raw data
# ======================================
df = pd.read_csv(
    "data/ETFs/aadr.us.txt",   # ← 你的真实文件名
    sep=","
)


# ======================================
# Step 2: time index
# ======================================
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
df = df.sort_index()


# ======================================
# Step 3: daily return
# 计算日收益率
# ======================================
df["daily_return"] = df["Close"].pct_change().fillna(0.0)


# ======================================
# Step 4: equity curve
# 如果从第一天开始一直拿着，会变成多少钱
# ======================================
df["equity"] = (1 + df["daily_return"]).cumprod()
print(df[["Close", "daily_return", "equity"]].head())

# ======================================
# Step 5: plot equity curve
# 这条线回答的只有一个问题：“如果我从第一天一直拿着，会发生什么？”
# ======================================
plt.figure(figsize=(10, 4))
plt.plot(df.index, df["equity"])
plt.xlabel("Date")
plt.ylabel("Equity")
plt.title("Equity Curve (Buy and Hold)")
plt.grid(True)
plt.show()



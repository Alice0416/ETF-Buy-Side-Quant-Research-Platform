# Buy-Side ETF Quant Research Pipeline

An end-to-end buy-side style quantitative research project using historical US ETF price-volume data.

This project implements a full systematic investment research loop, covering data cleaning and validation, universe construction, cross-sectional signal research, transaction-cost-aware backtesting, and performance & risk reporting.

---

## 1. Research Objective

The goal of this project is to evaluate whether a simple and interpretable cross-sectional momentum signal can generate robust portfolio-level performance when applied to a broad ETF universe under realistic trading assumptions.

The project is designed from a buy-side perspective, emphasizing:
- data quality and robustness
- explicit universe definition
- separation of signals and trading rules
- transaction costs and turnover
- risk-aware evaluation

---

## 2. Data

- Source: Kaggle US Stocks & ETFs Price-Volume Dataset
- Asset class: US-listed ETFs
- Frequency: Daily
- Fields used: OHLCV (Open, High, Low, Close, Volume)

### Data Handling
- Raw data is treated as read-only
- All assets are standardized into a unified OHLCV format
- Automated data quality checks are applied to each ETF
- Cleaned data is stored in parquet format for research efficiency

Raw data and generated artifacts are intentionally excluded from version control.

---

## 3. Research Pipeline

The research workflow follows a structured ABCDE pipeline:

### A. Data Pipeline & Quality Control
- Batch discovery of ETF files
- OHLCV standardization
- Logical consistency checks (price validity, OHLC constraints)
- Liquidity diagnostics (zero-volume days)
- Output: QC summary + curated parquet files

### B. Universe Construction
Assets are included in the research universe only if they satisfy:
- sufficient historical length
- no price logic violations
- acceptable liquidity characteristics

This step avoids survivorship and selection bias by separating eligibility from performance.

### C. Signal (Feature) Research
- Signal: 1-month cross-sectional momentum
- Definition: past 21-trading-day return
- Signals are computed independently of trading rules

This layer expresses relative strength across eligible ETFs on each date.

### D. Backtesting
- Strategy: Long-only, Top-N ETFs by signal rank
- Rebalancing frequency: Monthly
- Portfolio construction: Equal-weight
- Transaction costs: Proportional to turnover (bps-based)

The backtest simulates realistic capital deployment rather than theoretical signal returns.

### E. Performance & Risk Reporting
Evaluation metrics include:
- Equity curve
- Maximum drawdown
- CAGR, volatility, Sharpe ratio
- Turnover and trading costs

Both return and risk characteristics are explicitly assessed.

---

## 4. Key Results

Results are evaluated at the portfolio level rather than on individual ETFs.

Primary diagnostics:
- Equity curve: long-term capital growth
- Drawdown profile: downside risk and investor pain
- Risk-adjusted metrics: Sharpe ratio, volatility

(Exact numerical results depend on parameter choices and are reproducible via the pipeline.)

---

## 5. Project Structure
src/
io.py # data discovery & single-asset loading
quality.py # data quality metrics
curate.py # batch data pipeline
universe.py # universe construction rules
features.py # signal definitions
backtest.py # portfolio simulation
analytics.py # performance & risk metrics
Data and outputs are intentionally excluded from version control.

---

## 6. Limitations & Extensions

This project intentionally uses a simple rule-based signal as a baseline.

Natural extensions include:
- volatility-adjusted momentum
- multi-horizon signals
- out-of-sample testing
- machine learning-based signal aggregation

The current structure is designed to support such extensions without modifying the core pipeline.

---

## 7. Summary

This project demonstrates a complete buy-side quantitative research workflow, emphasizing robustness, interpretability, and engineering discipline over model complexity.s

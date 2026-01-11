from pathlib import Path
from src.io import list_data_files, read_one_ohlcv

files = list_data_files(Path("Data/ETFs"))
fp = files[0]

df = read_one_ohlcv(fp)

# print("file:", fp)
# print(df.head())
# print(df.dtypes)
# print("rows:", len(df), "start:", df.index.min(), "end:", df.index.max())
from src.quality import qc_metrics

qc = qc_metrics(df)
print(qc)

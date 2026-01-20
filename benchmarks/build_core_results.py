import pandas as pd
from pathlib import Path

OUT = Path("benchmarks")
OUT.mkdir(exist_ok=True)

rows = []

# In-dataset
rows.append({
    "train": "StudentLife",
    "test": "StudentLife",
    "setting": "in-dataset",
    "roc_auc": 0.5268,
    "balanced_accuracy": 0.5232
})

# Cross-dataset
rows.append({
    "train": "StudentLife",
    "test": "Depresjon",
    "setting": "cross-dataset",
    "roc_auc": 0.6576,
    "balanced_accuracy": 0.5000
})

rows.append({
    "train": "Depresjon",
    "test": "StudentLife",
    "setting": "cross-dataset",
    "roc_auc": 0.4671,
    "balanced_accuracy": 0.5000
})

df = pd.DataFrame(rows)
df.to_csv(OUT / "core_results.csv", index=False)

print("Core benchmark results written:")
print(df)
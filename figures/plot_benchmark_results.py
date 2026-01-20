import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks" / "benchmark_results.csv"
OUT = ROOT / "figures" / "benchmark_performance.png"

df = pd.read_csv(BENCH)

# Create readable labels
df["setting"] = df["train"].str.replace("_model_table", "") + " → " + df["test"].str.replace("_model_table", "")

settings = df["setting"].tolist()
roc_auc = df["roc_auc"].values
bal_acc = df["balanced_accuracy"].values

x = np.arange(len(settings))
width = 0.35

plt.figure(figsize=(10, 5))

plt.bar(x - width/2, roc_auc, width, label="ROC-AUC")
plt.bar(x + width/2, bal_acc, width, label="Balanced Accuracy")

plt.axhline(0.5, linestyle="--", color="gray", label="Chance level")

plt.xticks(x, settings, rotation=25, ha="right")
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("In-dataset vs Cross-dataset Generalization Performance")

plt.legend()
plt.tight_layout()

OUT.parent.mkdir(exist_ok=True)
plt.savefig(OUT, dpi=200)
plt.close()

print(f"Saved figure to: {OUT}")
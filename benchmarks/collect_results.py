import pandas as pd
from pathlib import Path

BENCH = Path("benchmarks")

def main():
    files = [
        BENCH / "studentlife_in_dataset.csv",
        BENCH / "depresjon_in_dataset.csv",
        BENCH / "studentlife_to_depresjon.csv",
        BENCH / "depresjon_to_studentlife.csv",
    ]

    dfs = []
    for f in files:
        if not f.exists():
            raise FileNotFoundError(f"Missing benchmark file: {f}")
        dfs.append(pd.read_csv(f))

    df = pd.concat(dfs, ignore_index=True)

    # enforce clean, consistent column order if present
    preferred_cols = [
        "train",
        "test",
        "shared_features",
        "n_shared_features",
        "roc_auc",
        "balanced_accuracy",
    ]
    cols = [c for c in preferred_cols if c in df.columns]
    df = df[cols] if cols else df

    out = BENCH / "benchmark_results.csv"
    df.to_csv(out, index=False)

    print("Cross-dataset benchmark summary written to:", out)
    print(df)

if __name__ == "__main__":
    main()
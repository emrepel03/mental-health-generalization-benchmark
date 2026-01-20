import argparse
from pathlib import Path
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, balanced_accuracy_score


def load_table(path):
    df = pd.read_csv(path)
    if "label" not in df.columns:
        raise ValueError(f"'label' column missing in {path}")
    return df


def main(args):
    train_df = load_table(args.train)
    test_df  = load_table(args.test)

    # Identify shared feature columns
    exclude = {"participant_id", "label", "phq9_sum"}
    train_feats = set(train_df.columns) - exclude
    test_feats  = set(test_df.columns) - exclude
    shared = sorted(train_feats & test_feats)

    if len(shared) == 0:
        raise ValueError("No shared features between train and test datasets.")

    print(f"Shared features ({len(shared)}): {shared}")

    X_train = train_df[shared].values
    y_train = train_df["label"].values
    X_test  = test_df[shared].values
    y_test  = test_df["label"].values

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    probs = model.predict_proba(X_test)[:, 1]
    preds = (probs >= 0.5).astype(int)

    roc_auc = roc_auc_score(y_test, probs)
    bal_acc = balanced_accuracy_score(y_test, preds)

    print(f"ROC-AUC: {roc_auc:.4f}")
    print(f"Balanced Accuracy: {bal_acc:.4f}")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    result = pd.DataFrame([{
        "train": Path(args.train).stem,
        "test": Path(args.test).stem,
        "n_shared_features": len(shared),
        "roc_auc": roc_auc,
        "balanced_accuracy": bal_acc
    }])

    result.to_csv(out_path, index=False)
    print(f"Saved results to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cross-dataset benchmark runner")
    parser.add_argument("--train", required=True, help="Training CSV")
    parser.add_argument("--test", required=True, help="Testing CSV")
    parser.add_argument("--out", required=True, help="Output CSV")

    args = parser.parse_args()
    main(args)
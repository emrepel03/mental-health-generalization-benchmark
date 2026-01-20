import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, balanced_accuracy_score

df = pd.read_csv("features/tables/studentlife_model_table.csv")

X = df.drop(columns=["participant_id", "label", "phq9_sum"])
y = df["label"]

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

aucs = []
baccs = []

for train_idx, test_idx in skf.split(X, y):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(penalty="l2", solver="liblinear")
    model.fit(X_train, y_train)

    probs = model.predict_proba(X_test)[:, 1]
    preds = model.predict(X_test)

    aucs.append(roc_auc_score(y_test, probs))
    baccs.append(balanced_accuracy_score(y_test, preds))

print("StudentLife Logistic Regression")
print("ROC-AUC:", np.mean(aucs))
print("Balanced Accuracy:", np.mean(baccs))
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, balanced_accuracy_score

train_df = pd.read_csv("features/tables/depresjon_model_table.csv")
test_df  = pd.read_csv("features/tables/studentlife_model_table.csv")

train_features = [c for c in train_df.columns if c not in ["participant_id", "label"]]
test_features  = [c for c in test_df.columns  if c not in ["participant_id", "label", "phq9_sum"]]

shared = sorted(set(train_features).intersection(set(test_features)))

print("Shared features:", shared)
print("Num shared features:", len(shared))

X_train = train_df[shared]
y_train = train_df["label"]

X_test  = test_df[shared]
y_test  = test_df["label"]

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

model = LogisticRegression(penalty="l2", solver="liblinear")
model.fit(X_train, y_train)

probs = model.predict_proba(X_test)[:, 1]
preds = model.predict(X_test)

print("\nTrain: Depresjon → Test: StudentLife")
print("ROC-AUC:", roc_auc_score(y_test, probs))
print("Balanced Accuracy:", balanced_accuracy_score(y_test, preds))
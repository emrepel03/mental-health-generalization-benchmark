import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, balanced_accuracy_score

# Load data
train_df = pd.read_csv("features/tables/studentlife_model_table.csv")
test_df  = pd.read_csv("features/tables/depresjon_model_table.csv")

# Define candidate feature columns (exclude IDs/labels/outcome helpers)
train_features = [c for c in train_df.columns if c not in ["participant_id", "label", "phq9_sum"]]
test_features  = [c for c in test_df.columns  if c not in ["participant_id", "label"]]

# Use ONLY shared columns (this is the cross-dataset-safe baseline)
shared = sorted(set(train_features).intersection(set(test_features)))

print("Shared features:", shared)
print("Num shared features:", len(shared))

X_train = train_df[shared]
y_train = train_df["label"]

X_test  = test_df[shared]
y_test  = test_df["label"]

# Normalize using TRAIN stats only
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# Train
model = LogisticRegression(penalty="l2", solver="liblinear")
model.fit(X_train, y_train)

# Evaluate
probs = model.predict_proba(X_test)[:, 1]
preds = model.predict(X_test)

print("\nTrain: StudentLife → Test: Depresjon")
print("ROC-AUC:", roc_auc_score(y_test, probs))
print("Balanced Accuracy:", balanced_accuracy_score(y_test, preds))
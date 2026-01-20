import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def fit_and_get_coefs(df, feature_cols):
    X = df[feature_cols]
    y = df["label"]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    model = LogisticRegression(penalty="l2", solver="liblinear")
    model.fit(X, y)

    return pd.Series(model.coef_[0], index=feature_cols)

# Load data
sl = pd.read_csv("features/tables/studentlife_model_table.csv")
dp = pd.read_csv("features/tables/depresjon_model_table.csv")

features = ["activity_mean", "activity_active_ratio"]

coef_sl = fit_and_get_coefs(sl, features)
coef_dp = fit_and_get_coefs(dp, features)

summary = pd.DataFrame({
    "StudentLife_coef": coef_sl,
    "Depresjon_coef": coef_dp,
    "Same_sign": np.sign(coef_sl) == np.sign(coef_dp)
})

print(summary)
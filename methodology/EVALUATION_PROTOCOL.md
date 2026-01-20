# Evaluation Protocol

## Datasets
- StudentLife
- Depresjon

## Task
Binary classification of depression status using passive-sensing features.

## Features
- Only features present in BOTH train and test datasets are used.
- Feature sets are automatically intersected per evaluation.
- No label-derived features are allowed.

## Models
- Logistic Regression
- StandardScaler fitted on training data only.

## Evaluation Settings
1. In-dataset (train = test, same dataset)
2. Cross-dataset (train ≠ test)

## Metrics
- ROC-AUC
- Balanced Accuracy

## Leakage Rules
- No subject overlap between datasets.
- No use of dataset-specific metadata.
- No hyperparameter tuning across datasets.
- No feature engineering after seeing results.

## Reproducibility
- All results are generated via `benchmarks/run.py`
- Aggregated via `benchmarks/collect_results.py`
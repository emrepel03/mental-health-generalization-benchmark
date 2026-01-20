# Benchmark Results

This table summarizes all benchmark evaluations performed under the frozen protocol.

## Logistic Regression Results

| Train Dataset | Test Dataset | Setting        | # Shared Features | ROC-AUC | Balanced Accuracy |
|--------------|-------------|----------------|------------------|--------|-------------------|
| StudentLife | StudentLife | In-dataset     | 7                | 0.789  | 0.625 |
| Depresjon   | Depresjon   | In-dataset     | 3                | 0.688  | 0.624 |
| StudentLife | Depresjon   | Cross-dataset  | 2                | 0.658  | 0.500 |
| Depresjon   | StudentLife | Cross-dataset  | 2                | 0.467  | 0.500 |

## Key Observation

Models that perform moderately well in-dataset collapse to chance-level
balanced accuracy when transferred across datasets, despite using the same
behavioral modality.

This demonstrates a clear generalization gap.
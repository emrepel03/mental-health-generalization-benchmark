# Baseline Logistic Regression Results

## In-Dataset (StudentLife)

- ROC-AUC: ~0.53
- Balanced Accuracy: ~0.52
- Notes: Slightly above chance, no evidence of leakage

## Cross-Dataset (Shared Features Only)

### StudentLife → Depresjon
- Shared features: activity_mean, activity_active_ratio
- ROC-AUC: ~0.66
- Balanced Accuracy: 0.50
- Interpretation: Ranking survives, threshold collapses

### Depresjon → StudentLife
- Shared features: activity_mean, activity_active_ratio
- ROC-AUC: ~0.47
- Balanced Accuracy: 0.50
- Interpretation: No transferable signal in this direction

## Key Takeaway

Cross-dataset generalization is asymmetric and feature-constrained.
Performance inflation in single-dataset studies is expected.
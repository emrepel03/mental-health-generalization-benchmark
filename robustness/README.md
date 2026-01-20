# Feature Robustness Analysis

This analysis evaluates whether shared passive-sensing features exhibit
consistent effects across datasets.

## Results

Two shared features were evaluated:

| Feature | StudentLife Sign | Depresjon Sign | Stable |
|--------|-----------------|---------------|--------|
| activity_mean | Negative | Negative | Yes |
| activity_active_ratio | Positive | Negative | No |

## Interpretation

- Overall activity level (activity_mean) is a robust signal that generalizes
  across populations and sensing setups.

- Relative activity proportion (activity_active_ratio) is population-dependent
  and reverses sign between student and clinical cohorts, likely reflecting
  different behavioral interpretations (healthy activity vs agitation).

## Implication

Models relying on unstable features may appear performant in single-dataset
settings but fail under deployment shift.
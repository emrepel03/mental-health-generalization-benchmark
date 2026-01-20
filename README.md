## What this benchmark shows (TL;DR)

This project evaluates whether mental-health prediction models trained on passive sensing data
generalize across datasets and populations.

**Key finding:**  
Models that appear to perform above chance within a single dataset **fail to generalize reliably**
when evaluated on a different dataset, even when using identical features and evaluation protocols.

### Core results (logistic regression, frozen protocol)

| Train dataset | Test dataset | Setting | ROC-AUC | Balanced accuracy |
|---|---|---|---|---|
| StudentLife | StudentLife | In-dataset | 0.53 | 0.52 |
| StudentLife | Depresjon | Cross-dataset | 0.66 | 0.50 |
| Depresjon | StudentLife | Cross-dataset | 0.47 | 0.50 |

### Interpretation
- In-dataset performance is **near chance**, despite standard features and labels.
- Cross-dataset ROC-AUC can appear moderate, but **balanced accuracy collapses to chance**,
  indicating decision thresholds do not transfer.
- Feature signs are **not stable across datasets**, suggesting dataset-specific correlations
  rather than generalizable behavioral signals.

### Why this matters
Many mental-health ML papers report strong single-dataset performance.
This benchmark shows that such results **do not guarantee robustness, transportability, or clinical readiness**.

This repository provides a **reproducible, leakage-safe evaluation framework**
to test generalization, robustness, and fairness limitations before deployment.

## What this benchmark shows

This project demonstrates that mental-health prediction models based on passive sensing data
can achieve seemingly strong performance when evaluated within the same dataset,
yet fail to generalize across datasets collected from different populations and contexts.
Despite using identical features and models, cross-dataset performance collapses to chance-level
Balanced Accuracy, exposing a critical gap between reported accuracy and real-world reliability.
These results highlight the necessity of standardized cross-dataset benchmarks before deploying
machine-learning systems in clinical or population-level mental-health settings.
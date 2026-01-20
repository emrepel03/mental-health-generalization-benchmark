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
# Mental Health Generalization Benchmark

A reproducible benchmark evaluating whether mental‑health prediction models trained on passive sensing data
generalize across datasets, populations, and collection contexts.

---

## TL;DR — What this benchmark shows

**Core finding:**  
Mental‑health prediction models that appear to perform above chance within a single dataset
**do not generalize reliably** when evaluated on a different dataset, even when using
identical features, models, and evaluation protocols.

Cross‑dataset evaluation exposes a critical gap between reported performance and real‑world reliability.

---

## Core Results (Logistic Regression, Frozen Protocol)

| Train dataset | Test dataset | Setting | ROC‑AUC | Balanced accuracy |
|---|---|---|---|---|
| StudentLife | StudentLife | In‑dataset | 0.53 | 0.52 |
| Depresjon | Depresjon | In‑dataset | 0.69 | 0.62 |
| StudentLife | Depresjon | Cross‑dataset | 0.66 | 0.50 |
| Depresjon | StudentLife | Cross‑dataset | 0.47 | 0.50 |

![Benchmark performance across datasets](figures/benchmark_performance.png)

**Key observation:**  
While ROC‑AUC may appear moderate in cross‑dataset settings, **balanced accuracy collapses to chance**,
indicating that learned decision boundaries do not transfer across datasets.

---

## Interpretation

- In‑dataset performance is **near chance**, despite standard feature engineering and widely used labels.
- Cross‑dataset evaluation reveals **non‑transferable decision thresholds**, even when features overlap.
- Feature coefficients are **not stable across datasets**, suggesting dataset‑specific correlations
  rather than robust behavioral signals.

These results indicate that many reported single‑dataset findings may reflect
overfitting to population‑specific or context‑specific structure.

---

## Why this matters

A large body of mental‑health machine‑learning literature reports strong performance
using passive sensing data, often without external validation.

This benchmark demonstrates that:
- Single‑dataset performance **does not guarantee robustness**
- Cross‑population transportability remains largely untested
- Deployment‑ready claims require stronger evidence than in‑dataset metrics alone

Without standardized cross‑dataset evaluation, reported accuracy can be misleading.

---

## What this repository provides

This repository offers a **leakage‑safe, reproducible benchmark pipeline** for evaluating:

- In‑dataset vs cross‑dataset generalization
- Feature overlap and stability
- Performance degradation under dataset shift
- Minimum metadata requirements for fairness analysis

The framework is designed to be extended with additional datasets, models, and sensing modalities.

---

## Repository structure (high‑level)

- `features/` — feature extraction and label construction
- `benchmarks/` — benchmark runners and result aggregation
- `models/` — baseline models (logistic regression)
- `evaluation/` — metrics and evaluation utilities
- `robustness/` — feature stability analysis
- `fairness/` — metadata availability and subgroup tooling
- `figures/` — benchmark visualizations

---

## Reproducibility

All reported results can be reproduced end‑to‑end using the provided scripts:

```bash
python features/extraction/build_feature_tables.py
python benchmarks/run.py
python benchmarks/collect_results.py
python figures/plot_benchmark_results.py
```

No manual notebook steps are required.

---

## Scope and limitations

- Datasets differ in population, sensing resolution, and label construction
- Only overlapping features are used in cross‑dataset evaluation
- Results should be interpreted as a **lower bound** on generalization performance

The goal of this benchmark is not to maximize accuracy,
but to **stress‑test generalization claims** under realistic conditions.

---

## Citation

If you use this benchmark or build upon it, please cite the repository and the original datasets
used in the evaluation.
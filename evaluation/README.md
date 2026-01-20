# Evaluation Protocol (Locked)

This document defines the fixed evaluation protocol for all experiments in this repository.

Once defined, the following are NOT changed:
- data splits
- metrics
- leakage rules
- target definitions

## Tasks

We evaluate binary depression classification.

- StudentLife: PHQ-9 ≥ 10 → depressed (1), else non-depressed (0)
- Depresjon: condition = depressed (1), control = non-depressed (0)

## Splits

### In-dataset evaluation
- Stratified 5-fold cross-validation
- Split unit: participant
- No temporal leakage (aggregated features only)

### Cross-dataset evaluation
- Train on StudentLife, test on Depresjon
- Train on Depresjon, test on StudentLife
- No rebalancing across datasets

## Metrics

Primary:
- ROC-AUC

Secondary:
- Balanced accuracy
- Precision / Recall
- F1-score

## Leakage Rules (Strict)

- Labels are never used during feature extraction
- No normalization across train + test together
- All preprocessing fitted on training data only
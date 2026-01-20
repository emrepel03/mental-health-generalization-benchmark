# Benchmark Protocol (Frozen)

This document defines the fixed evaluation protocol used in this project.
All reported results must follow this protocol unless explicitly stated.

## Datasets
- StudentLife (PHQ-9 binary label)
- Depresjon (clinical condition vs control)

## Feature Construction
- Features are computed per participant
- No temporal overlap between features and labels
- No feature uses label information

## Labels
- StudentLife: PHQ-9 sum ≥ 10 → depressed (1), else (0)
- Depresjon: condition_* → 1, control_* → 0

## Evaluation Settings
1. In-dataset evaluation
   - Train and test on same dataset
   - Stratified split
2. Cross-dataset evaluation
   - Train on one dataset, test on the other
   - Only shared features are used

## Shared Feature Rule
Only features present in *both* datasets are allowed in cross-dataset runs.

## Models
- Logistic Regression (scikit-learn default, standardized features)

## Metrics
- ROC-AUC
- Balanced Accuracy

## Leakage Rules
- No participant appears in both train and test
- No feature derived from labels
- Scaling fitted on training data only

## Status
This protocol is frozen.
Any deviation must be explicitly documented.
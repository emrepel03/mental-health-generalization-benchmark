# Evaluation Protocol

This document defines the evaluation setup used in this project.
All choices here are fixed before any modeling to avoid bias, leakage, or post-hoc tuning.

## Task Definition
- Binary classification
- Target: Depression (yes / no)
- One prediction per participant

## Datasets
- StudentLife
- Depresjon

## Unit of Prediction
- Participant-level
- Each subject contributes exactly one feature vector and one label

## Evaluation Regimes

### 1. In-Dataset Evaluation
- Train and test on the same dataset
- Subject-level split
- Stratified by label
- Purpose: establish an upper-bound performance

### 2. Cross-Dataset Evaluation
- Train on one dataset
- Test on the other dataset
- No refitting, no recalibration
- Purpose: measure generalization under dataset shift

## Splitting Rules
- No participant appears in both train and test
- No mixing of datasets during cross-dataset evaluation

## Metrics
- ROC-AUC
- Balanced Accuracy
- Expected Calibration Error (ECE)
- Sensitivity at fixed specificity

Accuracy alone is not reported.

## Leakage Prevention
- Feature normalization is fit on training data only
- No label information used during feature extraction
- No dataset-aware tuning
- No temporal leakage

This protocol is fixed and applied consistently across all experiments.
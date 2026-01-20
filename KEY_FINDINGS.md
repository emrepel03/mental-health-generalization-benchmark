# Key Findings

## 1. In-dataset performance is misleading
Models trained and evaluated on the same dataset achieve apparently strong performance
(StudentLife ROC-AUC ≈ 0.79, Depresjon ROC-AUC ≈ 0.69).
This level of performance is typical of results reported in the literature.

## 2. Cross-dataset generalization fails
When models are trained on one dataset and evaluated on another, performance collapses.
Balanced Accuracy drops to chance level (≈ 0.50) in both transfer directions,
indicating that the models fail to make reliable predictions on unseen populations.

## 3. ROC-AUC alone hides failure
Although ROC-AUC remains moderately high in some cross-dataset settings,
Balanced Accuracy reveals that predictions are not clinically useful.
This demonstrates that ROC-AUC alone is insufficient for evaluating deployment readiness.

## Conclusion
Mental-health prediction models trained on passive sensing data learn dataset-specific signals
that do not generalize across studies. Benchmarking cross-dataset performance is therefore
essential before any clinical or real-world deployment.
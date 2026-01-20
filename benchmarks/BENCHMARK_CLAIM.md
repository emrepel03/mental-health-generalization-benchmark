# Benchmark Claim

This benchmark evaluates whether behavioral features extracted from passive
sensing data generalize across independent mental-health datasets.

Using two public datasets with different populations, sensing pipelines, and
label definitions, we show that:

1. In-dataset performance is moderate and above chance.
2. Cross-dataset performance collapses to chance-level balanced accuracy.
3. Feature coefficients are unstable across datasets.

These results indicate that current passive-sensing mental-health models are
highly dataset-specific and do not generalize reliably without explicit
cross-dataset validation.

This benchmark provides a minimal, reproducible framework to measure and
expose this generalization gap.
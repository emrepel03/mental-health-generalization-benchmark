# Minimum Metadata Required for Credible Fairness Audits

## What we found in this benchmark
Both datasets used in this benchmark (StudentLife, Depresjon) contain **no subgroup metadata in the modeling tables** (no gender, age, or device/platform identifiers).  
Therefore, **subgroup fairness metrics cannot be computed** and any fairness claim would be invalid.

## Minimum metadata (must-have) to run a credible audit
| Metadata field | Why it matters | Minimum format |
|---|---|---|
| Gender / sex | performance gaps are common; clinical risk if sensitivity differs | categorical (e.g., female/male/other/unknown) |
| Age | digital behavior and symptoms vary by age; risk of hidden shift | binned age (e.g., 18–24, 25–34, …) |
| Device ecosystem | sensing differs by OS/hardware; can create fake “model differences” | Android vs iOS; wearable model if applicable |
| Country / site | cultural + healthcare context shifts label meaning and behavior | country code or site ID |
| Enrollment / study arm | clinical vs non-clinical populations are not comparable | indicator for clinical recruitment / diagnosis status |

## Strong recommendation for future dataset additions
If a dataset does not include at least **gender + age-bin + device/platform**, it can still be used for **generalization stress-testing**, but it should be treated as **not auditable for fairness**.
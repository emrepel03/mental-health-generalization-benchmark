

# Datasets Used in This Benchmark

This benchmark evaluates generalization, robustness, and fairness of mental-health prediction models using **public passive-sensing datasets**.
Dataset selection is intentionally limited and fixed to enable clean cross-dataset evaluation and full reproducibility.

Once defined here, **datasets and variables are frozen** and will not be expanded later.

---

## 1. StudentLife Dataset

**Reference**  
Wang et al. (2014), *StudentLife: Assessing Mental Health, Academic Performance and Behavioral Trends of College Students using Smartphones* (UbiComp).

**Population**
- 48 undergraduate students
- Dartmouth College, USA
- Single academic term (~10 weeks)
- Android smartphone users only

**Data Modality**
- Smartphone-based passive sensing
- Continuous background collection

**Mental Health Label**
- Depression measured using **PHQ-9**
- Binary label defined as:
  - Depressed: PHQ-9 ≥ 10
  - Not depressed: PHQ-9 < 10
- Labels derived from `survey/PHQ-9.csv`

**Passive-Sensing Feature Families Used**
Only aggregated features are used. No raw time-series models.

- **Mobility**
  - GPS-based daily distance
  - Location entropy
  - Time spent at primary locations
- **Activity**
  - Inferred physical activity states
  - Daily active vs inactive duration
- **Sleep**
  - Sleep duration and variability (PSQI-based summaries)
- **Phone Use**
  - App usage duration
  - Screen interaction proxies
- **Social Proxies**
  - Call and SMS counts per day

**Explicitly Excluded**
- EMA free-text responses
- Affect scales (PANAS)
- Stress, loneliness, flourishing scores
- Academic performance variables
- Any raw accelerometer or GPS sequences

**Known Limitations**
- Small sample size
- Homogeneous population (students)
- Single country (USA)
- Android-only device ecosystem
- Limited demographic diversity

---

## 2. Depresjon Dataset

**Reference**  
Garcia-Ceja et al. (2018), *Depresjon: A Motor Activity Database of Depression Episodes in Unipolar and Bipolar Patients* (ACM MMSys).

**Population**
- 23 depressed patients (unipolar + bipolar)
- 32 healthy controls
- Adult European clinical population

**Data Modality**
- Wearable actigraphy (Actiwatch AW4)
- Continuous motor activity (1-minute resolution)

**Mental Health Label**
- Depression diagnosis from clinical assessment
- Binary label:
  - Depressed: condition group
  - Not depressed: control group
- Supplementary severity information from MADRS scores

**Passive-Sensing Feature Families Used**
- **Activity**
  - Daily total activity
  - Activity variability
  - Circadian regularity metrics

**Explicitly Excluded**
- Raw high-frequency signal modeling
- Deep learning approaches
- Symptom severity regression (MADRS prediction)

**Available Metadata**
- Gender
- Age (binned)
- Clinical subtype (unipolar / bipolar)
- Inpatient vs outpatient status
- Education and work status (coarse)

**Known Limitations**
- Small sample size
- Wearable-only sensing (no phone data)
- Limited longitudinal duration per subject
- Coarse demographic bins

---

## 3. Cross-Dataset Compatibility Notes

The two datasets differ intentionally across multiple dimensions:

| Dimension        | StudentLife          | Depresjon              |
|------------------|----------------------|------------------------|
| Population       | Students             | Clinical adults        |
| Geography        | USA                  | Europe                 |
| Sensors          | Smartphone           | Wearable               |
| Label Type       | PHQ-9 screening      | Clinical diagnosis     |
| Data Density     | Multi-modal          | Single modality        |

These differences create **realistic distribution shift**, which is the core objective of this benchmark.

---

## 4. Fairness and Metadata Constraints

Fairness analyses are conducted **only when metadata is explicitly available**.
No demographic variables are imputed.

- StudentLife: extremely limited demographic metadata → fairness analysis is constrained
- Depresjon: supports limited subgroup analysis (gender, age bins)

A dedicated analysis will document:
**Minimum metadata required for credible fairness audits in passive-sensing mental-health ML.**

---

## 5. Dataset Scope Lock

- No additional datasets will be added
- No new variables outside the families listed above will be introduced
- No task reformulation (e.g., regression) is permitted

This dataset definition is **final and binding** for the remainder of the project.
"""
Build participant-level labels for each dataset.

Output files (CSV):
- features/tables/studentlife_labels.csv
- features/tables/depresjon_labels.csv
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "features" / "tables"

PHQ_MAP = {
    "Not at all": 0,
    "Several days": 1,
    "More than half the days": 2,
    "Nearly every day": 3,
}

PHQ_ITEMS = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, hopeless.",
    "Trouble falling or staying asleep, or sleeping too much.",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself or that you are a failure or have let yourself or your family down",
    "Trouble concentrating on things, such as reading the newspaper or watching television",
    "Moving or speaking so slowly that other people could have noticed. Or the opposite being so figety or restless that you have been moving around a lot more than usual",
    "Thoughts that you would be better off dead, or of hurting yourself",
]

def build_studentlife_labels():
    df = pd.read_csv(RAW / "studentlife" / "survey" / "PHQ-9.csv")
    df = df[df["type"] == "pre"].copy()

    for col in PHQ_ITEMS:
        df[col] = df[col].map(PHQ_MAP)

    df["phq9_sum"] = df[PHQ_ITEMS].sum(axis=1)
    df["label"] = (df["phq9_sum"] >= 10).astype(int)

    out = df[["uid", "phq9_sum", "label"]].rename(columns={"uid": "participant_id"})
    out.to_csv(OUT / "studentlife_labels.csv", index=False)

def build_depresjon_labels():
    scores = pd.read_csv(RAW / "depresjon" / "scores.csv")
    scores["label"] = scores["number"].str.startswith("condition").astype(int)
    out = scores[["number", "label"]].rename(columns={"number": "participant_id"})
    out.to_csv(OUT / "depresjon_labels.csv", index=False)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    build_studentlife_labels()
    build_depresjon_labels()
    print("Labels written.")

if __name__ == "__main__":
    main()
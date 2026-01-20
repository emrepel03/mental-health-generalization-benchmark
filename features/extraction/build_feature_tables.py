import pandas as pd
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "features" / "tables"

def extract_studentlife_activity():
    activity_dir = RAW / "studentlife" / "sensing" / "activity"
    rows = []

    for f in activity_dir.glob("activity_*.csv"):
        uid = f.stem.replace("activity_", "")
        df = pd.read_csv(f)

        # column has a leading space
        col = [c for c in df.columns if "activity" in c.lower()][0]
        values = df[col]

        mean_activity = values.mean()
        prop_active = (values > 0).mean()

        rows.append({
            "participant_id": uid,
            "activity_mean": mean_activity,
            "activity_active_ratio": prop_active
        })

    return pd.DataFrame(rows)

def extract_studentlife_gps():
    gps_dir = RAW / "studentlife" / "sensing" / "gps"
    rows = []

    for f in gps_dir.glob("gps_*.csv"):
        uid = f.stem.replace("gps_", "")
        cols = [
            "time",
            "provider",
            "network_type",
            "accuracy",
            "latitude",
            "longitude",
            "altitude",
            "bearing",
            "speed",
            "travelstate",
            "_extra",
        ]
        df = pd.read_csv(f, engine="python", header=0, names=cols)

        # drop the extra column created by trailing commas
        if "_extra" in df.columns:
            df = df.drop(columns=["_extra"])

        # drop rows without coordinates
        df = df.dropna(subset=["latitude", "longitude"])

        # coerce numeric columns (some files contain strings)
        for c in ["speed", "latitude", "longitude"]:
            df[c] = pd.to_numeric(df[c], errors="coerce")
        df = df.dropna(subset=["latitude", "longitude"])

        if len(df) < 2:
            continue

        # mean speed
        mean_speed = df["speed"].dropna().mean()

        # approximate distance traveled
        lat = np.radians(df["latitude"].astype(float).values)
        lon = np.radians(df["longitude"].astype(float).values)

        dlat = np.diff(lat)
        dlon = np.diff(lon)

        a = np.sin(dlat / 2) ** 2 + np.cos(lat[:-1]) * np.cos(lat[1:]) * np.sin(dlon / 2) ** 2
        c = 2 * np.arcsin(np.sqrt(a))
        distance = 6371 * c  # km
        total_distance = distance.sum()

        # location variance
        loc_var = df[["latitude", "longitude"]].var().mean()

        rows.append(
            {
                "participant_id": uid,
                "gps_mean_speed": mean_speed,
                "gps_total_distance_km": total_distance,
                "gps_location_variance": loc_var,
            }
        )

    return pd.DataFrame(rows)

def extract_studentlife_app_usage():
    app_dir = RAW / "studentlife" / "app_usage"
    rows = []

    for f in app_dir.glob("running_app_*.csv"):
        uid = f.stem.replace("running_app_", "")
        df = pd.read_csv(f)

        total_records = len(df)

        if "RUNNING_TASKS_topActivity_mPackage" in df.columns:
            unique_apps = df["RUNNING_TASKS_topActivity_mPackage"].nunique()
        else:
            unique_apps = pd.NA

        rows.append(
            {
                "participant_id": uid,
                "app_total_records": total_records,
                "app_unique_packages": unique_apps,
            }
        )

    return pd.DataFrame(rows)


# --- New function to build model tables ---
def build_model_tables():
    """Merge feature tables with label tables to create final modeling tables."""

    # StudentLife
    sl_feat_path = OUT / "studentlife_features.csv"
    sl_lab_path = OUT / "studentlife_labels.csv"
    if sl_feat_path.exists() and sl_lab_path.exists():
        sl_feat = pd.read_csv(sl_feat_path)
        sl_lab = pd.read_csv(sl_lab_path)
        studentlife = sl_feat.merge(sl_lab, on="participant_id", how="inner")
        studentlife.to_csv(OUT / "studentlife_model_table.csv", index=False)
        print("StudentLife model table written:", studentlife.shape)
    else:
        print("StudentLife model table not written (missing studentlife_features.csv or studentlife_labels.csv).")

    # Depresjon
    dp_feat_path = OUT / "depresjon_features.csv"
    dp_lab_path = OUT / "depresjon_labels.csv"
    if dp_feat_path.exists() and dp_lab_path.exists():
        dp_feat = pd.read_csv(dp_feat_path)
        dp_lab = pd.read_csv(dp_lab_path)
        depresjon = dp_feat.merge(dp_lab, on="participant_id", how="inner")
        depresjon.to_csv(OUT / "depresjon_model_table.csv", index=False)
        print("Depresjon model table written:", depresjon.shape)
    else:
        print("Depresjon model table not written (missing depresjon_features.csv or depresjon_labels.csv).")

def main():
    OUT.mkdir(parents=True, exist_ok=True)

    act = extract_studentlife_activity()
    gps = extract_studentlife_gps()
    app = extract_studentlife_app_usage()

    df = act.merge(gps, on="participant_id", how="outer")
    df = df.merge(app, on="participant_id", how="outer")

    df.to_csv(OUT / "studentlife_features.csv", index=False)
    print("StudentLife activity + GPS + app usage features written.")

    build_model_tables()

if __name__ == "__main__":
    main()
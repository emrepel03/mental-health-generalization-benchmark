import pandas as pd

datasets = {
    "StudentLife": "features/tables/studentlife_model_table.csv",
    "Depresjon": "features/tables/depresjon_model_table.csv",
}

metadata_fields = ["gender", "age", "device", "platform"]

rows = []

for name, path in datasets.items():
    df = pd.read_csv(path)

    available = []
    missing = []

    for field in metadata_fields:
        if field in df.columns:
            available.append(field)
        else:
            missing.append(field)

    rows.append({
        "dataset": name,
        "available_metadata": ", ".join(available) if available else "None",
        "missing_metadata": ", ".join(missing)
    })

summary = pd.DataFrame(rows)
print(summary)
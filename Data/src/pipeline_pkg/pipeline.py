import json
from .loader import load_data
from .model import load_model, predict
from .metrics import generate_metrics
from .config import OUTPUT_DIR, METRICS_DIR, OUTPUT_FILE, METRICS_FILE
import os

def run_pipeline():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(METRICS_DIR, exist_ok=True)

    # Prevent duplicate run
    if OUTPUT_FILE.exists():
        print("Already processed today")
        return False

    df = load_data()
    model = load_model()

    preds = predict(model, df)
    df["prediction"] = preds

    df.to_csv(str(OUTPUT_FILE), index=False)

    metrics = generate_metrics(df)

    with open(str(METRICS_FILE), "w") as f:
        json.dump(metrics, f, indent=2)

    return True

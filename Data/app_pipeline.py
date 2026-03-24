import sys
import os
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from datetime import datetime
import pandas as pd
from src.pipeline_pkg.model import load_model, load_scaler,predict,predict_proba
from src.pipeline_pkg.metrics import classification_metrics

def calculate_metrics(df):
    return {
        "rows_processed": len(df),
        "dummy_accuracy": 0.95
    }

def main():
    today = datetime.now().strftime("%Y-%m-%d")

    input_file = "src/diabetes2.csv"
    output_dir = "output"
    metrics_dir = "metrics"

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(metrics_dir, exist_ok=True)

    # Load data
    data = pd.read_csv(input_file)
    ids = [i for i in range(len(data))]
    y_true = data.get("Outcome")

    # Load model
    model = load_model()

    # Load scaler
    scaler = load_scaler()

    # Preprocess data
    features = data.drop(columns=["Outcome"])
    features_scaled = scaler.transform(features)

    # Predict
    predictions = predict(model, features_scaled)

    #predict probabilities
    probabilities = predict_proba(model, features_scaled)[:, 1]

    # Create a DataFrame with the results
    results = pd.DataFrame({
        "ID": ids,
        "Actual": y_true,
        "Predicted": predictions,
        "Probability": probabilities
    })

    # Save predictions
    output_file = f"{output_dir}/predictions_{today}.csv"
    results.to_csv(output_file, index=False)

    # Metrics
    metrics = classification_metrics(y_true, predictions, probabilities)

    metrics_file = f"{metrics_dir}/metrics_{today}.json"
    with open(metrics_file, "w") as f:
        json.dump(metrics, f, indent=4)

    print("Run successful!")

if __name__ == "__main__":
    main()
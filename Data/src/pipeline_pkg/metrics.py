def generate_metrics(df):
    return {
        "rows": len(df),
        "mean_prediction": float(df["prediction"].mean()),
    }

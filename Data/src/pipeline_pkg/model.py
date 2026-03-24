import pickle,joblib
from .config import MODEL_PATH, SCALER_PATH

def load_model():
    with open(str(MODEL_PATH), "rb") as f:
        #print(f"Model loaded from: {MODEL_PATH}")
        return pickle.load(f)

def load_scaler():
    with open(str(SCALER_PATH), "rb") as f:
        #print(f"Scaler loaded from: {SCALER_PATH}")
        return joblib.load(f)

def predict(model, df):
    print(f"Making predictions for {len(df)} samples")
    return model.predict(df)

def predict_proba(model, df):
    print(f"Calculating probabilities for {len(df)} samples")
    return model.predict_proba(df)

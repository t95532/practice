import pickle
from .config import MODEL_PATH

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

def predict(model, df):
    return model.predict(df)

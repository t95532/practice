import pandas as pd
from .config import INPUT_FILE

def load_data():
    return pd.read_csv(INPUT_FILE)

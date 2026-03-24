from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = BASE_DIR / "Data"

LIB_DIR = DATA_DIR / "lib"
SRC_DIR = DATA_DIR / "src"

OUTPUT_DIR = DATA_DIR / "output"
METRICS_DIR = DATA_DIR / "metrics"

MODEL_PATH = LIB_DIR / "model.pkl"
SCALER_PATH = LIB_DIR / "scaler.joblib"
INPUT_FILE = SRC_DIR / "input.csv"

TODAY = datetime.now().strftime("%Y-%m-%d")

OUTPUT_FILE = OUTPUT_DIR / f"{TODAY}.csv"
METRICS_FILE = METRICS_DIR / f"{TODAY}.json"

# print(f"BASE_DIR: {BASE_DIR}")
# print(f"DATA_DIR: {DATA_DIR}")
# print(f"LIB_DIR: {LIB_DIR}")
# print(f"SRC_DIR: {SRC_DIR}")
# print(f"OUTPUT_DIR: {OUTPUT_DIR}")
# print(f"METRICS_DIR: {METRICS_DIR}")
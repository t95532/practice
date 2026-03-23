from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "Data"

LIB_DIR = DATA_DIR / "lib"
SRC_DIR = DATA_DIR / "src"

OUTPUT_DIR = DATA_DIR / "output"
METRICS_DIR = DATA_DIR / "metrics"

MODEL_PATH = LIB_DIR / "model.pkl"
INPUT_FILE = SRC_DIR / "input.csv"

TODAY = datetime.now().strftime("%Y-%m-%d")

OUTPUT_FILE = OUTPUT_DIR / f"{TODAY}.csv"
METRICS_FILE = METRICS_DIR / f"{TODAY}.json"

# AI Coding Agent Instructions for ML Practice Codebase

## Project Overview
A collection of machine learning and data science practice projects demonstrating various ML workflows:
- **Prediction Models**: Diabetes prediction (Streamlit app), breast cancer classification, customer churn analysis
- **NLP Tasks**: Sentiment analysis, next-word prediction (LSTM), emotion capture
- **Data Processing**: Text preprocessing, discretization, feature engineering
- **Infrastructure**: Dockerized Streamlit apps, MLflow experiment tracking, Jenkins CI/CD pipeline

## Architecture Patterns

### Model Deployment Pattern (`Data/` directory)
Models are served via **Streamlit** with loaded artifacts in `lib/` subdirectory:
- `model.pkl` - Serialized scikit-learn model (loaded with `pickle.load()`)
- `scaler.joblib` - Pre-fit StandardScaler (loaded with `joblib.load()`)
- Key pattern: Load artifacts on app startup, apply scaler before predictions
- Example: See [Data/app.py](Data/app.py) - instantiates UI and prediction pipeline

### Data Processing Pipeline
Two-phase approach:
1. **Text Processing**: [preprocess.py](preprocess.py) provides `preprocess_text()` → `clean_text()` → `tokenize_text()` → `lemmatize_text()` for NLP tasks
2. **Numerical Binning**: [Discritization.py](Discritization.py) defines `discretize()` with bin functions for age, income, rates (returns categorical strings)

### Experiment Tracking
MLflow integration stores runs in `Data/mlruns/` directory with model artifacts organized by run UUID. Projects use standard sklearn + MLflow workflows (not shown in notebooks yet).

## Project Structure
```
Data/
  ├── app.py              # Streamlit prediction UI
  ├── requirements.txt    # pip dependencies (streamlit, joblib, scikit-learn, pandas, numpy)
  ├── lib/
  │   ├── model.pkl       # Serialized model
  │   └── scaler.joblib   # Feature scaler
  └── Dockerfile          # Multi-stage not used; simple Python 3.10 base
Jenkins/
  ├── PythonScripts/      # Jupyter notebooks for model dev
  └── DataSet/            # Raw CSV files
notebooks (root)
  ├── diabetes.ipynb      # Model training templates
  ├── pyspark.ipynb       # Spark examples
  └── [other].ipynb       # Various ML experiments
```

## Development Workflows

### Running Streamlit App Locally
```bash
cd Data
streamlit run app.py
# Accesses at localhost:8501
```

### Docker Deployment
```bash
cd Data
docker build -t ml-app .
docker run -p 8501:8501 ml-app
```

### Jenkins Pipeline
- Defined in root [Jenkinsfile](Jenkinsfile)
- Current stages: Checkout → Build → Test (echo placeholders)
- Extend with: `pip install -r requirements.txt`, pytest, Docker build steps

## Key Patterns & Conventions

### Model Loading Convention
Always use `pathlib.Path(__file__).resolve().parent` to build absolute paths relative to script location. This ensures artifacts load correctly whether running locally or in containers.

```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
scaler = joblib.load(BASE_DIR / "lib" / "scaler.joblib")
```

### Dependency Management
- `Data/requirements.txt` lists pip packages (not version-pinned; update when adding dependencies)
- Notebooks assume scikit-learn, numpy, pandas, nltk, streamlit pre-installed
- Download nltk data explicitly: `nltk.download('stopwords')`, `nltk.download('punkt')`

### Discretization Pattern
Bin ranges are domain-specific. When adding new features:
```python
def discretize_feature(value):
    if value < threshold_1: return 'Category_1'
    elif value < threshold_2: return 'Category_2'
    else: return 'Category_3'
```

### Data Files Location
- CSVs stored in subdirectories: `Jenkins/DataSet/`, `Data/src/`
- Notebooks use absolute/relative paths to load; check each notebook's data loading cell for exact paths

## Critical Dependencies
- **scikit-learn**: Model training, scaling, TF-IDF vectorization
- **joblib**: Model persistence (use over pickle for large arrays)
- **streamlit**: Production UI framework
- **nltk**: NLP preprocessing (requires corpus downloads)
- **pandas, numpy**: Data manipulation
- **MLflow**: Experiment tracking (infrastructure in place, not actively used in current notebooks)

## Common Pitfalls
1. **Path Issues**: Notebooks use hardcoded paths (e.g., `C:\Users\ADMIN\...`). Refactor to use relative paths when extending.
2. **Missing Artifacts**: Ensure `scaler.joblib` and `model.pkl` exist in `Data/lib/` before running Streamlit app.
3. **NLTK Data**: First time using NLTK, run `nltk.download()` to fetch required corpora.
4. **Notebook-to-Production**: Models trained in notebooks need explicit serialization step before moving to `app.py`.

## Extending This Codebase
- **New Prediction Model**: Train in notebook, serialize to `Data/lib/`, update `app.py` UI and prediction logic
- **New NLP Task**: Add preprocessing function to [preprocess.py](preprocess.py), integrate into notebook
- **New Dataset**: Place CSV in appropriate subdirectory, update paths in notebooks
- **CI/CD**: Expand [Jenkinsfile](Jenkinsfile) with `RUN pip install -r requirements.txt` and pytest stages

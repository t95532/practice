# 📊 Daily ML Pipeline with GitHub Actions

This project runs a **daily automated machine learning pipeline** using GitHub Actions. It processes input data, generates predictions, calculates metrics, and commits results back to the repository.

---

# 🧭 Overview

Every day, the workflow:

1. Reads input data from `src/diabetes2.csv`
2. Runs it through a model
3. Saves predictions to `output/`
4. Saves metrics to `metrics/` (JSON format)
5. Commits results back to GitHub with the run date

---

# 📁 Project Structure

```
Data/
├── app.py                  # Main pipeline script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Optional container setup

├── src/
│   └── diabetes2.csv       # Input dataset

├── output/                 # Daily predictions
├── metrics/                # Daily metrics (JSON)

├── mlruns/                 # MLflow tracking (optional)
├── mlflow.db               # MLflow database

├── notebooks/              # Experimentation (optional)
├── scripts/                # Utility scripts (recommended)

├── .github/
│   └── workflows/
│       └── daily-run.yml   # Automation workflow
```

---

# ⚙️ Workflow Execution (Step-by-Step)

## ⏰ 1. Daily Trigger

GitHub Actions runs automatically based on a cron schedule.

```
.github/workflows/daily-run.yml
```

---

## 📥 2. Repository Checkout

A fresh runner downloads the repository:

```
practice/
└── Data/
```

---

## 🐍 3. Environment Setup

* Python installed
* Dependencies installed from:

```
Data/requirements.txt
```

---

## ▶️ 4. Run Pipeline

Command executed:

```
cd Data
python app.py
```

---

# 🔍 Inside `app.py`

## 📁 Step 1: Read Input Data

```
src/diabetes2.csv
```

---

## 🧠 Step 2: Load Model

* Load trained model (local file, MLflow, or other source)

---

## 🤖 Step 3: Generate Predictions

* Apply model on dataset
* Output: DataFrame with predictions

---

## 💾 Step 4: Save Predictions

```
output/predictions_YYYY-MM-DD.csv
```

---

## 📊 Step 5: Generate Metrics

Example:

```
{
  "date": "2026-03-23",
  "rows_processed": 100,
  "accuracy": 0.95
}
```

---

## 📝 Step 6: Save Metrics

```
metrics/metrics_YYYY-MM-DD.json
```

---

# 📦 After Execution

```
Data/
├── output/
│   └── predictions_2026-03-23.csv

├── metrics/
│   └── metrics_2026-03-23.json
```

---

# 🔁 Commit & Push

The workflow commits results:

```
git add output/ metrics/
git commit -m "Daily job run on YYYY-MM-DD"
git push
```

---

# 🔄 Example After Multiple Days

```
output/
├── predictions_2026-03-22.csv
├── predictions_2026-03-23.csv

metrics/
├── metrics_2026-03-22.json
├── metrics_2026-03-23.json
```

---

# 🧠 Key Concepts

## 🔹 Stateless Execution

* Each run starts fresh
* No previous memory
* Only committed files persist

## 🔹 Persistence via Git

* Results are saved only if pushed to repo

## 🔹 Folder Roles

| Folder               | Purpose             |
| -------------------- | ------------------- |
| `src/`               | Input data          |
| `app.py`             | Pipeline controller |
| `output/`            | Predictions         |
| `metrics/`           | Evaluation results  |
| `.github/workflows/` | Automation          |

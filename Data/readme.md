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

---

# ⚠️ Important Notes

## 1. Ensure Folders Exist

```
os.makedirs("output", exist_ok=True)
os.makedirs("metrics", exist_ok=True)
```

---

## 2. GitHub Permissions

Enable:

* Settings → Actions → General → **Read & Write permissions**

---

## 3. Avoid Empty Commit Errors

```
git commit -m "..." || echo "No changes to commit"
```

---

## 4. Repository Size Growth

Daily outputs increase repo size.

### Future Improvements:

* Keep last N days only
* Store results in cloud (S3, DB)

---

# 🚀 GitHub Actions Workflow

```
name: Daily ML Run

on:
  schedule:
    - cron: "30 6 * * *"   # 12 PM IST
  workflow_dispatch:

jobs:
  run-pipeline:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        working-directory: Data
        run: pip install -r requirements.txt

      - name: Run pipeline
        working-directory: Data
        run: python app.py

      - name: Commit results
        run: |
          cd Data
          git config --global user.name "github-actions"
          git config --global user.email "actions@github.com"

          DATE=$(date +'%Y-%m-%d')

          git add output/ metrics/
          git commit -m "Daily job run on $DATE" || echo "No changes"
          git push
```

---

# 🔥 Summary

This system creates a **fully automated daily ML pipeline**:

```
Input → Model → Predictions → Metrics → Git Commit
```

* No manual work required
* Daily tracking of results
* Simple and scalable setup

---

# 📌 Future Enhancements

* Add model versioning
* Integrate MLflow properly
* Store outputs in cloud storage
* Add alerting (email/Slack)
* Clean old files automatically

---
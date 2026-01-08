# !pip install streamlit
# !pip install pickle
# !pip install joblib
# !pip install patlib
# !pip install numpy

import streamlit as st
import joblib
import pickle
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Diabetes Prediction", layout="centered")

# -----------------------------
# Load scaler & model
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent

# project root (same level as Data)
SCALER_PATH = BASE_DIR / "lib" / "scaler.joblib"
MODEL_PATH = BASE_DIR / "lib" / "model.pkl"

scaler = joblib.load(SCALER_PATH)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# -----------------------------
# UI
# -----------------------------
st.title("🩺 Diabetes Prediction App")

pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age", min_value=0, step=1)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                             skin_thickness, insulin, bmi, dpf, age]])

    # Standardize
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High risk of diabetes ({probability:.2%})")
    else:
        st.success(f"✅ Low risk of diabetes ({probability:.2%})")

import sys
import os

# Add the parent directory (score_genie/) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from src.preprocessing import load_and_clean_data
from src.model import train_model
from src.evaluate_model import evaluate_model

# Load and preprocess data once to train the model
df, encoders = load_and_clean_data("data/student-mat.csv")
X = df.drop('G3', axis=1)
y = df['G3']
model = train_model(X, y, model_type='linear')

st.set_page_config(page_title="Score Genie", layout="centered")

# Title of the app
st.title("🎓 Score Genie")
st.markdown("Enter student details to predict their final exam score (G3).")

# Input form
with st.form("input_form"):
    age = st.slider("Age", 15, 22, 17)
    study_time = st.slider("Study Time (1=low, 4=high)", 1, 4, 2)
    failures = st.number_input("Number of Past Failures", min_value=0, max_value=3, value=0)
    absences = st.number_input("Number of Absences", min_value=0, max_value=100, value=4)
    goout = st.slider("Going Out Frequency (1-5)", 1, 5, 3)
    health = st.slider("Health (1=worst, 5=best)", 1, 5, 3)
    G1 = st.number_input("Grade Term 1 (G1)", min_value=0, max_value=20, value=10)
    G2 = st.number_input("Grade Term 2 (G2)", min_value=0, max_value=20, value=12)

    submitted = st.form_submit_button("Predict Grade")

if submitted:
    # Prepare input data
    input_data = pd.DataFrame([{
        'age': age,
        'Medu': 2,
        'Fedu': 2,
        'studytime': study_time,
        'failures': failures,
        'goout': goout,
        'health': health,
        'absences': absences,
        'G1': G1,
        'G2': G2
    }])

    # Align input with model training features
    # Fill missing columns with 0 (default encoded values)
    for col in X.columns:
        if col not in input_data.columns:
            input_data[col] = 0

    # Predict
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Final Grade (G3): **{round(prediction, 2) if round(prediction, 2)<=20 else 20} / 20**")

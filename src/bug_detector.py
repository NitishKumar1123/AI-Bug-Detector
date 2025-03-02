# src/bug_detector.py
import joblib
import pandas as pd
import os

# Load the trained model and vectorizer
vectorizer = joblib.load("models/vectorizer.pkl")
model = joblib.load("models/model.pkl")

# Load dataset for bug fixes
df = pd.read_csv("dataset/cplusplus_bugs.csv")

def detect_bug(code_snippet):
    """Detects bugs in a given C++ code snippet using the trained model."""
    
    # Convert input code to feature vector
    code_features = vectorizer.transform([code_snippet])
    
    # Predict bug type
    prediction = model.predict(code_features)[0]

    # Check if "Fixed Code" column exists
    if "Fixed Code" in df.columns:
        fix = df[df["Bug Type"] == prediction]["Fixed Code"].values
        suggested_fix = fix[0] if len(fix) > 0 else "No fix available."
    else:
        suggested_fix = "No fix available."

    return prediction, suggested_fix

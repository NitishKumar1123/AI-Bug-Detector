# models/predict.py
import joblib
import os

# Corrected path to model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

def predict_bug(code_snippet):
    """Predicts the bug type for a given C++ code snippet."""
    prediction = model.predict([code_snippet])[0]
    return prediction

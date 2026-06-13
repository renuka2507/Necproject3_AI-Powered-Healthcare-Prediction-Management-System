import joblib
import numpy as np
import os

try:
    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    model = joblib.load(model_path)
except:
    model = None

def predict_disease(age, bp, sugar, bmi):

    if model is None:
        return {
            "disease": "model_not_loaded",
            "risk": "unknown"
        }

    input_data = np.array([[age, bp, sugar, bmi]])

    prediction = model.predict(input_data)[0]

    if prediction == "heart":
        risk = "High"
    elif prediction == "diabetes":
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "disease": str(prediction),
        "risk": risk
    }
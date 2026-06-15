import joblib
import numpy as np

model = joblib.load("malware_model.pkl")

def predict_app(features):
    prob = model.predict_proba([features])[0][1]
    risk_score = int(prob * 100)

    return risk_score

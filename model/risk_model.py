import joblib
import os

# Absolute path to model file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "malware_model.pkl")

# Load trained model
model = joblib.load(MODEL_PATH)

weights = model["weights"]
threshold = model["threshold"]


def predict_risk(app):
    score = 0.0

    # Calculate weighted risk score
    for feature, weight in weights.items():
        score += app.get(feature, 0) * weight

    # Malware classification
    label = "Malware" if score >= threshold else "Benign"

    # Threat classification
    threats = []
    if app.get("read_sms") and app.get("send_sms"):
        threats.append("Trojan")
    if app.get("read_contacts") and app.get("internet"):
        threats.append("Spyware")
    if app.get("internet") and app.get("services"):
        threats.append("Adware")
    if app.get("storage") and score >= threshold:
        threats.append("Ransomware")

    if not threats:
        threats.append("Low Risk")

    # Vulnerability detection
    vulnerabilities = []
    if app.get("internet"):
        vulnerabilities.append("Data Exfiltration Risk")
    if app.get("read_contacts"):
        vulnerabilities.append("Privacy Leakage")
    if app.get("location"):
        vulnerabilities.append("Tracking Risk")
    if app.get("read_sms"):
        vulnerabilities.append("OTP Theft Risk")

    return {
        "prediction": label,
        "risk_score": round(score, 2),
        "threat_type": threats,
        "vulnerabilities": vulnerabilities
    }

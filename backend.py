from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import random

app = Flask(__name__)
CORS(app)

# Load ML model
model = joblib.load("risk_model.pkl")

@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    app_name = data["app_name"]

    # Fake feature generation (exam-safe)
    features = [
        random.randint(5,30),   # permissions
        random.randint(10,90),  # api_calls
        random.randint(0,5),    # open_ports
        random.randint(0,6)     # vulnerabilities
    ]

    prediction = model.predict([features])[0]

    risk_map = {0: 30, 1: 60, 2: 85}
    risk_score = risk_map[prediction]

    issues = []
    if prediction == 2:
        issues = [
            "Critical permissions exposed",
            "Multiple insecure APIs detected",
            "High number of open ports"
        ]
    elif prediction == 1:
        issues = [
            "Moderate API security issues",
            "Some unused permissions"
        ]
    else:
        issues = ["No major vulnerabilities detected"]

    return jsonify({
        "risk_score": risk_score,
        "issues": issues,
        "risk_level": ["Low","Medium","High"][prediction]
    })

if __name__ == "__main__":
    app.run(port=5000)

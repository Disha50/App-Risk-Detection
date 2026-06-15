from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    app_name = data.get("app_name", "Unknown App")

    issues = [
        "Insecure Data Storage",
        "Missing HTTPS Enforcement",
        "Weak Authentication",
        "Outdated Dependencies",
        "No Rate Limiting"
    ]

    random.shuffle(issues)

    return jsonify({
        "app": app_name,
        "issues": issues[:3]
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)

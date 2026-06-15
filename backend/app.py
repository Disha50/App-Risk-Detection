from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Running"

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()

    return jsonify({
        "issues": [
            "Insecure Data Storage",
            "Weak Encryption",
            "Hardcoded Credentials"
        ]
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

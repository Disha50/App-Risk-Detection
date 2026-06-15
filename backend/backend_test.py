from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Running"

@app.route("/scan", methods=["POST"])
def scan():
    return jsonify({"issues": ["Test Issue 1", "Test Issue 2"]})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

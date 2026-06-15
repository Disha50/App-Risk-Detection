from flask import Blueprint, request, jsonify
import sqlite3
import hashlib

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = hashlib.sha256(data["password"].encode()).hexdigest()

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()

    if user:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})

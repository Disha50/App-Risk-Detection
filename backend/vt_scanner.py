import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VT_API_KEY")
BASE_URL = "https://www.virustotal.com/api/v3/search"

def scan_app_virustotal(app_name):
    headers = {
        "x-apikey": API_KEY
    }

    params = {
        "query": app_name,
        "limit": 1
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    if not data.get("data"):
        return None

    attributes = data["data"][0]["attributes"]

    stats = attributes.get("last_analysis_stats", {})

    return {
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "harmless": stats.get("harmless", 0),
        "undetected": stats.get("undetected", 0)
    }

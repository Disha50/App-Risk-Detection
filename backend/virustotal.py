import requests

API_KEY = "YOUR_API_KEY"

def vt_scan(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

    headers = {
        "x-apikey": API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    stats = data["data"]["attributes"]["last_analysis_stats"]

    return stats

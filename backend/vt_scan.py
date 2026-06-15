import requests

API_KEY = "PUT_YOUR_VIRUSTOTAL_API_KEY_HERE"

def vt_scan(file_path):
    url = "https://www.virustotal.com/api/v3/files"
    headers = {"x-apikey": API_KEY}

    with open(file_path, "rb") as f:
        files = {"file": f}
        r = requests.post(url, headers=headers, files=files)

    return r.json()

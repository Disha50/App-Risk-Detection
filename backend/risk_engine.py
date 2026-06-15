def calculate_risk(vt_data):
    malicious = vt_data["malicious"]
    suspicious = vt_data["suspicious"]

    risk_score = (malicious * 15) + (suspicious * 8)

    risk_score = min(risk_score, 100)

    if risk_score >= 70:
        level = "HIGH"
    elif risk_score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return risk_score, level

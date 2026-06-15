from risk_model import predict_risk

app = {
    "internet": 1,
    "read_sms": 1,
    "send_sms": 1,
    "read_contacts": 0,
    "location": 0,
    "camera": 0,
    "storage": 1,
    "services": 1,
    "receivers": 1,
    "apk_size": 20
}

result = predict_risk(app)
print(result)

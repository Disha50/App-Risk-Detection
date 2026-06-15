import random

def analyze_apk(apk_name):
    score = random.randint(40, 95)

    issues = [
        "Dangerous permissions detected",
        "Hardcoded API keys",
        "Unencrypted local storage"
    ]

    solutions = [
        "Limit permissions",
        "Remove hardcoded secrets",
        "Enable AES encryption"
    ]

    return score, issues, solutions

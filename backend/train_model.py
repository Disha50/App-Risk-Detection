import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
df = pd.read_csv("risk_data.csv")

X = df.drop("risk", axis=1)
y = df["risk"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "risk_model.pkl")

print("✅ ML Model Trained & Saved")

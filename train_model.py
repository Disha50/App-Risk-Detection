import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# ----------------------------
# Create Dataset
# ----------------------------
np.random.seed(42)

data = {
    "permissions": np.random.randint(5, 30, 200),
    "apis": np.random.randint(1, 25, 200),
}

df = pd.DataFrame(data)

# Rule-based labeling (for training)
df["risk"] = np.where(
    (df["permissions"] > 15) | (df["apis"] > 10), 1, 0
)

# ----------------------------
# Train-Test Split
# ----------------------------
X = df[["permissions", "apis"]]
y = df["risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------
# Train Model
# ----------------------------
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# ----------------------------
# Evaluation
# ----------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# ----------------------------
# Confusion Matrix Plot
# ----------------------------
cm = confusion_matrix(y_test, y_pred)
plt.figure()
plt.imshow(cm)
plt.title("Risk Prediction Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.show()

# ----------------------------
# Save Model
# ----------------------------
joblib.dump(model, "risk_model.pkl")
print("Model saved as risk_model.pkl")

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# Sample training data
data = {
    "age": [25, 45, 60, 35, 55, 30],
    "bp": [120, 150, 160, 130, 170, 110],
    "sugar": [90, 180, 200, 100, 220, 85],
    "bmi": [22, 30, 32, 25, 35, 21],
    "disease": [
        "normal",
        "diabetes",
        "heart",
        "normal",
        "heart",
        "normal"
    ]
}

df = pd.DataFrame(data)

X = df[["age", "bp", "sugar", "bmi"]]
y = df["disease"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
joblib.dump(model, model_path)

print("✅ Model trained successfully!")
print("Saved to:", model_path)
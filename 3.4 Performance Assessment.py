import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Create bins and labels
# -----------------------------
bins = [0, 250, 500, 1200]
labels = ["Inexpensive", "Standard Price", "Expensive"]

df["price_category"] = pd.cut(df["price"], bins=bins, labels=labels, include_lowest=True)

# -----------------------------
# 2. Prepare features and target
# -----------------------------
X = df.drop(columns=["price", "price_category"])
y = df["price_category"]

# -----------------------------
# 3. Train-test split (80/20)
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.20, random_state=42, stratify=y
)

# -----------------------------
# 4. Initialize models
# -----------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=500),
    "Random Forest": RandomForestClassifier(n_estimators=200),
    "SVM": SVC()
}

accuracy_results = {}
correct_incorrect = {}

# -----------------------------
# 5. Train, predict, evaluate
# -----------------------------
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions, average="weighted")
    cm = confusion_matrix(y_test, predictions)

    accuracy_results[name] = accuracy
    correct = (predictions == y_test).sum()
    incorrect = (predictions != y_test).sum()
    correct_incorrect[name] = (correct, incorrect)

    print(f"\n=== {name} ===")
    print(f"Training Accuracy: {accuracy:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print("Confusion Matrix:")
    print(cm)

# -----------------------------
# 6. Bar graph: Training Accuracy
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(accuracy_results.keys(), accuracy_results.values(), color=["blue","green","purple"])
plt.title("Training Accuracy by Model")
plt.ylabel("Accuracy")
plt.ylim(0,1)
plt.show()

# -----------------------------
# 7. Bar graph: Correct vs Incorrect
# -----------------------------
correct_vals = [v[0] for v in correct_incorrect.values()]
incorrect_vals = [v[1] for v in correct_incorrect.values()]

x = np.arange(len(models))
width = 0.35

plt.figure(figsize=(10,6))
plt.bar(x - width/2, correct_vals, width, label="Correct", color="green")
plt.bar(x + width/2, incorrect_vals, width, label="Incorrect", color="red")

plt.xticks(x, models.keys())
plt.ylabel("Count")
plt.title("Correct vs Incorrect Predictions by Model")
plt.legend()
plt.show()

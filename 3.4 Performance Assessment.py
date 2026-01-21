# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
import matplotlib.pyplot as plt
from datetime import datetime
from IPython.display import display, Markdown
import seaborn as sns

# Date and Student ID
todays_date = datetime.now().strftime("%Y-%m-%d")
student_id = "StudentID"

# -----------------------------------------
# Step 1: Load and Prepare Dataset
# -----------------------------------------
file_path = r'C:\Files\Excel\Predictive_PythonR\AirbnbListings_V3.xlsx'
df = pd.read_excel(file_path)

# Create bins and labels for price
bins = [0, 250, 500, 1200]
labels = ["Inexpensive", "Standard Price", "Expensive"]
df["price_category"] = pd.cut(df["price"], bins=bins, labels=labels, include_lowest=True)

# Display header
display(Markdown(f"### Date: {todays_date}"))
display(Markdown(f"### Student ID: {student_id}"))
display(df.head())

# -----------------------------------------
# Step 2: Feature Selection
# -----------------------------------------
X = df.drop(columns=["price", "price_category"])
y = df["price_category"]

# Train-test split (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

display(Markdown("### Features"))
display(X.head())
display(Markdown("### Target"))
display(y.head())

# -----------------------------------------
# Step 3: Initialize Models
# -----------------------------------------
logistic_model = LogisticRegression(max_iter=500)
rf_classifier = RandomForestClassifier(random_state=42)
svm_classifier = SVC()

# Train models
logistic_model.fit(X_train, y_train)
rf_classifier.fit(X_train, y_train)
svm_classifier.fit(X_train, y_train)

# Predictions
y_pred_logistic = logistic_model.predict(X_test)
y_pred_rf = rf_classifier.predict(X_test)
y_pred_svm = svm_classifier.predict(X_test)

# -----------------------------------------
# Step 4: Training Accuracy
# -----------------------------------------
training_accuracy_logistic = accuracy_score(y_train, logistic_model.predict(X_train))
training_accuracy_rf = accuracy_score(y_train, rf_classifier.predict(X_train))
training_accuracy_svm = accuracy_score(y_train, svm_classifier.predict(X_train))

display(Markdown("### Training Accuracy Results"))
display(Markdown(f"**Logistic Regression:** {training_accuracy_logistic:.3f}"))
display(Markdown(f"**Random Forest:** {training_accuracy_rf:.3f}"))
display(Markdown(f"**SVM:** {training_accuracy_svm:.3f}"))

# -----------------------------------------
# Step 5: F1 Scores
# -----------------------------------------
f1_logistic = f1_score(y_test, y_pred_logistic, average="weighted")
f1_rf = f1_score(y_test, y_pred_rf, average="weighted")
f1_svm = f1_score(y_test, y_pred_svm, average="weighted")

display(Markdown("### F1 Scores"))
display(Markdown(f"**Logistic Regression:** {f1_logistic:.3f}"))
display(Markdown(f"**Random Forest:** {f1_rf:.3f}"))
display(Markdown(f"**SVM:** {f1_svm:.3f}"))

# -----------------------------------------
# Step 6: Confusion Matrices
# -----------------------------------------
conf_matrix_logistic = confusion_matrix(y_test, y_pred_logistic)
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
conf_matrix_svm = confusion_matrix(y_test, y_pred_svm)

display(Markdown("### Confusion Matrices"))
display(Markdown("#### Logistic Regression"))
display(conf_matrix_logistic)

display(Markdown("#### Random Forest"))
display(conf_matrix_rf)

display(Markdown("#### SVM"))
display(conf_matrix_svm)

# -----------------------------------------
# Step 7: Compare Predictions Against Full Dataset
# -----------------------------------------
df["Pred_Logistic"] = logistic_model.predict(X)
df["Pred_RF"] = rf_classifier.predict(X)
df["Pred_SVM"] = svm_classifier.predict(X)

log_correct = sum(df["price_category"] == df["Pred_Logistic"])
rf_correct = sum(df["price_category"] == df["Pred_RF"])
svm_correct = sum(df["price_category"] == df["Pred_SVM"])

log_incorrect = len(df) - log_correct
rf_incorrect = len(df) - rf_correct
svm_incorrect = len(df) - svm_correct

# -----------------------------------------
# Step 8: Bar Graph – Training Accuracy
# -----------------------------------------
plt.figure(figsize=(10, 5))
plt.bar(["Logistic", "Random Forest", "SVM"],
        [training_accuracy_logistic, training_accuracy_rf, training_accuracy_svm],
        color=["blue", "green", "purple"])
plt.title("Training Accuracy by Model")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.show()

# -----------------------------------------
# Step 9: Bar Graph – Correct vs Incorrect
# -----------------------------------------
correct_counts = [log_correct, rf_correct, svm_correct]
incorrect_counts = [log_incorrect, rf_incorrect, svm_incorrect]

x = range(3)
bar_width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x, correct_counts, width=bar_width, label="Correct", color="green")
plt.bar([i + bar_width for i in x], incorrect_counts, width=bar_width, label="Incorrect", color="red")

plt.xticks([i + bar_width / 2 for i in x], ["Logistic", "Random Forest", "SVM"])
plt.ylabel("Count")
plt.title("Correct vs Incorrect Predictions")
plt.legend()
plt.show()

import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore
import joblib  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.metrics import (  # type: ignore
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# Load the data
data_path = "data/heart.csv"
df = pd.read_csv(data_path)

# Prepare Data
X = df.drop("target", axis=1)
y = df["target"]

# Load the Scaler and Transform Features
scaler_path = "models/scaler.joblib"
scaler = joblib.load(scaler_path)
X = scaler.transform(X)

# Split Data
# IMPORTANT: Use the SAME random_state you used during training!
# This ensures X_test is actually data the model hasn't seen before.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Load the Model
model_path = "models/heart_disease_model.joblib"
model = joblib.load(model_path)

# Make Predictions
y_pred = model.predict(X_test)

# Print Results
print("Model Evaluation Metrics:")
print("-" * 30)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Generate the matrix
cm = confusion_matrix(y_test, y_pred)

# Plotting
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")

# Save the plot to assets folder
plt.savefig("assets/confusion_matrix.png")
plt.show()

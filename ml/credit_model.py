import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dummy dataset
X = pd.DataFrame({"credit_score": [650, 720, 580, 690, 740], "income": [45000, 62000, 30000, 52000, 70000]})
y = [1, 0, 1, 0, 0]  # 1 = default, 0 = no default

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

with mlflow.start_run():
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "credit_model")

print(f"Logged model with accuracy: {accuracy:.2f}")

import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("churn-prediction")

train = pd.read_csv("data/processed/train_processed.csv")
test = pd.read_csv("data/processed/test_processed.csv")

X_train = train.drop("Survived", axis=1)
y_train = train["Survived"]

X_test = test.drop("Survived", axis=1)
y_test = test["Survived"]

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

with mlflow.start_run():
    mlflow.log_param("model", "logistic_regression")

    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model"
    )
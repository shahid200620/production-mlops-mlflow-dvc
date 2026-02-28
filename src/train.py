import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import mlflow
import pickle
import os

def train():

    train_df = pd.read_csv("data/processed/train_processed.csv")
    test_df = pd.read_csv("data/processed/test_processed.csv")

    X_train = train_df.drop("Survived", axis=1)
    y_train = train_df["Survived"]

    X_test = test_df.drop("Survived", axis=1)
    y_test = test_df["Survived"]

    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("churn-prediction")

    os.makedirs("model_artifacts", exist_ok=True)

    for c in [0.1, 1.0, 10.0]:

        with mlflow.start_run():

            model = LogisticRegression(C=c, max_iter=500)

            model.fit(X_train, y_train)

            preds = model.predict(X_test)

            acc = accuracy_score(y_test, preds)

            mlflow.log_param("C", c)
            mlflow.log_metric("accuracy", acc)

            model_path = f"model_artifacts/model_{c}.pkl"

            with open(model_path, "wb") as f:
                pickle.dump(model, f)

            mlflow.log_artifact(model_path)


if __name__ == "__main__":
    train()
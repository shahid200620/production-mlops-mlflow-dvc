import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("churn-prediction")

train = pd.read_csv("data/processed/train_processed.csv")
X = train.drop("Survived", axis=1)
y = train["Survived"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

with mlflow.start_run() as run:
    mlflow.sklearn.log_model(model, artifact_path="model")
    print("RUN_ID:", run.info.run_id)
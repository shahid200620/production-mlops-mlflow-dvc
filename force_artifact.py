import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("churn-prediction")

with mlflow.start_run():
    with open("artifact.txt", "w") as f:
        f.write("test artifact")

    mlflow.log_artifact("artifact.txt")
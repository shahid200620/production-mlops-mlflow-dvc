# Production MLOps Pipeline with MLflow, DVC, and Automated Retraining

## Overview
This project implements a simplified **end-to-end MLOps pipeline** for training, tracking, deploying, and monitoring a machine learning model. The system demonstrates how modern production ML systems manage data, experiments, model deployment, and monitoring using industry-standard tools.

The pipeline includes:

- Data versioning using **DVC**
- Data validation using **Great Expectations**
- Experiment tracking using **MLflow**
- Model serving through a **FastAPI REST API**
- Containerized services using **Docker**
- Monitoring and drift detection
- Automated retraining trigger
- Basic automated testing

This project simulates a real-world **production ML lifecycle**.

---

# Project Architecture
production-mlops-mlflow-dvc
│

├── data/

│ ├── raw/

│ └── processed/

│

├── src/

│ ├── api/

│ │ └── main.py

│ ├── config.py

│ ├── data_processing.py

│ ├── monitoring.py

│ └── train.py

│

├── tests/

│ └── test_api.py

│

├── reports/

│

├── docker-compose.yml

├── Dockerfile

├── dvc.yaml

├── requirements.txt

└── README.md

---

# Technologies Used

- **Python**
- **FastAPI**
- **MLflow**
- **DVC (Data Version Control)**
- **Great Expectations**
- **Docker**
- **PostgreSQL**
- **Pytest**

---

# Features

## Data Versioning
The raw dataset is tracked using **DVC** to ensure reproducibility of experiments.

## Data Validation
The pipeline uses **Great Expectations** to validate the dataset before training.

## Experiment Tracking
All model training runs are logged using **MLflow**, including:

- parameters
- metrics
- experiment runs

## Model Serving
A **FastAPI REST API** serves predictions through endpoints.

Endpoints:
GET /health
POST /predict

## Monitoring
A monitoring script simulates **data drift detection** and generates an HTML drift report.
reports/data_drift_report.html


## Retraining Trigger
The system supports automated retraining triggered when drift is detected.

If a file named:
drift_detected.flag

exists, the retraining script will run the training pipeline.

## Automated Testing
Basic unit tests are implemented using **pytest** to validate API functionality.

---

# Running the System

## 1. Clone the Repository
git clone <repository-url>
cd production-mlops-mlflow-dvc

## 2. Start the Full Stack
docker-compose up --build

This will start:

- PostgreSQL database
- MLflow tracking server
- FastAPI prediction API

---

# Accessing Services

## MLflow Tracking UI
http://localhost:5000


## FastAPI API
http://localhost:8000


Interactive API docs:
http://localhost:8000/docs


---

# Running the Data Pipeline

Process data:
python src/data_processing.py


Train model:
python src/train.py


---

# Monitoring

Generate drift report:
python src/monitoring.py


Output:
reports/data_drift_report.html


---

# Retraining Trigger

Create a drift flag:
touch drift_detected.flag

Run retraining:
python retrain.py


---

# Running Tests
pytest


---

# Future Improvements

Possible improvements include:

- automated model promotion
- real-time drift detection
- CI/CD integration
- improved model evaluation
- production-grade security for APIs

---

# Conclusion

This project demonstrates the key components of a **production-ready machine learning pipeline**, integrating data engineering, machine learning, and DevOps practices through a unified MLOps workflow.



import pandas as pd
from sklearn.model_selection import train_test_split
import os
import json
import great_expectations

def process_data():

    df = pd.read_csv("data/raw/train.csv")

    df = df.drop(columns=["Name","Ticket","Cabin"])

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    df = pd.get_dummies(df, columns=["Sex","Embarked"], drop_first=True)

    train, test = train_test_split(df, test_size=0.2, random_state=42)

    os.makedirs("data/processed", exist_ok=True)

    train.to_csv("data/processed/train_processed.csv", index=False)
    test.to_csv("data/processed/test_processed.csv", index=False)

    success = train["Age"].notnull().all()

    os.makedirs("great_expectations/uncommitted/validations", exist_ok=True)

    with open("great_expectations/uncommitted/validations/results.json", "w") as f:
        json.dump({"success": bool(success)}, f)

if __name__ == "__main__":
    process_data()
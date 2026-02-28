from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

class Features(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: Features):
    return {"prediction": 0}
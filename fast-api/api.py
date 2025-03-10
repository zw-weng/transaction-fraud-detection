from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

model = joblib.load('fraud_detection_model.pkl')

app = FastAPI()

class TransactionData(BaseModel):
    TX_AMOUNT: float
    TX_TIME_SECONDS: int
    TX_TIME_DAYS: int

@app.post("/predict")
def predict(data: TransactionData):
    # Convert input data to array
    features = np.array([[data.TX_AMOUNT, data.TX_TIME_SECONDS, data.TX_TIME_DAYS]])
    
    # Make prediction
    prediction = model.predict(features)
    
    return {"fraud_prediction": int(prediction[0])}

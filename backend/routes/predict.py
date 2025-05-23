# routes/predict.py

from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import numpy as np

router = APIRouter()

# Load the trained model
model = joblib.load("glucose_predictor.pkl")

# Input schema
class GlucoseInput(BaseModel):
    Pregnancies: int
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@router.post("/", tags=["Predict"])
def predict_glucose(data: GlucoseInput):
    input_data = [
        data.Pregnancies,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]

    input_array = np.array(input_data).reshape(1, -1)
    predicted_glucose = model.predict(input_array)[0]

    return {
        "predicted_glucose": round(predicted_glucose, 2)
    }

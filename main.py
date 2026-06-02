from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
import os

app = FastAPI(title="Heart Disease Prediction API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and scaler
model_path = os.path.join(os.path.dirname(__file__), "heart_model.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)
except Exception as e:
    print(f"Error loading models: {e}")
    model = None
    scaler = None

class PredictionInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Heart Disease Prediction ML Service"}

@app.post("/predict")
def predict_heart_disease(data: PredictionInput):
    if model is None or scaler is None:
        raise HTTPException(status_code=500, detail="Model or scaler not loaded properly")

    try:
        # Convert input to DataFrame (to match training structure if applicable)
        input_data = pd.DataFrame([{
            "age": data.age,
            "sex": data.sex,
            "cp": data.cp,
            "trestbps": data.trestbps,
            "chol": data.chol,
            "fbs": data.fbs,
            "restecg": data.restecg,
            "thalach": data.thalach,
            "exang": data.exang,
            "oldpeak": data.oldpeak,
            "slope": data.slope,
            "ca": data.ca,
            "thal": data.thal
        }])

        # Scale features
        scaled_data = scaler.transform(input_data)

        # Predict
        prediction = model.predict(scaled_data)[0]
        
        # Determine label and risk
        is_disease = int(prediction) == 1
        label = "Heart Disease Detected" if is_disease else "No Heart Disease"
        risk = "High" if is_disease else "Low"

        return {
            "prediction": int(prediction),
            "label": label,
            "risk": risk
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Import necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Load the saved model and scalers
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler_X.pkl", "rb") as file:
    scaler_X = pickle.load(file)

with open("scaler_y.pkl", "rb") as file:
    scaler_y = pickle.load(file)

# Define the input data model using Pydantic
class PredictionInput(BaseModel):
    Item_Potatoes: int
    Area_United_Kingdom: int
    Item_Sweet_potatoes: int
    Area_Japan: int
    Year: int
    average_rain_fall_mm_per_year: float
    pesticides_tonnes: float
    avg_temp: float

    # Add range constraints for numeric inputs
    class Config:
        schema_extra = {
            "example": {
                "Item_Potatoes": 1,
                "Area_United_Kingdom": 1,
                "Item_Sweet_potatoes": 1,
                "Area_Japan": 1,
                "Year": 2024,
                "average_rain_fall_mm_per_year": 800.0,
                "pesticides_tonnes": 50.0,
                "avg_temp": 25.0,
            }
        }

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["POST"],  # Allow only POST requests
    allow_headers=["*"],  # Allow all headers
)

# Define the prediction endpoint
@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        # Convert input data to a numpy array
        input_array = np.array([
            input_data.Item_Potatoes,
            input_data.Area_United_Kingdom,
            input_data.Item_Sweet_potatoes,
            input_data.Area_Japan,
            input_data.Year,
            input_data.average_rain_fall_mm_per_year,
            input_data.pesticides_tonnes,
            input_data.avg_temp
        ]).reshape(1, -1)

        # Scale the input features
        input_scaled = scaler_X.transform(input_array)

        # Make a prediction
        prediction_scaled = model.predict(input_scaled)

        # Scale the prediction back to the original range
        prediction = scaler_y.inverse_transform(prediction_scaled.reshape(-1, 1))[0][0]

        # Return the prediction
        return {"predicted_crop_yield": prediction}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the app using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
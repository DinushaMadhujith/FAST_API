from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from mangum import Mangum

# Initialize FastAPI app
app = FastAPI()
handler = Mangum(app)
# Load the trained model from the .pkl file
model_path = "model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Define the request body with the specified house features
class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: int       # 1 for Yes, 0 for No
    guestroom: int      # 1 for Yes, 0 for No
    basement: int       # 1 for Yes, 0 for No
    hotwaterheating: int # 1 for Yes, 0 for No
    airconditioning: int # 1 for Yes, 0 for No
    parking: int
    prefarea: int       # 1 for Yes, 0 for No
    furnishingstatus: int # 0 for Unfurnished, 1 for Semi-Furnished, 2 for Furnished

@app.get("/")
def read_root():
    return {'message': "House Price Prediction API"}

# Define the prediction endpoint
@app.post("/predict/")
async def predict_price(features: HouseFeatures):
    # Prepare input data for the model as a NumPy array
    input_data = np.array([[features.area, features.bedrooms, features.bathrooms, features.stories,
                            features.mainroad, features.guestroom, features.basement, features.hotwaterheating,
                            features.airconditioning, features.parking, features.prefarea, features.furnishingstatus]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return the prediction as a response
    return {"predicted_price": f"${prediction[0]:,.2f}"}

# Run the FastAPI app using Uvicorn
# Command to run: `uvicorn main:app --reload`

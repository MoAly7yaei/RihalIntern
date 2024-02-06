from fastapi import FastAPI
from deployment import Model
import uvicorn

app = FastAPI()

@app.get("/predict")
async def predict(text: str):
    prediction = Model.predecion(text)
    return {"prediction": "Stressed" if prediction == 1 else "Not Stressed"}


def __init__():
    uvicorn.run(app)
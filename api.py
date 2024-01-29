from fastapi import FastAPI
from deployment import Model
import uvicorn

app = FastAPI()

@app.get("/predict")
async def predict(text: str):
    prediction = Model.predecion(text)
    return {"prediction": int(prediction)}


if __name__ == '__api__':
    uvicorn.run(app)
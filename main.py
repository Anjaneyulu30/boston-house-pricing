import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

###load model and scaler
model=pickle.load(open("regmodel.pkl","rb"))
scaler=pickle.load(open("scaler.pkl","rb"))

###FASTAPI APP
app=FastAPI(title="Bouston House Pricing API")

##input schema

class BostonInput(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: float
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: int
    TAX: int
    PTRATIO: float
    B: float
    LSTAT: float


@app.get("/")
def home():
    return {"message":"API is running"}

@app.post("/predict")
def predict(data: BostonInput):
    X=np.array([[data.CRIM,data.ZN,data.INDUS,data.CHAS,data.NOX,data.RM,data.AGE,data.DIS,data.RAD,
                 data.TAX,data.PTRATIO,data.B,data.LSTAT]])
    X_scaled=scaler.transform(X)
    y_pred=model.predict(X_scaled)
    return {"predicted price":round(float(y_pred[0]),2)}


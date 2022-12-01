from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()


class iris(BaseModel):
    sepallength: float
    sepalwidth: float
    petallength: float
    petalwidth: float


@app.post('/predict')
async def predict_speceis(iris : iris):
    data = iris.dict()
    model = "Basic001/DecesionTreeModel.pkl"
    with open(model, 'rb') as file:  
        Pickled_LR_Model = pickle.load(file)
    data_in = [[data['sepallength'], data['sepalwidth'], data['petallength'], data['petalwidth']]]
    predictation = Pickled_LR_Model.predict(data_in)
    return {
        'predictation' : predictation
    }

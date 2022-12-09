from fastapi import APIRouter
import pickle
import numpy as np
import pandas as pd
from model import *


mlmodel = APIRouter()

#load the model

regmodel = pickle.load(open('/Volumes/Badhon/Project/Personal Project/ML Project/End_To_End_ML_Project/EndToEnd_ML_Project/Basic002/regmodel.pkl', 'rb'))

@mlmodel.get('/')
def home():
    return {
        "Data" : "OK"
    }

@mlmodel.post('/predict')
def predict(data : prediction):
    data  = data.__dict__
    return data
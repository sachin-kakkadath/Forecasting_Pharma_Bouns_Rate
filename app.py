
from fastapi import FastAPI
import uvicorn
import pickle

from models import pharmainput

import numpy as np

import pandas as pd

import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

app = FastAPI()

model1 = pickle.load(open("drug_1.pkl","rb"))
model2 = pickle.load(open("drug_2.pkl","rb"))
model3 = pickle.load(open("drug_3.pkl","rb"))
model4 = pickle.load(open("drug_4.pkl","rb"))
#model5 = pickle.load(open("drug_5.pkl","rb"))

@app.get('/')
def index():
    return {'message': 'This is the homepage of the API '}

@app.post('/get_pharama_bounce_rate')
#def get_pharama_bounce_rate(quantity : int , dateofbill : str,drugname : str):
def get_pharama_bounce_rate(req : pharmainput):

    dob = req.dateofbill
    quant = req.quantity
    drn = req.drugname

    if drn == 'MULTIPLE ELECTROLYTES 500ML IVF':
        model = model1
    elif drn == 'SODIUM CHLORIDE 0.9%':
        model = model2
    elif drn == 'SODIUM CHLORIDE IVF 100ML':
        model = model3
    elif drn == 'PARACETAMOL 1GM IV INJ':
        model = model4
    else :
        return{"error" : "drug not found" }
    
    features=list([dob, quant,drn])
    pred_name = model.predict(features)

    return {'prediction': pred_name}

if __name__ == '__main__':
    uvicorn.run(app)
    #uvicorn.run(app, host='127.0.0.1', port=6000, debug=True)


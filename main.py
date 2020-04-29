import os
import json
import pandas as pd
from fastapi import FastAPI


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

dataset = os.path.join(DATA_DIR,'gigs.csv')
app = FastAPI()

@app.get('/')
def root():
    """
    Root URL, for versoning 

    :param none,
    :return string , status string
    """
    return f"Kazigig DATA API"

@app.get("/get_data")
def read_data():
    df = pd.read_csv(dataset)
    return df.to_dict("date")

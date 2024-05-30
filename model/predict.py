import joblib
from flask import jsonify, request
import numpy as np
import json
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,area,bhk):
    load_saved_artifacts()
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def prediction():
    location = request.json['location']
    area = request.json['area']
    bhk = request.json['type']

    return jsonify({"price":str(get_estimated_price(location, area, bhk))})

def load_saved_artifacts():
    global  __data_columns
    global __locations

    with open("./model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[2:]  # first 3 columns are sqft, bath, bhk

    global __model
    __model = joblib.load('./model/Chennai_Home_prices_model.joblib')

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns
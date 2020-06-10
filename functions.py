import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import json
from features import callingFeatures

def loading_model():
    with open('Banglore_house_price_model.pickle', 'rb') as fp:
        model = pickle.load(fp)

    return model

def predicting_price(model,location, sqft,bath, bhk):
    x = callingFeatures(location, sqft, bath, bhk)
    ans = model.predict([x])[0]
    return ans



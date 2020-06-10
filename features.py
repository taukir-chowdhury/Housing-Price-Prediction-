import numpy as np
import json

def callingFeatures(location,sqft,bath,bhk):    
    
    f = open('columns.json')
    loaded_file = json.load(f)

    #loading columns from json
    columns = []
    for i in loaded_file.values():
        for j in i:
            columns.append(j)
    
    # Searching for columns
    j = 0
    for i in columns:
        if i == location.lower():
            loc_index = j
            break
        j += 1
    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return x

#print(predict_price('Indira Nagar', 1200, 4, 3))

import json
import pickle
import numpy as np
import os

__locations = None
__data_columns = None
__model = None
def get_estimated_price(locations, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(locations.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_name():
    load_saved_artifacts()
    return __locations

def load_saved_artifacts():
    print('Loading saved artifacts...start')
    global __data_columns
    global __locations
    global __model
    
    # Print current working directory
    
    # Construct the full path to columns.json
    # columns_file_path = './artifacts/city.json'
    base_dir = os.path.abspath(os.path.dirname(__file__))
    columns_file_path = os.path.join(base_dir, 'artifacts', 'city.json')
    
    # Check if the file exists
    if not os.path.exists(columns_file_path):
        print(f"Error: {columns_file_path} does not  exist.")
        return
    
    # Load data_columns from columns.json
    with open(columns_file_path, 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    # Load the model from pickle file
    path_to_model=os.path.join(base_dir, 'artifacts', 'banglore_home_price_model.pickle')
    # with open('./artifacts/banglore_home_price_model.pickle', 'rb') as f:
    with open(path_to_model, 'rb') as f:
        __model = pickle.load(f)
    
    print('Loading saved artifacts...done')

if __name__ == '__main__':
    print(__locations)
    # load_saved_artifacts()
    # print(get_location_name())
    # print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location

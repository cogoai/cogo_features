import requests 
import numpy as np
import json
import os

url = os.environ['COGO_FEATURES_SERVER_URL']

def fetch_feature_remotely(text):
    response = requests.post(url, json={'utterences': [text]})
    result = response.json()['result'][0]
    return np.array(json.loads(result))

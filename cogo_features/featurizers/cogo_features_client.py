import requests 
import numpy as np
import json
import os

def fetch_feature_remotely(text):
    print('fetching feature remotely.....')
    response = requests.post(os.environ['COGO_FEATURES_SERVER_URL'], json={'utterences': [text]})
    result = response.json()['result'][0]
    return np.array(json.loads(result))

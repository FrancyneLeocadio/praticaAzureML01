import json
import numpy as np
from azureml.core.model import Model
from sklearn.linear_model import LogisticRegression

def init():
    global model
    model_path = Model.get_model_path("modelo_classificacao")
    model = LogisticRegression()
    model.load(model_path)

def run(data):
    try:
        data = json.loads(data)
        predictions = model.predict(np.array(data['features']))
        return json.dumps(predictions.tolist())
    except Exception as e:
        return str(e)
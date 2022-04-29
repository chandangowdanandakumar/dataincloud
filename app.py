from crypt import methods
from flask import Flask, render_template, request
import pickle
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    payload = request.get_json()
    print(payload)
    res = model()
    if res > 0.9:
        result = {"result":True}
    else:
        result = {"result":False}
    return json.dumps(result)

def model():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LogisticRegression
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    dataset = load_iris()
    names = dataset.feature_names
    features = dataset.data
    labels = dataset.target
    feature_train, feature_test, label_train, label_test = train_test_split(
        features, labels, test_size=0.2, random_state=42
    )
    model = pickle.load(open('model.pkl','rb'))
    model.fit(feature_train, label_train)
    label_pred = model.predict(feature_test)
    from sklearn.metrics import accuracy_score
    print((accuracy_score(label_pred, label_test)))
    return (accuracy_score(label_pred, label_test))


if __name__ == '__main__':
    app.run(debug=True)
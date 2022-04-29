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
    model = pickle.load(open('model.pkl','rb'))
    result = {"result":False}
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
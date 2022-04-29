from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():

    result = {"result":True}
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
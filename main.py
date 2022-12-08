from flask import Flask, jsonify, render_template, request
from six.moves import urllib
import pandas as pd
import os
import json

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    timeInterval = 1000
    data = pd.DataFrame()
    url = os.environ['API_URL'] + '/hw5/GetData.php'
    data['time'] = pd.DataFrame(json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['values'])
    return jsonify(data)

@app.route('/predict')
def predict():
    return 0

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

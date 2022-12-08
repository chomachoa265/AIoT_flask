from flask import Flask, jsonify, render_template, request
from six.moves import urllib
import pandas as pd
import os

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    timeInterval = 1000
    data = pd.DataFrame()
    print(vars)
#     url = ${{ API_URL }} + '/hw5/getData'
#     data['time'] = pd.DataFrame(json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['values'])
    return data

@app.route('/predict')
def predict():
    return 0

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

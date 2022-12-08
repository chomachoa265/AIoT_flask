from flask import Flask, jsonify, render_template, request
from six.moves import urllib
import pandas as pd
import os
import json

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    # url = "https://0fda-2001-b400-e4d4-9966-4931-116-faac-5376.jp.ngrok.io" + '/hw5/GetData.php'
    url = os.environ['API_URL'] + '/hw5/GetData.php'
    data = json.loads(urllib.request.urlopen(url).read())
    return jsonify(data)

@app.route('/predict')
def predict():
    return 0

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

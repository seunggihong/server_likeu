from flask import Flask, request, render_template, jsonify
from flask_restx import Api, Resource

import json
from dotenv import load_dotenv
import os

load_dotenv()
USER_URL = os.environ.get('USER_URL')
AD_URL = os.environ.get('AD_URL')

app = Flask(__name__)
api = Api(app)

def load_data(url="/"):
    with open(url) as f:
        data = json.load(f)
    return data

@app.route('/users')
def index():
    data = load_data(USER_URL)
    return jsonify(data)

@app.route('/ads')
def ad_list():
    data = load_data(AD_URL)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)

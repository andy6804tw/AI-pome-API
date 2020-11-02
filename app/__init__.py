# -*- coding: UTF-8 -*-
import requests
import json

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def getResult():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    URL='https://ai.foxconn.com/textbook/interactive/rnn/lstm/5455945/predict'
    params={'word':'人工智慧'}
    r = requests.post(URL, data=params, headers=headers)
    result=json.loads(r.text)['result']
    return jsonify({'result': str(result)})

@app.route('/predict', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    word=insertValues['word']
    # 進行預測
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    URL='https://ai.foxconn.com/textbook/interactive/rnn/lstm/5455945/predict'
    params={'word':word}
    r = requests.post(URL, data=params, headers=headers)
    result=json.loads(r.text)['result']
    return jsonify({'result': str(result)})
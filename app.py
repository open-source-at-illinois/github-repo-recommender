from http.client import BAD_REQUEST, OK
from flask_cors import CORS
from flask import Flask, render_template, request
import os
import sys

from ai.hugging_face.hugging_face import llm

app = Flask(__name__, template_folder='./frontend')
CORS(app)

@app.get('/')
def home_page():
    return render_template('index.html')

@app.post('/')
def process_query():
    data = request.json
    keywords = data['text']
    query = 'Give me github repositories based on'
    for keyword in keywords:
        query += keyword + ', '
    query = query[:-2]
    query = query[:-1] + 'and ' + query[-1] + '.'
    response = llm(query)
    return {'message':response}, OK


    



if __name__ == "__main__":
    app.run(host='localhost', debug=True)
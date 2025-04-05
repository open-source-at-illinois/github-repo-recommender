from http.client import BAD_REQUEST, OK
from flask_cors import CORS
from flask import Flask, render_template, request
import os
import sys

from ai.hugging_face.hugging_face import llm
# import re
import markdown

app = Flask(__name__, template_folder='./frontend')
CORS(app)

default_response = 'Waiting for input ....' 

@app.get('/')
def home_page():
    return render_template('index.html', response=default_response)

@app.post('/')
def process_query():
    keywords = request.form['keywords']
    keywords = 'and'.join(keywords.split(','))
    query = f'Give me a list of github repositories using {keywords}'
    llm_response = llm(query)
    # formatted_response = re.sub(r'\*\*(.*?)\*\*', r'\1', llm_response)
    # formatted_response = formatted_response.replace('*', '')
    formatted_response = markdown.markdown(llm_response)
    return render_template('index.html', response=formatted_response)


    



if __name__ == "__main__":
    app.run(host='localhost', debug=True)
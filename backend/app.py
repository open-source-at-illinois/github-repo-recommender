from http.client import BAD_REQUEST, OK
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend/static')

response = "Send some keywords!"

@app.get('/')
def home_page():
    return render_template('index.html', response=response)

@app.post('/')
def get_keywords():
    keywords = request.form['keywords']
    response = f"keywords received: {keywords}"

    return render_template('index.html', response=response)
    return {"message": f"keywords received: {keywords}"}, OK


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
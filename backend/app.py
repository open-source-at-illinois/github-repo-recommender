from flask import Flask, render_template

app = Flask(__name__, template_folder='../frontend')

@app.get('/')
def home_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
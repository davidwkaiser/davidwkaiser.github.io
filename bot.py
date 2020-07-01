from flask import Flask
from flask import url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/iframe')
def iframe():
    return render_template("iframe.html")

@app.route('/messenger')
def messenger():
    return render_template("messenger.html")    

# @app.route('/assistant')
# def assistant():
#     return render_template("assistant.html")   

@app.route('/covid')
def covid():
	return render_template("covid.html")
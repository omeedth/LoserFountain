# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello World!"

from flask import Flask
from flask import render_template

# @app.route('/hello/')
# @app.route('/hello/<name>')

app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('flask.html', name=name)

#git subtree push --prefix Bot heroku master

from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():

    return """Funciona :D"""


if __name__ == '__main__':
    app.run()

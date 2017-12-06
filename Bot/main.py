from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():

    return """Holi"""

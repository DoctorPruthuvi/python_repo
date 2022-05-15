from email import message
from urllib import request
from flask import Flask, jsonify, request
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/new year")
def super_simple():
    return jsonify(message="happy New year") , 200

@app.route("/not_found")
def not_found():
    return jsonify(message="Error Not found!") , 404

@app.route("/parameters")
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))


if __name__ == '__main__':
    app.run()
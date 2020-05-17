import values
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)

@app.route('/api/app/auth/getToken')
def hello_world():
    return "<h1>Hello world from Flask!<h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

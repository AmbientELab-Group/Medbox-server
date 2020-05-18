from flask import Blueprint
from flask import request, jsonify
from .defs import *

auth_api = Blueprint('auth_api', __name__)

@auth_api.route("/api/app/auth/authenticate", methods=['POST'])
def authenticate():
    if int(request.json["CODE"]) != SECURITY_CODE:
        response = {
            'token': '',
            'status': 'INVALID_CODE'
        }
    else:
        response = {
            'token': TOKEN,
            'status': 'OK'
        }
    
    return jsonify(response)
        

@auth_api.route("/api/app/auth/test-token", methods=['POST'])
def testToken():
    if request.json["TOKEN"] == TOKEN:
        response = {
            'valid': True,
            'status': 'OK'
        }
    
    else:
        response = {
            'valid': False,
            'status': 'OK'
        }
    return jsonify(response)

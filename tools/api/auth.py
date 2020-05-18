from flask import Blueprint
from flask import request, jsonify
from .defs import *

auth_api = Blueprint('auth_api', __name__)

@auth_api.route("/api/app/auth/authenticate", methods=['POST'])
def authenticate():
    if int(request.json["code"]) != SECURITY_CODE:
        response = {
            'token': '',
            'request_status': 'INVALID_CODE'
        }
    else:
        response = {
            'token': TOKEN,
            'request_status': 'OK'
        }
    
    return jsonify(response)
        

@auth_api.route("/api/app/auth/test-token", methods=['POST'])
def testToken():
    if request.json["token"] == TOKEN:
        response = {
            'valid': True,
            'request_status': 'OK'
        }
    
    else:
        response = {
            'valid': False,
            'request_status': 'OK'
        }
    return jsonify(response)

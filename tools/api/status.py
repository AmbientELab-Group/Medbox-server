from flask import Blueprint
from flask import request, jsonify
from .defs import *

status_api = Blueprint('status_api', __name__)

@status_api.route("/api/app/status/device-list", methods=['POST'])
def deviceList():
    if request.json["TOKEN"] != TOKEN:
        response = {
            'status': 'INVALID_TOKEN'
        }
        return jsonify(response)
    
    response = {
        'status': 'OK',
        'devices': DEVICES
    }
    return jsonify(response)
    
@status_api.route("/api/app/status/device-status", methods=['POST'])
def deviceStatus():
    if request.json["TOKEN"] != TOKEN:
        response = {
            'status': 'INVALID_TOKEN'
        }
        return jsonify(response)
    
    if request.json["DEVICE"] == DEVICE1_ID:
        response = {
            'status': 'OK',
            'device_status': 'OK',
            'battery_level': 50,
            'last_seen': '2020-04-25 12:14:34',
            'containers':[
                    {
                        'level': 60
                    },
                    {
                        'level': 80
                    },
                    {
                        'level': 40
                    }
                ]
        }
        return jsonify(response)

    elif request.json["DEVICE"] == DEVICE2_ID:
        response = {
            'status': 'OK',
            'device_status': 'LOW_MEDS',
            'battery_level': 50,
            'last_seen': '2020-04-24 12:14:34',
            'containers':[
                    {
                        'level': 20
                    },
                    {
                        'level': 80
                    }
                ]
        }
        return jsonify(response)

    else:
        response = {
            'status': 'DEVICE_NOT_FOUND',
            'notifications': []
        }
        return jsonify(response)

@status_api.route("/api/app/status/adherence", methods=['POST'])
def adherenceStatus():
    if request.json["TOKEN"] != TOKEN:
        response = {
            'status': 'INVALID_TOKEN'
        }
        return jsonify(response)
    
    if request.json["DEVICE"] == DEVICE1_ID:
        response = {
            'status': 'OK',
            'adherence':[
                ('2020-04-1', 10),
                ('2020-04-2', 10),
                ('2020-04-3', 10),
                ('2020-04-4', 10),
                ('2020-04-5', 10),
                ('2020-04-6', 10),
                ('2020-04-7', 10),
                ('2020-04-8', 0),
                ('2020-04-9', 10),
                ('2020-04-10', 8),
                ('2020-04-11', 8),
                ('2020-04-12', 7),
                ('2020-04-13', 10),
                ('2020-04-14', 10),
                ('2020-04-15', 10)
            ]
        }
        return jsonify(response)

    elif request.json["DEVICE"] == DEVICE2_ID:
        response = {
            'status': 'OK',
            'adherence':[
                ('2020-04-1', 10),
                ('2020-04-2', 10),
                ('2020-04-3', 5),
                ('2020-04-4', None),
                ('2020-04-5', None),
                ('2020-04-6', 10),
                ('2020-04-7', 10),
                ('2020-04-8', 0),
                ('2020-04-9', 10),
                ('2020-04-10', 8),
                ('2020-04-11', 8),
                ('2020-04-12', 7),
                ('2020-04-13', 10),
                ('2020-04-14', 10),
                ('2020-04-15', 10)
            ]
        }
        return jsonify(response)

    else:
        response = {
            'status': 'DEVICE_NOT_FOUND',
            'notifications': []
        }
        return jsonify(response)

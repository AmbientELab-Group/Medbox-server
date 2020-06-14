from flask import Blueprint
from flask import request, jsonify
from .defs import *

status_api = Blueprint('status_api', __name__)

@status_api.route("/api/app/status/device-list", methods=['POST'])
def deviceList():
    if request.json["token"] != TOKEN:
        response = {
            'request_status': 'INVALID_TOKEN'
        }
        return jsonify(response)
    
    response = {
        'request_status': 'OK',
        'devices': [
                {
                    'device_name': DEVICE1_NAME,
                    'device_id': DEVICE1_ID
                },
                {
                    'device_name': DEVICE2_NAME,
                    'device_id': DEVICE2_ID
                }
            ]
    }
    return jsonify(response)
    
@status_api.route("/api/app/status/device-status", methods=['POST'])
def deviceStatus():
    if request.json["token"] != TOKEN:
        response = {
            'request_status': 'INVALID_TOKEN'
        }
        return jsonify(response)
    
    # device statuses:
    # OK - Everything is OK
    # LOW_MEDS - Please replace container
    # OUT_OF_MEDS - Out of meds
    # LOW_BATTERY - Low battery
    # DEAD_BATTERY - Dead battery
    # NO_CONNECTION - Connectivity issues
    # LATE_MEDS_CONTAINER_FULL - Late meds container is full
    # DEVICE_BROKEN - Device is broken.
    if request.json["device"] == DEVICE1_ID:
        response = {
            'request_status': 'OK',
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

    elif request.json["device"] == DEVICE2_ID:
        response = {
            'request_status': 'OK',
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
            'request_status': 'DEVICE_NOT_FOUND',
            'notifications': []
        }
        return jsonify(response)

@status_api.route("/api/app/status/adherence", methods=['POST'])
def adherenceStatus():
    if request.json["token"] != TOKEN:
        response = {
            'request_status': 'INVALID_TOKEN'
        }
        return jsonify(response)
    
    if request.json["device"] == DEVICE1_ID:
        response = {
            'request_status': 'OK',
            'adherence':[
                {'time': '2020-06-1', 'score': 0},
                {'time': '2020-06-2', 'score': 6},
                {'time': '2020-06-3', 'score': 3},
                {'time': '2020-06-4', 'score': 6},
                {'time': '2020-06-5', 'score': 3},
                {'time': '2020-06-6', 'score': 4},
                {'time': '2020-06-7', 'score': 8},
                {'time': '2020-06-8', 'score': 2},
                {'time': '2020-05-25', 'score': 4}
            ]
        }
        return jsonify(response)

    elif request.json["device"] == DEVICE2_ID:
        response = {
            'request_status': 'OK',
            'adherence':[
                {'time': '2020-06-1', 'score': 10},
                {'time': '2020-06-2', 'score': 10},
                {'time': '2020-06-3', 'score': 10},
                {'time': '2020-06-4', 'score': 6},
                {'time': '2020-06-5', 'score': 3},
                {'time': '2020-06-6', 'score': 4},
                {'time': '2020-06-7', 'score': 8},
                {'time': '2020-06-8', 'score': 9},
                {'time': '2020-05-31', 'score': 10}
            ]
        }
        return jsonify(response)

    else:
        response = {
            'request_status': 'DEVICE_NOT_FOUND',
            'notifications': []
        }
        return jsonify(response)

from flask import Blueprint
from flask import request, jsonify
from .defs import *

notification_api = Blueprint('notification_api', __name__)

device1Notifications = [
    {
        'device': DEVICE1_ID,
        'time': '2020-3-12 21:12:13',
        'notification': 'Medication dispensed',
        'severity': 'INFO'
    },
    {
        'device': DEVICE1_ID,
        'time': '2020-3-9 21:12:13',
        'notification': 'Batteries are running out!',
        'severity': 'WARNING'
    },
    {
        'device': DEVICE1_ID,
        'time': '2020-3-8 21:12:13',
        'notification': 'Emergency medication dispensed!',
        'severity': 'CRITICAL'
    }
]
            
device2Notifications = [
    {
        'device': DEVICE2_ID,
        'time': '2020-3-12 21:22:13',
        'notification': 'Medication dispensed',
        'severity': 'INFO'
    }
]

@notification_api.route("/api/app/notify/fetch/all", methods=['POST'])
def getAllNotifications():
    if request.json["TOKEN"] != TOKEN:
        response = {
            'status': 'INVALID_TOKEN',
            'notifications': []
        }
    else:
        response = {
            'status': 'OK',
            'notifications': device1Notifications + device2Notifications
        }
    return jsonify(response)
    
@notification_api.route("/api/app/notify/fetch/by-device/all", methods=['POST'])
def getNotificationsByDevice():
    if request.json["TOKEN"] != TOKEN:
        response = {
            'status': 'INVALID_TOKEN',
            'notifications': []
        }
        return jsonify(response)

    if request.json["DEVICE"] == DEVICE1_ID:
        response = {
            'status': 'OK',
            'notifications': device1Notifications
        }
        return jsonify(response)

    elif request.json["DEVICE"] == DEVICE2_ID:
        response = {
            'status': 'OK',
            'notifications': device2Notifications
        }
        return jsonify(response)

    else:
        response ={
            'status': 'DEVICE_NOT_FOUND',
            'notifications': []
        }
        return jsonify(response)

@notification_api.route("/api/app/notify/fetch/by-device/latest", methods=['POST'])
def getLatestNotificationsByDevice():
    if request.json["TOKEN"] != TOKEN:
        response = {
            'status': 'INVALID_TOKEN',
            'notifications': []
        }
        return jsonify(response)

    if request.json["DEVICE"] == DEVICE1_ID:
        response = {
            'status': 'OK',
            'notifications': device1Notifications[:2]
        }
        return jsonify(response)

    elif request.json["DEVICE"] == DEVICE2_ID:
        response = {
            'status': 'OK',
            'notifications': [device2Notifications[0]]
        }
        return jsonify(response)

    else:
        response = {
            'status': 'DEVICE_NOT_FOUND',
            'notifications': []
        }
        return jsonify(response)

@notification_api.route("/api/app/notify/fetch/latest", methods=['POST'])
def getLatestNotifications():
    if request.json["TOKEN"] != TOKEN:
        response = {
            'status': 'INVALID_TOKEN',
            'notifications': []
        }
        return jsonify(response)
    
    response = {
        'status': 'OK',
        'notifications': device1Notifications[:1]+[device2Notifications[0]]
    }
    return jsonify(response)

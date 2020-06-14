from flask import Blueprint
from flask import request, jsonify
from .defs import *

notification_api = Blueprint('notification_api', __name__)

device1Notifications = [
    {
        'device_ID': DEVICE1_ID,
        'device_name': DEVICE1_NAME,
        'time': '2020-6-11 20:11:00',
        'notification_title': 'Medication dispensed', 
        'notification': '',
        'severity': 'INFO'
    },
    {
        'device_ID': DEVICE1_ID,
        'device_name': DEVICE1_NAME,
        'time': '2020-3-12 21:12:13',
        'notification_title': 'Medication dispensed', 
        'notification': '',
        'severity': 'INFO'
    },
    {
        'device_ID': DEVICE1_ID,
        'device_name': DEVICE1_NAME,
        'time': '2020-3-9 21:12:13',
        'notification_title': 'Batteries running out!',
        'notification': 'You have 5 days of batteries left!',
        'severity': 'WARNING'
    },
    {
        'device_ID': DEVICE1_ID,
        'device_name': DEVICE1_NAME,
        'time': '2020-3-8 21:12:13',
        'notification_title': 'Emergency medications dispensed!',
        'notification': '',
        'severity': 'CRITICAL'
    }
]
            
device2Notifications = [
    {
        'device_ID': DEVICE2_ID,
        'device_name': DEVICE2_NAME,
        'time': '2020-3-12 21:22:13',
        'notification_title': 'Medication dispensed', 
        'notification': '',
        'severity': 'INFO'
    }
]

@notification_api.route("/api/app/notify/fetch/all", methods=['POST'])
def getAllNotifications():
    if request.json["token"] != TOKEN:
        response = {
            'request_status': 'INVALID_TOKEN',
            'notifications': []
        }
    else:
        response = {
            'request_status': 'OK',
            'notifications': device1Notifications + device2Notifications
        }
    return jsonify(response)
    
@notification_api.route("/api/app/notify/fetch/by-device/all", methods=['POST'])
def getNotificationsByDevice():
    if request.json["token"] != TOKEN:
        response = {
            'request_status': 'INVALID_TOKEN',
            'notifications': []
        }
        return jsonify(response)

    if request.json["device"] == DEVICE1_ID:
        response = {
            'request_status': 'OK',
            'notifications': device1Notifications
        }
        return jsonify(response)

    elif request.json["device"] == DEVICE2_ID:
        response = {
            'request_status': 'OK',
            'notifications': device2Notifications
        }
        return jsonify(response)

    else:
        response ={
            'request_status': 'DEVICE_NOT_FOUND',
            'notifications': []
        }
        return jsonify(response)

@notification_api.route("/api/app/notify/fetch/latest", methods=['POST'])
def getLatestNotifications():
    if request.json["token"] != TOKEN:
        response = {
            'request_status': 'INVALID_TOKEN',
            'notifications': []
        }
        return jsonify(response)
    
    response = {
        'request_status': 'OK',
        'notifications': device1Notifications[:1]+[device2Notifications[0]]
    }
    return jsonify(response)

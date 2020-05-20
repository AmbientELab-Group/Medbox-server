# App API map

Here is some quick map of the application API.


## Authentication API
A set of APIs for authentication.

#### http://10.0.2.2:8000/api/app/auth/authenticate
API for performing pairing.

You have to send:

```
{
    "code": "Put here a code entered by user."
}
```

You will get:

```
{
    "token": "Token or empty string if error occurs",
    "request_status": "INVALID_CODE or OK"
}
```

#### http://10.0.2.2:8000/api/app/auth/test-token
API for checking if token is correct.

You have to send:

```
{
    "token": "Token"
}
```

You will get:

```
{
    "valid": true or false,
    "request_status": "OK or ERR"
}
```

## Notifiations API
APIs for getting notifications.

#### http://10.0.2.2:8000/api/app/notify/fetch/all
Fetch all notifications.

You have to send:

```
{
    "token": "Token"
}
```

You will get:

```
{
    "notifications": [
        {
            "device_ID": "Device ID string",
            "time": "Datetime string, ex 2020-3-12 21:12:13",
            "notification_title": "Title of the notification",
            "notification": "Body of the notification",
            "severity": "CRITICAL, WARNING or INFO"
        },
        ...
    ],
    "request_status": "OK or ERR"
}
```

#### http://10.0.2.2:8000/api/app/notify/fetch/by-device/all
Fetch all notifications by device ID

You send:

```
{
    "token": "Token",
    "device": "Device ID string"
}
```

You will get:

```
{
    "notifications": [
        {
            "device_ID": "Device ID string",
            "time": "Datetime string, ex 2020-3-12 21:12:13",
            "notification_title": "Title of the notification",
            "notification": "Body of the notification",
            "severity": "CRITICAL, WARNING or INFO"
        },
        ...
    ],
    "request_status": "OK or ERR"
}
```


#### http://10.0.2.2:8000/api/app/notify/fetch/latest
Fetch latest notifications.

You send:

```
{
    "token": "Token"
}
```

You will get:

```
{
    "notifications": [
        {
            "device_ID": "Device ID string",
            "time": "Datetime string, ex 2020-3-12 21:12:13",
            "notification_title": "Title of the notification",
            "notification": "Body of the notification",
            "severity": "CRITICAL, WARNING or INFO"
        },
        ...
    ],
    "request_status": "OK or ERR"
}
```

## Status API
API for acquiring device statuses.

#### http://10.0.2.2:8000/api/app/status/device-list
Fetch a list of devices paired with the account.

You send:
```
{
     "token": "Token"
}
```

You get:

```
{
    "devices": [
        {
            "device_name": "Human readable name of the device",
            "device_id": "ID of the device
        },
        ...
    ],
    "request_status": "OK or ERR"
}

```

#### http://10.0.2.2:8000/api/app/status/device-status
Fetch the status of the device.

You send:

```
{
    "token": "Token",
    "device": "Device ID string"
}
```

You get:

```
{
    "device_status": "Status of the device",
    "battery_level": integer from 0 to 100,
    "last_seen": "Date and time of last device connection to the server.",
    "containers": [
        {
            "level": integer from 0 to 100
        },
        ...
    ],
    "request_status": "OK or ERR"
}
```

Possible device statuses:

device statuses:
 - OK -> Everything is OK
 - LOW_MEDS -> Please replace container
 - OUT_OF_MEDS -> Out of meds
 - LOW_BATTERY -> Low battery
 - DEAD_BATTERY -> Dead battery
 - NO_CONNECTION -> Connectivity issues
 - LATE_MEDS_CONTAINER_FULL -> Late meds container is full
 - DEVICE_BROKEN -> Device is broken.

#### http://10.0.2.2:8000/api/app/status/adherence
Fetch the adherence information from the device.

You send:

```
{
    "token": "Token",
    "device": "Device ID string"
}
```

You get:

```
{
    "adherence": [
        {
            "time": "Date and time",
            "score": Score from 0 to 10
        },
        ...
    ],
    "request_status": "OK or ERR"
}
```

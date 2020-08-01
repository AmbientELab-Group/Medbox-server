# Key components

Server software has 4 major components:

 - Website backend
 - Device API
 - Mobile App API
 - Database

# Functons assigned to every components

Website backend:

Key functionalities (not in order):

 - User registration and account management
 - Authentication of users (Handled by django).
 - Treatment profile design.
 - Device management panel. 
 - Adherence monitoring panel.
 - Assigning an app

(Generally all stuff related to the operation of the website).

Device API :

 - Pairing of the device.
 - Uploading treatment profile into the device.
 - Collecting event reports (medicine taken, batteries are running out, device is on fire ...)

Mobile App API :

 - Pairing of the mobile app.
 - Providing notifications regarding the device operaton.

Database:

 - Stores stuff.

# Containers

 - webapp-server -> Django runs there.
 - mainDB -> Database runs there.


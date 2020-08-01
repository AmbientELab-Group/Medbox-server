# Current structure of the API

# Pairing procedure

Currently this is the only thing that is done.

It has the following steps:

 - 1) Device talks to the server for the first time requesting a unique security token and a unique 6 digit code.
 - 2) Server creates a device record in the database and assigns a security token to it also creates a pairing code and assigns
 it to the device.
 - 3) Server sends a pairing code and a token to the device.
 - 4) Device speaks a 6 digit code to the user.
 - 5) User enters the code on the pairing page.
 - 6) If the code is correct the device record get's linked to his account.
 - 7) If code expires (after a few minuts) pairing has failed so it starts from step 1).

What has to be done:

 - Implement a more optimal way of generating tokens.
 - Create a service for cleaning old tokens and codes.


# Other APIs that have to be implemented

#### Treatment download API

Current procedure is:

 - 1) User displays instructions on the website, takes the container out and refills it.
 - 2) User puts the container back. Device querries this API for the assigned treatment.
 - 3) It get's a tretment in a JSON format, it processes it and notifies about the result of this operation through reporting API.

The API should querry the database and export the treatment assigned to the device as a JSON string.
Treatment correctness will be handled by the website. To simplify reporting errors to the user.

Structure of the treatment has to be determined.

#### Reporting API

This is an API for reporting all things that happen to the device.
Structure is to be determined by it will have to report the following things: 

 - The fact that medicine ha been taken (with time stamp).
 - Status of the device (batteries, container levels).
 - Events connected to the device itself like "container taken out", "batteries running out" (debug messages included here).

So far this will be probably be it but we may add more stuff in the future.

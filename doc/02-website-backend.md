# Users roles and other remarks

A lot of design decisions have been made to satisfy requirements of Problem Based Learning Course.
Some of them are quite shitty because this won't be a product, it will be a research tool.

One of them is a decision to have 3 user roles:

##### Caretaker

Fancy name for a normal user. He can do all stuff except browsing for different patient data.
He cannot access other patients data.

##### Doctor

All he can do is create treatment profiles and monitor adherence.

##### Admin

This is a flag that can be set for any user and he will gain access to the admin panel.

TODO: This is unnecessary complication. We can remove roles and replace them with a field for permissions
(django already has a built in system for this). In fact currently we do not have any need for special permissions.

# Pages and what do they do??

Here is a list of all pages on the website and their functionalities.

##### path('', pages.index, name='index')

Root path, redirects to login page.

##### path('auth/login', pages.auth.login, name='login-page'),

Shows login form if user is not authenticated.
Otherwise redirects to user dashboard.

##### path('auth/logout', pages.auth.logout, name='logout-page'),

Page that logs the user out and redirects him to the login page.

##### path('auth/register', pages.auth.register, name='registration-page'),

Page that contains registration page for the user.

##### path('account/dashboard', pages.account.dashboard, name='user-dashboard'),

Page that contains a user dashboard. It should contain some frequently used functions.
Currently it just has a link to account edit and password change.

TODO: If we don't find any stuff to put here we can just remove this page and make some dropdown menu.

##### path('account/edit', pages.account.edit, name='user-account-edit'),

This page contains a form to edit user credentials and some stuff like that.
This works so only UI work has to be done here.

##### path('account/passwd-change', pages.account.passwdChange, name='user-password-change'),

This page contains password change form.
This works so only UI work has to be done here.

##### path('account/apps/dashboard', pages.account.apps.dashboard, name='user-apps-dashboard'),

This page contains a dashboard for applications paired with the account.
Currently this is empty since app is a steaming pile of sh*t and API does not exist.

##### path('account/apps/add', pages.account.apps.add, name='user-apps-add'),

This page was supposed to be a form for adding new apps to the account. Quite
possibly we will just use username and password for this.

TODO: Delete this page since we will just use a login and password from the main acount.

##### path('treatment/dashboard', pages.treatment.dashboard, name='treatment-dashboard'),

This page contains a list of all treatments assigned to the current account.

This page had some additional features depending on the user role but this is no longer necessary.

TODO: Make this page the same for all users. Delete an option to search for treatments.

##### path('treatment/<str:treatmentID>/edit', pages.treatment.edit, name='treatment-edit'),

Page that provides an interface for edyting new treatments and adding new treatments.
Adding new treatment happens if ID is set to new.

TODO: UI work is necessary here to make it look nice.

##### path('treatment/<str:treatmentID>/exportToken', pages.treatment.exportToken, name='treatment-export-token'),

This page was supposed to be used by doctor to export a treatment as a key.

TODO: This is no longer necessary. Delete this page.

##### path('treatment/<str:treatmentID>/medicine/<str:medicineID>/edit', pages.treatment.medicine.edit, name='treatment-medicine-edit'),

Page for edyting a medicine properties or adding a new medicine.

TODO: This shouldn't be a separate page. Edyting medicine should be integrated into the treatment edit page. This
path should be just an API to apply changes to the database.

##### path('treatment/<str:treatmentID>/medicine/<str:medicineID>/delete', pages.treatment.medicine.delete, name='treatment-medicine-delete'),

Link for deleting a medicine. It displays a confirmation.

TODO: Confirmation should be included into the treatment edit page.
This should be just an API interface to delete a medicine.

##### path('treatment/import', pages.treatment.importPage, name='treatment-import'),

This page was for caretaker so he can import a treatment to his account.

TODO: This is no longer necessary. Delete this page.

##### path('treatment/adherence', pages.treatment.adherence, name='treatment-adherence'),

This page is supposed to fetch an information about the adherence connected with the given treatment
and display some graphs.

TODO: Currently this is an empty page. Change link so it contains treatment ID.
Oh and implement the whole thing. This will be done after the report collection
will be done in the device API.

##### path('devices/dispensor/dashboard', pages.devices.dispensor.dashboard, name='devices-dispensor-dashboard'),

This page contains a list of all all devices connected with the account and options associated
with each device.

TODO: Make it look nice in the UI. New features will be added as needed.

##### path('devices/dispensor/add', pages.devices.dispensor.add, name='devices-dispensor-add'),

This page will provide instructions for device pairing and have a field to enter the
pairing code.

TODO: Make it look nice and add instructions.

##### path('devices/dispensor/<str:dispensorID>/delete', pages.devices.dispensor.delete, name='devices-dispensor-delete'),

Page for deleting a device. It should contain a confirmation.

TODO: Add confirmation and make sure that we cannot delete not my devices.

##### path('devices/dispensor/status', pages.devices.dispensor.status, name='devices-dispensor-status'),

This page contains a status of the particular device.

TODO: Implement this.

This page will be implemented after API for receiving reports from the device.

##### path('devices/dispensor/refill', pages.devices.dispensor.refill, name='devices-dispensor-refill')

This page will be related to refill procedure. It will allow user to assign a treatment to the device (or this will be done
somewhere else) and will provide user with instructions how to refill the device.

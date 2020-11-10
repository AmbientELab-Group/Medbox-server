#!/bin/sh
# to run it inside a container type (in this directory):
# docker exec -i medbox-backend_server bash < migrate.sh
# don't forget to create superuser afterwards
./manage.py makemigrations AdminPanel
./manage.py makemigrations AppAPI
./manage.py makemigrations DeviceAPI
./manage.py migrate

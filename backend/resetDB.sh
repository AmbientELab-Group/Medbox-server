#!/bin/sh
# removes all migration files and recreates "mainDB" database

rm -r ./app/*/migrations/*
docker cp ./resetDB.sql medbox-database_server:/
docker exec medbox-database_server /bin/sh -c 'psql -U postgres < /resetDB.sql'
docker exec medbox-database_server /bin/sh -c 'rm resetDB.sql'
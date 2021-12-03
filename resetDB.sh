#!/bin/bash
# removes all migration files, recreates "mainDB" database, performs all migrations and creates superuser
read -p "This command will erease all your DB entries. Do you want to continue? (y/n) " answer
case ${answer:0:1} in
    y|Y ) ;;
    * ) echo "Command aborted"; exit;;
esac

docker-compose stop medbox-database_server medbox-backend_server
rm -r ./app/*/migrations/*

docker-compose up -d medbox-database_server
docker cp ./resetDB.sql medbox-database_server:/
docker exec medbox-database_server /bin/sh -c 'psql -U postgres < /resetDB.sql'
docker exec medbox-database_server /bin/sh -c 'rm resetDB.sql'

docker-compose up -d medbox-backend_server
docker exec -i medbox-backend_server bash < migrate.sh

docker-compose stop medbox-database_server medbox-backend_server
docker-compose up medbox-database_server medbox-backend_server

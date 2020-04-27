# Medbox Server Side Software

This is the repository for the Medbox server side services.

## How do I start working with this?!!

Your are probably asking yourself this question right now.
So here is a quick guide on how to get your environment up and running.

Note: Shell commands are the same for windows, the prompt will however look different
depending on your platform of choice.

### Installing tools
First you need to install docker (https://docs.docker.com/get-docker/)
and docker-compose (https://docs.docker.com/compose/install/).

You will also need git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
so you can publish your work back to this repository.

If you want more graphical way to manage your work please consider using git kraken.
It provides a very user friendly way to manage versioning control using git.
Here is a link: https://www.gitkraken.com/

Once you are done with installation please make sure that docker is working by running:

```
docker run hello-world
```

This command should download a hello world example and run it.
If it does not work please make sure that virtualization is enabled in your BIOS.
If it still does not work please consult your search engine of choice.

Once you are done with this you can remove the created image and container so it does not
clutter your list of images.

First list all containers to get the container ID.

```
[krzys@starship Medbox-server]$ docker ps --all
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                          PORTS               NAMES
b792a79316f3        hello-world         "/hello"            2 minutes ago       Exited (0) About a minute ago                       wonderful_elion
```

and remove it by running:

```
docker rm [CONTAINER ID]
```

Then list all your images to get the image ID 

```
[krzys@starship Medbox-server]$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              bf756fb1ae65        3 months ago        13.3kB
```

and then remove the image by running:

```
docker rmi [IMAGE ID]
```

### Building base images
Once docker is running you will need to build the base images used in this projects.
If you are running on macOS or linux then your are lucky. Just execute the provided shell script.

```
./build-base.sh
```

It will perform the build automatically. 

If you are using windows you will need to execute the following commands manually:

```
docker build Base/django-base/ --tag django-base
docker build Base/falcon-base/ --tag falcon-base
```

Not much more complicated but this most likely will change in the future.

You will also need to execute those commands any time you change anything in /Base directory.
So base images can be rebuilt.

Once you are done with this step you should have the following images on your system:

```
[krzys@starship Medbox-server]$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
falcon-base         latest              1e92397b1227        38 seconds ago       954MB
django-base         latest              4cca58b89179        About a minute ago   976MB
python              3.8-buster          a6be143418fc        3 days ago           933MB
```

## Workflow

Ok so now about how to make changes and test them.

### Building images

In order to rebuild the base images please refer to *Building base images*.

If you want to build everyting else then run the following command:

```
[krzys@starship Medbox-server]$ docker-compose build
```

It will build the following images:

 - device-api
 - app-api
 - web

Note: You need to build base images before executing this command.

### Running the services

In order to run all services, execute:

```
[krzys@starship Medbox-server]$ docker-compose up
```

After this yoy should have the followinf containers running:

```
[krzys@starship Medbox-server]$ docker ps --all
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                  PORTS                    NAMES
09d4f286804f        web                 "python manage.py ru…"   1 second ago        Up Less than a second   0.0.0.0:8000->8000/tcp   webapp-server
16b0e0d899b2        app-api             "gunicorn -b 0.0.0.0…"   1 second ago        Up Less than a second   0.0.0.0:8002->8001/tcp   app-api-server
a5a929c8b956        device-api          "gunicorn -b 0.0.0.0…"   1 second ago        Up Less than a second   0.0.0.0:8001->8001/tcp   device-api-server
85598781cf49        postgres            "docker-entrypoint.s…"   2 seconds ago       Up 1 second             5432/tcp                 app-db
13f2e6659277        postgres            "docker-entrypoint.s…"   2 seconds ago       Up 1 second             5432/tcp                 users-db
a2ed36f53b8d        postgres            "docker-entrypoint.s…"   2 seconds ago       Up 1 second             5432/tcp                 treatments-db


```

If you want to exit run:

```
[krzys@starship Medbox-server]$ docker-compose down
```

You have to run this in a separate console window but still inside the project directory. This command will kill all containers
and remove them.

### Applying your changes

Generally in order to apply your changes you should use the following workflow:

```
docker-compose down

# make modifications

docker-compose build
docker-compose up

# test modifications
```

Databases are stored inside the volumens so the tables are preserved. However all edits made to the files inside the containers
will be lost after you execute docker-compose down so all source code should be stored in the project directory.


### Opening shell
If there is a need to manually run some scripts inside the container (for example manage.py for django) you can do that by opening
a terminal in the container. In order to do that first make sure that container is running (by running `docker-compose up`), then check the container
ID using `docker ps` command and finally run the following command:

```
docker exec -ti [CONTAINER ID] bash
```

For example:

```
[krzys@starship Medbox-server]$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                  PORTS                    NAMES
09d4f286804f        web                 "python manage.py ru…"   1 second ago        Up Less than a second   0.0.0.0:8000->8000/tcp   webapp-server
16b0e0d899b2        app-api             "gunicorn -b 0.0.0.0…"   1 second ago        Up Less than a second   0.0.0.0:8002->8001/tcp   app-api-server
a5a929c8b956        device-api          "gunicorn -b 0.0.0.0…"   1 second ago        Up Less than a second   0.0.0.0:8001->8001/tcp   device-api-server
85598781cf49        postgres            "docker-entrypoint.s…"   2 seconds ago       Up 1 second             5432/tcp                 app-db
13f2e6659277        postgres            "docker-entrypoint.s…"   2 seconds ago       Up 1 second             5432/tcp                 users-db
a2ed36f53b8d        postgres            "docker-entrypoint.s…"   2 seconds ago       Up 1 second             5432/tcp                 treatments-db


[krzys@starship Medbox-server]$ docker exec -ti b4b79d327e36 bash
root@b4b79d327e36:/usr/src/app# ls
Dockerfile  MedboxWeb  db.sqlite3  manage.py

root@b4b79d327e36:/usr/src/app# 
```

Type `exit` when you are done.

But please remember that any changes stored inside the container are lost.

### Accessing database

If you want you can access the database by running the SQL console.
In order to open it you neeed to first make sure that the container is running and then run:

```
docker exec -ti [DB CONTAINER ID ] psql -U [DATABASE USER]
```

Then you get access to the Postgres shell.

Here is a quick tutorial on how to use this: https://tomcam.github.io/postgres/

Once you are done type \q to exit the shell.

### Acessing the website
In order to access all the services that are running inside the containers you just need to start everything with  `docker-compose up`
and then you can access all services at localhost.

Here is where all the stuff will be available:

 - Django app: localhost:8000
 - Device API: localhost:8001
 - App API: localhost:8002
 
Website can be accessed directly from the web browser. 

API's can be accessed using for example Postman software. (https://www.postman.com/).


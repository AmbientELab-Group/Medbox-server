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

### Initializind database
Once docker is running you will need to perform the first build.
First you need to build all imagess, just execute (you may need to run 
`chmod -R 777 .` 
before to give proper permissions):

```
sudo docker-compose build
```

You can skip this step if images are already built (if you erased your database and
yout want to rebuild everything.

Them you need to initialise database, otherwise django will fail.
In order to do that you have to run:

```
sudo docker-compose up mainDB
```

Then once the database is up and running, press CTRL+C to exit and then run

```
sudo docker-compose down
```

Next step is to perform migrations and setup your admin account.

In oder to do that first bring the system up:

```
sudo docker-compose up
```

You should get the following output from the server:

```
webapp-server | Watching for file changes with StatReloader
webapp-server | Performing system checks...
webapp-server | 
webapp-server | System check identified no issues (0 silenced).
webapp-server | 
webapp-server | You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): Website, admin, auth, contenttypes, sessions.
webapp-server | Run 'python manage.py migrate' to apply them.
webapp-server | May 13, 2020 - 15:57:07
webapp-server | Django version 2.2.12, using settings 'MedboxWeb.settings'
webapp-server | Starting development server at http://0.0.0.0:8000/
webapp-server | Quit the server with CONTROL-C.
```

If you get any error something is wrong. Contact the chief project wizard (@Bill2462).

Then open the another console and see if containers are running. You should see something like that:

```
[krzys@starship Medbox-server]$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
4354a1d70d78        webserver           "python manage.py ru…"   4 minutes ago       Up 4 minutes        0.0.0.0:8000->8000/tcp   webapp-server
c7d618bcd1fa        postgres            "docker-entrypoint.s…"   4 minutes ago       Up 4 minutes        5432/tcp                 medbox-server_mainDB_1
```

If you have those two containers then everything is ok and you can apply the migrations.

In order to do that open a shell to webserver container:

```
[krzys@starship Medbox-server]$ docker exec -ti [CONTAINER ID]  bash
user@4354a1d70d78:/usr/src/app$ 
```

Then apply migrations by running the following command:

```
user@4354a1d70d78:/usr/src/app$ python3 manage.py migrate
```

Then create a superuser by running:

```
user@4354a1d70d78:/usr/src/app$ python3 manage.py createsuperuser
```

Email and password are up to you (they don't have to be real.

And that's it. Now you can go to localhost:8000/admin and use entered credentials to access the admin panel.

## Workflow

Ok so now about how to make changes and test them.

### Running the services

In order to run all services, execute:

```
[krzys@starship Medbox-server]$ docker-compose up
```

After this yoy should have the followinf containers running:

```
[krzys@starship Medbox-server]$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
4354a1d70d78        webserver           "python manage.py ru…"   10 minutes ago      Up 10 minutes       0.0.0.0:8000->8000/tcp   webapp-server
c7d618bcd1fa        postgres            "docker-entrypoint.s…"   10 minutes ago      Up 10 minutes       5432/tcp                 medbox-server_mainDB_1
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
and then you can access all services at localhost:8000.d
 
Website can be accessed directly from the web browser. 

API's can be accessed using for example Postman software. (https://www.postman.com/).


# Medbox Server Side Software

This a main repository for Medbox project server side infrastructure codebase.

## How do I start working with this?!!

Your are probably asking yourself this question right now.
So here is a quick guide on how to get your environment up and running.

## Install required tools.

The following tools are required to run this project.

 - docker (https://docs.docker.com/get-docker/)
 - docker-compose (https://docs.docker.com/compose/install/)
 - git (https://git-scm.com)
 
If you are running Linux you can easily install all above packages through your distribution's package manager.

If you are running macOS follow the instructions provide on the website of each one of above packages.

If you are using Windows then god help you. Try to follow the instructions provided by docker, they might work.

You might also want to install postman which is an excelent tool for developing and testing API's (https://www.postman.com/downloads/).


IMPORTANT NOTE: On linux sometimes you have to manually enable docker daemon:

```
systemctl enable docker
```

If you fail to do this docker will stop working after reboot.

## Docker without root

By default you cannot run docker as any user other than root. This is because usually, on a production server you do not want
unprivileged users messing with your docker containers.

However, this is really annoying inside a development environment. You will have to run all docker related commands
using sudo and enter your password every couple of minutes. This gets annoying very quickly, trust me.
The other option is to open a root shell. This is also a bad idea.
For example you might leave your computer unattended for 5 minutes and your evil young brother can install a script that
will randomly play *insert your most hated music here* without any apparent reason and you won't even know what is happening.
Then, after countless hours spent on trying to find out what is happening, you will finally give up and erase your drive by throwing your machine into an active
volcano hoping that this will destroy all evil spirits inside.

To avoid loosing your sanity you can add your user to docker admin group which will allow you to manage containers
through a normal shell.

Here is how to do this on 

Linux:

```
sudo groupadd docker
systemctl restart docker
sudo gpasswd -a username docker
```

Replace `username` with your username. You will have to logout and login for changes to take effect.

macOS: It probably works out of the box.

Windows: Who knows? It's windows, docker probably works out of the box if you manage to install it.

## Testing docker

Once you are done with installation please make sure that docker is working by running:

```
docker run hello-world
```

This command should download a hello world example and run it.
If it does not work please make sure that virtualization is enabled in your BIOS.
If it still does not work please consult your search engine of choice or ask other project members.

## First build

Once you have your tools set up you are ready to clone and build the project.

### Adding SSH key to your account.

Unfortunately, github is dropping support for login & password authentication through git so you have to start by setting up an SSH key.

Here is how to do this on Linux (simple way):

1. Go to `.ssh` directory in your home folder (yes there is a point before ssh).
2. Generate keypair by running : `ssh-keygen -C "your_email@example.com"`. Replace `your_email@example.com` with your email used
on github. The ssh-keygen will ask you where to put your key and how to name it. By default it is named `id_rsa` and is put inside `.ssh` in
your home directory. This is fine unless your are planning to use multiple keys for different services. If you are fine with the default arrangement then
press enter without typing anything. Then you will be asked to enter a passphrase for the key. It provides
additional security but you will have to enter the chosen password everytime you use the key. If you do not want any passphrase press enter without typing anything.
3. Open `id_rsa.pub` in a text editor.
4. Go to your account settings on github and open tab called `ssh and GPG keys`. Then press button with `add new ssh key` on it.
5. Enter any name you want and put contents of `id_rsa.pub` file inside `key` field. NEVER DO THAT WITH YOUR PRIVATE KEY (id_rsa). KEEP YOUR PRIVATE KEY SECRET AT ALL TIMES.

After your key is added, you can test your connection by running:

```
ssh -T git@github.com
```

You may get a warning like this:

```
> The authenticity of host 'github.com (IP ADDRESS)' can't be established.
> RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
> Are you sure you want to continue connecting (yes/no)?
```

In this case type yes and proceed.

You should get something like this as a response

```
> Hi username! You've successfully authenticated, but GitHub does not
> provide shell access.
```

That means that your key was added succesfully.

### Cloning repository and adding origin

Now you are clear to clone the repository.

To do that please first open terminal in a directory that you want to put it in and then run:

```
git clone git@github.com:Bill2462/Medbox-server.git
```

Once this is done you will have a copy of the entire project history tree on your machine.

Now you need to add a remote server so you will be able to publish your changes.

Main server is usually named `origin`.

To add it please run

```
git remote add origin git@github.com:Bill2462/Medbox-server.git
```

Once this is done please verify that remote was added correctly by running:

```
git remote -v
```

You should see something like this:

```
origin  git@github.com:Bill2462/Medbox-server.git (fetch)
origin  git@github.com:Bill2462/Medbox-server.git (push)
```

### Build all images

Now you are ready to build docker images. First checkout at main development branch by running:

```
git checkout dev
```

and then run the build:

```
docker-compose build
```

This might take a while depending on your internet connection.

After build is finished list all images:

```
docker images
```

The output list should have those two images on it:
 
 - medbox-frontend_server
 - medbox-backend_server

If you have those images then your build was succesfull.

### Database initialization

Unfortunately you need to initialize the database separately, otherwise django will fail.

To do that run:

```
docker-compose up medbox-database_server
```

Wait until you get a message that look's something like this:

```
020-11-04 10:21:12.077 UTC [47] LOG:  database system is ready to accept connections
```

and then shutdown the server by pressing ctrl+c and then run:

```
docker-compose down
```

### Applying first migrations and creating admin account

Next step is performing migrations and creating new superuser account.
You will use that account to access the admin panel.

To do that first bring the backend and database service up by running:

```
docker-compose up medbox-backend_server
```

You should get the following output from the server:

```
medbox-backend_server     | Watching for file changes with StatReloader
medbox-backend_server     | Performing system checks...
medbox-backend_server     | 
medbox-backend_server     | System check identified no issues (0 silenced).
medbox-backend_server     | 
medbox-backend_server     | You have 28 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): AdminPanel, AppAPI, DeviceAPI, admin, auth, contenttypes, sessions.
medbox-backend_server     | Run 'python manage.py migrate' to apply them.
medbox-backend_server     | November 04, 2020 - 10:23:10
medbox-backend_server     | Django version 3.0, using settings 'MedboxWeb.settings'
medbox-backend_server     | Starting development server at http://0.0.0.0:8000/
medbox-backend_server     | Quit the server with CONTROL-C.
```

Then you have to list all running containers using:

```
docker ps
```

Copy the ID of the backend server container and then open bash shell inside it by running:

```
docker exec -ti [CONTAINER ID]  bash
```

After this you should see a command prompt like this:

```
user@4354a1d70d78:/usr/src/app$ 
```

Then apply migrations by running the following command:

```
user@4354a1d70d78:/usr/src/app$ python3 manage.py migrate
```

Now you can create your admin account by running:

```
user@4354a1d70d78:/usr/src/app$ python3 manage.py createsuperuser
```

You will be asked to provide email and password. Email does not have to be real. Please write down your email and password
as you will need them to access the admin page.

To exit the shell type exit and press enter.

## Docker cheatsheet

To start selected services run:

```
docker-compose up [service names listed here]
```

You need to run this in a directory that has docker-compose.yml file inside.


To kill specific services and remove their containers please run:

```
docker-compose down [service names listed here]
```

To kill all services and dissolve their bodies in acid run:

```
docker-compose down
```

To build an image for a specific service please run:

```
docker-compose build [service_name]
```

If you want to remove some specific images you need to run:

```
docker rmi [image_id]
```

If you want to remove a container that is not running please run:

```
docker rm [container_id]
```

If you want to kill a container please run:

```
docker kill [container_id]
```

If you want to list all contaners please run:

```
docker ps --all
```

Sometimes docker creates some dangling images during the build process.
They are not needed, you can save some storage space by removing them using command:

```
docker image prune
```

If you want to access database SQL console please run:

```
docker exec -ti [DB CONTAINER ID ] psql -U [DATABASE USER]
```

You can find username and password in the environmental variables file inside the backend folder.

Here is a quick tutorial on how to use postgres shell: https://tomcam.github.io/postgres/

#### TIP
This is a command you will use most often working with backend:
```
docker-compose up medbox-backend_server medbox-database_server
```
it correctly spins up DB and backend containers.

## Workflow

If you want to start working on something, create a feature branch from dev

```
git checkout dev
git branch your-branch-name
git checkout your-branch-name
```

Next publish your branch to the server:

```
git push origin your-branch-name
```

Now make changes in the code and commit them to your branch. Remember to make commits regularly,
write descriptive commit messages and push your commits to the server often. This will help other people in keeping track
of your work.

To publish your changes you run:

```
git push origin your-branch-name
```

Once you are done please create a pull request to branch dev and request a review.

Once code is ok, pull request will be merged to dev.

Do not commit directly to master and try to not commit directly to dev.

DO NOT EVER RUN PUSH WITH --force FLAG. THIS WILL REWRITE HISTORY AND CAUSE PROBLEMS FOR OTHER DEVELOPERS.

If you want to propose a change please talk to the team on the chat and then open an issue describing the change.

If you have any questions please ask on chat.


## Style guide

- Use flake8 linter.
- Use correct naming convention. CamelCase for classes - snake_case for everything else.
- Do not use single quotes - "correct" > 'not so much'
- Take a look at how existing code is commented and try to follow this practice. Generally try to make use of python doc strings and be explicit about what a given function is trying to achieve. That should be enough in most cases but feel free to add some line comments if you feel like your code is a bit hacky-wacky today

## Database

Normally all you have to do to keep your DB fresh and happy, is to apply migrations after any changes in python models (not necessarily done by you, e.g. sb done some changes in a different commit and since DB is not synced with git you have to sync DB structure manually).

In order to do this you can TRY executing the migrations that came with the commit (make sure backend and DB containers are up):
```
docker exec -it medbox-backend_server bash
./manage.py migrate
```
and this MAY work (with Django you never know).

In case it didn't, go ahead and do the full reset using the scripts kindly provided by your colleagues:
```
cd /backend
./resetDB.sh                                                <- before running this only DB container should be up
docker exec -it medbox-backend_server bash < migrate.sh     <- before running this both server and DB should be up
```
Finish the process with creating new superuser:
```
docker exec -it medbox-backend_server bash
./manage.py createsuperuser
```

#### Warning
*This procedure will wipe out the whole content of your DB. If you want to persist sth copy it rather before than after.*
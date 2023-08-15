## Dockerizing

Dockerizing is the process of packing, deploying, and running applications using Docker containers.

`Docker` is an open source tool that ships your application with all the necessary functionalities as one package.

You can use Docker to pack your application with everything you need to run the application (such as libraries) and ship it as one package - a container. Containers are created from images that specify their precise contents. 

Dockerizing is a big hit nowadays. All the big names use it - Google, VMware, or Amazon support it.

There are two parts of Docker:

The `Docker Engine` - a portable packaging tool

The `Docker Hub` - cloud service for sharing applications

### Install Docker Desktop on Windows

#### Install interactively
. Double-click Docker Dektop Installer.exe to run the installer.

. when prompted, ensure the use WSL2 instead of Hyper-V option on the Configuration page is selected or not depending on your choice of backend.
If your system only supports one of the two options, you will not be able to select which backend to use.

. Follow the instructions on the installation wizard to authorize the installer and proceed with the install.

. When the installation is successful, select Close to complete the installation process.

#### Install from the command line
  
  After downloading Docker Desktop Installer.exe, run the following command in a terminal to install Docker Desktop:

``` bash
"Docker Desktop Installer.exe" install
```

If you’re using PowerShell you should run it as:

``` powershell
Start-Process 'Docker Desktop Installer.exe' -Wait install
```
If using the Windows Command Prompt:

``` prompt
start /w "" "Docker Desktop Installer.exe" install
```

### Setting up and Dockerizing Django app

#### Step 1

To install the package, you use project on the docker conatine, you should freeze you pip package. Created a file
named requirements.txt and place it in the top level directory of your source bundle.

``` shell
pip freeze -l > requirements.txt

```

In the project directory, create a file named “docker-compose.yml” and another file called “Dockerfile”
docker can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text
document that contains all commands a user could call on the command line to assemble an image. Using docker
build.

Dockers need a base image, like `Python` or Ubuntu, or Centos, as the first line of the file. If you choose Python, it is easier,
but you can choose Ubuntu if you want more flexibility. The best choice would be to use the Python base image and the Python 3.10 images.
Next is ENV PYTHONUNBUFFERED 1, which means Python output is logged to the terminal, allowing Django logs to be monitored in real-time. Next, we should write create a working directory. In the next step, we should select WORKDIR /code;

In the next step, we should expose Django Port for with EXPOSE 8000 following configures your Django application on the port you want based on this example we run my app on 8000 port. with CMD docker command like this :  (CMD run your command on the last step )

``` docker

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]

```

Now run the following command in terminal to build your image and exect you container

``` bash

docker compose up --build

```

Now we can deploy our app on cloud azure et aws; we can upload and clone code on these platforms


## Deployment of app on cloud

### Secure senstive data - best practice Django

Before deploying we should protect sensitive variables in Settigns.py, Hide secret key and database Configuration, Password management and protect private
confidential presonal data in Django.
First we start by installing python decouple, we create dot env file in same folder and take all sensitive variables and past on .env file

### Depoyment

You should choose the docker-compose version; we chose version 3, and in the next step, specify the number of services you’d like. We just write MySQL database and Django application and Nginx configuration on this file, You can set any other service you want.
For the Django web app, we write configuration on the web part of this file one thing you see on the web part is the build stage that’s A sign of building a dockerfile context main show your working directory path, and on the following line, you write your dockerfile path. The Dockerfile section explained how to write Dockerfiles for Django applications.

Because you use docker and container concept, none of your container ports you can see on your machine Except you expose or map your container port manually. For this reason, we map the 8000 container port to the 8000 machine port by this part of configuring file

``` YAML
ports:
  - 8000:8000 
```




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




# Deployment of app on cloud

### Secure senstive data - best practice Django

Before deploying we should protect sensitive variables in Settigns.py, Hide secret key and database Configuration, Password management and protect private
confidential presonal data in Django.
First we start by installing python $\color{green}{decouple}$ , we create dot env file in same folder and take all sensitive variables and past on .env file

### Installing Docker on ubutntu

The docker installation package available in the official ubutnu repository may not be the latest version. To ensure we get the latest version, we'll install
Docker from the official Docker repository. To do that, we'll add a new package source, add the GPG key from Docker to ensure the downloads are valid, and then install the package.

First, update your existing list of package:

``` bash
sudo apt update
```

next, install a few prerequisite packages which let `apt` use packages over HTTPS:

``` bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

Then add the $\color{orange}{GPG / key}$ for the official `Docker` repository to your system:

``` bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
What's the GPG key : A GPG key, also known as a GnuPG key or OpenPGP key, is a cryptographic key used for secure communication and data integrity. GPG stands for "GNU Privacy Guard," and it is an open-source implementation of the OpenPGP standard, which provides a framework for encrypting and signing data.



Add the `Docker` repository to `APT` sources:

``` bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```

This will also update our package database with the Docker packages from the newly added repo.

Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:

``` bash
apt-cache policy docker-ce
```

You’ll see output like output image under capture, although the version number for Docker may be different



Finally, install `Docker`:

``` bash
sudo apt install docker-ce
```

Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it’s running:

``` bash
sudo systemctl status docker
```
Or start the `Docker` by this command:

``` bash
sudo systemctl start docker
```




### Deployment

You should choose the docker-compose version; we chose version 3, and in the next step, specify the number of services you’d like. We just write MySQL database and Django application and Nginx configuration on this file, You can set any other service you want.
For the Django web app, we write configuration on the web part of this file one thing you see on the web part is the build stage that’s A sign of building a dockerfile context main show your working directory path, and on the following line, you write your dockerfile path. The Dockerfile section explained how to write Dockerfiles for Django applications.

Because you use docker and container concept, none of your container ports you can see on your machine Except you expose or map your container port manually. For this reason, we map the 8000 container port to the 8000 machine port by this part of configuring file

``` YAML
ports:
  - 8000:8000 
```

The .env file that we configured in the first step is giving the Django application to docker. As a result, we wrote this section of the config file and specified where the .env file could be found.

``` YAML
env_file: .env
```

Clone the application from Github

``` bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```


How to fix docker: Got permission denied issue

``` bash
sudo groupadd docker
```

Add your user to the docker group.

``` bash
sudo usermod -aG docker $USER
```

Log in to the new docker group (to avoid having to log out / log in again; but if not enough, try to reboot):

``` bash
newgrp docker
```

Check if docker can be run without root

``` bash
docker run hello-world
```

Reboot if still got error

``` bash
reboot
```


#### ERROR Invalid HTTP HOST HEADER : Disallowed Host at Invalid HTTP_HOST

The error log is straightforward. You need to add your adresse to your ALLOWED_HOSTS setting
In you project settings.py file, set ALLOWED_HOSTS like this : 

``` python
ALLOWED_HOSTS = ['198.211.19.20', 'localhost', '127.0.0.1']
```


## Configure load balancing using Ngnix

Advantages of load balancing : 

Load balancing is an excellent way to scale out your application and increase its performance and redundancy. Nginx, a popular web server software, can be configured as a simple yet powerful load balancer to improve your server’s resource availability and efficiency.

How does Nginx work? Nginx acts as a single entry point to a distributed web application working on multiple separate servers.
As a prerequisite, we need to have at least two container with web server software installed and configured to see the benefit of the load balancer.

#### Installing nginx







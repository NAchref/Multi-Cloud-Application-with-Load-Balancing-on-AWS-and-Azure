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
1. Double-click Docker Dektop Installer.exe to run the installer.
2. when prompted, ensure the use WSL2 instead of Hyper-V option on the Configuration page is selected or not depending on your choice of backend.
If your system only supports one of the two options, you will not be able to select which backend to use.
3. Follow the instructions on the installation wizard to authorize the installer and proceed with the install.
4. When the installation is successful, select Close to complete the installation process.

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


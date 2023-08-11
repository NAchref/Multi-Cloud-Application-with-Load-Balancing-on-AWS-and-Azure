## Dockerizing

Dockerizing is the process of packing, deploying, and running applications using Docker containers.

`Docker` is an open source tool that ships your application with all the necessary functionalities as one package.

You can use Docker to pack your application with everything you need to run the application (such as libraries) and ship it as one package - a container. Containers are created from images that specify their precise contents. 

Dockerizing is a big hit nowadays. All the big names use it - Google, VMware, or Amazon support it.

* There are two parts of Docker:

The `Docker Engine` - a portable packaging tool

The `Docker Hub` - cloud service for sharing applications

### Install Docker Desktop on Windows

* Install interactively
1. Double-click Docker Dektop Installer.exe to run the installer.
2. when prompted, ensure the use WSL2 instead of Hyper-V option on the Configuration page is selected or not depending on your choice of backend.
If your system only supports one of the two options, you will not be able to select which backend to use.
3. Follow the instructions on the installation wizard to authorize the installer and proceed with the install.
4. When the installation is successful, select Close to complete the installation process.

* Install from the command line
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


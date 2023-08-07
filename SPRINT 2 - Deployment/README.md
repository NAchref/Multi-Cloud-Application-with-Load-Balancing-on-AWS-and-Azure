# Sprint 2 - Deplyment of application on AWS & Azure 

* Deploy the application on `EC2` web server and connect to RDS service of databasing on Amazon 
* Deploy the application on `AZM` web server and connect to SQL azure service on Microsoft Azur 


## AWS Deployement 

### Create EC2 instance & configuration : 

To create an `EC2 instance` on AWS, several essential steps need to be followed to ensure a successful setup. 
The procss involes using the AWS management Console. Firstly, i log in to the AWS Management Console with my credentials. Then, navigate to the EC2
Dashbord and select the `Lanch instance` (Lancer instance) option. Next, I choose the desired Amazon Machine Image (AMI) in my case i choose Ubnunto
and i configure to create a Security Group and also checked to allow SSH traffic from. Finally check all your configuration and press Launch instance. So i get a pop up to create `key pair` or not or to processed without key pair ( key pair allows you to connect to your instance securely), For me i choose to move for processed without key pair.

### Setup :

* Update the System

``` bash
sudo apt-get update

```

   
* To get this repository, run the following command inside your git enabled terminal

 ``` bash
git clone https://github.com/yeshwanthlm/django-on-ec2.git

```  

* You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

* Download django usig pip


 ``` bash
sudo apt install python3-pip -y
```
 ``` bash
pip install django
```


### Step II

#### AWS

Create a `RDS instance` represented Mysql and configure with security group with inbounded accept all traffic on `IPv4`, Then downlod `MySQLWorkbench` and connected to it.
After check the connection between the RDS instance and MysqlWorkBench add a database with command `CREATE DATABASE 'Database name'` this database will point our app to it , I update settigns.py to connect Django app inside my Ec2 instance to my RDS database instance.
To connect Ec2 instance Django app run the following command inside terminal : 

install another library to use the MySQL database

``` bash
pip install mysqlclient
```
Open settings.py here inside the DATABASES variable configure MySQL database values, and add values of your database.

``` pyhton

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```

First, i have replaced the ‘django.db.backends.sqlite3’ to ‘django.db.backends.mysql’. This is basically indicating i shift SQLite to `MySQL` database.

NAME: It indicates the name of the database we want to connect.
USER: The MYSQL username is the one who has access to the database and manages it.
PASSWORD: It is the password of the database. 
HOST: It is indicated by the endPoint of database inside RDS instance and “PORT” “3306” that the MySQL database is accessible at hostname “0.0.1” and on port “3306.”


Then `Run the server`

Run the migration command

``` python
python manage.py makemigrations

```

Finally

``` python
python manage.py runserver 0.0.0.0:8000

```


### AZURE


* Launch Azure Cloud Shell
   The Azure Cloud Shell is a interactive shell that you can use to run the steps and commands. It has common Azure tools preinstalled and configured to use    with your account.
   To open the Cloud Shell, just select Try it from the upper right corner of a code block.

* Create a resource group
  Create a resource group with the az group create command.

 ``` shell

resourcegroup="myResourceGroupCLI"
location="CanadaEast"
az group create --name $resourcegroup --location $location

```

* Create virtual machine
  Create a VM with az vm create. The following example creates a VM named myVM.

 ``` shell
   vmname="myVM"
   username="azureuser"
   az vm create \
    --resource-group $resourcegroup \
    --name $vmname \
    --image Win2022AzureEditionCore \
    --public-ip-sku Standard \
    --admin-username $username
   
  ````

















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







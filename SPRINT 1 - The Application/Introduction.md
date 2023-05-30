# Introduce the web application 

The choice of the web application to create on cloud Azure and AWS would depend on several factors such as your skills, experience, and the purpose of the application you want to create. However, We decied to create E-commerce web application.

## E-commerce web application: 

If you want to create an e-commerce web application, you could consider using a platform like Magento, Shopify or WooCommerce, and deploy it on a cloud service. These platforms have built-in support for e-commerce features like shopping carts, payment gateways, and inventory management.

## Django

I have chosen to develop my e-commerce website using Django because of its powerful and flexible framework that enables rapid development and scalability. Django follows the Model-View-Controller (MVC) architectural pattern and is based on the Don't Repeat Yourself (DRY) principle. This allows for efficient development of web applications, as code is written once and reused wherever possible. Django's built-in features such as an Object-Relational Mapping (ORM), a templating engine, and an authentication system, along with a large library of third-party packages, make it an ideal choice for building complex web applications such as e-commerce platforms.

One of the key benefits of using Django for an e-commerce website is its ability to handle large amounts of data and transactions. Django's ORM layer provides an easy way to interact with a database and manage data related to products, orders, customers, and more. Additionally, Django provides tools for handling user input securely, which is essential for online transactions.

Finally, I plan to host my website on a cloud platform, which will provide scalability, reliability, and cost-effectiveness. Cloud platforms offer the ability to easily scale resources up or down based on traffic demand, ensuring that my website can handle a large number of users without any performance issues. Cloud platforms also offer high availability and reliability by replicating data across multiple servers and data centers, ensuring that my website is always available and performing well. Additionally, cloud platforms provide several security features such as firewalls, identity and access management, and encryption, which can help protect my website and user data from cyber attacks. Overall, using Django and hosting on a cloud platform provides the necessary features and benefits to build and run a successful e-commerce website.


##  Steps With Django: Set Up a Django Project

* Prepare Your Environment.
* Install Django and Pin Your Dependencies.
* Set Up a Django Project.
* Start a Django App.

Now that we have Django installed, let's create our project. CD into where you want your project files, mine will be in the desktop. We will use django-admin startproject “project name”.

## Once you create your project be sure to CD into it before the next step.

-- django-admin startproject Carscommerce

## Create app


### Create the first app files with python manage.py startapp “appname".

-- python manage.py startapp store



### Prepare Environment

* Install Package. First, install python 3 the latest version(download python 3.11), the version of django that combine with python 3.11 is the version 4.2
* From the command line,  into a directory where you’d like to store your code, then run the following command: 
* $ django-admin startproject CarsEcommerce

## Add app to settings.py

When you open up your project you should see the app we just created in your project folder. Make sure you add the new app to INSTALLED_APPS within settings.py

In your command promt run "python manage.py runnserver" and open up port 127.0.0.1:8000.


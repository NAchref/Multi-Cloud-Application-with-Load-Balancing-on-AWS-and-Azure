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

``` django
django-admin startproject Carscommerce

```

## Create app


### Create the first app files with python manage.py startapp “appname".


``` pyhton
python manage.py startapp store

```



### Prepare Environment

* Install Package. First, install python 3 the latest version(download python 3.11), the version of django that combine with python 3.11 is the version 4.2
* From the command line,  into a directory where you’d like to store your code, then run the following command:

 ``` django  
  django-admin startproject CarsEcommerce

```

## Add app to settings.py

When you open up your project you should see the app we just created in your project folder. Make sure you add the new app to INSTALLED_APPS within settings.py

In your command promt run "python manage.py runnserver" and open up port 127.0.0.1:8000.





## Create Templates Folder

. Inside the new app (store) create a folder called "Templates", inside the templates folder create another folder with the same name as the app.
. Inside the folder we called "store" (Inside the templates folder) is where we will store our html files. 

Right now, let's create all the templates we will need along with one main template that all the other templates will inherit from.

* Main.html → Template which all will inherit from
* Store.html → Home page/store front with all products
* Cart.html → Users shopping cart
* Checkout.html → Checkout page  



## Create Views

Inside your apps views.py file create 3 views. Right now we just want to render the templates we created.

/// File: store/views.py

#### URLS

Create a file called "urls.py" inside your app.

Inside the app import “path” along with the “views” and create a urlpatterns list. Inside "urlpatterns " create 3 paths, one for each view and give them a name.

/// File: store/urls.py

#### Base URLs Configuration

To connect our new urls we need to open up the urls.py file in the root directory and "include" it. 

First import "inlcude" just after "path" and add a path that points to the new urls.py we created inside "store".

/// File: CarsEcommerce/urls.py

###  Static Files

In your root directory create a folder called "static".

Inside the new “static” folder, let's create a folder called "CSS" and another called "Images". These files will hold all of our CSS and Images.

### CSS File

Inside the CSS folder, let's create a file call main.css. This file will later be the main source of styling for each page along with the bootstrap CDN. 

Inside "main.css",

### STATICFILES_DIRES

Now in order to see this effect, let's configure things in settings.py and then add this link to our template.

In "settings.py", we should already have "STATIC_URL". Now we will just need to add "STATICFILES_DIRS" and point it to the new static folder we created in our base directory.

## Add Static Files to Page








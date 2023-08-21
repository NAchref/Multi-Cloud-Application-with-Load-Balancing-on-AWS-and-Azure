# Graduation-project
## Multi-Cloud-Application-with-Load-Balancing-on-AWS-and-Azure

The purpose of this graduation project is to develop and deploy a multi-cloud application on both AWS and Azure platforms, and to implement a load balancing mechanism between the two platforms to optimize the application's performance and availability.

Our project is a `cloud application` framework that provides `intra-` and `inter-cloud` resilience to reduce vendor disruptions. Much research has been done on intra-loud resilience, which allows applications to move from one server to another. However, intra-loud reliability platforms are not as common.

## Architecture

![alt text](https://github.com/NAchref/Multi-Cloud-Application-with-Load-Balancing-on-AWS-and-Azure/blob/main/PLAN%20%26%20ARCHITECTURE/Architecture.jpg)

## Vision and Goals Of The Project: 

My project is a framework for cloud applications to mitigate provider outages by providing resiliency at both the both $\color{orange}{intra-}$ and $\color{orange}{inter-}$ cloud levels, making it possible for pieces of applications to migrate from one server to another. Intra-cloud reliability platforms, however, are not nearly as common. We have included this in order to protect applications from several issues ranging from cyber attacks to hardware failures. If parts of AWS or AZURE go down, for example, the application itself should be alive and kicking, as resources will be directed to the provider that is still up.

We will implemented `load balancing` at both the $\color{orange}{intra-}$ and $\color{orange}{inter-}$ cloud levels so that all requests are serviced, as well as duplicated data throughout different cloud providers in order to ensure that application users always have access to their current data. We will tested our framework with our own application by running it on multiple cloud providers and testing its reliability when different cloud instances are turned off.


## Release Planning:

### Sprint 1:

Create a sample e-commerce application with `django` that have a simple CRUD Locally

### Sprint 2:
 
Get a basic web server running on Azure that can connect to `AzureSQL`
Get a basic web server running on AWS that can connect to `RDS`
Ensure the web app can serve static content
Ensure the web app can serve dynamic content and have will CRUD functionality as described

### Sprint 3:

`Containerized` applications Django using Docker and upload it to Ec2 instance and connected to RDS DataBase.
In same time upload container to Azure Vm and connected to Mysql Azure database.

### Sprint 4 

Start creating a `load balancing` service between container on same instance using the Amazon `Elastic Load Balancing (ELB)`, And on the same mission using `Azure Load Balancer` on azure 
virtual machine 




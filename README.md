# Overview
This project is a walkthrough that guides users to creating a simple django application (a reverse geocoder in this case) and how to deploy it on AWS. This README contains:
* Architectural design
* Getting started
* CloudFormation guide
* Reference
* Consulting

The project utilizes the following tools

## 1. Architectural designs
TODO

### *General Architecture*
TODO
### *AWS architecture*
#### AWS Workload components
* Route53: An A record routing traffic to the ALB will be used to access the application.
* Application Load Balancer (ALB): The load balancer forwarding traffic to the application server.
* EC2: Compute instance hosting the django application and an Nginx web server.
* RDS: A PostgreSQL database extended with POSTGIS to enable spatial data management.

![AWS workload design](img/aws-gecoder.png)

## 2. Getting Started
#### Database setup
Start by creating a normal RDS (PostgreSQL) database and extend it with a POSTGIS extension using the following commands
```code
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
``` 

Finally, ensure to transfer ownership of the objects to the rds superuser role.

### Django application setup

## 3. Supporting Material/Guide
TODO
## 4. CloudFormation guide
TODO
## 5. References
TODO
## 6. Consulting
TODO
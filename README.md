# Microservices
This project consists of two microservices run in docker containers: an admin service written in Django, and a main app service written in Flask. The admin service allows you to view and manage your products and their likes. The main app service allows customers to view and like your products.

## Requirements
- Python 3.10
- Django 4.0+
- Flask 2.0+
- RabbitMQ Account
- An AMQP URL (you can get this by creating an account and a project with RabbitMQ)

## Getting Started
Clone the repository:
```sh
git clone https://github.com/AlonsoBear/Microservices.git
```

Create inside both services ```admin``` and ```app``` a ```.env``` file.
Set the AMQP_URL environment variable with your RabbitMQ AMQP URL:
```sh
AMQP_URL=<your-amqp-url>
```

Once you have both ```.env``` files and have Docker Desktop running, run
inside both ```admin``` and ```app``` services the following command:
```sh
docker-compose up
```

When you have all set up you only need to run the migrations on both services
Within the ```admin``` service, run the following command:
```sh
docker-compose up exec backend python manage.py migrate
```
Within the ```app``` service, run the following command:
```sh
docker-compose up exec backend flask upgrade
```

You can now access the admin service at http://localhost:8000 and the main app service at http://localhost:5000.

## Synchronization between Microservices
The admin and main app services are kept in sync through the use of an event messaging system called RabbitMQ. Any changes made in the admin service will be automatically reflected in the main app service.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
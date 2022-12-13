# Super Simple Project
This project consists of two microservices: an admin service written in Django, and a main app service. The admin service allows you to view and manage your products and their likes. The main app service allows customers to view and like your products.

## Requirements
Django
RabbitMQ
An AMQP URL (you can get this by creating an account and a project with RabbitMQ)

## Getting Started
Clone the repository:
Copy code
git clone https://github.com/user/repo.git
Install the required dependencies:
Copy code
pip install -r requirements.txt
Set the AMQP_URL environment variable with your RabbitMQ AMQP URL:
Copy code
export AMQP_URL=amqp://user:password@host:port/vhost
Run the Django migrations:
Copy code
python manage.py migrate
Start the Django development server:
Copy code
python manage.py runserver
In a separate terminal, start the main app service:
Copy code
python main_app.py
You can now access the admin service at http://localhost:8000/admin and the main app service at http://localhost:8000.

Synchronization between Microservices
The admin and main app services are kept in sync through the use of an event messaging system called RabbitMQ. Any changes made in the admin service will be automatically reflected in the main app service.

License
This project is licensed under the MIT License - see the LICENSE file for details.
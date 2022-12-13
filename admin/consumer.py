import json
import pika
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()
from products.models import Product


AMQP_URL = os.getenv("AMQP_URL", "NO HABIA PERRO")
print(AMQP_URL)
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(channel, method, properties, body):
    print('Received in admmin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print(f'Product {id} liked')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')
channel.start_consuming()

channel.close()

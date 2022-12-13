import pika, json
import os

AMQP_URL = os.getenv("AMQP_URL", None)
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
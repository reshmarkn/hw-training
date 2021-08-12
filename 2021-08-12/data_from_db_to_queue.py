from pymongo import MongoClient
import pika
db = MongoClient().zappos
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='zapos')
for item in db.woman_asics_shoes_links.find():
    url = item.get('PRODUCT_URL')
    channel.basic_publish(exchange='',routing_key='zapos',body=str(url))
connection.close()
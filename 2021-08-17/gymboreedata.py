from pymongo import MongoClient
import pika
db = MongoClient().gymboree
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='gymboree')
for item in db.gyboree_product_links.find():
    url = item.get('product_url')
    channel.basic_publish(exchange='',routing_key='gymboree',body=str(url))
connection.close()
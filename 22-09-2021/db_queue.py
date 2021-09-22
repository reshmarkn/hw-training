from pymongo import MongoClient
import pika
db = MongoClient().BIPA
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='bipa')
for item in db.bipa_product_links.find():
    url = item.get('product_url')
    channel.basic_publish(exchange='',routing_key='bipa',body=str(url))
connection.close()
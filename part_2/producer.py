from mongoengine import EmbeddedDocument, Document, CASCADE
from mongoengine.fields import DateTimeField, EmbeddedDocumentField, ListField, StringField, ReferenceField, \
    BooleanField
import faker
from bson import ObjectId
import pika

from web_hw_8.db_connection import db


class Contacts(Document):
    fullname = StringField()
    email = StringField()
    flag = BooleanField(default=False)


if __name__ == "__main__":
    fake_object = faker.Faker()

    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='line of contacts waiting for...')

    for _ in range(2):
        Contacts(fullname=fake_object.name(), email=fake_object.email()).save()

    contacts = Contacts.objects()
    for contact in contacts:
        contact_id = contact._data['id']
        print(contact_id)

        channel.basic_publish(exchange='', routing_key='line of contacts waiting for...', body=str(contact_id))
        print("!!!  ID were sent to line  !!!")

    connection.close()



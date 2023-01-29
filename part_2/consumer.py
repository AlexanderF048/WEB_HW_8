import pika
from producer import Contacts
from bson import ObjectId


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='line of contacts waiting for...')

    def callback(ch, method, properties, body):
        print(body)

        db_contact_update = Contacts.objects(id=ObjectId(body.decode(encoding="utf-8"))).first()  # in "byte" format  , but needs to be ObjectId
        print(f"!!!  Contact {body} founded in DB and waitin for update !!!")
        db_contact_update.update(flag=True)

    channel.basic_consume(queue='line of contacts waiting for...', on_message_callback=callback, auto_ack=True)

    print('!!!  Waiting for messages.  !!!')
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()

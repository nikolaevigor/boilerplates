import sys

print('queue name, routing key, body')

args = sys.argv[1:]

import pika

_RABBIT_USER = 'guest'
_RABBIT_PASSWORD = 'guest'
_RABBIT_HOST = '0.0.0.0'
_RABBIT_PORT = '5672'
_RABBIT_VHOST = '/'



_EXCHANGE_NAME = 'main'
_QUEUE_NAME = args[0]
_ROUTING_KEY = args[1]

rabbit_credentials = pika.PlainCredentials(_RABBIT_USER, _RABBIT_PASSWORD)
connection_params = conn_params = pika.ConnectionParameters(host=_RABBIT_HOST, port=_RABBIT_PORT, heartbeat=600, virtual_host=_RABBIT_VHOST,
                                                            credentials=rabbit_credentials,
                                                            connection_attempts=5,
                                                            retry_delay=5)

connection = pika.adapters.BlockingConnection(parameters=conn_params)
channel = connection.channel()
channel.exchange_declare(_EXCHANGE_NAME, exchange_type='direct')
channel.queue_declare(queue=_QUEUE_NAME)
channel.queue_bind(exchange=_EXCHANGE_NAME, queue=_QUEUE_NAME, routing_key=_ROUTING_KEY)

print(args)
channel.basic_publish(_EXCHANGE_NAME, _ROUTING_KEY, args[2])

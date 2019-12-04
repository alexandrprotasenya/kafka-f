from kafka import KafkaConsumer

import json
import uuid


consumer = KafkaConsumer(
    'events',
    client_id=str(uuid.uuid4())[:10],
    group_id='creators',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode())
)
consumer.poll()


for msg in consumer:
    print(msg.value)

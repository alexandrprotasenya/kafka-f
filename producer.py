from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
for i in range(100):
    future = producer.send('events', value={'balansed': False})
    result = future.get(timeout=10)
    print(result)

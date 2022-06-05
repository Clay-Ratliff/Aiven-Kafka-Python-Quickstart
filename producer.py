from kafka import KafkaProducer
from datetime import datetime, timezone
import json
import uuid

def producer(service_uri, ca_path, cert_path, key_path, message_count):
    producer = KafkaProducer(
        bootstrap_servers=service_uri,
        security_protocol="SSL",
        ssl_cafile=ca_path,
        ssl_certfile=cert_path,
        ssl_keyfile=key_path,
    )

    for i in range(0, message_count):
        json_object = get_sensor_data()
        message = json.dumps(json_object)
        message_key = str(uuid.uuid4())
        producer.send("sensor-data", key=message_key.encode("utf-8"), value=message.encode("utf-8"))

    # Wait for all messages to be sent
    producer.flush()

def get_sensor_data():
    with open('sample.json') as f:
        event_json = json.load(f)

    event_json['event_id'] = str(uuid.uuid4())
    event_json['timestamp'] = datetime.now(timezone.utc).astimezone().isoformat()
    return event_json


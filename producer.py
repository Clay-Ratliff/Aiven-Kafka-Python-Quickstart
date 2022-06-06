# The KafkaProducer is the heart of sending messages to Kafka
from kafka import KafkaProducer

# The datetime and timezone packages are just used to provide 
# a convenience method to create a timezone aware datetime
from datetime import datetime, timezone

# The json package provides us with an easy way to handle json
import json

# Likewise the uuid package creates uuid's for us.
import uuid

# Producer accepts the parameters passed from the CLI and uses them to
# construct a producer object with a secure connection to the Kafka service
def producer(service_uri, ca_path, cert_path, key_path, message_count):
    producer = KafkaProducer(
        bootstrap_servers=service_uri,
        security_protocol="SSL",
        ssl_cafile=ca_path,
        ssl_certfile=cert_path,
        ssl_keyfile=key_path,
    )

# The for loop just uses message_count to determine how many messages to send
    for i in range(0, message_count):
        # Get the sensor data. In a real application this would represent more complex work
        json_object = get_sensor_data()
        # This line accpets the returned JSON object and converts it into a JSON string
        message = json.dumps(json_object)
        # This generates a message key based on a UUID, which is then converted to a string
        message_key = str(uuid.uuid4())
        # This actually sends the message to the Kafka service.
        # Note that we have to encode the key and value as utf-8 because the send function expects
        # the types of both key and message to be bytes. If we don't explicitly encode them, the UUID
        # and key will throw encoding errors.  To see what will happen, remove the '.encode("utf-8")'
        # code from one or both of them to produce the encoding error.
        producer.send("sensor-data", key=message_key.encode("utf-8"), value=message.encode("utf-8"))

    # Ensure that all the messages are sent once generation has been completed.
    producer.flush()

def get_sensor_data():
    # Read in the sample JSON message template
    with open('sample.json') as f:
        event_json = json.load(f)

    # Replace the event_id template value with a new UUID
    event_json['event_id'] = str(uuid.uuid4())
    # Insert a timestamp into the message using the ISO 8601 format
    event_json['timestamp'] = datetime.now(timezone.utc).astimezone().isoformat()
    return event_json


from threading import Thread
import paho.mqtt.client as mqtt
from .logs import Logger
from config import Config
import json


# The callback for when the client receives a connection response from the server.
def on_connect(_client, user_data, flags, rc):
    Logger.info("Connected with result code "+str(rc))
    client.subscribe("events/#")


# the callback for whn the client receives msg from server
def on_message(_client, user_data, msg):
    if "events/" in msg.topic:
        try:
            tram = json.loads(msg.payload.decode())
            serial = tram["serial"]
            if serial is None:
                return
            """is_device = [x for x in devices if (x["serial"] == serial)]
            if len(is_device) > 0:
                tram["dateEvent"] = datetime.now()"""
        except Exception as ex:
            Logger.error(ex)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Config.MQTT_BROKER_URL, Config.MQTT_BROKER_PORT)
loop = Thread(target=client.loop_forever, args=())

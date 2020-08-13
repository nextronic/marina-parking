from threading import Thread
from time import sleep

import paho.mqtt.client as mqtt
from .logs import Logger
from config import Config
import json


# The callback for when the client receives a connection response from the server.
def on_connect(_client, user_data, flags, rc):
    Logger.info("Connected with result code "+str(rc))
    client.subscribe("events/#")
    client.subscribe("res/#")


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
    elif "res/" in msg.topic:
        try:
            tram = json.loads(msg.payload.decode())
            serial = tram["serial"]
            if serial is None:
                return
            del actions[serial]
        except Exception as ex:
            Logger.error(ex)


def SendItem(queue):
    global actions
    for display in queue.display:
        index = 0
        if queue.status == 1:
            index = display.index
        else:
            index = 2 if display.index == 1 else 1
        actions[display.serial] = {"serial": display.serial, "msg": queue.company.name, "img": index, "order": queue.order}


def PubItem():
    global actions
    while 1:
        for key in actions:
            client.publish(f'actions/{key}', json.dumps(actions[key]))
        sleep(2.5)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Config.MQTT_BROKER_URL, int(Config.MQTT_BROKER_PORT))
loop = Thread(target=client.loop_forever, args=())
sender = Thread(target=PubItem, args=())
actions = {}



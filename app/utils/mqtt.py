from threading import Thread
from time import sleep
from PIL import Image, ImageDraw, ImageFont
import socket
import paho.mqtt.client as mqtt
from .logs import Logger
from config import Config
import json
import queue


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


def convert(r, g, b):
    output = 0b00000000
    if r > 100:
        output = output or 0b00000001
    if g > 150:
        output |= 0b00000010
    if b > 100:
        output |= 0b00000100
    return output


def SendItem(queue):
    global actions
    for display in queue.display:
        actions.put({"serial": display.serial, "status": queue.status,"order":queue.order , "index": display.index, "name": queue.company.name})


def PubItem():
    _in = Image.open('./in.png')
    _out = Image.open('./out.png')
    font = ImageFont.truetype('arial.ttf', 13)
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    global actions
    while 1:
        display = actions.get()
        if display is None:
            sleep(0.5)
            continue
        img = Image.new('RGB', (64, 32))
        txt = Image.new('RGB', (32, 32), color='black')
        d = ImageDraw.Draw(txt)
        d.text((0, 16), display["name"], fill=(255, 255, 255), font=font)
        d.text((0, 0), "N "+str(display['order']), fill=(255, 255, 255), font=font)

        if display["status"] == 1:
            img.paste(_in if display["index"] == 1 else _out, (0, 0))
        else:
            img.paste(_in if display["index"] == 2 else _out, (0, 0))
        img.paste(txt, (34, 0))
        tmp = []
        for i in range(32):
            tmp.append(0x23)
            tmp.append(i)
            for j in range(64):
                r, g, b = img.getpixel((j, i))
                tmp.append(convert(r, g, b))
        client.publish(f'actions/{display["serial"]}', bytes(tmp))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Config.MQTT_BROKER_URL, int(Config.MQTT_BROKER_PORT))
loop = Thread(target=client.loop_forever, args=())
sender = Thread(target=PubItem, args=())
actions = queue.Queue()



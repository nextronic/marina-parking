from os import getenv
from dotenv import load_dotenv
load_dotenv()


class Config:
    MQTT_BROKER_URL = getenv('MQTT_HOST', 'localhost')
    MQTT_BROKER_PORT = getenv('MQTT_PORT', 1883)
    MQTT_USERNAME = getenv('MQTT_USER', '')
    MQTT_PASSWORD = getenv('MQTT_PASSWD', '')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = getenv('DB_URI', 'sqlite:///app/db/config.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY="g@AagE745f4BydNJf63hlnpi5edu*L2QCJNbz%MmqsGsMjS1T9ibked*!7QLE6cn"

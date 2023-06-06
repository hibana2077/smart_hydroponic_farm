import logging
import network
from machine import Pin,PWM
import time
import urequests
import math

"""
input:
    webcam
    water tank
    temperature
    humidity
upload to server
"""
SERVER_URL = "http://smartfarm.hibana2077.com"
REFRESH_TIME = 10
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#set CAMERA PIN
CAMERA1 = Pin(35,Pin.IN)
CAMERA2 = Pin(34,Pin.IN)

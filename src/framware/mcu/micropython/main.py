'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-04-12 13:17:43
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-05-01 10:19:05
FilePath: /smart_hydroponic_farm/micropython/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import logging
import network
from machine import Pin,PWM
import time
import urequests
import math

refreshtime = 10
url = "http://smartfarm.hibana2077.com"
logging.basicConfig(level=logging.INFO)

# workflow of this program
# 1. connect to wifi
# 2. recorded the sensor data
# 3. send the data to server
# 4. get the data from server
# 5. set the light

#set ARGB PIN
R = PWM(Pin(25))
G = PWM(Pin(26))
B = PWM(Pin(27))

#set sensor PIN
#DHT11
DHT11 = Pin(33,Pin.IN)
#water tank sensor
water_tank = Pin(32,Pin.IN)
#camera
camera1 = Pin(35,Pin.IN)
camera2 = Pin(34,Pin.IN)
#PH sensor
PH = Pin(36,Pin.IN)

#set sensor data
#DHT11
DHT11_temp = 0
DHT11_hum = 0
#water tank sensor
water_tank_data = 0
#camera
camera1_data = 0
camera2_data = 0
#PH sensor
PH_data = 0

#API endpoint
api_list = {
    "post_data": {"method": "POST", "url": url + "/api/v1/data"},
    "get_instruction": {"method": "GET", "url": url + "/api/v1/instruction"}
}


#set plant light
#ref: http://docs.micropython.org/en/v1.15/esp32/quickref.html#neopixel-driver
light_wavelength_category = {
    "grow_fast": 780,
    "grow_slow": 700,
    "photosynthesis": 660,
    "kill_bacteria": 610,
    "urtal_photosynthesis_and_kill_bacteria": 435,
    "default": 380
}

def get_hd_info():
    import machine as m
    cpu_freq = m.freq()
    
    

def wave_2_rgb(wavelength, intensity):
    r = intensity * math.sin(wavelength * 0.024) ** 2
    g = intensity * math.sin(wavelength * 0.024 + 2 * math.pi / 3) ** 2
    b = intensity * math.sin(wavelength * 0.024 + 4 * math.pi / 3) ** 2
    return list(map(int, (r, g, b)))


'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-03-08 20:54:31
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-03-08 22:07:16
FilePath: \基於滴灌式水耕農法之改進研究以及實作\lab.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import network
from machine import Pin,PWM
import time
import urequests

s = int(input("=>"))

#set ARGB PIN
R = PWM(Pin(25))
G = PWM(Pin(26))
B = PWM(Pin(27))
A = PWM(Pin(14))

def do_connect():
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('R15-D3A4', '0978526075')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

#setting plant light
def plant_light(R,G,B,A):
    R.duty(256)
    G.duty(1023)
    B.duty(256)
    A.duty(1023)
    time.sleep(0.5)

def get_duty(R,G,B,A):
    Rf = R.duty()
    Gf = G.duty()
    Bf = B.duty()
    Af = A.duty()
    print(f"R:{Rf} G:{Gf} B:{Bf} A:{Af}")
    

do_connect()
while True:
    plant_light(R,G,B,A)
    get_duty(R,G,B,A)



import machine
import time
import esp32

#get temperature
def get_temp():
    temp = esp32.raw_temperature()
    return temp

#Fahrenheit to Celsius
def f2c(temp):
    temp = (temp - 32) * 5 / 9
    return temp

#set ARGB PIN
R = machine.PWM(machine.Pin(25))
G = machine.PWM(machine.Pin(26))
B = machine.PWM(machine.Pin(27))
A = machine.PWM(machine.Pin(14))

#judgement temperature
def temp_judge(temp):
    if temp<=20:
        R.duty(256)
        G.duty(1023)
        B.duty(256)
        A.duty(1023)
        print("cold")
    elif temp>20 and temp<=30:
        R.duty(1023)
        G.duty(256)
        B.duty(256)
        A.duty(1023)
        print("warm")
    elif temp>30:
        R.duty(256)
        G.duty(256)
        B.duty(1023)
        A.duty(1023)
        print("hot")

while True:
    temp = get_temp()
    temp = f2c(temp)
    temp_judge(temp)
    time.sleep(0.5)

## 顏色要再調整
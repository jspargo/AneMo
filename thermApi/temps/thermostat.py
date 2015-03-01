# AneMo - Raspberry Pi based temperature control system
#           for home automation
# 
# Updated by Jack Spargo - 28/02/2015
# based on 04_thermomether.py by [to be added + licence]

import RPi.GPIO as GPIO
import time, math

GPIO.setmode(GPIO.BCM)

a_pin = 18
b_pin = 23

red_pin = 16
green_pin = 20
blue_pin = 21

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

redLed = GPIO.PWM(red_pin, 500)
greenLed = GPIO.PWM(green_pin, 500)
blueLed = GPIO.PWM(blue_pin, 500)

redLed.start(100)
greenLed.start(100)
blueLed.start(100)

fiddle_factor = 0.9
temp_upper_threshold = 20.5
temp_lower_threshold = 17.5;

def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.01)

def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, True)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000

def analog_read():
    discharge()
    return charge_time()

def read_resistance():
    n = 100
    total = 0;
    for i in range(1, n):
        total = total + analog_read()
    reading = total / float(n)
    resistance = reading * 6.05 - 939
    return resistance

def temp_from_r(R):
    B = 3800.0
    R0 = 1000.0
    t0 = 273.15
    t25 = t0 + 25.0
    inv_T = 1/t25 + 1/B * math.log(R/R0)
    T = 1/inv_T - t0
    return T * fiddle_factor

def lightChange(r,g,b):
    R_val = r * 100.0
    G_val = g * 100.0
    B_val = b * 100.0
    redLed.ChangeDutyCycle(R_val)
    greenLed.ChangeDutyCycle(G_val)
    blueLed.ChangeDutyCycle(B_val)   

while True:
    temp_c = temp_from_r(read_resistance())
    reading_str = "{:.2f}".format(temp_c)
    if temp_c < temp_lower_threshold:
	lightChange(1,0,0)
    if temp_c >= temp_lower_threshold and temp_c < temp_upper_threshold:
	lightChange(0,1,0)
    if temp_c >= temp_upper_threshold:
	lightChange(0,0,1)
    time.sleep(0.1)

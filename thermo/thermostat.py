#!flask/bin/python

# AneMo - Raspberry Pi based temperature control system
#           for home automation
# 
# Updated by Jack Spargo - 28/02/2015
# based on 04_thermomether.py by [to be added + licence]

import RPi.GPIO as GPIO
import time, math

class currentTemp():

    a_pin = 18
    b_pin = 23
    fiddle_factor = 0.9

    def keyboard_interupt(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

    def discharge(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.a_pin, GPIO.IN)
        GPIO.setup(self.b_pin, GPIO.OUT)
        GPIO.output(self.b_pin, False)
        time.sleep(0.01)
        return

    def charge_time(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.b_pin, GPIO.IN)
        GPIO.setup(self.a_pin, GPIO.OUT)
        GPIO.output(self.a_pin, True)
        t1 = time.time()
        while not GPIO.input(self.b_pin):
            pass
        t2 = time.time()
        GPIO.cleanup()
        return (t2 - t1) * 1000000

    def analog_read(self):
        self.discharge()
        return self.charge_time()

    def read_resistance(self):
        n = 100
        total = 0;
        for i in range(1, n):
            total = total + self.analog_read()
        reading = total / float(n)
        resistance = reading * 6.05 - 939
        return resistance

    def temp_from_r(self, R):
        B = 3800.0
        R0 = 1000.0
        t0 = 273.15
        t25 = t0 + 25.0
        inv_T = 1/t25 + 1/B * math.log(R/R0)
        T = 1/inv_T - t0
        return T * self.fiddle_factor

    def record_temp(self):
        temp_c = self.temp_from_r(self.read_resistance())
        reading_str = "{:.2f}".format(temp_c)
	return reading_str    

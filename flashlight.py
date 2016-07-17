# import libraries
import RPi.GPIO as GPIO
import time

#initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

#define a function to turn the light on and off
def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(10)
	GPIO.output(pin,False)
	time.sleep(1)
	return

def funnyBlink(pin):
	GPIO.output(pin,True)
	time.sleep(.1)
	GPIO.output(pin,False)
	time.sleep(.15)
        GPIO.output(pin,True)
        time.sleep(.1)
        GPIO.output(pin,False)
        time.sleep(.05)
        GPIO.output(pin,True)
        time.sleep(.1)
        GPIO.output(pin,False)
        time.sleep(.05)
        GPIO.output(pin,True)
        time.sleep(.1)
        GPIO.output(pin,False)
        time.sleep(.1)
        GPIO.output(pin,True)
        time.sleep(.1)
        GPIO.output(pin,False)
        time.sleep(.015)
        GPIO.output(pin,True)
        time.sleep(.2)
        GPIO.output(pin,False)
        time.sleep(.1)
	GPIO.output(pin,True)
        time.sleep(.2)
	return

#use blinkone function in a loop, then cleanup!
for i in range(0,1):
	funnyBlink(4)
GPIO.cleanup()

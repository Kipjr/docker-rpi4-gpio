# coding=utf-8
# Needed modules will be imported and configured
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
# Declaration and initialisation of the input pins which are connected with the sensor.
PIN_CLK = 16
PIN_DT = 15
BUTTON_PIN = 14
 
GPIO.setup(PIN_CLK, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_DT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
# Needed variables will be initialised
Counter = 0
Richtung = True
PIN_CLK_LETZTER = 0
PIN_CLK_AKTUELL = 0
delayTime = 0.01
 
# Initial reading of Pin_CLK
PIN_CLK_LETZTER = GPIO.input(PIN_CLK)
 
# This output function will start at signal detection
def ausgabeFunktion(null):
    global Counter
 
    PIN_CLK_AKTUELL = GPIO.input(PIN_CLK)
 
    if PIN_CLK_AKTUELL != PIN_CLK_LETZTER:
 
        if GPIO.input(PIN_DT) != PIN_CLK_AKTUELL:
            Counter += 1
            Richtung = True;
        else:
            Richtung = False
            Counter = Counter - 1
 
        print "Rotation detected: "
 
        if Richtung:
            print "Rotational direction: Clockwise"
        else:
            print "Rotational direction: Counterclockwise"
 
        print "Current position: ", Counter
        print "------------------------------"
 
def CounterReset(null):
    global Counter
 
    print "Position reset!"
    print "------------------------------"
    Counter = 0
 
# To include a debounce directly, the output function will be initialised from the GPIO Python Module via callback-option
GPIO.add_event_detect(PIN_CLK, GPIO.BOTH, callback=ausgabeFunktion, bouncetime=50)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=CounterReset, bouncetime=50)
 
 
print "Sensor-Test [press ctrl-c to end]"
 
# Main program loop
try:
        while True:
            time.sleep(delayTime)
 
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
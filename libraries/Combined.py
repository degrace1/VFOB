
from Motor import *
import math
import time


class BoltState:

    # constructor
    def __init__(self, x, y):
        self.ultrasonic = Ultrasonic()
        self.distance = self.ultrasonic.get_distance()
        self.bolt_location = []
        self.bolt_location.append(x)
        self.bolt_location.append(y)

    # set methods
    def setDistance(self):
        self.distance = self.ultrasonic.get_distance()

    def addLocation(self, x, y):  # maybe dont need this hm
        self.bolt_location.append(x)
        self.bolt_location.append(y)

    def setLocation(self, x, y):  # can probs remove x & y and change to function from data
        self.bolt_location.clear()
        self.addLocation(x, y)

    # get methods
    def getDistance(self):
        return self.distance

    def getLocation(self):
        return self.bolt_location

    # show object params in line form
    def logInLine(self):
        temp = ""
        delim = ","
        temp += "distance=" + str(self.distance) + delim
        temp += "x=" + str(self.bolt_location[0]) + delim
        temp += "y=" + str(self.bolt_location[1])
        return temp

    def run(self):
        PWM = Motor()
        x = self.bolt_location[0]
        distance = self.distance
        angle = math.tan(distance / x)
        travel = math.sqrt(math.pow(x, 2)+math.pow(distance, 2))
        # turn angle
        #PWM.destroy()
        PWM.setMotorModel(0,0,0,0)
        turnTime = 3  #FIXME
        try:
            
            PWM.setMotorModel(2000,2000,-1250,-1250)  #turn right
            time.sleep(turnTime)
            # drive travel
            
            speed = 35.4  #FIXME add speed here
            
            sec = speed/travel
            PWM.setMotorModel(800, 800, 1250, 1250)
            time.sleep(sec)
            PWM.setMotorModel(0, 0, 0, 0)
        
        except KeyboardInterrupt:
            PWM.setMotorModel(0,0,0,0)
        
import time
from Motor import *
import RPi.GPIO as GPIO

from PCA9685 import PCA9685
class Ultrasonic:
    def __init__(self): #initiate and set upnpins for i/o
        GPIO.setwarnings(False)
        self.trigger_pin = 27
        self.echo_pin = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin,GPIO.OUT)
        GPIO.setup(self.echo_pin,GPIO.IN)
    def send_trigger_pulse(self): #sends out an ultrasonic wave forwards
        GPIO.output(self.trigger_pin,True)
        time.sleep(0.00015)
        GPIO.output(self.trigger_pin,False)

    def wait_for_echo(self,value,timeout): #waits for wave to come bounce back
        count = timeout
        #change count to understand distance
        while GPIO.input(self.echo_pin) != value and count>0: 
            count = count-1
     
    def get_distance(self):        #calculate distance
        distance_cm=[0,0,0,0,0]    #initial distance 0
        for i in range(3):         #loop 3x
            self.send_trigger_pulse()       #send a trigger pulse to start wave
            self.wait_for_echo(True,10000)  #wait for echo to come back
            start = time.time()             #start timer
            self.wait_for_echo(False,10000) #wait for echo
            finish = time.time()            #finish timer
            pulse_len = finish-start        #calc total time from lengths
            # multiply by usonic speed and divide by two (for there and back
            distance_cm[i] = (pulse_len * 34300) / 2 
        distance_cm=sorted(distance_cm)     #sort
        return int(distance_cm[2])          #return distance

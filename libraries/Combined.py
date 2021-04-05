from ultrasonic_sensor import *
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
        self.addLocation(x,y)

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
        x = self.bolt_location[0]
        distance = self.distance
        angle = math.tan(distance / x)
        travel = math.sqrt(math.pow(x, 2)+math.pow(distance, 2))
        # turn angle
        # drive travel
        speed = 1  #FIXME add speed here
        sec = speed/travel
        PWM.setMotorModel(800, 800, 800, 800)
        time.sleep(sec)
        PWM.setMotorModel(0, 0, 0, 0)

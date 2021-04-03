from ultrasonic_sensor import *
import sys
import zmq
import time
import socket



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

    def addLocation(self, x, y): #maybe dont need this hm
        self.bolt_location.append(x)
        self.bolt_location.append(y)

    def setLocation(self, x, y):
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




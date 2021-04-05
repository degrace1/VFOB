import os
import sys
import zmq
import time
from libraries.CarRun import *
from libraries.Motor import *

from libraries.Combined import *
from libraries.ObjectDet import *

sys.path.append(os.path.relpath("./libraries"))

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

x=  #add here x
y=  #add here y

me = BoltState()
me.setDistance()
me.setlocation(x,y)



while True:
    # wait for next request from client
    message = socket.recv()
    print("Received request: ", message)
    time.sleep(1)
    #get x from objectdet
    #update x in me
    #get y from objectdet
    #update y in me
    me.setLocation(x,y)
    me.setDistance()

    sentMessage = me.logInLine()
    socket.send(sentMessage % port)

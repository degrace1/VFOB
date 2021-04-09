import os
import sys
import zmq
import time
sys.path.append(os.path.relpath("./libraries"))

from Motor import *

from Combined import *


sys.path.append(os.path.relpath("./libraries"))

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

# get x from objectdet
x =100
# update x in me
# get y from objectdet
y =100
# update y in me

me = BoltState(x,y)
me.setDistance()
me.run()



'''
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
'''
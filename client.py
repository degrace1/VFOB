# Made By Grace on 4/2/21
# Name: client.py
# This program connects to the server through port "5556"
# and sends a message asking for info.
# What needs to be changed:
# - change request to send only when needed
# - change message to be split differently (will be sent in the format "Distance=#,x=#,b=#")


import zmq
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

context = zmq.Context()
print ("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

#  Do 10 requests, waiting each time for a response
for request in range (1,10): #change this to be when u need it, like after servos are moving
    print ("Sending request ", request,"...")
    socket.send ("Plz give me location")
    #  Get the reply.
    message = socket.recv()
    print ("Received reply ", request, "[", message, "]")

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# userclient

#Cameron Roberts
#5/6/2020
#Python Capstone Networking Prof Amamra

# Import socket module 

import socket
import time

#define tcp connect parameters
TCP_IP = 'localhost'
TCP_PORT = 10000
BUFFER_SIZE = 1024


#instantiate socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((TCP_IP, TCP_PORT))


#clock data
clockStart = time.clock()
timeStart = time.time()

#opening file
with open('received_file', 'wb') as fStream:
    print '  FILE DATA'
    print '-------------'
    while True:
        #data write loop
        data = mySocket.recv(BUFFER_SIZE)
        print data
        if not data:
            fStream.close()
            break
        
        fStream.write(data)

clockEnd = time.clock()
timeEnd = time.time()
#duration calcs
durationTime =timeEnd-timeStart
durationClock=clockEnd-clockStart

#closing client socket
mySocket.close()

#output
print('Transfer Success, Connection Closed')
print 'Time: Start = ',timeStart, ' End = ',timeEnd, 'Time Elapsed = ', durationTime
print 'Clock: Start = ',clockStart, ' End = ',clockEnd, 'Total = ', durationClock

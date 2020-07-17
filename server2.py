#Cameron Roberts
#5/6/2020
#Python Capstone Networking Prof Amamra
import socket
from threading import Thread


TCP_IP = 'localhost'
TCP_PORT = 10000
BUFFER_SIZE = 1024
#class defining each thread
class ClientThread(Thread):

    def __init__(self,ip,port,sock):#assign thread self values
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print "  User Thread Info: "+ip+":"+str(port)

    def run(self):#define run parameters
        filename='mytext.txt'
        fStream = open(filename,'rb')
        while True:
            l = fStream.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                l = fStream.read(BUFFER_SIZE)
            if not l:
                fStream.close()
                self.sock.close()
                break

#keep array of threads
threads = []

while True:
    #initialize socket
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((TCP_IP, TCP_PORT))
    tcpsock.listen(5)
    
    print "Awaiting Connection...."
    (conn, (ip,port)) = tcpsock.accept()
    print ' User Connected'
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)
    #close socket, so that it can be reused
    tcpsock.close()

for t in threads:
    t.join()#join all threads
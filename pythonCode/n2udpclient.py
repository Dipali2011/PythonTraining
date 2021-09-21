import socket
msgfromclient = "hello udp server"
bytesTosend = str.encode(msgfromclient)

serverAddressPort = ('127.0.0.1',20001)

buffersize = 1024

UPDCLIENTSOCKET = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM) #1
UDPCLIENTSOCKET.sendto(bytesTosend, serverAddressPort) #2
msgfromserver = UDPCLIENTSOCKET.recvfrom(buffersize) #3
msg = "message from server{}".format(msgfromserver[0])
print(msg)
import socket
localIP = '127.0.0.1'
localport = 28001

bufferSize = 1024

msgFromServer = "Hello UPD Client"

bytesToSend = str.encode(msgFromServer)

UPDSERVERSOCKET = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

UPDSERVERSOCKET.bind((localIP,localport)) # 2

print("UPD server up and listening.....")
while True:
    bytesAddressPair = UPDSERVERSOCKET.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientmsg = "Message from client{}".format(message)
    ClientIP = "Client IP address:{}".format(address)
    print(clientmsg)
    print(ClientIP)
    UPDSERVERSOCKET.sendto(bytesToSend,address) #4
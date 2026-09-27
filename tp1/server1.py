from socket import *
import random
serverPort = 1234
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('server ready')
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode().upper()
	if random.randint(1,10) > 5:
		print("not replying to this client")
		continue
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)

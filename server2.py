from socket import *
import datetime

serverPort = 1234
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('server ready')
while True:
	connectionSocket, address = serverSocket.accept()
	now = datetime.datetime.now()
	message = connectionSocket.send(str(now.time()).encode('utf-8'))
	print('sent time to ' + str(address))
	connectionSocket.close()


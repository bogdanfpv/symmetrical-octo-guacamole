from socket import *
from datetime import datetime

serverName = '127.0.0.1'
serverPort = 1234
times = []
for i in range(0,6):
	clientSocket = socket(AF_INET,SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	serverTime = datetime.strptime(clientSocket.recv(2048).decode('utf-8'), '%H:%M:%S.%f').time()
	t_local = datetime.now().time()
	diff = (serverTime.hour*3600 + serverTime.minute*60 + serverTime.second + serverTime.microsecond/1e6) - (t_local.hour*3600 + t_local.minute*60 + t_local.second + t_local.microsecond/1e6)
	times.append(diff)
	clientSocket.close()
avg = sum(times) / len(times)
print(avg)

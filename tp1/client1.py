import time
import random
from socket import *
t_end = time.time() + 60 * 0.25
serverName = '127.0.0.1'
serverPort = 1234
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
message = input('lowercase sentence:')
i=0
while time.time() < t_end:
	try:
		clientSocket.sendto(message.encode(),(serverName,serverPort))
	except TimeoutError:
		print("client sendto call timed out")
	try:
		modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
		print(modifiedMessage.decode())
		print(i)
		i+=1
	except TimeoutError:
		print("client recv call timed out")
	time.sleep(2.5)
clientSocket.close()

from socket import *
from sys import *
from pathlib import Path

serverPort = 1234
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('web server ready')
while True:
	connectionSocket, address = serverSocket.accept()
	requete = connectionSocket.recv(2048).decode('utf-8')
	filename = requete.split()[1][1:]
	
	file = Path(filename)
	if file.is_file():
		with open(filename, 'rb') as f:
			contenu = f.read()
		entete = 'HTTP/1.1 200 OK\r\n\r\n'
		reponse = entete.encode('utf-8') + contenu
	else:
		entete = 'HTTP/1.1 404 Not Found\r\n\r\n'
		contenu = 'Fichier non trouve'
		reponse = entete.encode('utf-8') + contenu.encode('utf-8')
	connectionSocket.send(reponse)
	connectionSocket.close()	

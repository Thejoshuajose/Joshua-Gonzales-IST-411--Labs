#Project: Lab 5 Client and Server Using Networking Sockets
#Purpose Details: To learn howw clients connect to servers using networking
#Course: IST411
#Author: Joshua Gonzales
#Date Developed: 9/26/24
#Last Date Changed: 9/26/24
#Rev: 1

#Client

import socket
import json
import urllib.request
import sys

try:
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	jsonServerAddress = ('127.0.0.1',8080)
	clientsocket.connect(jsonServerAddress)
	print("Client is connected to the server...")
	jsonResponse = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts/1')
	print("Payload has been received...")
	jsonPayload = jsonResponse.read()
	#payload = json.loads(jsonPayload)
	clientsocket.sendall(jsonPayload)
	print("Payload Sent...")
except Exception as e :
	print("error: ",e)
finally:
	clientsocket.close()


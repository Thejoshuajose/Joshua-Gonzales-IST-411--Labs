#Project: Lab 5 Client and Server Using Netwworking Sockets
#Purpose Details: To Learn how clients connect to servers using Networking
#Course: IST411
#Author: Joshua Gonzales
#Date Developed: 9/26/24
#Last Date Changed: 9/26/24

#Server

import sys
import json
import socket


try:
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('0.0.0.0', 8080))
	server_socket.listen(1)
	print("Server is listening for connection on port 8080...")
	while True:
		clientsocket, address = server_socket.accept()
		print(f"Connection from {address} has been established....")
		data = clientsocket.recv(1024)
		print("Payload Recieved....")
		json_payload = data.decode('utf-8')
		print("Received JSON payload:",json_payload)
		clientsocket.close()
except KeyboardInterrupt:
        print("Server shutting down.")
except Exception as e:
        print("An error occurred: ",{e})
finally:
        server_socket.close()




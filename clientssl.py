#Project: Lab 7 Client and Server Using SSL
#Project Details: Use client and server applications to send information securly with SSL
#Course: IST411
#Author: Joshua Gonzales
#Date Developed: 10/8/24
#Last Date Changed: 10/8/24
#Rev: 1

import socket
import ssl
import json


HOST = 'localhost'
PORT = 8080


payload = {
    "message": "Hello, this is a secure message from Joshua Gonzales!"
}


context = ssl.create_default_context()
context.load_verify_locations(cafile="server.crt")

print(f"Client connecting on port {PORT} using SSL")

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.sendall(json.dumps(payload).encode())
        print("Payload has been sent")
        print(f"TLS version: {ssock.version()}")

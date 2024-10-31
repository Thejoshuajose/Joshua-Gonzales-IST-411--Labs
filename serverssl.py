#Project: Lab 7 Client Server Socket Using SSL
#Purpose Details: Create a server and client that receives and sends paylooads securly via SSL
#Course: IST411
#Author: Joshua Gonzales
#Date Developed: 10/8/24
#Last Date Changed: 10/8/24
#Rev: 1

import socket
import ssl
import json


HOST = '0.0.0.0'
PORT = 8080


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"Listening on port {PORT}...")

    with context.wrap_socket(sock, server_side=True) as ssock:
        while True:
            conn, addr = ssock.accept()
            print("Accepting Connections from outside...")
            print(f"Connection from {addr}...")

            data = conn.recv(1024)
            print("Data Received....")
            if data:
                json_payload = json.loads(data.decode())
                print(f"JSON payload: {json_payload}")

            print(f"TLS version: {conn.version()}")

            conn.close()

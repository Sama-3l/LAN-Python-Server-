import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.137.1"
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnect"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
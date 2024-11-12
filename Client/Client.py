import socket
import ClientUI

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("70:66:55:62:7a:9c", 4))

try:
    while True:
        data = client.recv(1024)
        if not data:
            break

        if data.decode() == "1":
            print(ClientUI.Connect())
except OSError as e:
    pass

client.close()
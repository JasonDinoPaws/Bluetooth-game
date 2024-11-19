import socket
import ClientUI

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("70:66:55:62:7a:9c", 4))

client.send(socket.gethostname().encode())

try:
    while True:
        data = client.recv(1024)
        if not data:
            break

        if data.decode() == "1":
            client.send(str(ClientUI.Connect()).encode())
    print("Update Window")
except OSError as e:
    pass

client.close()
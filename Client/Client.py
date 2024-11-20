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

        dec = data.decode()
        if dec == "1":
            client.send(ClientUI.Connect().encode())
        elif dec == "2":
            ClientUI.Virus()
    print("Update Window")
except OSError as e:
    pass


client.close()
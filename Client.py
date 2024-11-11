import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("70:66:55:62:7a:9c", 4))


try:
    while True:
        client.send(input("EnterMessage:").encode())
        data = client.recv(1024)
        if not data:
            break
        print(f"Message from server: {data.decode()}")
except OSError as e:
    pass

client.close()
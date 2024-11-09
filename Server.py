import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("70:66:55:62:7a:9c", 4))
server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message from {addr}: {data.decode()}")
        client.send(input("EnterMessage:").encode())
except OSError as e:
    pass

client.close()
server.close()
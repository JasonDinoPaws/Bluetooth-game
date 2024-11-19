import socket

allowed = 2
connected = []
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("70:66:55:62:7a:9c", 4))
server.listen(allowed)

while len(connected) < allowed:
    client, addr = server.accept()
    hn = client.recv(1024)
    connected.append([client,addr,hn.decode()])
    print(hn.decode(),"Has connected with address",addr)

def SendToClients(clients,mess:str):
    for cl,ad in clients:
        cl.send(mess.encode())

try:
    while True:
        SendToClients(connected,input("Send Message: "))

except OSError as e:
    pass

server.close()
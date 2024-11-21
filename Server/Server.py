import socket
#import ServerUi

connected = []
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("6c:2f:80:71:84:8b", 4))
server.listen(1)

#print("Socket Open")

#ServerUi.viewcleints(connected)
while len(connected) < 1:#not ServerUi.Start and ServerUi.window.winfo_exists():
    client, addr = server.accept()
    hn = client.recv(1024)
    connected.append([client,addr,hn.decode(),False])
    print(hn.decode(),"Has connected with address",addr[0])
    #ServerUi.viewcleints(connected)

def SendToClients(mess:str):
    for cl,_,_,ac in connected:
        if ac:
            cl.send(mess.encode())

def connect():
    for cl,_,_,_ in connected:
        cl.send(str("1").encode())
    
    for p in range(len(connected)):
        cl,_,hn,_ = connected[p]
        data = cl.recv(1024)
        print(hn,"Status:",data)
        if not data or data.decode() == "no":
            cl.close()
            continue
        connected[p][3] = True

    for _,_,hn,ac in connected:
        print(hn,"connection status:",ac)


            

try:
    while True:#ServerUi.window.winfo_exists():
        act = input("Send Message: ")
        if act == "1":
            connect() 
        else:
            SendToClients(act)

except OSError as e:
    pass

server.close()
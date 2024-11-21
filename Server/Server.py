import socket
import pyautogui
from ShellUi import textupdate

connected = []
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("6c:2f:80:71:84:8b", 4))
server.listen(1)

# Checks for any clients that want to connect
while len(connected) < 4:#not ServerUi.Start and ServerUi.window.winfo_exists():
    client, addr = server.accept()
    hn = client.recv(1024)
    connected.append([client,addr,hn.decode(),False])
    textupdate(hn.decode(),"has connected with address",addr[0])


# Sends any commands to all clients that are connected
def SendToClients(mess:str):
    for cl,_,_,ac in connected:
        if ac:
            cl.send(mess.encode())

# asks all the clients if we are allowed to conneect
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

targetsite = "gnu.org"

#COMMAND LIST 

mktest = "mkdir test"

pinga = ("ping",targetsite)







try:
    while True:#ServerUi.window.winfo_exists():
        act = input("Send Message: ")
        if act == "1":
            connect() 
        elif act == "test":
            SendToClients("cmdmode")
            SendToClients(mktest)
        else:
            SendToClients(act)

except OSError as e:
    pass

server.close()
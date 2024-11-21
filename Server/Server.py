import socket
import pyautogui
import keyboard
from time import sleep
from ShellUi import textupdate,window

connected = []
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("6c:2f:80:71:84:8b", 4))
server.listen(1)

# Checks for any clients that want to connect
while len(connected) < 5:
    client, addr = server.accept()
    hn = client.recv(1024)
    connected.append([client,addr,hn.decode(),False])
    textupdate(hn.decode()+" has connected with address "+addr[0])
    textupdate()
textupdate("Max amount of clients, entering shell")
textupdate()

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






text = ""
try:
    while True:
        key = keyboard.read_key()

        if key == 'enter':
            textupdate()
            if text == "1":
                connect() 
            elif text == "test":
                SendToClients("cmdmode")
                SendToClients(mktest)
            else:
                SendToClients(text)
            text = ""
        elif key == "backspace":
            text = text[0:len(text)-1]
            textupdate(text)
        elif key != "":
            text += key
            textupdate(text)
        sleep(.1)
except OSError as e:
    pass

server.close()
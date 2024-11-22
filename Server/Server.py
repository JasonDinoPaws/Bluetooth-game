import socket
import pyautogui
import keyboard
from time import sleep
from ShellUi import Line,newLine,window
text = ""
numclients = 1


while window.winfo_exists():
    Line("Set the number of clients: "+text)
    key = keyboard.read_key()

    if key == 'enter':
        newLine()
        if text.isdigit():
            numclients = int(text)
            break
        else:
            Line("\""+text+"\" is not a integer",True)
            text = ""
    elif key == "backspace":
        text = text[0:len(text)-1]
    elif key != "":
        text += key
    sleep(.115)
Line("----------------------------",True)
Line("Starting Server",True)
Line("----------------",True)

connected = []
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("6c:2f:80:71:84:8b", 4))
server.listen(1)

# Checks for any clients that want to connect
while len(connected) < numclients:
    client, addr = server.accept()
    hn = client.recv(1024)
    connected.append([client,addr,hn.decode(),"None"])
    Line(hn.decode()+" has connected with address "+addr[0],True)
Line("Max amount of clients, entering shell",True)
Line("----------------------------",True)

# Sends any commands to all clients that are connected
def SendToClients(mess:str,isFile = False):
    for cl,_,_,ac in connected:
        if ac:
            if isFile:
                cl.sendfile(open(mess,"rb"))
            else:
                cl.send(mess.encode())

# asks all the clients if we are allowed to conneect
def connect():
    for cl,_,_,_ in connected:
        cl.send(str("1").encode())
    
    for p in range(len(connected)):
        cl,_,hn,_ = connected[p]
        data = cl.recv(1024)
        if not data:
            connected[p][3] = "Ded"
            Line(hn+" has lost connection",True)
        else:
            connected[p][3] = data.decode() == "yes"
            Line(hn+" connection status: "+str(connected[p][3]),True)

targetsite = "gnu.org"

#COMMAND LIST 
commands = {
    1: "Asks all connected clients if we are allowed to ne fully connected",
    2: "Tells all fully connected clients to turn the \"Virus\" method",
    3: "Tells all fully connecte clients to take a screenshot and send it back",
    "img": "Sends a image",
    "status": "Prints the connected client statuses",
    "end": "Stops everything"
}

mktest = "mkdir test"

pinga = ("ping",targetsite)





text = ""
Line("Type \"?\" for commands",True)
try:
    while True:
        Line("Command: "+text)
        key = keyboard.read_key()

        if key == 'enter':
            newLine()
            if text == "end":
                break

            elif text == "1":
                connect() 
            elif text == "test":
                SendToClients("cmdmode")
                SendToClients(mktest)
            elif text == "img":
                SendToClients("C:/Users/jaypa/OneDrive/Documents/GitHub/Bluetooth-game/Server/Lucky.png",True)
            elif text == "status":
                for _,add,hn,ac in [["",("Address",4),"Host name","Allowed"]]+connected:
                    print(add,hn,ac)
                    Line(str(hn)+" | "+str(add[0])+" | "+str(ac),True)
            else:
                SendToClients(text)
            text = ""

        elif key in ["shift","ctrl","alt"]:
            continue

        elif key == "?":
            Line("-----------",True)
            for c,d in commands.items():
                Line(str(c)+": "+d,True)
            Line("-----------",True)

        elif key == "backspace":
            text = text[0:len(text)-1]

        elif key == "space":
            text += " "

        elif key != "":
            text += key

        sleep(.115)
except OSError as e:
    pass

server.close()
if window.winfo_exists():
    window.quit()
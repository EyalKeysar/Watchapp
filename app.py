from libs.ServerAPI.ServerAPI import ServerAPI
from src.GUI.GUI import GUI
import time

def main():
    serverAPI = ServerAPI()
    root = GUI(serverAPI)
    root.mainloop()
    # time.sleep(5)
    # serverAPI.login("aaaa", "aaaa")


if __name__ == "__main__":
    main()
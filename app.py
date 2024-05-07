from libs.ServerAPI.ServerAPI import ServerAPI
from src.MockServerAPI.mock_server_api import MockServerAPI
from src.GUI.GUI import GUI
import time
import threading


def main():
    serverAPI = ServerAPI()
    mock_server = MockServerAPI()
    # root = GUI(serverAPI)
    root = GUI(mock_server)
    root.mainloop()
    # time.sleep(5)
    # serverAPI.login("aaaa", "aaaa")


if __name__ == "__main__":
    main()
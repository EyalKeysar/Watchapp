from libs.ServerAPI.ServerAPI import ServerAPI
from src.GUI.GUI import GUI


def main():
    serverAPI = ServerAPI()
    root = GUI(serverAPI)
    root.mainloop()

if __name__ == "__main__":
    main()
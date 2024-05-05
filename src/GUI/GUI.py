import tkinter as tk
import customtkinter as Ctk
from customtkinter import CTkTabview
from .consts import *
from PIL import Image, ImageTk
from .sign_in_screens import SignUpFrame, LoginFrame
from .dashboard import DashboardFrame
import threading
import os

class GUI(Ctk.CTk):
    def __init__(self, server_api, dark_theme=True):
        self.server_api = server_api
        threading.Thread(target=self.server_api.connect).start()
        super().__init__()
        # Ctk.set_appearance_mode("Dark") if dark_theme else Ctk.set_appearance_mode("Light")
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.title("Watchapp")

        Ctk.set_appearance_mode("Dark")

        ico = Image.open(os.path.join(os.path.dirname(__file__), "icon.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, ImageTk.PhotoImage(ico))
        
        
        # bg = tk.PhotoImage(file="C:/Networks/Watchapp/tests/screens_tests/dark_bg.jpg")
        #make it bg
        
        self.logo = LogoFrame(self, self.server_api, fg_color=BG_COLOR)
        self.logo.grid(row=0, column=0, sticky="ew", columnspan=100) # Just a lot of columnspan to make sure it's centered and full width
        self.frame = SignUpFrame(self, self.server_api, fg_color=BG_COLOR)
        self.frame.grid(row=1, column=0, pady=DIST_FROM_LOGO, sticky=STICKY_LAYOUT, columnspan=100) # Just a lot of columnspan to make sure it's centered and full width

class LogoFrame(Ctk.CTkFrame):
    def __init__(self, parent, server_api, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.server_api = server_api
        self.grid_columnconfigure(0, weight=1)

        # label = Ctk.CTkLabel(self, text="Watchapp", font=("Arial", 30), fg_color=kwargs.get("fg_color"))
        # label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # relative logo
        path = os.path.join(os.path.dirname(__file__), "logo.png")
        image = Image.open(path)
        image = image.resize((300, 39))
        photo = ImageTk.PhotoImage(image)
        label = Ctk.CTkLabel(self, text="", image=photo, fg_color=kwargs.get("fg_color"))
        label.image = photo
        label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        
        self.connection_status = Ctk.CTkLabel(self, text=DISCONNECTED_TEXT, font=("Arial", 30), fg_color=kwargs.get("fg_color"), text_color=DISCONNECTED_COLOR)
        self.connection_status.grid(row=0, column=0, pady=10, padx=10, sticky="e")
        self.update_connection_status()
        
    
    def update_connection_status(self):
        try:
            status = self.server_api.is_connected
            if status:
                self.connection_status.configure(text=CONNECTED_TEXT, text_color=CONNECTED_COLOR)
            else:
                self.connection_status.configure(text=DISCONNECTED_TEXT, text_color=DISCONNECTED_COLOR)

        except:
            pass
        self.after(1000, self.update_connection_status)

def main():
    root = GUI()
    root.mainloop()

if __name__ == "__main__":
    main()
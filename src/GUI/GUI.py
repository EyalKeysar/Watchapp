import tkinter as tk
import customtkinter as Ctk
from customtkinter import CTkTabview
from .consts import *
from PIL import Image, ImageTk
from .sign_in_screens import SignUpFrame, LoginFrame
from .dashboard import DashboardFrame

class GUI(Ctk.CTk):
    def __init__(self, server_api, dark_theme=True):
        self.server_api = server_api
        super().__init__()
        # Ctk.set_appearance_mode("Dark") if dark_theme else Ctk.set_appearance_mode("Light")
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.title("Watchapp")
        
        # bg = tk.PhotoImage(file="C:/Networks/Watchapp/tests/screens_tests/dark_bg.jpg")
        #make it bg
        
        self.logo = LogoFrame(self, fg_color=BG_COLOR)
        self.logo.grid(row=0, column=0, sticky="ew", columnspan=100) # Just a lot of columnspan to make sure it's centered and full width
        self.frame = SignUpFrame(self, self.server_api, fg_color=BG_COLOR)
        self.frame.grid(row=1, column=0, pady=DIST_FROM_LOGO, sticky=STICKY_LAYOUT)

class LogoFrame(Ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)

        label = Ctk.CTkLabel(self, text="Watchapp", font=("Arial", 30), fg_color=kwargs.get("fg_color"))
        label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        
        self.connection_status = Ctk.CTkLabel(self, text=DISCONNECTED_TEXT, font=("Arial", 30), fg_color=kwargs.get("fg_color"), text_color=DISCONNECTED_COLOR)
        self.connection_status.grid(row=0, column=0, pady=10, padx=10, sticky="e")
        self.update_connection_status()
        
    
    def update_connection_status(self):
        try:
            raise NotImplementedError
            status = False # TODO: get status from server
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
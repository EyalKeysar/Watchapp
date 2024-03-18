import tkinter as tk
import customtkinter as Ctk
from consts import *
from PIL import Image, ImageTk
from sign_in_screens import SignUpFrame, LoginFrame

class GUI(Ctk.CTk):
    def __init__(self, dark_theme=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Ctk.set_appearance_mode("Dark") if dark_theme else Ctk.set_appearance_mode("Light")
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.title("Watchapp")
        
        # bg = tk.PhotoImage(file="C:/Networks/Watchapp/tests/screens_tests/dark_bg.jpg")
        #make it bg
        
        self.logo = LogoFrame(self, fg_color=BG_COLOR)
        self.logo.grid(row=0, column=0, sticky="ew")
        self.frame = SignUpFrame(self, fg_color=BG_COLOR)
        self.frame.grid(row=1, column=0, pady=DIST_FROM_LOGO, sticky=STICKY_LAYOUT)


class LogoFrame(Ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)

        label = Ctk.CTkLabel(self, text="Watchapp", font=("Arial", 30), fg_color=kwargs.get("fg_color"))
        label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        
        connection_status = Ctk.CTkLabel(self, text=DISCONNECTED_TEXT, font=("Arial", 30), fg_color=kwargs.get("fg_color"), text_color=DISCONNECTED_COLOR)
        connection_status.grid(row=0, column=0, pady=10, padx=10, sticky="e")


def main():
    root = GUI(dark_theme=True)
    root.mainloop()

if __name__ == "__main__":
    main()
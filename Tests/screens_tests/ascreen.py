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
        self.logo = LogoFrame(self, fg_color="transparent")
        self.logo.grid(row=0, column=0, sticky=STICKY_LAYOUT)
        self.frame = SignUpFrame(self, fg_color="#353438")
        self.frame.grid(row=1, column=0, sticky=STICKY_LAYOUT)


class LogoFrame(Ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        logo_theme = "dark_logo" if Ctk.get_appearance_mode() == "Dark" else "light_logo"
        logoimage = Image.open(f"C:/Dev/school/Watchapp/Tests/screens_tests/{logo_theme}.png")
        logoimage = logoimage.resize((LOGO_WIDTH, LOGO_HEIGHT))
        photoimage = ImageTk.PhotoImage(logoimage)
        self.logo = Ctk.CTkLabel(self, text="", image=photoimage)
        self.logo.photo = photoimage
        self.logo.grid(row=1, column=0, pady=10)




def main():
    root = GUI(dark_theme=True)
    root.mainloop()

if __name__ == "__main__":
    main()
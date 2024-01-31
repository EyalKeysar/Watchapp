import tkinter as tk
import customtkinter as Ctk
from consts import *
from PIL import Image, ImageTk


class GUI(Ctk.CTk):
    def __init__(self, dark_theme=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Ctk.set_appearance_mode("Dark") if dark_theme else Ctk.set_appearance_mode("Light")
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.title("Watchapp")
        self.logo = LogoFrame(self)
        self.logo.grid(row=0, column=0, sticky="nsew")
        self.frame = LoginFrame(self)
        self.frame.grid(row=1, column=0, sticky="nsew")


class LogoFrame(Ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        logoimage = Image.open("C:/Networks/Watchapp/tests/screens_tests/dark_logo.png") if Ctk.get_appearance_mode() == "Dark" else Image.open("C:/Networks/Watchapp/tests/screens_tests/light_logo.png")
        logoimage = logoimage.resize((LOGO_WIDTH, LOGO_HEIGHT))
        photoimage = ImageTk.PhotoImage(logoimage)
        self.logo = Ctk.CTkLabel(self, text="", image=photoimage)
        self.logo.photo = photoimage
        self.logo.grid(row=1, column=0, pady=10)

class LoginFrame(Ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(sticky="nsew")    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.title = Ctk.CTkLabel(self, text="Login", font=("Arial", 100))
        self.title.grid(row=0, column=0, pady=10)

        self.username = Ctk.CTkEntry(self, placeholder_text="Username", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.username.grid(row=1, column=0, pady=10)

        self.password = Ctk.CTkEntry(self, placeholder_text="Password", show="*", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.password.grid(row=2, column=0, pady=10)


        self.forgot_password = Ctk.CTkButton(self, text="Forgot password?", command=self.forgot_password)
        self.forgot_password.grid(row=3, column=0, pady=10)


        self.login = Ctk.CTkButton(self, text="Login", command=self.login, width=LOGIN_BTN_WIDTH, height=LOGIN_BTN_HEIGHT, font=LOGIN_BTN_FONT)
        self.login.grid(row=4, column=0, pady=10)

    
    def login(self):
        print(f"Username: {self.username.get()}")
        print(f"Password: {self.password.get()}")
    
    def forgot_password(self):
        print("Forgot password?")
        



def main():
    root = GUI()
    root.mainloop()

if __name__ == "__main__":
    main()
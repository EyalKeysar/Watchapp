import tkinter as tk
from customtkinter import *
from consts import *
from PIL import Image, ImageTk

class GUI(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.title("Watchapp")
        self.logo = LogoFrame(self)
        self.logo.grid(row=0, column=0, sticky="nsew")
        self.frame = LoginFrame(self)
        self.frame.grid(row=1, column=0, sticky="nsew")


class LogoFrame(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        LOGO_WIDTH = 600
        LOGO_HEIGHT = 200

        logoimage = Image.open("C:/Dev/school/Watchapp/Tests/screens_tests/logo.png")
        logoimage = logoimage.resize((LOGO_WIDTH, LOGO_HEIGHT))
        photoimage = ImageTk.PhotoImage(logoimage)
        self.logo = CTkLabel(self, text="", image=photoimage)
        self.logo.photo = photoimage
        self.logo.grid(row=1, column=0, pady=10)

class LoginFrame(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(sticky="nsew")    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.padding_label = CTkLabel(self, text="", width=600, height=10).grid(row=0, column=0)

        self.title = CTkLabel(self, text="Login", font=("Arial", 100))
        self.title.grid(row=0, column=0, pady=10)

        ENTRY_WIDTH = 300
        ENTRY_HEIGHT = 60
        ENTRY_FONT = ("Arial", 30)

        self.username = CTkEntry(self, placeholder_text="Username", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.username.grid(row=1, column=0, pady=10)

        self.password = CTkEntry(self, placeholder_text="Password", show="*", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.password.grid(row=2, column=0, pady=10)

        FORGOT_PSWD_WIDTH = 300
        FORGOT_PSWD_HEIGHT = 60
        FORGOT_PSWD_FONT = ("Arial", 20)

        self.forgot_password = CTkButton(self, text="Forgot password?", command=self.forgot_password)
        self.forgot_password.grid(row=3, column=0, pady=10)

        LOGIN_BTN_WIDTH = 300
        LOGIN_BTN_HEIGHT = 60
        LOGIN_BTN_FONT = ("Arial", 30)

        self.login = CTkButton(self, text="Login", command=self.login, width=LOGIN_BTN_WIDTH, height=LOGIN_BTN_HEIGHT, font=LOGIN_BTN_FONT)
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
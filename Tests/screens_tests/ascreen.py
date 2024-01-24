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
        self.logo.grid(row=0, column=0, sticky=STICKY_LAYOUT)
        self.frame = SignUpFrame(self)
        self.frame.grid(row=1, column=0, sticky=STICKY_LAYOUT)


class LogoFrame(Ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        logoimage = Image.open(f"C:/Networks/Watchapp/tests/screens_tests/{"dark_logo" if Ctk.get_appearance_mode() == "Dark" else "light_logo"}.png")
        logoimage = logoimage.resize((LOGO_WIDTH, LOGO_HEIGHT))
        photoimage = ImageTk.PhotoImage(logoimage)
        self.logo = Ctk.CTkLabel(self, text="", image=photoimage)
        self.logo.photo = photoimage
        self.logo.grid(row=1, column=0, pady=10)

class LoginFrame(Ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.title = Ctk.CTkLabel(self, text="Login", font=(GENERAL_FONT, TITLE_FONT_SIZE))
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
        
class SignUpFrame(Ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.passwords_match = False
        
        self.title = Ctk.CTkLabel(self, text="Sign Up", font=(GENERAL_FONT, TITLE_FONT_SIZE))
        self.title.grid(row=0, column=0, pady=10)

        self.username = Ctk.CTkEntry(self, placeholder_text="Username", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.username.grid(row=1, column=0, pady=10)

        self.password = Ctk.CTkEntry(self, placeholder_text="Password", show="*", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.password.grid(row=2, column=0, pady=10)
        
        self.confirm_password = Ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.confirm_password.grid(row=3, column=0, pady=10)

        self.not_matching_passwords = Ctk.CTkLabel(self, text=" * Passwords do not match", font=(GENERAL_FONT, 20), text_color="red")
        self.invalid_username = Ctk.CTkLabel(self, text=" * Invalid username", font=(GENERAL_FONT, 20), text_color="red")
        self.invalid_password = Ctk.CTkLabel(self, text=" * Invalid password", font=(GENERAL_FONT, 20), text_color="red")

        
        self.already_have_account = Ctk.CTkButton(self, text="Already have an account?", command=self.already_have_account)
        self.already_have_account.grid(row=7, column=0, pady=10)
        
        self.sign_up = Ctk.CTkButton(self, text="Sign Up", command=self.sign_up, width=LOGIN_BTN_WIDTH, height=LOGIN_BTN_HEIGHT, font=LOGIN_BTN_FONT)
        self.sign_up.grid(row=8, column=0, pady=10)

    def sign_up(self):
        if self.password.get() == self.confirm_password.get():
            self.passwords_match = True; self.not_matching_passwords.grid_forget()
        else:
            self.passwords_match = False; self.not_matching_passwords.grid(row=4, column=0, pady=SIGN_UP_ERROR_PADY)
        
        if len(self.username.get()) < 4: 
            self.invalid_username.grid(row=5, column=0, pady=SIGN_UP_ERROR_PADY)
        else: 
            self.invalid_username.grid_forget()
            
        if len(self.password.get()) < 4:
            self.invalid_password.grid(row=6, column=0, pady=SIGN_UP_ERROR_PADY)
        else:
            self.invalid_password.grid_forget()
            
        if self.passwords_match and len(self.username.get()) >= 4 and len(self.password.get()) >= 4:
            print(f"Username: {self.username.get()}")
            print(f"Password: {self.password.get()}")

    def already_have_account(self):
        print("Already have an account?")


def main():
    root = GUI()
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
import customtkinter as Ctk
from .consts import *
from PIL import Image, ImageTk

from .dashboard import DashboardFrame, CardFrame

class LoginFrame(Ctk.CTkFrame):
    def __init__(self, parent, server_api, *args, **kwargs):
        self.parent = parent
        self.server_api = server_api
        
        super().__init__(parent, *args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.title = Ctk.CTkLabel(self, text="Login", font=(GENERAL_FONT, TITLE_FONT_SIZE))
        self.title.grid(
            row=0, column=0, 
            pady=LOGIN_Y_PADDING, 
            padx=LOGIN_X_PADDING)

        self.email = Ctk.CTkEntry(self, placeholder_text="Email Address", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.email.grid(
            row=1, column=0, 
            pady=LOGIN_Y_PADDING,
            padx=LOGIN_X_PADDING)

        self.password = Ctk.CTkEntry(self, placeholder_text="Password", show="*", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.password.grid(
            row=2, column=0, 
            pady=LOGIN_Y_PADDING,
            padx=LOGIN_X_PADDING)

        self.forgot_password = Ctk.CTkButton(self, text="Forgot password?", command=self.forgot_password)
        self.forgot_password.grid(
            row=3, column=0, 
            pady=LOGIN_Y_PADDING,
            padx=LOGIN_X_PADDING)

        self.login = Ctk.CTkButton(self, text="Login", command=self.login, width=LOGIN_BTN_WIDTH, height=LOGIN_BTN_HEIGHT, font=LOGIN_BTN_FONT)
        self.login.grid(row=5, column=0, 
                        pady=LOGIN_Y_PADDING,
                        padx=LOGIN_X_PADDING)
        
        self.doesnt_have_account = Ctk.CTkButton(self, text="Doesn't have an account?", command=self.doesnt_have_account)
        self.doesnt_have_account.grid(row=4, column=0, 
                                      pady=LOGIN_Y_PADDING,
                                      padx=LOGIN_X_PADDING)
    
    def login(self):
        print(f"Email: {self.email.get()}")
        print(f"Password: {self.password.get()}")
        if self.server_api.login(self.email.get(), self.password.get()) == "False":
            print("Login failed")
            self.invalid_credentials = Ctk.CTkLabel(self, text=" * Invalid credentials", font=(GENERAL_FONT, 20), text_color="red")
            self.invalid_credentials.grid(row=6, column=0, pady=LOGIN_ERROR_PADY)
        else:
            print("Login successful")
            # Load Dashboard frame
            self.grid_forget()
            self.parent.frame = DashboardFrame(self.parent, self.server_api, fg_color=BG_COLOR)



        
    
    def forgot_password(self):
        print("Forgot password?")
    
    def doesnt_have_account(self):
        print("Doesn't have an account?")
        # Load Sign Up frame
        self.grid_forget()
        self.parent.frame = SignUpFrame(self.parent, self.server_api, fg_color=BG_COLOR)
        self.parent.frame.grid(row=1, column=0, pady=DIST_FROM_LOGO, sticky=STICKY_LAYOUT)
        
class SignUpFrame(Ctk.CTkFrame):
    
    def __init__(self, parent, server_api, *args, **kwargs):
        self.parent = parent
        self.server_api = server_api
        super().__init__(parent, *args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.passwords_match = False
        
        title_r, title_c = 0, 0
        username_r, username_c = 1, 0
        email_r, email_c = 2, 0
        password_r, password_c = 3, 0
        conf_password_r, conf_password_c = 4, 0
        already_have_account_r, already_have_account_c = 8, 0
        sign_up_r, sign_up_c = 9, 0 
        
        
        self.title = Ctk.CTkLabel(self, text="Sign Up", font=(GENERAL_FONT, TITLE_FONT_SIZE))
        self.title.grid(row=title_r, column=title_c, columnspan=MID_COL_SPAN_SIGNUP, pady=SIGNUP_Y_PADDING)

        self.username = Ctk.CTkEntry(self, placeholder_text="Username", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.username.grid(row=username_r, column=username_c, padx=SIGNUP_X_PADDING, pady=SIGNUP_Y_PADDING)
        
        self.email = Ctk.CTkEntry(self, placeholder_text="Email", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.email.grid(row=email_r, column=email_c, padx=SIGNUP_X_PADDING, pady=SIGNUP_Y_PADDING)

        self.password = Ctk.CTkEntry(self, placeholder_text="Password", show="*", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.password.grid(row=password_r, column=password_c, padx=SIGNUP_X_PADDING, pady=SIGNUP_Y_PADDING)
        
        self.confirm_password = Ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.confirm_password.grid(row=conf_password_r, column=conf_password_c, padx=SIGNUP_X_PADDING, pady=SIGNUP_Y_PADDING)

        self.not_matching_passwords = Ctk.CTkLabel(self, text=" * Passwords do not match", font=(GENERAL_FONT, 20), text_color="red")
        self.invalid_username = Ctk.CTkLabel(self, text=" * Invalid username", font=(GENERAL_FONT, 20), text_color="red")
        self.invalid_password = Ctk.CTkLabel(self, text=" * Invalid password", font=(GENERAL_FONT, 20), text_color="red")

        self.already_have_account = Ctk.CTkButton(self, text="Already have an account?", command=self.already_have_account)
        self.already_have_account.grid(row=already_have_account_r, column=already_have_account_c, columnspan=MID_COL_SPAN_SIGNUP, pady=10)
        
        self.sign_up = Ctk.CTkButton(self, text="Sign Up", command=self.sign_up, width=LOGIN_BTN_WIDTH, height=LOGIN_BTN_HEIGHT, font=LOGIN_BTN_FONT)
        self.sign_up.grid(row=sign_up_r, column=sign_up_c, columnspan=MID_COL_SPAN_SIGNUP, padx=SIGNUP_X_PADDING, pady=SIGNUP_Y_PADDING)

    def sign_up(self):
        if self.password.get() == self.confirm_password.get():
            self.passwords_match = True; self.not_matching_passwords.grid_forget()
        else:
            self.passwords_match = False; self.not_matching_passwords.grid(row=5, column=0, columnspan=MID_COL_SPAN_SIGNUP, pady=SIGN_UP_ERROR_PADY)
            return
        
        if len(self.username.get()) < 4: 
            self.invalid_username.grid(row=6, column=0, columnspan=MID_COL_SPAN_SIGNUP, pady=SIGN_UP_ERROR_PADY)
            return
        else: 
            self.invalid_username.grid_forget()
            
        if len(self.password.get()) < 4:
            self.invalid_password.grid(row=7, column=0, columnspan=MID_COL_SPAN_SIGNUP, pady=SIGN_UP_ERROR_PADY)
            return
        else:
            self.invalid_password.grid_forget()
            
        if self.passwords_match and len(self.username.get()) >= 4 and len(self.password.get()) >= 4:
            print(f"Username: {self.username.get()}")
            print(f"Password: {self.password.get()}")
            print(f"Email: {self.email.get()}")
            
            status = (self.server_api.signup(self.email.get(), self.password.get(), self.username.get()))
            if status == "False":
                print("Sign up failed")
                self.email_already_exists = Ctk.CTkLabel(self, text=" * Email already exists", font=(GENERAL_FONT, 20), text_color="red")
                self.email_already_exists.grid(row=8, column=0, columnspan=MID_COL_SPAN_SIGNUP, pady=SIGN_UP_ERROR_PADY)
            else:
                raise NotImplementedError # "should add after sign in gui"
                pass

# R U R' U' R' F R2 U' R' U' R U R' F'


    def already_have_account(self):
        print("Already have an account?")
        # Load Login frame
        self.grid_forget()
        self.parent.frame = LoginFrame(self.parent, self.server_api, fg_color=BG_COLOR)
        self.parent.frame.grid(row=1, column=0, pady=DIST_FROM_LOGO, sticky=STICKY_LAYOUT)
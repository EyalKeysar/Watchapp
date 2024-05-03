import tkinter as tk
from tkinter import ttk
from tkinter_webcam import webcam
from typing import Tuple


import customtkinter as Ctk
from .consts import *
from PIL import Image, ImageTk
import math
from .Customlistbox import CustomScrolledListbox

class DashboardFrame(Ctk.CTkFrame):
    def __init__(self, parent, server_api, *args, **kwargs):
        self.parent = parent
        self.server_api = server_api
        super().__init__(parent, *args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)
        self.grid_columnconfigure(0, weight=1)

        self.title = Ctk.CTkLabel(self, text="Dashboard", font=(GENERAL_FONT, TITLE_FONT_SIZE))
        self.title.grid(row=0, column=0, pady=10, padx=10)

        self.add_child_button = Ctk.CTkButton(self.parent, text="+", command=self.add_child, width=50, height=50, font=(GENERAL_FONT, 20))
        self.add_child_button.grid(row=1, column=1, pady=10, padx=10)

        self.logout_button = Ctk.CTkButton(self.parent, text="➜", command=self.logout, width=70, height=50, font=(GENERAL_FONT, 25))
        self.logout_button.grid(row=1, column=2, pady=10, padx=40)

        self.server_api.get_children()

        self.cards = []
        max_cards_per_row = 2
        card_width = 500  # Adjust according to your card size
        card_height = 200  # Adjust according to your card size
        row_height = card_height + 20  # Adjust vertical spacing between rows
        for i, child_data in enumerate(self.server_api.children):
            row = i // max_cards_per_row + 1
            column = i % max_cards_per_row
            x_offset = ((SCREEN_WIDTH - min(len(self.server_api.children) - (row - 1) * max_cards_per_row, max_cards_per_row) * card_width) / 2 ) + 40
            y_offset = -50  # Adjust vertical offset as needed
            x_pos = x_offset + column * card_width
            y_pos = y_offset + row * row_height
            card = CardFrame(self.parent, self.server_api, child_data)
            card.place(x=x_pos, y=y_pos)
            self.cards.append(card)



    def add_child(self):
        self.grid_forget()
        for card in self.cards:
            card.place_forget()
        self.add_child_frame = AddChildFrame(self.parent, self.server_api)
        self.add_child_frame.place(x=SCREEN_WIDTH // 2 - 200, y=SCREEN_HEIGHT // 2 - 100)

    def logout(self):
        pass

class CardFrame(Ctk.CTkFrame):
    def __init__(self, parent, server_api, child_data, *args, **kwargs):
        self.server_api = server_api
        self.parent = parent
        super().__init__(parent, *args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.default_fg_color = "brown"
        self.child_name = child_data.child_name
        
        print("child_data",child_data)
        print("child data type",type(child_data))

        self.title = Ctk.CTkLabel(self, text=child_data.child_name, font=(GENERAL_FONT, 30))
        self.title.grid(row=0, column=0, pady=10, padx=50, columnspan=3)

        self.active_status = Ctk.CTkLabel(self, text="Inactive", font=(GENERAL_FONT, 15),text_color="red")
        self.active_status.grid(row=0, column=2, pady=10)
        
        self.name = Ctk.CTkLabel(self, text="Statistics", font=(GENERAL_FONT, 20))
        self.name.grid(row=1, column=0, pady=10, padx=50, columnspan=3)

        self.stat1 = Ctk.CTkLabel(self, text="time used", font=(GENERAL_FONT, 15))
        self.stat1.grid(row=2, column=0, pady=10, padx=50)
        self.stat2 = Ctk.CTkLabel(self, text="Stat 2", font=(GENERAL_FONT, 15))
        self.stat2.grid(row=2, column=1, pady=10, padx=50)
        self.stat3 = Ctk.CTkLabel(self, text="Stat 3", font=(GENERAL_FONT, 15))
        self.stat3.grid(row=2, column=2, pady=10, padx=50)

        self.view_button = Ctk.CTkButton(self, text="View", command=self.view_child, width=300, height=30, font=(GENERAL_FONT, 20))
        self.view_button.grid(row=3, column=0, pady=10, padx=50, columnspan=3)

        # self.update_active_status()

        self.bind("<Button-1>", self.on_card_click)

    def on_card_click(self, event):
        print(f"Card {self.title.cget('text')} clicked")

    def view_child(self):
        print(f"Viewing child {self.title.cget('text')}")
        for card in self.parent.frame.cards:
            card.place_forget()
        self.parent.frame.grid_forget()
        self.parent.frame.add_child_button.grid_forget()
        self.parent.frame = ChildView(self.parent, self.server_api, self.child_name)
        self.parent.frame.grid(row=1, column=0, columnspan=100)


    def update_active_status(self):
        try:
            raise NotImplementedError
            status = False # TODO: get status from server
            if status:
                self.active_status.configure(text="Active", text_color='green')
            else:
                self.active_status.configure(text="Inactive", text_color='red')

        except:
            pass
        self.after(1000, self.update_active_status)


class AddChildFrame(Ctk.CTkFrame):
    def __init__(self, parent, server_api, *args, **kwargs):
        self.parent = parent
        self.server_api = server_api
        
        super().__init__(parent, *args, **kwargs)
        # self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.title = Ctk.CTkLabel(self, text="Add Child", font=(GENERAL_FONT, TITLE_FONT_SIZE))
        self.title.grid(
            row=0, column=0, 
            pady=LOGIN_Y_PADDING, 
            padx=LOGIN_X_PADDING)

        self.auth_str = Ctk.CTkEntry(self, placeholder_text="Auth code", width=300, height=30, font=(GENERAL_FONT, 25))
        self.auth_str.grid(
            row=1, column=0, 
            pady=LOGIN_Y_PADDING,
            padx=LOGIN_X_PADDING)
        self.child_name = Ctk.CTkEntry(self, placeholder_text="Child Name", width=300, height=30, font=(GENERAL_FONT, 25))
        self.child_name.grid(
            row=2, column=0, 
            pady=LOGIN_Y_PADDING,
            padx=LOGIN_X_PADDING)
        
        self.add_child_btn = Ctk.CTkButton(self, text="Add Child", command=self.add_child, width=LOGIN_BTN_WIDTH, height=LOGIN_BTN_HEIGHT, font=LOGIN_BTN_FONT)
        self.add_child_btn.grid(row=5, column=0, 
                        pady=LOGIN_Y_PADDING,
                        padx=LOGIN_X_PADDING)
        
        self.go_back_btn = Ctk.CTkButton(self, text="Go Back", command=self.go_back, width=LOGIN_BTN_WIDTH, height=LOGIN_BTN_HEIGHT, font=LOGIN_BTN_FONT)
        self.go_back_btn.grid(row=6, column=0, 
                        pady=LOGIN_Y_PADDING,
                        padx=LOGIN_X_PADDING)

    def add_child(self):
        print(f"Auth code: {self.auth_str.get()}")

        respond = self.server_api.confirm_agent(self.auth_str.get(), self.child_name.get())
        print("rr respond",respond)
        # self.server_api.add_child(self.child_id.get())
        self.go_back()


    def go_back(self):
        self.grid_forget()
        self.place_forget()

        self.parent.frame = DashboardFrame(self.parent, self.server_api, fg_color=BG_COLOR)
        self.parent.frame.grid(row=1, column=0, columnspan=100)



class ChildView(Ctk.CTkFrame):
    def __init__(self, parent, server_api, child_name, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.child_name = child_name
        self.server_api = server_api
        self.grid(sticky=tk.NSEW)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title = Ctk.CTkLabel(self, text="Child View", font=(GENERAL_FONT, TITLE_FONT_SIZE))
        self.title.grid(row=0, column=0, pady=10, padx=10, columnspan=10)


        COLUMNS = ("id", "program_name", "start_time", "end_time", "allowed_time", "time_span", "usage")

        # Creating Treeview widget
        self.restrictions = ttk.Treeview(self, columns=COLUMNS, show="headings")
        self.restrictions.grid(row=1, column=0, pady=10, padx=10, columnspan=10, sticky=tk.NSEW)

        # Configuring style for Treeview

        style = ttk.Style(self)
        style.theme_use('default')  # Ensure default theme is used
        style.configure('Dark.Treeview', background='#363636', foreground='white', fieldbackground='#363636', font=(GENERAL_FONT, 10))
        style.configure('Dark.Treeview.Heading', background='#363636', foreground='white', font=(GENERAL_FONT, 10))
        style.map('Treeview', background=[('selected', '#3e465c')], foreground=[('selected', 'white')])
        style.map('Treeview.Heading', background=[('active', '#363636')])
        self.restrictions.configure(style='Dark.Treeview')

        # Define headings for columns
        self.restrictions.heading("id", text="ID")
        self.restrictions.heading("program_name", text="Program Name")
        self.restrictions.heading("start_time", text="Start Time")
        self.restrictions.heading("end_time", text="End Time")
        self.restrictions.heading("allowed_time", text="Allowed Time")
        self.restrictions.heading("time_span", text="Time Span")
        self.restrictions.heading("usage", text="Usage")

        self.restrictions.column("id", width=20)
        self.restrictions.column("program_name", width=50)
        self.restrictions.column("start_time", width=150)
        self.restrictions.column("end_time", width=150)
        self.restrictions.column("allowed_time", width=100)
        self.restrictions.column("time_span", width=100)
        self.restrictions.column("usage", width=200)


        # Inserting sample data
        sample_data = self.server_api.get_restrictions(self.child_name)

        for data in sample_data:
            self.restrictions.insert("", "end", values=(data.id, data.program_name, data.start_time, data.end_time, data.allowed_time, data.time_span, data.usage_time))


        self.add_restriction_button = Ctk.CTkButton(self, text="Add Restriction", command=self.add_restriction, width=200, height=30, font=(GENERAL_FONT, 20), text_color='light green')
        self.add_restriction_button.grid(row=2, column=0, pady=10, padx=10)

        # Initially set the buttons to disabled state and gray color
        self.modify_restriction_button = Ctk.CTkButton(self, text="Modify Restriction", command=self.modify_restriction, width=200, height=30, font=(GENERAL_FONT, 20), state='disabled')
        self.delete_restriction_button = Ctk.CTkButton(self, text="Delete Restriction", command=self.delete_restriction, width=200, height=30, font=(GENERAL_FONT, 20), state='disabled')
        self.modify_restriction_button.grid(row=3, column=0, pady=10, padx=10)
        self.delete_restriction_button.grid(row=4, column=0, pady=10, padx=10)
        # Bind a function to the Treeview's select event
        self.restrictions.bind('<<TreeviewSelect>>', self.on_select)

        self.go_back_btn = Ctk.CTkButton(self, text="Go Back", command=self.go_back, width=200, height=30, font=(GENERAL_FONT, 20))
        self.go_back_btn.grid(row=5, column=0, pady=10, padx=10)

    def on_select(self, event):
        # Change the state and color of the buttons when a row is selected
        self.modify_restriction_button.configure(state='normal')
        self.delete_restriction_button.configure(state='normal', text_color='red')


    def add_restriction(self):
        self.grid_forget()
        self.parent.frame.grid_forget()
        self.parent.frame = AddRestrictionFrame(self.parent, self.server_api, self.child_name)
        self.parent.frame.grid(row=1, column=0, columnspan=100)

    def modify_restriction(self):
        pass
        # self.parent.frame = ModifyRestrictionFrame(self.parent, self.server_api)
        # self.parent.frame.grid(row=1, column=0, columnspan=100)

    def delete_restriction(self):
        pass
        # self.parent.frame = DeleteRestrictionFrame(self.parent, self.server_api)
        # self.parent.frame.grid(row=1, column=0, columnspan=100)

    def go_back(self):
        self.grid_forget()
        self.place_forget()

        self.parent.frame = DashboardFrame(self.parent, self.server_api)
        self.parent.frame.grid(row=1, column=0, columnspan=100)

class AddRestrictionFrame(Ctk.CTkFrame):
    def __init__(self, parent, server_api, child_name, *args, **kwargs):
        self.parent = parent
        self.server_api = server_api
        self.child_name = child_name
        super().__init__(parent, *args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.title = Ctk.CTkLabel(self, text=f"Add Restriction", font=(GENERAL_FONT, TITLE_FONT_SIZE))
        self.title.grid(
            row=0, column=0, columnspan=4,
            pady=40, 
            padx=10)



        self.program_options = self.server_api.get_programs(self.child_name)
        self.search_entry = Ctk.CTkEntry(self, placeholder_text="Search Program", width=300, height=30, font=(GENERAL_FONT, 25))
        self.search_entry.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
        self.search_entry.bind("<KeyRelease>", self.search)

        self.program_name = Ctk.CTkOptionMenu(self, values=self.program_options, width=300, height=30, font=(GENERAL_FONT, 20))
        self.program_name.configure(dropdown_font=(GENERAL_FONT, 15))
        self.program_name.grid(row=1, column=2, columnspan=2, pady=10, padx=10)

        self.start_time_label = Ctk.CTkLabel(self, text="Start Time", font=(GENERAL_FONT, 20))
        self.start_time_label.grid(row=2, column=0, pady=10, padx=10)
        self.start_time = tk.Spinbox(self, from_=0, to=24, width=3, font=(GENERAL_FONT, 25), bg=BG_COLOR, fg='#1f6aa5', bd=0, wrap=True, command=self.validate_time_c)
        self.start_time.grid(row=2, column=1, pady=10, padx=10)

        self.start_time.bind("<KeyRelease>", self.validate_time)


        self.end_time_label = Ctk.CTkLabel(self, text="End Time", font=(GENERAL_FONT, 20))
        self.end_time_label.grid(row=2, column=2, pady=10, padx=10)
        self.end_time = tk.Spinbox(self, from_=0, to=24, width=3, font=(GENERAL_FONT, 25), bg=BG_COLOR, fg='#1f6aa5', bd=0, wrap=True, command=self.validate_time_c)
        self.end_time.grid(row=2, column=3, pady=10, padx=10)
        self.end_time.delete(0, tk.END)
        self.end_time.insert(0, 24)
        # set function to validate the time on change
        self.end_time.bind("<KeyRelease>", self.validate_time)


        self.allowed_time_label = Ctk.CTkLabel(self, text="Allowed Time", font=(GENERAL_FONT, 20))
        self.allowed_time_label.grid(row=4, column=0, pady=10, padx=10)
        self.allowed_time = tk.Spinbox(self, from_=0, to=731, width=3, font=(GENERAL_FONT, 25), bg=BG_COLOR, fg='#1f6aa5', bd=0, wrap=True, command=self.validate_allowed_time_c)
        self.allowed_time.grid(row=4, column=1, pady=10, padx=10)
        self.allowed_time.delete(0, tk.END)
        self.allowed_time.insert(0, 24)
        self.allowed_time.bind("<KeyRelease>", self.validate_allowed_time)

        self.time_spans = ["Daily", "Weekly", "Monthly"]
        self.time_span = Ctk.CTkOptionMenu(self, values=self.time_spans, width=300, height=30, font=(GENERAL_FONT, 20), command=self.validate_allowed_time)
        self.time_span.configure(dropdown_font=(GENERAL_FONT, 15))
        self.time_span.grid(row=4, column=2, columnspan=2, pady=10, padx=10)



        self.add_restriction_btn = Ctk.CTkButton(self, text="Add Restriction", command=self.add_restriction, width=LOGIN_BTN_WIDTH, height=50, font=LOGIN_BTN_FONT)
        self.add_restriction_btn.grid(row=10, column=0, columnspan=4,
                        pady=10,
                        padx=10)
        
        self.go_back_btn = Ctk.CTkButton(self, text="Go Back", command=self.go_back, width=200, height=40, font=LOGIN_BTN_FONT)
        self.go_back_btn.grid(row=11, column=0, columnspan=4,
                        pady=10,
                        padx=10)

    def add_restriction(self):
        print(f"Program: {self.program_name.get()}")
        print(f"Start Time: {self.start_time.get()}")
        print(f"End Time: {self.end_time.get()}")
        print(f"Allowed Time: {self.allowed_time.get()}")
        print(f"Time Span: {self.time_span.get()}")
        self.server_api.add_restriction(self.child_name, self.program_name.get(), self.start_time.get(), self.end_time.get(), self.allowed_time.get(), self.time_span.get())
        self.go_back()

    def go_back(self):
        self.grid_forget()
        self.place_forget()

        self.parent.frame = ChildView(self.parent, self.server_api, self.child_name)
        self.parent.frame.grid(row=1, column=0, columnspan=100)


    def select_time_span(self):
        for btn in self.time_spans_btns:
            btn.configure(text_color='black')
        self.add_restriction_btn.configure(text="Add Restriction", text_color='black')


    def search(self, event):
        # update self.program_name with the search results
        search_term = self.search_entry.get().lower()
        print(f"Searching for {search_term}")

        # Assuming self.program_options is a list of all possible options
        # Filter the options based on the search term
        filtered_options = [option for option in self.program_options if search_term in option.lower()]

        # Update the OptionMenu with the filtered options
        self.program_name.configure(values=filtered_options)

    def validate_time(self, event):
        # Validate the end time to be greater than the start time
        try: 
            start_time = int(self.start_time.get())
        except ValueError:
            self.start_time.configure(fg='red')
            return

        try: 
            end_time = int(self.end_time.get())
        except ValueError:
            self.end_time.configure(fg='red')
            return


        if end_time <= start_time or end_time > 24:
            self.end_time.configure(fg='red')
        else:
            self.end_time.configure(fg='#1f6aa5')

        if start_time < 0 or start_time > 24:
            self.start_time.configure(fg='red')
        else:
            self.start_time.configure(fg='#1f6aa5')

    def validate_allowed_time(self, event):
        # Validate the allowed time to be greater than 0
        try:
            allowed_time = int(self.allowed_time.get())
        except ValueError:
            self.allowed_time.configure(fg='red')
            return
        
        time_span = self.time_span.get()
        if time_span == "Daily" and allowed_time > 24 or time_span == "Weekly" and allowed_time > 168 or time_span == "Monthly" and allowed_time > 744 or allowed_time < 0 or allowed_time > 744:
            self.allowed_time.configure(fg='red')
        else:
            self.allowed_time.configure(fg='#1f6aa5')

    def validate_time_c(self):
        self.validate_time(None)

    def validate_allowed_time_c(self):
        self.validate_allowed_time(None)
        
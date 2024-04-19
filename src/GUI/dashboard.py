import tkinter as tk
from typing import Tuple
import customtkinter as Ctk
from .consts import *
from PIL import Image, ImageTk
import math

class DashboardFrame(Ctk.CTkFrame):
    def __init__(self, parent, server_api, *args, **kwargs):
        self.parent = parent
        self.server_api = server_api
        super().__init__(parent, *args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)
        self.grid_columnconfigure(0, weight=1)

        self.title = Ctk.CTkLabel(self, text="Dashboard", font=(GENERAL_FONT, TITLE_FONT_SIZE))
        self.title.grid(row=0, column=0, pady=10, padx=10)

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



# class CardFrame(Ctk.CTkFrame):
#     def __init__(self, parent, server_api, child_data, *args, **kwargs):
#         self.server_api = server_api
#         super().__init__(parent, *args, **kwargs)
#         self.grid(sticky=STICKY_LAYOUT)    
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)
        
#         self.title = Ctk.CTkLabel(self, text=child_data[0], font=(GENERAL_FONT, 30))
#         self.title.grid(
#             row=0, column=0, 
#             pady=LOGIN_Y_PADDING, 
#             padx=LOGIN_X_PADDING)
        
#         self.name = Ctk.CTkLabel(self, text="STATS", font=(GENERAL_FONT, 20))
#         self.name.grid(
#             row=1, column=0, 
#             pady=LOGIN_Y_PADDING,
#             padx=LOGIN_X_PADDING)

# class DashboardFrame(Ctk.CTkFrame):
#     def __init__(self, parent, server_api, *args, **kwargs):
#         self.parent = parent
#         self.server_api = server_api
#         super().__init__(parent, *args, **kwargs)
#         self.grid(sticky=STICKY_LAYOUT)
#         self.grid_columnconfigure(0, weight=1)

#         self.title = Ctk.CTkLabel(self, text="Dashboard", font=(GENERAL_FONT, TITLE_FONT_SIZE))
#         self.title.grid(row=0, column=0, pady=10, padx=10)

#         self.server_api.get_children()

#         self.cards = []
#         max_cards_per_row = 4
#         card_width = 600  # Adjust according to your card size
#         card_height = 250  # Adjust according to your card size
#         row_height = card_height + 20  # Adjust vertical spacing between rows
#         total_cards = len(self.server_api.children)
#         num_full_rows = total_cards // max_cards_per_row
#         remaining_cards = total_cards % max_cards_per_row
#         x_offset_first_row = ((SCREEN_WIDTH - max_cards_per_row * card_width) / 2 ) + 40
#         x_offset_subsequent_rows = ((SCREEN_WIDTH - remaining_cards * card_width) / 2 ) + 40 if remaining_cards else x_offset_first_row
#         y_offset = -100  # Adjust vertical offset as needed
#         for i, child_data in enumerate(self.server_api.children):
#             row = i // max_cards_per_row + 1
#             column = i % max_cards_per_row
#             x_offset = x_offset_first_row if row == 1 else x_offset_subsequent_rows
#             x_pos = x_offset + column * card_width
#             y_pos = y_offset + row * row_height
#             card = CardFrame(self.parent, self.server_api, child_data, width=card_width, height=card_height)
#             card.place(x=x_pos, y=y_pos)
#             self.cards.append(card)






class CardFrame(Ctk.CTkFrame):
    def __init__(self, parent, server_api, child_data, *args, **kwargs):
        self.server_api = server_api
        super().__init__(parent, *args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.default_fg_color = "dark gray"
        
        self.title = Ctk.CTkLabel(self, text=child_data[0], font=(GENERAL_FONT, 30))
        self.title.grid(row=0, column=0, pady=10, padx=50, columnspan=3)
        
        self.name = Ctk.CTkLabel(self, text="STATS", font=(GENERAL_FONT, 20))
        self.name.grid(row=1, column=0, pady=10, padx=50)

        self.stat1 = Ctk.CTkLabel(self, text="Stat 1", font=(GENERAL_FONT, 15))
        self.stat1.grid(row=2, column=0, pady=10, padx=50)
        self.stat2 = Ctk.CTkLabel(self, text="Stat 2", font=(GENERAL_FONT, 15))
        self.stat2.grid(row=2, column=1, pady=10, padx=50)
        self.stat3 = Ctk.CTkLabel(self, text="Stat 3", font=(GENERAL_FONT, 15))
        self.stat3.grid(row=2, column=2, pady=10, padx=50)

        self.view_button = Ctk.CTkButton(self, text="View", command=self.view_child, width=300, height=30, font=(GENERAL_FONT, 20))
        self.view_button.grid(row=3, column=0, pady=10, padx=50, columnspan=3)


        self.bind("<Button-1>", self.on_card_click)

    def on_card_click(self, event):
        print(f"Card {self.title.cget('text')} clicked")

    def view_child(self):
        print(f"Viewing child {self.title.cget('text')}")


        

class AddChildFrame(Ctk.CTkFrame):
    def __init__(self, server_api, *args, **kwargs):
        self.server_api = server_api
        super().__init__(*args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.title = Ctk.CTkLabel(self, text="Add Child", font=(GENERAL_FONT, 30))
        self.title.grid(
            row=0, column=0, 
            pady=LOGIN_Y_PADDING, 
            padx=LOGIN_X_PADDING)
        
        self.name = Ctk.CTkEntry(self, placeholder_text="Name", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.name.grid(
            row=1, column=0, 
            pady=LOGIN_Y_PADDING,
            padx=LOGIN_X_PADDING)
        
        self.age = Ctk.CTkEntry(self, placeholder_text="Age", width=ENTRY_WIDTH, height=ENTRY_HEIGHT, font=ENTRY_FONT)
        self.age.grid(
            row=2, column=0, 
            pady=LOGIN_Y_PADDING,
            padx=LOGIN_X_PADDING)
        
        self.add_child = Ctk.CTkButton(self, text="Add Child", command=self.add_child, width=LOGIN_BTN_WIDTH, height=LOGIN_BTN_HEIGHT, font=LOGIN_BTN_FONT)
        self.add_child.grid(row=3, column=0, 
                        pady=LOGIN_Y_PADDING,
                        padx=LOGIN_X_PADDING)

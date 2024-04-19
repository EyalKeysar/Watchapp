import tkinter as tk
from typing import Tuple
import customtkinter as Ctk
from .consts import *
from PIL import Image, ImageTk
import math

# class DashboardFrame(Ctk.CTkFrame):
#     def __init__(self, parent, server_api, *args, **kwargs):
#         self.parent = parent
#         self.server_api = server_api
#         super().__init__(parent, *args, **kwargs)
#         self.grid(sticky=STICKY_LAYOUT)    
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)
        
#         self.title = Ctk.CTkLabel(self, text="Dashboard", font=(GENERAL_FONT, TITLE_FONT_SIZE))
#         self.title.grid(
#             row=1, column=0, 
#             pady=LOGIN_Y_PADDING, 
#             padx=LOGIN_X_PADDING)
        
#         # ! Get cards (fetch children data) from server

#         self.server_api.get_children()

#         self.cards = []
#         for i in range(len(self.server_api.children)):
#             print(i)
#             self.cards.append(CardFrame(self.parent, self.server_api, self.server_api.children[i]))
#             self.cards[i].grid(row=2, column=i, pady=LOGIN_Y_PADDING, padx=LOGIN_X_PADDING)
# class DashboardFrame(Ctk.CTkFrame):
#     def __init__(self, parent, server_api, *args, **kwargs):
#         self.parent = parent
#         self.server_api = server_api
#         super().__init__(parent, *args, **kwargs)
#         self.grid(sticky=STICKY_LAYOUT)    
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)
        
#         self.title = Ctk.CTkLabel(self, text="Dashboard", font=(GENERAL_FONT, TITLE_FONT_SIZE))
#         self.title.grid(row=0, column=0, pady=10, padx=10)
        
#         self.server_api.get_children()

#         self.cards = []
#         for i, child_data in enumerate(self.server_api.children):
#             card = CardFrame(self.parent, self.server_api, child_data)
#             card.grid(row=1, column=i, pady=10, padx=10)
#             card.place(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)  # Example placement using place
#             self.cards.append(card)
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
#         card_width = 200  # Adjust according to your card size
#         card_height = 150  # Adjust according to your card size
#         for i, child_data in enumerate(self.server_api.children):
#             row = i // max_cards_per_row + 1
#             column = i % max_cards_per_row
#             x_offset = (SCREEN_WIDTH - max_cards_per_row * card_width) / 2  # Center cards horizontally
#             y_offset = 50  # Adjust vertical offset as needed
#             x_pos = x_offset + column * card_width
#             y_pos = y_offset + row * card_height
#             card = CardFrame(self.parent, self.server_api, child_data)
#             card.place(x=x_pos, y=y_pos)
#             self.cards.append(card)
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
        max_cards_per_row = 4
        card_width = 200  # Adjust according to your card size
        card_height = 150  # Adjust according to your card size
        row_height = card_height + 20  # Adjust vertical spacing between rows
        for i, child_data in enumerate(self.server_api.children):
            row = i // max_cards_per_row + 1
            column = i % max_cards_per_row
            x_offset = (SCREEN_WIDTH - min(len(self.server_api.children) - (row - 1) * max_cards_per_row, max_cards_per_row) * card_width) / 2
            y_offset = 50  # Adjust vertical offset as needed
            x_pos = x_offset + column * card_width
            y_pos = y_offset + row * row_height
            card = CardFrame(self.parent, self.server_api, child_data)
            card.place(x=x_pos, y=y_pos)
            self.cards.append(card)



class CardFrame(Ctk.CTkFrame):
    def __init__(self, parent, server_api, child_data, *args, **kwargs):
        self.server_api = server_api
        super().__init__(parent, *args, **kwargs)
        self.grid(sticky=STICKY_LAYOUT)    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.title = Ctk.CTkLabel(self, text="Card", font=(GENERAL_FONT, 30))
        self.title.grid(
            row=0, column=0, 
            pady=LOGIN_Y_PADDING, 
            padx=LOGIN_X_PADDING)
        
        self.name = Ctk.CTkLabel(self, text=child_data[0], font=(GENERAL_FONT, 20))
        self.name.grid(
            row=1, column=0, 
            pady=LOGIN_Y_PADDING,
            padx=LOGIN_X_PADDING)
        
        

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

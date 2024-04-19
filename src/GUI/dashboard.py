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
        pass

    def logout(self):
        pass





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

        self.active_status = Ctk.CTkLabel(self, text="Inactive", font=(GENERAL_FONT, 15),text_color="red")
        self.active_status.grid(row=0, column=2, pady=10)
        
        self.name = Ctk.CTkLabel(self, text="Statistics", font=(GENERAL_FONT, 20))
        self.name.grid(row=1, column=0, pady=10, padx=50, columnspan=3)

        self.stat1 = Ctk.CTkLabel(self, text="Stat 1", font=(GENERAL_FONT, 15))
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

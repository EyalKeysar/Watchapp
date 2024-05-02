import tkinter as tk

class CustomScrolledListbox(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.listbox = tk.Listbox(self, **kwargs)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def insert(self, index, *elements):
        self.listbox.insert(index, *elements)

    def delete(self, first, last=None):
        self.listbox.delete(first, last)

    def get(self, first, last=None):
        return self.listbox.get(first, last)

    def size(self):
        return self.listbox.size()

    def bind(self, event, handler):
        self.listbox.bind(event, handler)

    def set_bg_color(self, color):
        self.listbox.config(bg=color)
import tkinter as tk
from db import DB
from config import TITLE, WINDOWS
from datetime import datetime


class NotesApp:
    def __init__(self, root):
        self.db = DB()
        self.root = root
        self.root.title(TITLE)
        self.root.geometry(WINDOWS)

        self.create_widgets()


    def create_widgets(self):
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        self.add_button = tk.Button(self.list_frame, text='Добавить заметку', command=self.add_note)
        self.add_button.pack(fill=tk.X,pady=5)

        self.delete_button = tk.Button(self.list_frame, text='Удалить заметку', command=self.delete_note,state=tk.DISABLED)
        self.delete_button.pack(fill=tk.X,pady=5)
    def delete_note(self):
        pass
    def add_note(self):
        pass

a = tk.Tk()
note = NotesApp(a)
a.mainloop()
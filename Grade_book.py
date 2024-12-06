import sqlite3 as sql
import tkinter as tk
from tkinter import *

class Grade_book:
    def __init__(self):
        self.pesel = ""
        self.password = ""

    def set_pesel(self, pesel):
        self.pesel = pesel
        print(self.pesel)

    def set_password(self, password):
        self.password = password
        print(self.password)
    def create_grade_book(self):
        root = tk.Tk()
        root.title("Dzienniczek")
        root.geometry("400x200")
        tk.Label(root, text=f"Dzienniczek ucznia o peselu {self.pesel}", padx=20).pack(pady=20)
        root.mainloop()




import sqlite3 as sql
import tkinter as tk
from tkinter import *
from Grade_book import Grade_book

class Login_Window:
    def __init__(self, grade_book):
        self.Rank = ""
        self.Pesel = 0
        self.Pass = ""
        self.grade_book = grade_book

    def create_login_window(self):
        def submit():
            user_login = login.get()
            user_password = password.get()
            self.grade_book.set_pesel(user_login)
            self.grade_book.set_password(user_password)
            root.destroy()
            self.grade_book.create_grade_book()
            return user_login, user_password

        root = tk.Tk()
        root.title("Logowanie do dzienniczka")
        root.geometry("400x200")

        logowanie = tk.Frame(root)
        logowanie.pack(pady=20)
        tk.Label(logowanie, text="Podaj login:", padx=20).pack(side=LEFT)
        login = tk.Entry(logowanie)
        login.pack(side=LEFT)

        password_frame = tk.Frame(root)
        password_frame.pack(pady=20)
        tk.Label(password_frame, text="Podaj hasło:", padx=20).pack(side=LEFT)
        password = tk.Entry(password_frame)
        password.pack(side=LEFT)

        submit_button = tk.Button(root, text="Zaloguj", command=submit, pady=10, padx=20)
        submit_button.pack(pady=20)
        root.mainloop()

    def data_test(self):
        con = sql.connect('Database.db')
        cur = con.cursor()

        query = "SELECT COUNT(1) FROM dbo.uczniowie WHERE PESEL = ? AND Haslo = ?"
        cur.execute(query, (self.Pesel, self.Pass))

        result = cur.fetchone()
        if result[0] == 1:
            self.Rank = "Uczeń"
            print("Login successful")
        else:
            print("Login failed")

        con.close()
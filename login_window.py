import sqlite3 as sql
import tkinter as tk
from tkinter import messagebox

class Login_Window:
    def __init__(self, grade_book):
        self.Rank = ""
        self.Pesel = ""
        self.Pass = ""
        self.grade_book = grade_book

    def create_login_window(self):
        def submit(root):
            self.Pesel = login.get()
            self.Pass = password.get()

            if self.data_test():
                self.grade_book.set_pesel(self.Pesel)
                self.grade_book.set_password(self.Pass)
                self.grade_book.set_rank(self.Rank)
                root.destroy()
                self.grade_book.create_grade_book()
            else:
                tk.messagebox.showerror("Login failed", "Invalid PESEL or password")

        root = tk.Tk()
        root.title("Logowanie do dzienniczka")
        root.geometry("400x200")

        logowanie = tk.Frame(root)
        logowanie.pack(pady=20)
        tk.Label(logowanie, text="Podaj login:", padx=20).pack(side=tk.LEFT)
        login = tk.Entry(logowanie)
        login.pack(side=tk.LEFT)

        password_frame = tk.Frame(root)
        password_frame.pack(pady=20)
        tk.Label(password_frame, text="Podaj hasło:", padx=20).pack(side=tk.LEFT)
        password = tk.Entry(password_frame, show="*")
        password.pack(side=tk.LEFT)

        submit_button = tk.Button(root, text="Zaloguj", command=lambda: submit(root), pady=10, padx=20)
        submit_button.pack(pady=20)
        root.mainloop()

    def data_test(self):
        con = sql.connect('Database.db')
        cur = con.cursor()
        try:
            query = "SELECT COUNT(1) FROM uczen WHERE PESEL = ? AND Haslo = ?"
            cur.execute(query, (self.Pesel, self.Pass))
            self.Rank = "uczen"
            result = cur.fetchone()
            if result[0] == 1:
                return True
        except sql.Error as e:
            print(e)
            return False
        finally:
            con.close()
        con = sql.connect('Database.db')
        cur = con.cursor()
        try:
            query = "SELECT COUNT(1) FROM nauczyciel WHERE PESEL = ? AND haslo = ?"
            cur.execute(query, (self.Pesel, self.Pass))
            self.Rank = "nauczyciel"
            result = cur.fetchone()
            return result[0] == 1
        except sql.Error as e:
            print(e)
            return False
        finally:
            con.close()
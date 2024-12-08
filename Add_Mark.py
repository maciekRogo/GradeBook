import tkinter as tk
import sqlite3 as sql
from tkinter import ttk

class Mark:
    def __init__(self):
        self.pesel = ""


    def get_student_pesel(self, pesel):
        self.pesel = pesel
        print(self.pesel)
    def create_mark_window(self):
        root = tk.Tk()
        root.title("Dodawanie oceny")
        root.geometry("400x200")
        con = sql.connect("Database.db")
        subjects = []
        query = "SELECT nazwa FROM przedmiot"
        cur = con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        for i in result:
            subjects.append(i[0])
        combobox = ttk.Combobox(root, values=subjects, state="readonly")
        combobox.set("Wybierz przedmiot")
        combobox.pack(pady=20)
        def validate_grade(new_value):
            return new_value=="" or new_value == "-" or new_value == "+" or new_value == "1" or new_value == "2" or new_value == "3" or new_value == "4" or new_value == "5" or new_value == "6"
        validate_command = (root.register(validate_grade),"%P")
        student_grade = tk.Entry(root,validate="key", validatecommand=validate_command)
        student_grade.pack(pady=20)
        def submit():
            if combobox.get() == "Wybierz przedmiot" or student_grade.get() == "":
                tk.messagebox.showerror("Błąd", "Proszę wybrać przedmiot i wpisać ocenę")
                return
            query = "SELECT id FROM przedmiot WHERE nazwa = ?"
            cur.execute(query, (combobox.get(),))
            subject_id = cur.fetchone()[0]
            query = "INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (?, ?, ?)"
            cur.execute(query, (subject_id, self.pesel, student_grade.get()))
            con.commit()
            print("Ocena dodana")
            root.destroy()
            tk.messagebox.showinfo("Ocena", "Ocena została dodana")

        submit_button = tk.Button(root, text="Dodaj ocenę", command=submit)
        submit_button.pack(pady=20)
        root.mainloop()


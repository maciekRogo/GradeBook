import tkinter as tk
from os.path import exists
from tkinter import ttk
import sqlite3 as sql


class Grade_book:
    def __init__(self, points,grades):
        self.pesel = ""
        self.password = ""
        self.rank = ""
        self.name = ""
        self.surename = ""
        self.con = None
        self.cur = None
        self.points = points
        self.grades = grades
        self.root = None

    def set_pesel(self, pesel):
        self.pesel = pesel

    def set_password(self, password):
        self.password = password

    def set_rank(self, rank):
        self.rank = rank

    def create_grade_book(self):
        root = tk.Tk()
        root.title("Dzienniczek")
        root.geometry("600x400")
        self.con = sql.connect('Database.db')
        self.cur = self.con.cursor()

        def add_points(student_pesel):
            self.points.get_student_pesel(student_pesel)
            self.points.create_points_window()

        def add_student_grade(student_pesel):
            self.grades.get_student_pesel(student_pesel)
            self.grades.create_mark_window()

        if self.rank == "uczen":
            query = "SELECT imie,nazwisko,pkt FROM uczen WHERE PESEL = ?"
            self.cur.execute(query, (self.pesel,))
            result = self.cur.fetchall()
            self.name = result[0][0]
            self.surename = result[0][1]
            name_surename = tk.Label(root, text=f"Witaj {self.name} {self.surename}", font=("Arial", 16))
            name_surename.place(x=10, y=10)
            pkt = tk.Label(root, text=f"Twoje punkty: {result[0][2]}", font=("Arial", 10))
            pkt.place(x=10, y=40)
            grades = tk.Label(root, text="Twoje oceny:", font=("Arial", 14))
            grades.place(x=10, y=70)
            query = "SELECT ocena.ocena, przedmiot.nazwa FROM ocena JOIN przedmiot ON ocena.id_przedmiotu = przedmiot.id WHERE ocena.id_ucznia = ?"
            self.cur.execute(query, (self.pesel,))
            result = self.cur.fetchall()
            student_grades = {}
            y = 100
            for i in result:
                if i[1] in student_grades:
                    student_grades[i[1]].append(i[0])
                else:
                    student_grades[i[1]] = [i[0]]
            for key in student_grades:
                oceny = student_grades[key]
                oceny = [str(i) for i in oceny]
                oceny = ", ".join(oceny)
                oceny_label = tk.Label(root, text=f"{key}: {oceny}", font=("Arial", 10))
                oceny_label.place(x=10, y=y)
                y += 20

        elif self.rank == "nauczyciel":
            query = "SELECT imie,nazwisko FROM nauczyciel WHERE PESEL = ?"
            self.cur.execute(query, (self.pesel,))
            result = self.cur.fetchall()
            self.name = result[0][0]
            self.surename = result[0][1]
            name_surename = tk.Label(root, text=f"Witaj {self.name} {self.surename}", font=("Arial", 16))
            name_surename.place(x=10, y=10)
            grades = tk.Label(root, text="Twoje klasy:", font=("Arial", 14))
            grades.place(x=10, y=40)

            tree = ttk.Treeview(root)
            tree.heading("#0", text="Klasy")
            tree.place(x=10, y=70, width=300, height=360)

            # Populate the Treeview with classes
            self.cur.execute("SELECT id FROM klasa WHERE wychowawca_id = ?", (self.pesel,))
            classes = self.cur.fetchall()
            for klasa in classes:
                tree.insert("", "end", klasa[0], text=klasa[0])

            def on_class_click(event):
                selected_item = tree.selection()[0]
                for child in tree.get_children(selected_item):
                    tree.delete(child)
                self.cur.execute("SELECT PESEL, imie, nazwisko FROM uczen WHERE klasa = ?", (selected_item,))
                students = self.cur.fetchall()
                for student in students:
                    student_id = student[0]
                    tree.insert(selected_item, "end", student_id, text=f"{student[1]} {student[2]}")

            def on_student_click(event):
                selected_item = tree.selection()[0]
                self.cur.execute("SELECT * FROM uczen WHERE PESEL = ?", (selected_item,))
                student_data = self.cur.fetchone()
                y = 70
                for widget in root.winfo_children():
                    if isinstance(widget, tk.Label) and widget.winfo_y() >= 70:
                        widget.destroy()
                if student_data:
                    student_pesel = student_data[0]
                    student_name = student_data[1]
                    student_surename = student_data[2]
                    student_points = student_data[3]
                    student_class = student_data[5]
                    student_info = tk.Label(root, text=f"{student_name} {student_surename}  {student_class}",
                                            font=("Arial", 17))
                    student_info.place(x=320, y=70)
                    student_info = tk.Label(root, text=f"Pesel: {student_pesel}", font=("Arial", 10))
                    student_info.place(x=320, y=95)
                    student_info = tk.Label(root, text=f"Punkty: {student_points}", font=("Arial", 10))
                    student_info.place(x=320, y=120)
                    Student_grades = tk.Label(root, text="Oceny:", font=("Arial", 14))
                    Student_grades.place(x=320, y=150)
                    query = "SELECT ocena.ocena, przedmiot.nazwa FROM ocena JOIN przedmiot ON ocena.id_przedmiotu = przedmiot.id WHERE ocena.id_ucznia = ?"
                    self.cur.execute(query, (student_pesel,))
                    result = self.cur.fetchall()
                    student_grades = {}
                    y = 180
                    for i in result:
                        if i[1] in student_grades:
                            student_grades[i[1]].append(i[0])
                        else:
                            student_grades[i[1]] = [i[0]]
                    for key in student_grades:
                        oceny = student_grades[key]
                        oceny = [str(i) for i in oceny]
                        oceny = ", ".join(oceny)
                        oceny_label = tk.Label(root, text=f"{key}: {oceny}", font=("Arial", 10))
                        oceny_label.place(x=320, y=y)
                        y += 20

                    add_point = tk.Button(root, text="Zmień punkty", font=("Arial", 10), height=2, width=15,
                                          command=lambda: add_points(student_pesel))
                    add_point.place(x=320, y=350)
                    add_grade_button = tk.Button(root, text="Dodaj ocenę", font=("Arial", 10), height=2, width=15,
                                                 command=lambda: add_student_grade(student_pesel))
                    add_grade_button.place(x=450, y=350)

            tree.bind("<<TreeviewSelect>>", on_class_click)
            tree.bind("<Double-1>", on_student_click)
        root.mainloop()
        self.con.close()
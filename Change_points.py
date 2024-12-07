import tkinter as tk
import sqlite3 as sql

class Points:
    def __init__(self):
        self.pesel = ""

    def get_student_pesel(self, pesel):
        self.pesel = pesel
        print(self.pesel)

    def create_points_window(self):
        root = tk.Tk()
        root.title("Punkty")
        root.geometry("400x200")
        root.title("Zmienianie punktów")
        con = sql.connect('Database.db')
        cur = con.cursor()
        query = "SELECT imie, nazwisko, pkt FROM uczen WHERE PESEL = ?"
        cur.execute(query, (self.pesel,))
        result = cur.fetchall()
        pkt = tk.Label(root, text=f"Punkty {result[0][0]} {result[0][1]}:\n {result[0][2]}", font=("Arial", 16))

        def add_points(amount):
            query = "UPDATE uczen SET pkt = pkt + ? WHERE PESEL = ?"
            cur.execute(query, (amount, self.pesel))
            con.commit()
            print("Punkty dodane")
            root.destroy()
            tk.messagebox.showinfo("Punkty", "Punkty zostały dodane")

        def delete_points(amount):
            query = "UPDATE uczen SET pkt = pkt - ? WHERE PESEL = ?"
            cur.execute(query, (amount, self.pesel))
            con.commit()
            print("Punkty usunięte")
            root.destroy()
            tk.messagebox.showinfo("Punkty", "Punkty zostały usunięte")

        def validate(new_value):
            return new_value.isdigit() or new_value == ""

        validate_command = root.register(validate)
        quantity = tk.Entry(root, validate="key", validatecommand=(validate_command, '%P'))
        quantity.place(x=100, y=75, width=200)

        add = tk.Button(root, text="Dodaj punkty", command=lambda: add_points(int(quantity.get())))
        add.place(x=100, y=100)
        delete = tk.Button(root, text="Usuń punkty", command=lambda: delete_points(int(quantity.get())))
        delete.place(x=200, y=100)

        pkt.pack(pady=20)
        root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root, con))
        root.mainloop()

    def on_closing(self, root, con):
        con.close()
        root.destroy()

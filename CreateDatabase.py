import sqlite3 as sql

con = sql.connect("Database.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS ocena(
            id_przedmiotu INTEGER NOT NULL,
            id_ucznia INTEGER NOT NULL,
            ocena INTEGER NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            FOREIGN KEY(id_przedmiotu) REFERENCES przedmiot(id),
            FOREIGN KEY(id_ucznia) REFERENCES uczen(pesel)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS uczen(
            pesel INTEGER PRIMARY KEY,
            imie TEXT NOT NULL,
            nazwisko TEXT NOT NULL,
            pkt INTEGER NOT NULL,
            haslo TEXT NOT NULL,
            klasa TEXT NOT NULL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS klasa(
            id TEXT,
            wychowawca_id TEXT,
            FOREIGN KEY (wychowawca_id) REFERENCES nauczyciel(PESEL),
            FOREIGN KEY (id) REFERENCES uczen(klasa)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS nauczyciel(
            PESEL TEXT PRIMARY KEY NOT NULL,
            imie TEXT NOT NULL,
            nazwisko TEXT NOT NULL,
            haslo TEXT NOT NULL,
            sala INTEGER NOT NULL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS przedmiot(
            nazwa TEXT NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nauczyciel_id TEXT NOT NULL,
            FOREIGN KEY(nauczyciel_id) REFERENCES nauczyciel(PESEL)
           )''')
# Insert values into the ocena table
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (1, 12345678901, 5)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (2, 23456789012, 4)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (3, 23456789012, 1)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (5, 12345678901, 3)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (4, 23456789012, 6)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (2, 12345678901, 1)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (1, 12345678901, 5)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (2, 23456789012, 4)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (3, 23456789012, 1)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (5, 12345678901, 3)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (4, 23456789012, 6)")
cur.execute("INSERT INTO ocena (id_przedmiotu, id_ucznia, ocena) VALUES (2, 12345678901, 1)")

#Insert values into the uczen table
cur.execute("INSERT INTO uczen (pesel, imie, nazwisko, pkt, haslo, klasa) VALUES (12345678901, 'Jan', 'Kowalski', 85, 'password1', '1A')")
cur.execute("INSERT INTO uczen (pesel, imie, nazwisko, pkt, haslo, klasa) VALUES (12345678928, 'Adam', 'Nawałka', 123, 'password1', '1A')")
cur.execute("INSERT INTO uczen (pesel, imie, nazwisko, pkt, haslo, klasa) VALUES (12345678777, 'Robert', 'Lewandowski', 238, 'password1', '1A')")
cur.execute("INSERT INTO uczen (pesel, imie, nazwisko, pkt, haslo, klasa) VALUES (12345678234, 'Wojciech', 'Szczęsny', 15, 'password1', '1A')")
cur.execute("INSERT INTO uczen (pesel, imie, nazwisko, pkt, haslo, klasa) VALUES (23456789012, 'Anna', 'Nowak', 90, 'password2', '2B')")
cur.execute("INSERT INTO uczen (pesel, imie, nazwisko, pkt, haslo, klasa) VALUES (23456789013, 'Jan', 'Nowak', 110, 'password3', '3B')")

# Insert values into the klasa table
cur.execute("INSERT INTO klasa (id, wychowawca_id) VALUES ('1A', '12345678901')")
cur.execute("INSERT INTO klasa (id, wychowawca_id) VALUES ('2B', '23456789012')")

# Insert values into the nauczyciel table
cur.execute("INSERT INTO nauczyciel (PESEL, imie, nazwisko, haslo, sala) VALUES ('12345678901', 'Adam', 'Mickiewicz', 'password3', 101)")
cur.execute("INSERT INTO nauczyciel (PESEL, imie, nazwisko, haslo, sala) VALUES ('23456789012', 'Maria', 'Sklodowska', 'password4', 102)")

# Insert values into the przedmiot table
cur.execute("INSERT INTO przedmiot (nazwa, nauczyciel_id) VALUES ('Matematyka', '12345678901')")
cur.execute("INSERT INTO przedmiot (nazwa, nauczyciel_id) VALUES ('Fizyka', '23456789012')")
cur.execute("INSERT INTO przedmiot (nazwa, nauczyciel_id) VALUES ('Polski', '23456789012')")
cur.execute("INSERT INTO przedmiot (nazwa, nauczyciel_id) VALUES ('WF', '12345678901')")
cur.execute("INSERT INTO przedmiot (nazwa, nauczyciel_id) VALUES ('Angielski', '12345678901')")

con.commit()
con.close()
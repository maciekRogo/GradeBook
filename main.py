import sqlite3 as sql
import tkinter as tk
from tkinter import *
from login_window import Login_Window
from Grade_book import Grade_book

Grade_book_window = Grade_book()
Login_Window_main = Login_Window(Grade_book_window)
Login_Window_main.create_login_window()
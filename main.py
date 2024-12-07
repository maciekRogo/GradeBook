from login_window import Login_Window
from Grade_book import Grade_book
from Change_points import Points
from Add_Mark import Mark
points = Points()
grades = Mark()
Grade_book_window = Grade_book(points,grades)
Login_Window_main = Login_Window(Grade_book_window)
Login_Window_main.create_login_window()

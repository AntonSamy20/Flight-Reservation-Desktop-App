import sqlite3
from tkinter import *
from database import *

login = Tk()
login.title("Login")
login.geometry("500x500+400+80")
login.minsize(400, 400)
login.config(background="#F8F9FA")

# title
title = Label(
    login, 
    text="Flight Reservation\nLogin", 
    font=("Segoe UI", 22, "bold"), 
    fg="#2C3E50", 
    bg="#F8F9FA",
    justify="center"
)
title.pack(pady=40)

# frame
form_frame = Frame(login, bg="#F8F9FA")
form_frame.pack(pady=20)

# Username
username_label = Label(form_frame, text="👤 Username:", 
                       font=("Segoe UI", 12), bg="#F8F9FA")
username_label.grid(row=0, column=0, sticky="w", pady=10, padx=10)

username_entry = Entry(form_frame, font=("Segoe UI", 12), width=28, relief="solid", bd=1)
username_entry.grid(row=0, column=1, pady=10, padx=10)

# Password
password_label = Label(form_frame, text="🔑 Password:", 
                       font=("Segoe UI", 12), bg="#F8F9FA")
password_label.grid(row=1, column=0, sticky="w", pady=10, padx=10)

password_entry = Entry(form_frame, font=("Segoe UI", 12), width=28, show="*", relief="solid", bd=1)
password_entry.grid(row=1, column=1, pady=10, padx=10)

# button
btn_frame = Frame(login, bg="#F8F9FA")
btn_frame.pack(pady=30)

sign_in_btn = Button(btn_frame, text="Sign In", 
                     font=("Segoe UI", 12, "bold"), 
                     width=12, bg="#27AE60", fg="white", relief="flat", justify="center")
sign_in_btn.grid(row=0, column=0, padx=15)

register = Label(login, text="register now!", font=("Segoe UI", 10, "underline"), 
                       fg="#2980B9", bg="#F8F9FA")
register.pack(pady=5)


login.mainloop()

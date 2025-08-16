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

username = Entry(form_frame, font=("Segoe UI", 12), width=28, relief="solid", bd=1)
username.grid(row=0, column=1, pady=10, padx=10)

# Password
password_label = Label(form_frame, text="🔑 Password:", 
                       font=("Segoe UI", 12), bg="#F8F9FA")
password_label.grid(row=1, column=0, sticky="w", pady=10, padx=10)

password = Entry(form_frame, font=("Segoe UI", 12), width=28, show="*", relief='solid' , bd=1)
password.grid(row=1, column=1, pady=10, padx=10)


# button
btn_frame = Frame(login, bg="#F8F9FA")
btn_frame.pack(pady=10)

sign_in_btn = Button(btn_frame, text="Sign In", 
                     font=("Segoe UI", 12, "bold"), 
                     width=12, bg="#27AE60", fg="white", relief="flat", justify="center")
sign_in_btn.grid(row=0, column=0, padx=15)

# login function to check user and password
login_msg = Label(login, text="", bg="#F8F9FA", font=("Segoe UI", 12))
login_msg.pack(pady=10)

def login_user():
    username_val = username.get()
    password_val = password.get()
    if check_user(username_val, password_val):
        login_msg.config(text="Login successful!", fg="green")
    else:
        login_msg.config(text="Invalid username or password!", fg="red")

sign_in_btn.config(command=login_user)

# register line 
to_register = Label(login, text="register now!", font=("Segoe UI", 10, "underline"), 
                       fg="#2980B9", bg="#F8F9FA")
to_register.pack(pady=0)

def open_register():
    register = Toplevel(login)
    register.title("Register")
    register.geometry("400x300+450+120")
    register.config(background="#F8F9FA")

    Label(register, text="Create Account", font=("Segoe UI", 16, "bold"),
          bg="#F8F9FA").pack(pady=20)

    Label(register, text="Username:", bg="#F8F9FA").pack()
    new_username = Entry(register, width=25)
    new_username.pack(pady=5)
    Label(register, text="Password:", bg="#F8F9FA").pack()
    new_password = Entry(register, width=25)
    new_password.pack(pady=5)

    def register_user():
        username_val = new_username.get()
        password_val = new_password.get()
        if add_user(username_val, password_val):
            msg = Label(register, text="Account created successfully!", fg="green", bg="#F8F9FA").pack()
            register.after(2000, register.destroy)
        else:
            msg = Label(register, text="Username already exists!", fg="red", bg="#F8F9FA").pack()

    Button(register, text="Register", bg="#2980B9", fg="white", command=register_user).pack(pady=20)
    
to_register.bind("<Button-1>", lambda e: open_register())
login.mainloop()

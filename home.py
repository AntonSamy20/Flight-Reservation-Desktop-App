from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Flight Reservation")
root.geometry("500x500+400+80")
root.minsize(400, 400)

root.config(background="#F8F9FA")

title = Label(root, 
              text="✈ Flight Reservation App", 
              font=("Segoe UI", 20, "bold"), 
              fg="#2C3E50", 
              bg="#F8F9FA")
title.pack(pady=50)

btn_frame = Frame(root, bg="#F8F9FA")
btn_frame.pack(pady=40)

def book_flight():
    messagebox.showinfo("Book Flight", "Redirecting to booking page...")

def view_reservations():
    messagebox.showinfo("Reservations", "Showing your reservations...")

def make_button(master, text, bg, command):
    btn = Button(master,
                 text=text,
                 font=("Segoe UI", 14, "bold"),
                 width=20,
                 height=2,
                 bg=bg,
                 fg="white",
                 relief="flat",
                 cursor="hand2",
                 command=command)
    def on_enter(e): btn.config(bg="#C4D9EE")
    def on_leave(e): btn.config(bg=bg)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

book = make_button(btn_frame, "Book a Flight", "#27AE60", book_flight)
book.pack(pady=15)

view = make_button(btn_frame, "View Reservations", "#2980B9", view_reservations)
view.pack(pady=15)

root.mainloop()

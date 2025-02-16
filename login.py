import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # inserting the username and password
    if username == ".\ admin" and password == "Nkosi2001!":
        messagebox.showinfo("Login Successful", "Welcome, admin!/ Siyakwamukela mfethu.")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("iNKOSIKHONA SOLUTIONS https://inkosikhonasolutions.websites.co.in/")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="black")

# Create and place labels and entry fields
username_label = tk.Label(root, text="Username:", font=("Arial", 14), bg="black", fg="white")
username_label.pack(pady=(30, 10))

username_entry = tk.Entry(root, font=("Arial", 14), width=25)
username_entry.pack()

password_label = tk.Label(root, text="Password:", font=("Arial", 14), bg="black", fg="white")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 14), width=25)
password_entry.pack()

# Create and place buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

login_button = tk.Button(button_frame, text="Login", font=("Arial", 12), width=10, command=validate_login)
login_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), width=10, command=clear_fields)
clear_button.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()

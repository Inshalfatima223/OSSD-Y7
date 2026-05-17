import tkinter as tk
from tkinter import messagebox

USERS_FILE = "users.txt"

def read_file():
    users = {}
    try:
        with open(USERS_FILE, "r") as f:
            for line in f:
                user, pwd = line.strip().split(",")
                users[user] = pwd
    except FileNotFoundError:
        pass
    return users

def write_file(username, password):
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{password}\n")

def login():
    users = read_file()
    u, p = entry_user.get(), entry_pass.get()
    if users.get(u) == p:
        messagebox.showinfo("Success", f"Welcome, {u}!")
    else:
        messagebox.showerror("Error", "Invalid credentials.")

def signup():
    users = read_file()
    u, p = entry_user.get(), entry_pass.get()
    if u in users:
        messagebox.showerror("Error", "User already exists.")
    else:
        write_file(u, p)
        messagebox.showinfo("Success", "Account created!")

root = tk.Tk()
root.title("Login System")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Sign Up", command=signup).pack()

root.mainloop()
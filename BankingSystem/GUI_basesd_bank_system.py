import tkinter as tk
from tkinter import messagebox
import os
import json


USERS_DATABASE = "users_DB.json"

def load_users():
    if os.path.exists(USERS_DATABASE):
        with open(USERS_DATABASE,"r") as file:
            return json.load(file)
    return {}
def save_users(users):
    with open(USERS_DATABASE, "w") as file:
        json.dump(users, file, indent=4)

def save_user(username, password):
    users = load_users()
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        users[username] = {"password": password, "balance": 0, "transactions": []}
        with open(USERS_DATABASE, "w") as file:
            json.dump(users, file, indent=4)
        messagebox.showinfo("Success", "Registration successful! Please login.")
def deposit(username,amount_entry,balance_label):
    amount = amount_entry.get()
    if not amount.isdigit() or int(amount) <= 0:
        messagebox.showerror("Error", "Enter a valid amount")
        
    amount = int(amount)
    users = load_users()
    users[username]["balance"] += amount
    users[username]["transactions"].append(f"Deposited : ${amount}")
    save_users(users)
    
    balance_label.config(text=f"Balance: ${users[username]['balance']}")
    messagebox.showinfo("Success", f"${amount} Deposited!")

def withdraw(username, amount_entry, balance_label):
    amount = amount_entry.get()
    if not amount.isdigit() or int(amount) <= 0:
        messagebox.showerror("Error", "Enter a valid amount!")
        return

    amount = int(amount)
    users = load_users()
    
    if users[username]["balance"] < amount:
        messagebox.showerror("Error", "Insufficient balance!")
        return

    users[username]["balance"] -= amount
    users[username]["transactions"].append(f"Withdrew: ${amount}")
    save_users(users)

    balance_label.config(text=f"Balance: ${users[username]['balance']}")
    messagebox.showinfo("Success", f"${amount} Withdrawn!")



def open_dashboard(username):
    users = load_users()
    
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("300x300")

    tk.Label(dashboard, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=10)
    
    balance_label = tk.Label(dashboard, text=f"Balance: ${users[username]['balance']}", font=("Arial", 12))
    balance_label.pack(pady=5)

    tk.Label(dashboard, text="Enter amount:").pack()
    amount_entry = tk.Entry(dashboard)
    amount_entry.pack(pady=5)

    tk.Button(dashboard, text="Deposit", command=lambda: deposit(username, amount_entry, balance_label)).pack(pady=5)
    tk.Button(dashboard, text="Withdraw", command=lambda: withdraw(username, amount_entry, balance_label)).pack(pady=5)
    tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=20)

    dashboard.mainloop()
    
def login():
    username = entry_username.get()
    password = entry_password.get()
    users = load_users()
    
    if username in users and users[username]["password"] == password:
        messagebox.showinfo("Success", f"Welcome, {username}!")
        root.destroy()  # Close login window
        open_dashboard(username)  # Open the main dashboard
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Function to open the registration window
def open_register():
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("300x250")

    tk.Label(register_window, text="Username:").pack(pady=5)
    reg_username = tk.Entry(register_window)
    reg_username.pack(pady=5)

    tk.Label(register_window, text="Password:").pack(pady=5)
    reg_password = tk.Entry(register_window, show="*")
    reg_password.pack(pady=5)

    tk.Button(register_window, text="Register", command=lambda: save_user(reg_username.get(), reg_password.get())).pack(pady=10)
    
    
    # Main Login Window
root = tk.Tk()
root.title("Banking System")
root.geometry("350x250")

tk.Label(root, text="Username:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)
tk.Button(root, text="Register", command=open_register).pack(pady=5)

root.mainloop()
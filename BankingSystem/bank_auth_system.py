import tkinter as tk
from tkinter import messagebox
import json
import os





USER_DB = db_file = "users.json"

def load_users():
    if os.path.exists(db_file):
        with open(db_file, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(db_file, "w") as file:
        json.dump(users, file, indent=4)

def register_user(username, password):
    users = load_users()
    if username in users:
        print("❌ Username already exists!")
        return False
    users[username] = {"password": password, "balance": 0}
    save_users(users)
    print("✅ Registration successful!")
    return True

def login_user(username, password):
    users = load_users()
    if username in users and users[username]["password"] == password:
        print("✅ Login successful!")
        return username
    print("❌ Invalid username or password!")
    return None

def deposit(username, amount):
    users = load_users()
    if username:
        users[username]["balance"] += amount
        save_users(users)
        print(f"💰 Deposited ${amount}. New balance: ${users[username]['balance']}")
    else:
        print("❌ You must be logged in to deposit!")

def withdraw(username, amount):
    users = load_users()
    if username and users[username]["balance"] >= amount:
        users[username]["balance"] -= amount
        save_users(users)
        print(f"💸 Withdrawn ${amount}. Remaining balance: ${users[username]['balance']}")
    else:
        print("❌ Insufficient funds or not logged in!")

def transfer(users, sender, receiver, amount):
    if not sender:
        print("❌ You must be logged in to transfer money!")
        return
    if receiver not in users:
        print("❌ Receiver does not exist!")
        return
    if users[sender]["balance"] < amount:
        print("❌ Insufficient funds!")
        return
    users[sender]["balance"] -= amount
    users[receiver]["balance"] += amount
    save_users(users)
    print(f"✅ ${amount} transferred from {sender} to {receiver}.")

session = None
users = load_users()

while True:
    print("\n1. Register\n2. Login\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Logout\n7. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        register_user(uname, pwd)
    elif choice == "2":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        session = login_user(uname, pwd)
    elif choice == "3":
        if session:
            amt = float(input("Enter amount to deposit: "))
            deposit(session, amt)
        else:
            print("❌ You must be logged in to deposit!")
    elif choice == "4":
        if session:
            amt = float(input("Enter amount to withdraw: "))
            withdraw(session, amt)
        else:
            print("❌ You must be logged in to withdraw!")
    elif choice == "5":
        if session:
            receiver = input("Enter receiver's username: ")
            amt = float(input("Enter amount to transfer: "))
            transfer(users, session, receiver, amt)
        else:
            print("❌ You must be logged in to transfer money!")
    elif choice == "6":
        if session:
            print(f"👋 {session} logged out successfully.")
            session = None
        else:
            print("❌ No active session to logout!")
    elif choice == "7":
        print("🚪 Exiting system. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again!")

# Create the main window3

# def save_user(username, password):
#     users = load_users()
#     if username in users:
#         messagebox.showerror("Error", "Username already exists!")
#     else:
#         users[username] = {"password": password, "balance": 0, "transactions": []}
#         with open(USER_DB, "w") as file:
#             json.dump(users, file, indent=4)
#         messagebox.showinfo("Success", "Registration successful! Please login.")

# # Function to load user data
# def load_users():
#     if os.path.exists(USER_DB):
#         with open(USER_DB, "r") as file:
#             return json.load(file)
#     return {}

# # Function to handle login
# def login():
#     username = entry_username.get()
#     password = entry_password.get()
#     users = load_users()
    
#     if username in users and users[username]["password"] == password:
#         messagebox.showinfo("Success", f"Welcome, {username}!")
#         root.destroy()  # Close login window
#         open_dashboard(username)  # Open the main dashboard
#     else:
#         messagebox.showerror("Error", "Invalid username or password!")

# # Function to open the registration window
# def open_register():
#     register_window = tk.Toplevel(root)
#     register_window.title("Register")
#     register_window.geometry("300x250")

#     tk.Label(register_window, text="Username:").pack(pady=5)
#     reg_username = tk.Entry(register_window)
#     reg_username.pack(pady=5)

#     tk.Label(register_window, text="Password:").pack(pady=5)
#     reg_password = tk.Entry(register_window, show="*")
#     reg_password.pack(pady=5)

#     tk.Button(register_window, text="Register", command=lambda: save_user(reg_username.get(), reg_password.get())).pack(pady=10)

# # Function to open the user dashboard
# def open_dashboard(username):
#     dashboard = tk.Tk()
#     dashboard.title("Dashboard")
#     dashboard.geometry("300x200")

#     tk.Label(dashboard, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=20)
#     tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=20)
    
#     dashboard.mainloop()

# # Main Login Window
# root = tk.Tk()
# root.title("Banking System")
# root.geometry("350x250")

# tk.Label(root, text="Username:").pack(pady=5)
# entry_username = tk.Entry(root)
# entry_username.pack(pady=5)

# tk.Label(root, text="Password:").pack(pady=5)
# entry_password = tk.Entry(root, show="*")
# entry_password.pack(pady=5)

# tk.Button(root, text="Login", command=login).pack(pady=10)
# tk.Button(root, text="Register", command=open_register).pack(pady=5)

# root.mainloop()
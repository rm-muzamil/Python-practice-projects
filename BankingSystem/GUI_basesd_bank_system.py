import tkinter as tk
from tkinter import messagebox
import os
import json


USERS_DATABASE = "users_DB.json"





root = tk.Tk()
root.title("GUI BANK SYSTEM")
root.geometry("400x350")

tk.Label(root,text="Username :").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root,text="Password :").pack(pady=5)
entry_password = tk.Entry(root,show="*")
entry_password.pack(pady=5)


tk.Button(root,text="Login",command=login).pack(pady=10)
tk.Button(root,text="Register",command=open_register).pack(pady=5)

root.mainloop()


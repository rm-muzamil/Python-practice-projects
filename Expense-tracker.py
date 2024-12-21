import tkinter as tk
from tkinter import ttk, messagebox

# Expense list to store data
expenses = []

def add_expense():
    # Get inputs
    name = name_entry.get()
    amount = amount_entry.get()
    category = category_combobox.get()
    
    # Validate inputs
    if not name or not amount or not category:
        messagebox.showwarning("Input Error", "Please fill in all fields!")
        return
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid amount!")
        return
    
    # Add expense to the list
    expenses.append({"Name": name, "Amount": amount, "Category": category})
    
    # Update display
    update_expense_list()
    
    # Clear input fields
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_combobox.set("")

def update_expense_list():
    # Clear the treeview
    for row in expense_tree.get_children():
        expense_tree.delete(row)
    
    # Add expenses to the treeview
    for expense in expenses:
        expense_tree.insert("", "end", values=(expense["Name"], expense["Amount"], expense["Category"]))

def calculate_total():
    total = sum(expense["Amount"] for expense in expenses)
    messagebox.showinfo("Total Expense", f"Total Amount Spent: ${total:.2f}")

# Create the main application window
app = tk.Tk()
app.title("Expense Tracker")
app.geometry("600x400")

# Heading
heading_label = tk.Label(app, text="Expense Tracker", font=("Arial", 16))
heading_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(app)
input_frame.pack(pady=10)

# Name input
name_label = tk.Label(input_frame, text="Expense Name:", font=("Arial", 12))
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Amount input
amount_label = tk.Label(input_frame, text="Amount:", font=("Arial", 12))
amount_label.grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(input_frame, font=("Arial", 12))
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Category input
category_label = tk.Label(input_frame, text="Category:", font=("Arial", 12))
category_label.grid(row=2, column=0, padx=5, pady=5)
category_combobox = ttk.Combobox(input_frame, values=["Food", "Transport", "Shopping", "Bills", "Other"], font=("Arial", 12), state="readonly")
category_combobox.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(input_frame, text="Add Expense", font=("Arial", 12), command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Expense List Frame
list_frame = tk.Frame(app)
list_frame.pack(pady=10)

# Expense Treeview
columns = ("Name", "Amount", "Category")
expense_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)
expense_tree.pack()

# Define column headings
expense_tree.heading("Name", text="Name")
expense_tree.heading("Amount", text="Amount")
expense_tree.heading("Category", text="Category")

# Total Button
total_button = tk.Button(app, text="Calculate Total", font=("Arial", 12), command=calculate_total)
total_button.pack(pady=10)

# Run the application
app.mainloop()

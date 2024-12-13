# def displayTask(tasks):
#     print("\n To-Do List:")
#     if not tasks:
#         print("No task avaliable")
#     else:
#         for i,task in enumerate(tasks, 1):
#             print(f"{i}. {task}")
        
    
# def addTask(tasks):
#     task = input("Enter a new task")
#     tasks.append(task)
#     print(f"Task {task} added in List successfully")
# def removeTask(tasks):
#     displayTask(tasks)
#     try:
#         tasks_num = int(input("Enter task Number"))
#         if 1 <= tasks_num <= len(tasks):
#             removed_task = tasks.pop(tasks_num - 1)
#             print(f"{removed_task} task removed from List successfully")
#         else:
#             print("Invalid task number")
#     except ValueError:
#         print("Enter a valid number")
        
# def main():
#     tasks = []
#     while True:
#         print("To-Do App Menu:")
#         print("1. View Tasks")
#         print("2. Add Task")
#         print("3. Remove Task")
#         print("4. Exit")
        
#         choice = input("Enter your choice (1/2/3/4): ")
#         if choice == '1':
#             displayTask(tasks)
#         elif choice == '2':
#             addTask(tasks)
#         elif choice == '3':
#             removeTask(tasks)
#         elif choice == '4':
#             print("Exiting To-Do App. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.\n")
            
# main()

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove!")
        
def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Create the main window
app = tk.Tk()
app.title("To-Do App")

# Task entry
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(app, text="Remove Task", width=15, command=remove_task)
remove_button.pack(pady=5)

clear_button = tk.Button(app, text="Clear All Tasks", width=15, command=clear_tasks)
clear_button.pack(pady=5)
# Task list display
tasks_listbox = tk.Listbox(app, width=50, height=15)
tasks_listbox.pack(pady=10)

# Run the app
app.mainloop()
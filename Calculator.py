# def calculator(num1,num2,op):
#     if op == "+":
#         return num1 + num2
#     elif op == "-":
#         return num1 - num2
#     elif op == "*":
#         return num1 * num2
#     elif op == "/":
#         return num1 / num2
#     else:
#         return "Enter a valid operator"
    
# num1,num2,op = float(input("Enter first number")),float(input("enter secound number")),input("Enter operation like (+,-,*,/) : ")
# result = calculator(num1,num2,op)
# print(result)








import tkinter as tk

def press(key):
    expression_field.insert(tk.END, key)
    
def calculate():
    try:
        result = eval(expression_field.get())
        expression_field.delete(0, tk.END)
        expression_field.insert(0, result)
        
    except Exception as e:
        expression_field.delete(0, tk.END)
        expression_field.insert(0, "Error")
def clear():
    expression_field.delete(0, tk.END)

# Create the main window
app = tk.Tk()
app.title("Simple Calculator")

# Create the input field
expression_field = tk.Entry(app, font=("Arial", 16), bd=5, insertwidth=4, width=14, borderwidth=4)
expression_field.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',  
    '4', '5', '6', '*',  
    '1', '2', '3', '-',  
    'C', '0', '=', '+'  
]  

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 14), command=calculate).grid(row=row_val, column=col_val)
    elif button == "C":
        tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 14), command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 14), command=lambda key=button: press(key)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val >= 4:
        col_val = 0
        row_val += 1
        
app.mainloop()
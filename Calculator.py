def calculator(num1,num2,op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Enter a valid operator"
    
num1,num2,op = float(input("Enter first number")),float(input("enter secound number")),input("Enter operation like (+,-,*,/) : ")
result = calculator(num1,num2,op)
print(result)
# Task 1 

with open("student.txt","w") as file:
    file.write("\nAbubakar")
with open("student.txt","a") as file:
    file.write("\nAhmad")
with open("student.txt","a") as file:
    file.write("\nAli")
with open("student.txt","a") as file:
    file.write("\nAmad")
with open("student.txt","a") as file:
    file.write("\nAbdullah")
    
with open("student.txt","r") as file:
    print(file.read())
    
    
import json

data = {
    "namw" : "RM Muzammil",
    "class" : 13,
    "subject" : "BSSE" 
}

json_data = json.dumps(data,indent=1)

print(json_data)
python_data = json.loads(json_data)
print(python_data["class"])
with open("colleges.json","w") as file:
    file.write("hy")
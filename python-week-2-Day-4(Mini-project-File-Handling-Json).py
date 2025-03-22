import json
import os


users_file = "users_data.json"
def save_user(user):
    with open(users_file, "w") as file:
        json.dump(user,file,indent=4)
        
def load_user():
    if os.path.exists(users_file):
        with open(users_file, "r") as file:
            return json.load(file)
    return {}

def add_user(name,age,email):
    users = load_user()
    
    if name in users:
        print(f"Username already exists")
        return
    users[name] = {"age" : age,"email":email} 
    save_user(users)
    print(f"{name} is addded successfully")
    
def update_user(name,field,new_value):
    users = load_user()
    if name not in users:
        print(f"{name} is not found in database")
    if field in users[name]:
        users[name][field] = new_value
        save_user(users)
        print(f"{name} is updated successfully")
    else:
        print(f"{field} is not exists!")
        
        
def delete_user(name):
    users = load_user()
    if name in users:
        del users[name]
        save_user(users)
        print(f"{name} is deleted successfully")
    else:
        print(f"{name} is not found")
def show_users():
    users = load_user()
    
    if users:
        for name,details in users.items():
            print(f"{name} : {details}")
    else:
        print(f"No user Found")
        
# add_user("Muzammil",19,"ramuzamill87@gmail.com")
show_users()            
add_user("rana",19,"ramuzamill87@gmail.com")
show_users()            
update_user("rana", "age",20)
show_users()            

import re

pattren = r"\+\d++-\d++-\d+"

text = "My Numbers is +0309-187-7204 and +0328-055-1204"


match = re.findall(pattren,text)
print(match)

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]"
    return bool(re.search(pattern, email))

print(is_valid_email("test@example.com"))  # ✅ True
print(is_valid_email("test@example.com"))  # ✅ True
print(is_valid_email("invalid-email"))     # ❌ False

def is_valid_username(username):
    pattren = r"^[a-zA-Z]+[a-zA-Z0-9]+$"
    return bool(re.search(pattren,username))
print(is_valid_username("rm099"))
print(is_valid_username("8srm099"))


class Mathutils:
    @staticmethod
    def add(a,b):
        return a + b
    
print(Mathutils.add(5,6))

class Bank:
    bank_name = "Python Bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

Bank.change_bank_name("AI Bank")
print(Bank.bank_name)  # ✅ Output: AI Bank

class Example:
    class_var = 10

    @classmethod
    def modify_class_var(self, value):
        self.class_var = value  # Modifies class variable

print(Example.class_var)  # Output: 10
Example.modify_class_var(20)
print(Example.class_var)  # Output: 20


class Library:
    total_books = 0
    
    def __init__(self,title):
        self.title = title
        self.is_borrow = False
        Library.total_books += 1
        
    def borrow_book(self):
        if not self.is_borrow:
            self.is_borrow = True
            print(f'✅ "{self.title}" has been borrowed.')
        else:
            print(f'⚠️ "{self.title}" is already borrowed.')
            
    def returned(self):
        if self.is_borrow:
            self.is_borrow =False
            print(f'✅ "{self.title}" has been returned.')
        else:
            print(f'⚠️ "{self.title}" was not borrowed.')
    @classmethod
    def get_nOB(cls):
         return f"📚 Total books in library: {cls.total_books}"

book1 = Library("Python Crash Course")
book2 = Library("Machine Learning Basics")

# Borrowing and returning books
book1.borrow_book()   # ✅ "Python Crash Course" has been borrowed.
book1.borrow_book()   # ⚠️ "Python Crash Course" is already borrowed.
book1.returned()   # ✅ "Python Crash Course" has been returned.

# Checking total books
print(Library.get_nOB())  # 📚 Total books in library: 2



text = "I have 2 cats, 10 dogs, and 1 parrot. #tweet"

numbers = re.findall(r"\d+",text)
hashtag = re.findall(r"#\w+",text)
hashtags = re.findall(r"\W+",text)
print(numbers)
print(hashtag)
print(hashtags)



# custom decorator

import time

def timer(func):
    def wrapper(*ag,**kw):
        start_time = time.time()
        result = func(*ag,**kw)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def is_valid_email(email):
    time.sleep(0)
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]"
    return bool(re.search(pattern, email))

print(is_valid_email("test@example.com"))  # ✅ True
print(is_valid_email("test@example.com"))  # ✅ True
print(is_valid_email("invalid-email"))     # ❌ False


class Car:
    wheels = 4
    
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print(f"Car:{self.brand} {self.model}")
        
print(Car.wheels)
my_car = Car("toyota","Corolla")
my_car2 = Car("Honda","Civic")

my_car.display_info()
my_car2.display_info()

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display(self):
        print(f"Student : {self.name} Age : {self.age} Grade : {self.grade}")
        
s1 = Student("RM MUzammil",19,"A++")
s2 = Student("Zain",19,"A++")
s3 = Student("Bilal",19,"A++")
s4 = Student("Emma",19,"A++")

s1.display()
s2.display()
s3.display()

class Teacher:
    def __init__(self,name,age,dept,salary):
        self.name = name
        self.age  = age 
        self.dept = dept
        self.salary = salary
    def show_details(self):
        print(f"Teacher : {self.name} \n Age : {self.age} \n Department : {self.dept} \n Salary : {self.salary}")
        
    def update_dept(self,new_dept,new_salary):
        self.dept = new_dept
        self.salary = new_salary
    
t1 = Teacher("Ma'am Rimla Anwar",29,"SE",40000)
t2 = Teacher("Ma'am Mariam Afzal",32,"SE",45000)

t1.show_details()
t2.show_details()

t1.update_dept("CS","100000")
t1.show_details()

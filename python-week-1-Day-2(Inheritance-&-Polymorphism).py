class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print(f"Vehicle : {self.brand} Model : {self.model}")
        
        
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        
    def car_info(self):
        print(f"Car : {self.brand} {self.model} , Fuel : {self.fuel_type}")
        
class ElectricCar(Car):
    def __init__(self, brand, model, fuel_type,battery_capacity):
        super().__init__(brand, model, fuel_type)
        self.battery_capacity = battery_capacity
        
    def car_info(self):
        print(f"{self.brand} {self.model} Fuel : {self.fuel_type}, Battery: {self.battery_capacity} kWh")
        
        
        
        
car1 = Car("Toyota","Corolla","Petrol")
car1.display_info()
car1.car_info()
car2 = ElectricCar("Tesla" ,"Model 1", "electric charge", 100)
car2.car_info()
         
        
# Polymorphism

class Animal:
    def make_sound(self):
        print("Animal make sounds")
        
class Dog(Animal):
    def make_sound(self):
        print("Dog Barks")
        
class Cat(Animal):
    def make_sound(self):
        print("Cats meows")
        
d = Dog()
c = Cat()
d.make_sound()
c.make_sound()

#  MIni Project

class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
        
    def display_info(self):
        print(f"Employee : {self.name} \n Id : {self.id} \n Salary : {self.salary}")
        
class Manager(Employee):
    def __init__(self, name, id, salary,dept):
        super().__init__(name, id, salary)
        self.dept = dept
        
    def display_info(self):
        print(f"Manager : {self.name} \n Id : {self.id} \n Department : {self.dept} \n Salary : {self.salary}")
        
class Developer(Employee):
    def __init__(self, name, id, salary, stack):
        super().__init__(name, id, salary)
        self.stack = stack
        
    def display_info(self):
        print(f"Delveloper : {self.name} \n Id : {self.id} \n Department : {self.stack} \n Salary : {self.salary}")
        
emp1 = Employee("Alice",1001,10000)
man1 = Manager("Neha", 2001, "software",25000)
dev1 = Developer("John",3001,"Frontend", 22000)

emp1.display_info()
man1.display_info()
dev1.display_info()
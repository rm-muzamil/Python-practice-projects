# # Encapsulation

# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.__balance = balance
        
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"${amount} deposited. New balance: ${self.__balance}")
#         else:
#             print("Deposit amount must be positive.")
            
#     def withdraw(self,amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"${amount} withdrawn. Remaining balance: ${self.__balance}")
#         else:
#             print("Invalid withdrawal amount.")
            
#     def getBalance(self):
#         return self.__balance
    
# account1 = BankAccount("RM",10000)
# account1.deposit(5000)
# account1.withdraw(100)

# print("Curren Balance : ", account1.getBalance())

# from abc import ABC,abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14 *(self.radius)**2
    
# class Rectangular(Shape):
#     def __init__(self,width,lenght):
#         self.width = width
#         self.lenght = lenght
        
#     def area(self):
#         return self.width * self.lenght
    
# c = Circle(5)
# r = Rectangular(6,8)
# print(c.area())
# print(r.area())

# ...
# Project: Simple Banking System

from abc import ABC,abstractmethod
import datetime

class BankAccount(ABC):
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
        self.transactions = []
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    def get_balance(self):
        return self.__balance
    def _update_balance(self, amount, transaction_type):
        self.__balance += amount
        self.transactions.append(f"{transaction_type} :${amount} on {datetime.datetime.now()}")
    def show_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)
    def show_account_summary(self):
        print(f"\n Account Holder : {self.account_holder}")
        print(f"\n Balance : {self.__balance}")
        
    
      
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate = 0.3):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
        
    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount,"Deposit")
            print(f"${amount} deposited. New balance: ${self.get_balance()}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self._update_balance(-amount, "Withdraw")
            print(f"${amount} withdrawn. Remaining balance: ${self.get_balance()}")
        else:
            print("Insufficient balance or invalid amount!")
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self._update_balance(interest, "interest added")
        print(f"Interest of {interest:.2f} added. New balance : ${self.get_balance()}")

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance,overdraft_limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount,"Deposit")
            print(f"${amount} deposited. New balance: ${self.get_balance()}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:  # Overdraft of $500 allowed
            self._update_balance(-amount, "Withdraw")
            print(f"${amount} withdrawn. Remaining balance: ${self.get_balance()}")
        else:
            print("Withdrawal exceeds overdraft limit or invalid amount!")
            
def transfer_money(sender,receiver,amount):
        if sender.get_balance() >= amount:
            sender._update_balance(-amount,"Transfer Out")
            receiver._update_balance(amount,"Transfer In")
            print(f"\n${amount} transferred from {sender.account_holder} to {receiver.account_holder}")
        else:
            print("\nTransfer failed! Insufficient balance.")

        
# Creating accounts
savings = SavingsAccount("Alice", 2000)
current = CurrentAccount("Bob", 1000)

# Performing transactions
print("\n--- Savings Account Transactions ---")
savings.deposit(500)
savings.withdraw(300)
savings.apply_interest()
savings.show_transaction_history()
savings.show_account_summary()

print("\n--- Current Account Transactions ---")
current.deposit(1000)
current.withdraw(1200)
current.show_transaction_history()
current.show_account_summary()

# Transfer money between accounts
transfer_money(savings, current, 400)

# Show final summaries
print("\n--- Final Account Summaries ---")
savings.show_account_summary()
current.show_account_summary()
# # Exception Handling

# try:
#     x = 10/0
#     print(x)
# except ZeroDivisionError:
#     print("You can not divide by Zero")
# except ValueError:
#     print("Enter a valid Number")
    
    
# try:
#     file = open("test.txt","r")
#     data = file.read()
# except FileNotFoundError:
#     print("File Not Found")
# finally:
#     print("This will always execute, closing file...")
    
    

# def check_age(age):
#     if age < 18:
#         raise ValueError("Age atleast be 18")
#     else:
#         print("Okay")
        
# try:
#     check_age(10)
# except ValueError as e:
#     print(e)
    
    
    
# # File Handling

# with open("file_handling","w") as file:
#     file.write("HY, File Handling")
#     file.write("\n Another ...")
    
# with open("file_handling","r") as file:
#     content = file.read()
#     print(content)
# with open("file_handling","a") as file:
#     file.write("\n Addiation of content")
# file = open("file_handling","r")
# print(file.read())
    
    
    
    
# ............................................... Project ............................................... #


from abc import ABC,abstractmethod
import datetime
import os

class BankAccount(ABC):
    def __init__(self,account_holder, balance, filename):
        self.account_holder = account_holder
        self.filename = filename
        self.__balance = self.load_balance(balance)
      
        
    def load_balance(self, default_balance):
        """Load balance from file (if exists), otherwise use default"""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1]  # Get last transaction line
                    balance_str = last_line.split("Balance:")[-1].strip()  # Extract balance
                    balance_str = balance_str.replace("$", "")  # ✅ Remove '$' symbol
                    return float(balance_str)  # ✅ Convert to float safely
        return default_balance
    
    def save_transaction(self, transaction_type, amount):
        """Save transaction details to file"""
        with open(self.filename, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {transaction_type}: ${amount}, Balance: ${self.__balance}\n")
            
            
            
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
        self.save_transaction(transaction_type, amount)  # Save to file
    def show_transaction_history(self):
       
        print("\nTransaction History:")
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                print(file.read())
        else:
            print("No transaction history found.")
    def show_account_summary(self):
        print(f"\n Account Holder : {self.account_holder}")
        print(f"\n Balance : {self.__balance}")
        
    
      
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, filename, interest_rate = 0.3):
        super().__init__(account_holder, balance,filename)
        self.interest_rate = interest_rate
        
    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount,"Deposit")
            self.save_transaction("Deposit", amount)
            print(f"${amount} deposited. New balance: ${self.get_balance()}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self._update_balance(-amount, "Withdraw")
            self.save_transaction("Withdrawal", amount)
            print(f"${amount} withdrawn. Remaining balance: ${self.get_balance()}")
        else:
            print("Insufficient balance or invalid amount!")
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self._update_balance(interest, "interest added")
        print(f"Interest of {interest:.2f} added. New balance : ${self.get_balance()}")

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, filename, overdraft_limit=500):
        super().__init__(account_holder, balance, filename)  # Pass filename
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
            
def transfer_money(sender, receiver, amount):
    if isinstance(sender, CurrentAccount) and sender.get_balance() + sender.overdraft_limit >= amount:
        sender._update_balance(-amount, "Transfer Out")
        receiver._update_balance(amount, "Transfer In")
        sender.save_transaction("Transfer Out", amount)
        receiver.save_transaction("Transfer In", amount)
        print(f"\n${amount} transferred from {sender.account_holder} to {receiver.account_holder}")
    elif sender.get_balance() >= amount:
        sender._update_balance(-amount, "Transfer Out")
        receiver._update_balance(amount, "Transfer In")
        sender.save_transaction("Transfer Out", amount)
        receiver.save_transaction("Transfer In", amount)
        print(f"\n${amount} transferred from {sender.account_holder} to {receiver.account_holder}")
    else:
        print("\nTransfer failed! Insufficient balance.")

        

alice_account = CurrentAccount("Alice", 1000, "alice_transactions.txt")
bob_account = SavingsAccount("Bob", 500, "bob_transactions.txt")

# Perform transactions
# alice_account.deposit(500)
# alice_account.withdraw(300)
transfer_money(alice_account,bob_account,100)
alice_account.show_transaction_history()

# bob_account.deposit(1000)
# bob_account.withdraw(1200)
bob_account.show_transaction_history()
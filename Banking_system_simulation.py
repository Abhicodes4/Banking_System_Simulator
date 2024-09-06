import random

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print("Amount Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            print("You Withdrew:", amount)
        else:
            print("Invalid withdrawal amount or insufficient balance")

    def display(self):
        print("Net Available Balance =", self.balance)

    def display_transactions(self):
        if self.transactions:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions yet.")

class User:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.account_number = ''
        self.account = BankAccount()

    def create_account(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        self.account_number = random.randint(10000, 99999)
        print("Your Account number is :", self.account_number)
        print("Account created successfully!")

    def authenticate(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        account_number = input("Enter your account number: ")
        if username == self.username and password == self.password and account_number == str(self.account_number):
            print("Login successful!")
            return True
        else:
            print("Login failed!")
            return False

# Usage
user = User()
user.create_account()

if user.authenticate():
    user.account.deposit()
    user.account.withdraw()
    user.account.display()
    user.account.display_transactions()
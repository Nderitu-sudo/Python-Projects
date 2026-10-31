
#Encapsulation means bundling data and the methods that work on it inside a class, and controlling access to that data so it can’t be changed carelessly from outside.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance      # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid or insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())   # 120

account.withdraw(1000)         # Invalid or insufficient funds
print(account.__balance)       # AttributeError
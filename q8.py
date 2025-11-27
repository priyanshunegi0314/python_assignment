class Account:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance 
        self.__pin = pin       
    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Incorrect PIN!"

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount, pin):
        if pin == self.__pin and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Transaction failed!")

a = Account("Priyu", 5000, 1234)
print(a.get_balance(1234))

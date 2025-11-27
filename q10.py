from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("UPI payment of", amount, "successful!")

class CreditCard(Payment):
    def pay(self, amount):
        print("Credit Card payment of", amount)

class Wallet(Payment):
    def pay(self, amount):
        print("Wallet payment done!")

payments = [UPI(), CreditCard(), Wallet()]
for p in payments:
    p.pay(500)

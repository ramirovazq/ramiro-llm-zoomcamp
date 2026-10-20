# encapsulation
class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

# account = BadBankAccount(0.0)
# account.balance = -1
# print(account.balance)

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount 

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account = BankAccount()
print(account.balance)
#account.balance = -1 # should be not possible

account.deposit(1.99)
print(account.balance)
account.withdraw(1.00)
print(account.balance)
#account.withdraw(100.00)

# abstraction # reduce complexity by hiding implementation details

# class EmailService:

#     def _connect(self):
#         print("Connecting to email server...")

#     def _authenticate(self):
#         # simulate authentication process
#         print("Authenticating...")

#     def send_email(self):
#         self._connect()
#         self._authenticate()
#         print(f"Sending email ....")
#         self._disconnect()

#     def _disconnect(self):
#         print("Disconnecting from email server...")

# e = EmailService()
# e.send_email()

# Inheritance 
# Is a fundamental concept on object-oriented programming (OOP) that involves
# creating new classes (subclasses or derived classes) based on existing classes
# (superclass or base class)

# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start(self):
#         print("vehicle is starting ...")

#     def stop(self):
#         print("vehicle is stopping ...")

# class Car(Vehicle):
#     def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
#         super().__init__(brand, model, year)
#         self.number_of_doors = number_of_doors
#         self.number_of_wheels = number_of_wheels

# class Bike(Vehicle):
#     def __init__(self, brand, model, year, number_of_wheels):
#         super().__init__(brand, model, year)
#         self.number_of_wheels = number_of_wheels

# car = Car("Ford", "Mustang", 2023, 4, 4)
# bike = Bike("Yamaha", "MT-07", 2023, 2)

# print(car.__dict__)
# print(bike.__dict__)
# car.start()
# bike.start()
# car.stop()
# bike.stop() 

# Polymorphism: many forms "having multiple forms"


# Coupling
# class EmailSender:
#     def send(self, message):
#         print(f"Sending email: {message}")

# class Order:
#     def create(self):
#         # perform order creation logic, e.g. validate order details, check 
#         # product stock, save to database
#         email = EmailSender()
#         email.send("Hi your order was places successfully")

# order = Order()
# order.create()

# # Coupling - refactored solution

from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class EmailService(NotificationService):
    def send_notification(self, message):
        print(f"Send email: {message}")

class MobileService(NotificationService):
    def send_notification(self, message):
        print(f"Send text message: {message}")

class Order:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def create(self):
        # perform order creation logic, e.g. validate order details, check 
        # product stock, save to database

        # Instead of
        # email = EmailSender()
        # email.send("Hi your order was places successfully")
        self.notification_service.send_notification("Hi your order was places successfully")

order1 = Order(EmailService())
order1.create()

order2 = Order(MobileService())
order2.create()

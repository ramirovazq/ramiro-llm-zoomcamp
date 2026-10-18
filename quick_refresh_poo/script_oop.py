# class Dog:
#     def __init__(self, name, breed, owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner

#     def bark(self):
#         print("Whoof whoof")

# class Owner:
#     def __init__(self, name, address, contact_number):
#         self.name = name
#         self.address = address
#         self.phone_number = contact_number

# owner1 = Owner("John Doe", "123 Main St", "555-1234")
# dog1 = Dog("Bruce", "Scottish Terrier", owner1)
# dog1.bark()
# print(dog1.name)
# print(dog1.breed)

# dog1 = Dog("Freya", "Greyhound")
# dog1.bark()
# print(dog1.name)
# print(dog1.breed)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# person1 = Person("Alice", 30)
# person1.greet()

# person2 = Person("Bob", 42)
# person2.greet()

# class User:
#     def __init__(self, username, email, pasword):
#         self.username = username
#         self.email = email
#         self.pasword = pasword

#     def say_hi_to_user(self, user):
#         print(f"Sending messaget to {user.username}: Hi, {user.username}. It's {self.username}")

# user1 = User("dantheman", "dan@gmail.com", "123")
# # user2 = User("batman", "bat@outlook.com", "abc")
# # user1.say_hi_to_user(user2)
# print(user1.email)
# user1.email = "danny@gmail.com"
# print(user1.email)

# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self._email = email
#         self.pasword = password

#     def get_email(self):
#         return self._email

#     def set_email(self, new_email): 
#         if "@" in new_email:
#             self._email = new_email

# user1 = User("dantheman", " Dan@gmail.com", "123")
# print(user1.get_email())
# user1.set_email("dann232323")
# print(user1.get_email())

# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self._email = email
#         self.pasword = password

#     # getter property
#     @property 
#     def email(self):
#         print("Email accesed")
#         return self._email

#     @email.setter
#     def email(self, new_email):
#         if "@" in new_email:
#             self._email = new_email

# user1 = User("dantheman", "dan@gmail.com", "123")
# print(user1.email)
# user1.email = "danny121212"
# print(user1.email)

# static attributes or class attributes
# is an attribute that belongs to the class
# not to any specific instance of the class.

# class User:
#     user_count = 0

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#         User.user_count += 1

#     def display_user(self):
#         print(f"useranme: {self.username}, email: {self.email}")

# user1 = User("ramirovaz", "ramiro@hola.com")
# user2 = User("ramirobaltazar", "baltazar@hola.com")

# print(User.user_count)
# print(user1.user_count)
# print(user2.user_count)

# Static Method
# A static method in Python is a method that belongs to the class itself rather 
# than any instance of the class.
# To define a static method use decorator @staticmethod decorator

#static vs instance methods

class BankAccount:
    MIN_BALANCE = 100
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            #print(f"{self.owner}'s new balance: ${self._balance}")
            self.__log_transction_method("deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def _is_valid_amount(self, amount):
        return amount > 0

    def __log_transction_method(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return  0 <= rate <= 5

account = BankAccount("Alice", 500)
account.deposit(200)

print(account._is_valid_amount(300))
account.__log_transction_method("withdraw", 300)

#print(BankAccount.is_valid_interest_rate(3))
#print(BankAccount.is_valid_interest_rate(10))
#print(BankAccount.MIN_BALANCE)
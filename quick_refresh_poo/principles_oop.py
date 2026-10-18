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

class EmailService:

    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        # simulate authentication process
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print(f"Sending email ....")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server...")

e = EmailService()
e.send_email()

# 
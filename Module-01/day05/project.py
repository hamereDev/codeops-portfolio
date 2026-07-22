class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def statement(self):
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.__balance} ETB")


account1 = Account("Hamere", "1001")
account2 = Account("Meti", "1002", 5000)

account1.deposit(2000)
account2.deposit(1000)

account1.withdraw(500)
account2.withdraw(2500)

# account1.statement()
# account2.statement()

# print(account1.balance)
# print(account2.balance)
# SavingsAccount subclass
class SavingsAccount(Account):
    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)

    # Override statement()
    def statement(self):
        print("Savings Account")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} ETB")
        print(f"Interest Rate: {self.rate * 100}%")


# CurrentAccount subclass
class CurrentAccount(Account):
    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    # Override withdraw()
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if self.balance - amount < -self.overdraft:
            raise ValueError("Overdraft limit exceeded")

        # Access the private balance
        self._Account__balance -= amount

    # Override statement()
    def statement(self):
        print("Current Account")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} ETB")
        print(f"Overdraft Limit: {self.overdraft} ETB")


# Test code
savings1 = SavingsAccount("Meti", "2001", 2000, 0.10)
current1 = CurrentAccount("Abel", "3001", 500, 1000)

# Add interest
savings1.add_interest()

# Withdraw using overdraft
current1.withdraw(1200)

# Polymorphism loop
accounts = [account1, account2, savings1, current1]

for acc in accounts:
    acc.statement()
    print("-" * 40)
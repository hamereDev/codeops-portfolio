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

account1.statement()
account2.statement()

print(account1.balance)
print(account2.balance)
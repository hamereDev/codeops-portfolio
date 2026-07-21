
# Day 6 Larger Project - bank.py


# Singleton: BankConfig


class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # shared configuration
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
            cls._instance.currency = 'ETB'

        return cls._instance



# Observer classes


class SMSAlert:
    def update(self, event):
        print(f'[TeleBirr SMS] {event}')


class AuditLog:
    def update(self, event):
        print(f'[Audit Log] {event}')



# Base Account class


class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self._balance = balance
        self._observers = []

    @property
    def balance(self):
        return self._balance

    # ----- Observer methods -----
    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, event):
        for observer in self._observers:
            observer.update(event)

    # ----- Banking logic -----
    def deposit(self, amount):
        if amount <= 0:
            print('Deposit amount must be positive.')
            return

        self._balance += amount
        self._notify(f'{self.owner} deposited {amount} ETB')

    def withdraw(self, amount):
        if amount <= 0:
            print('Withdrawal amount must be positive.')
            return

        if amount > self._balance:
            print('Insufficient balance.')
            return

        self._balance -= amount
        self._notify(f'{self.owner} withdrew {amount} ETB')

    def statement(self):
        print(f'{self.owner} ({self.number}) - Balance: {self._balance} ETB')



# SavingsAccount


class SavingsAccount(Account):
    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.config = BankConfig()

    def add_interest(self):
        interest = self.balance * self.config.interest_rate
        self.deposit(interest)
        print(f'Interest added: {interest:.2f} ETB')


# CurrentAccount


class CurrentAccount(Account):
    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.config = BankConfig()

    def withdraw(self, amount):
        if amount <= 0:
            print('Withdrawal amount must be positive.')
            return

        # allow overdraft
        if self.balance - amount < -self.config.overdraft_limit:
            print('Overdraft limit exceeded.')
            return

        self._balance -= amount
        self._notify(f'{self.owner} withdrew {amount} ETB (Current Account)')



# Factory Pattern


class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == 'savings':
            return SavingsAccount(owner, number, balance)

        elif kind == 'current':
            return CurrentAccount(owner, number, balance)

        else:
            raise ValueError(f'Unknown account type: {kind}')



# Demo / Test


print('BankConfig Singleton ')
config1 = BankConfig()
config2 = BankConfig()

print('Currency:', config1.currency)
print('Same object?', config1 is config2)

print('\n Create Accounts Through Factory ')

savings = AccountFactory.create('savings', 'Hamere', 'CBE-1001', 5000)
current = AccountFactory.create('current', 'Selam', 'CBE-2001', 2000)

# attach observers
sms = SMSAlert()
log = AuditLog()

savings.subscribe(sms)
savings.subscribe(log)

current.subscribe(sms)
current.subscribe(log)

print('\n Savings Account Transactions ')
savings.deposit(1000)
savings.withdraw(500)
savings.add_interest()
savings.statement()

print('\n Current Account Transactions ')
current.withdraw(2500)   # allowed (overdraft)
current.withdraw(1000)   # may exceed limit depending on balance
current.statement()
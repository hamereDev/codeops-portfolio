class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.history = []  
    def deposit(self, amount):
        if amount <= 0:
            print('Deposit must be positive.')
            return

        self.balance += amount
        self.history.append(('deposit', amount))
        print(f'{self.owner} deposited {amount} ETB')

    def withdraw(self, amount):
        if amount <= 0:
            print('Withdrawal must be positive.')
            return

        if amount > self.balance:
            print('Insufficient balance.')
            return

        self.balance -= amount
        self.history.append(('withdraw', amount))
        print(f'{self.owner} withdrew {amount} ETB')
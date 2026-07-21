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
class AccountRegistry:
    def __init__(self):
        self.by_number = {}   # O(1) lookup
        self.order = []

    def add(self, acc):
        self.by_number[acc.account_number] = acc
        self.order.append(acc.account_number)

    def find(self, number):
        return self.by_number.get(number)
    def list_all(self):
        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts
    def undo_last(self):
        if not self.history:
            print('No transaction to undo.')
            return

        tx_type, amount = self.history.pop()

        if tx_type == 'deposit':
            self.balance -= amount
            print(f'Undo deposit of {amount} ETB')

        elif tx_type == 'withdraw':
            self.balance += amount
            print(f'Undo withdrawal of {amount} ETB')

    def statement(self):
        print(f'{self.owner} ({self.account_number}) - Balance: {self.balance} ETB')
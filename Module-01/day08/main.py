
# Day 7 Larger Project - registry.py
# Account Registry with O(1) lookup and undo



class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.history = []  # transaction history stack

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
# Binary search
def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
# Recursive sum
def recursive_total(history, index=0):
    if index >= len(history):
        return 0

    tx_type, amount = history[index]

    if tx_type == 'deposit':
        value = amount
    else:
        value = -amount

    return value + recursive_total(history, index + 1)

class AccountRegistry:
    def __init__(self):
        self.by_number = {}   # number -> Account (O(1))
        self.order = []       # insertion order

    def add(self, acc):
        if acc.account_number in self.by_number:
            print('Account already exists.')
            return

        self.by_number[acc.account_number] = acc
        self.order.append(acc.account_number)

        print(f'Added account {acc.account_number}')

    def find(self, number):
        return self.by_number.get(number)

    def list_all(self):
        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts
    def top_by_balance(self, n=5):
        accounts = sorted(
            self.by_number.values(),
            key=lambda a: a.balance,
            reverse=True
        )
        return accounts[:n]
    def find_by_number(self, number):
        numbers = sorted(self.by_number.keys())
        index = binary_search(numbers, number)

        if index >= 0:
            return self.by_number[numbers[index]]

        return None
    def total_transactions(self, number):
        account = self.find_by_number(number)

        if account is None:
            return None

        return recursive_total(account.history)
# Demo / Test


registry = AccountRegistry()

acc1 = Account('Almaz', 'CBE-1001', 5000)
acc2 = Account('Hamere', 'CBE-1002', 3000)
acc3 = Account('Kidist', 'CBE-1003', 7000)

registry.add(acc1)
registry.add(acc2)
registry.add(acc3)

print('\n O(1) Lookup ')

found = registry.find('CBE-1002')

if found:
    found.statement()

print('\n Ordered Listing ')

for acc in registry.list_all():
    acc.statement()

print('\n Transaction History Stack ')

acc1.deposit(1000)
acc1.withdraw(500)

print('Current balance:', acc1.balance)

print('\nUndo last transaction:')
acc1.undo_last()
print('Balance after undo:', acc1.balance)

print('\nUndo again:')
acc1.undo_last()
print('Balance after second undo:', acc1.balance)
# Demo / Test

registry = AccountRegistry()

acc1 = Account('Almaz', 'CBE-1001', 5000)
acc2 = Account('Hamere', 'CBE-1002', 3000)
acc3 = Account('Kidist', 'CBE-1003', 7000)

registry.add(acc1)
registry.add(acc2)
registry.add(acc3)

# Transactions
acc1.deposit(1000)
acc1.withdraw(500)

acc2.deposit(2000)

acc3.withdraw(1000)

print('\n--- Top 2 by balance ---')

for acc in registry.top_by_balance(2):
    acc.statement()

print('\n--- Binary search lookup ---')

found = registry.find_by_number('CBE-1002')

if found:
    found.statement()

print('\n--- Recursive transaction total ---')

print('CBE-1001:', registry.total_transactions('CBE-1001'))
print('CBE-1002:', registry.total_transactions('CBE-1002'))
print('CBE-1003:', registry.total_transactions('CBE-1003'))
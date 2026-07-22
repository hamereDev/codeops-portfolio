

class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self._balance = balance
        self.transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.transactions.append(amount)

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.transactions.append(-amount)

    def __str__(self):
        return f'{self.number} | {self.owner} | Balance: {self.balance}'


class AccountRegistry:
    def __init__(self):
        self.by_number = {}

    def add_account(self, account):
        self.by_number[account.number] = account
        

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


# Add these methods inside AccountRegistry

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
    

# Recursive sum helper
def recursive_sum(nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(nums[1:])


# Add this method inside AccountRegistry

    def total_transactions(self, number):
        account = self.find_by_number(number)

        if account is None:
            return None

        return recursive_sum(account.transactions)
    

#  TEST 

registry = AccountRegistry()

a1 = Account('Hamere', 1001, 2500)
a2 = Account('Meti', 1002, 6200)
a3 = Account('Selam', 1003, 4100)
a4 = Account('Hermi', 1004, 1800)

# Transactions
a1.deposit(500)
a1.withdraw(200)

a2.deposit(1000)
a2.withdraw(300)

a3.deposit(700)

# Add accounts
registry.add_account(a1)
registry.add_account(a2)
registry.add_account(a3)
registry.add_account(a4)

print(' Top accounts by balance')
for acct in registry.top_by_balance(3):
    print(acct)

print('\\n Find account 1003 ')
print(registry.find_by_number(1003))

print('\\n Total transactions for 1001 ')
print(registry.total_transactions(1001))
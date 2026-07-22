# day09

class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f'{self.account_number} | {self.owner} | {self.balance} ETB'


class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []      # sub-branches
        self.accounts = []      # accounts in this branch

    def add_child(self, branch):
        self.children.append(branch)

    def add_account(self, account):
        self.accounts.append(account)
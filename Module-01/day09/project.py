
# day09

from collections import deque


class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
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

    # Recursive total balance
    def total_balance(self):
        total = 0

        for acc in self.accounts:
            total += acc.balance

        for child in self.children:
            total += child.total_balance()

        return total

# BFS for transfers graph
def bfs(transfers, start):
    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)

            for neighbor in transfers.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited


# Sample Data 

# Accounts
a1 = Account('Almaz', 'CBE-1001', 5000)
a2 = Account('Hamere', 'CBE-1002', 3000)
a3 = Account('Kidist', 'CBE-1003', 7000)
a4 = Account('Sara', 'CBE-1004', 4500)
a5 = Account('Abel', 'CBE-1005', 2500)

# Branch tree (3 levels deep)
head_office = Branch('Head Office')

addis_region = Branch('Addis Region')
bahirdar_region = Branch('Bahir Dar Region')

bole_branch = Branch('Bole Branch')
piassa_branch = Branch('Piassa Branch')

# Build tree
head_office.add_child(addis_region)
head_office.add_child(bahirdar_region)

addis_region.add_child(bole_branch)
addis_region.add_child(piassa_branch)

# Add accounts
head_office.add_account(a1)
addis_region.add_account(a2)
bole_branch.add_account(a3)
piassa_branch.add_account(a4)
bahirdar_region.add_account(a5)

# Transfers graph
transfers = {
    'CBE-1001': ['CBE-1002', 'CBE-1003'],
    'CBE-1002': ['CBE-1004'],
    'CBE-1003': ['CBE-1005'],
    'CBE-1004': [],
    'CBE-1005': []
}


#  Tests 

print(' Recursive branch total ')
print('Head Office total:', head_office.total_balance(), 'ETB')

print('\\n BFS reachable accounts ')
reachable = bfs(transfers, 'CBE-1001')
print('From CBE-1001:', reachable)
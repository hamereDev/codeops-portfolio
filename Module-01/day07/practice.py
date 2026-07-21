# Exercise 1: Big-O

# O(1) - list index
numbers = [10, 20, 30]
print(numbers[1])

# O(n) - single loop
for n in numbers:
    pass

# O(n^2) - nested loop
for i in numbers:
    for j in numbers:
        pass

# O(1) average - dict lookup
accounts = {'CBE-1': 'Almaz'}
print(accounts['CBE-1'])

# O(log n) - binary search
# Binary search cuts the search space in half each step.
import time

account_list = [f'ACC-{i}' for i in range(100000)]
account_dict = {f'ACC-{i}': i for i in range(100000)}

target = 'ACC-99999'

start = time.perf_counter()
target in account_list
list_time = time.perf_counter() - start

start = time.perf_counter()
target in account_dict
dict_time = time.perf_counter() - start

print('List lookup:', list_time)
print('Dict lookup:', dict_time)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None


names = ['Almaz', 'Hamere', 'Kidist']

stack = Stack()
for name in names:
    stack.push(name)

reversed_names = []
while stack.peek() is not None:
    reversed_names.append(stack.pop())

print(reversed_names)
from collections import deque

queue = deque()

for customer in ['Almaz', 'Hamere', 'Kidist', 'Meti', 'Selam']:
    queue.append(customer)

while queue:
    print('Served:', queue.popleft())
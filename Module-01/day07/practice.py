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
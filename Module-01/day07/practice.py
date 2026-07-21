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
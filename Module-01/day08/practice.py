# day08/practice.py

# 1. Recursive sum and countdown

def total(nums):
    if not nums:
        return 0
    return nums[0] + total(nums[1:])


def count_down(n):
    if n <= 0:
        return
    print(n)
    count_down(n - 1)


# Test
numbers = [10, 20, 30, 40]
print('Total:', total(numbers))

print('Countdown:')
count_down(5)


# 2. Binary search

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


# Test
balances = [500, 1200, 2500, 3200, 4500, 6000]
print('Binary search index:', binary_search(balances, 3200))


# 3. Merge sort

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


# Test
unsorted_list = [42, 5, 19, 8, 33, 1]
sorted_list = merge_sort(unsorted_list)

print('Merge sorted:', sorted_list)
print('Matches sorted():', sorted_list == sorted(unsorted_list))


# 4. Sort with a key

accounts = [
    ('Hamere', 1200),
    ('Kidist', 4500),
    ('Meti', 3000),
    ('Hermi', 800),
]

sorted_accounts = sorted(accounts, key=lambda item: item[1], reverse=True)

print('Sorted accounts:')
for name, balance in sorted_accounts:
    print(name, '-', balance)


# 5. Two pointers

def has_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return True
        elif current < target:
            left += 1
        else:
            right -= 1

    return False


# Test
nums = [1, 2, 4, 7, 11, 15]
print('Has pair:', has_pair(nums, 15))
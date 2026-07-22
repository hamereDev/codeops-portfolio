# day09/practice.py

# 1. Build a BST

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)


# Test
balances = [5000, 2500, 7000, 1000, 4000, 6000, 9000]

root = None
for b in balances:
    root = insert(root, b)

print('In-order traversal (sorted):')
inorder(root)
print()


# 2. Tree depth / height

def height(node):
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)


print('\\nTree height:', height(root))


# 3. Graph BFS

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print('\\nBFS reachable from A:')
print(bfs(graph, 'A'))


# 4. Graph DFS

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


print('\\nDFS visit order from A:')
print(dfs(graph, 'A'))


# 5. Priority queue

import heapq

tasks = []

heapq.heappush(tasks, (3, 'Write report'))
heapq.heappush(tasks, (1, 'Fix bug'))
heapq.heappush(tasks, (5, 'Refactor code'))
heapq.heappush(tasks, (2, 'Reply email'))
heapq.heappush(tasks, (4, 'Run tests'))

print('\\nTasks by priority:')

while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, '-', task)
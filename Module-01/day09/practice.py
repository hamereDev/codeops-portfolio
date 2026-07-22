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
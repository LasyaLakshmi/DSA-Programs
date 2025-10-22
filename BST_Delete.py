class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node found
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Find inorder successor
        temp = root.right
        while temp.left:
            temp = temp.left
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

# Example usage
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

print("Inorder before deletion:")
inorder(root)
root = delete(root, 50)
print("\nInorder after deleting 50:")
inorder(root)

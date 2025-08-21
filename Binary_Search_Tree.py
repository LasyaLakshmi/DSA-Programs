class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # 1. Insertion
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    # 2. Search

    def search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    # 3. Deletion
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: Get inorder successor (smallest in the right subtree)
            temp = self._minValueNode(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Utility: Inorder traversal (for testing)
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        res = []
        if node:
            res = self._inorder(node.left)
            res.append(node.key)
            res = res + self._inorder(node.right)
        return res

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
print("\nInitial Tree:")
print(bst.inorder())
bst.delete(20)
bst.delete(30)
bst.delete(50)
print("\nTree after deletion:")
print(bst.inorder())
bst.insert(15)
bst.insert(75)
print("\nTree after insertion:")
print(bst.inorder())
print("\nSearching for 40:")
print("Exists in the tree:", bst.search(bst.root, 40) is not None)
print()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    def add(self, key):
        self.root = self.insert(self.root, key)
    def find_min(self, root):
        current = root
        while current and current.left:
            current = current.left
        return current.key if current else None
    def find_max(self, root):
        current = root
        while current and current.right:
            current = current.right
        return current.key if current else None
bst = BinarySearchTree()
notas = [85, 70, 95, 60, 75, 90, 100]
for nota in notas:
    bst.add(nota)

nota_minima = bst.find_min(bst.root)
nota_maxima = bst.find_max(bst.root)

print('Nota minima ' + str(nota_minima))
print('Nota Maxiam ' + str(nota_maxima))

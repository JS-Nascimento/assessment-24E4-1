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
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)
    def add(self, key):
        self.root = self.insert(self.root, key)
    def find(self, key):
        return self.search(self.root, key)
bst = BinarySearchTree()
precos = [100, 50, 150, 30, 70, 130, 170]
for preco in precos:
    bst.add(preco)

resultado = bst.find(70)

resultado_texto = "Disponível" if resultado else "Não disponível"
print(resultado_texto)

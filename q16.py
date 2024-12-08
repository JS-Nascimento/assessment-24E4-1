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

    def inorder_traversal(self, root):
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.key] + self.inorder_traversal(root.right)

    def find_min(self, root):

        current = root
        while current and current.left:
            current = current.left
        return current

    def delete(self, root, key):

        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Caso 1: Nó folha
            if root.left is None and root.right is None:
                return None
            # Caso 2: Nó com um filho
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Caso 3: Nó com dois filhos
            else:
                temp = self.find_min(root.right)
                root.key = temp.key
                root.right = self.delete(root.right, temp.key)
        return root

    def remove(self, key):

        self.root = self.delete(self.root, key)
bst = BinarySearchTree()
codigos = [45, 25, 65, 20, 30, 60, 70]
for codigo in codigos:
    bst.add(codigo)

def exibir_arvore(bst):
    return bst.inorder_traversal(bst.root)

resultado_remocao = {}

bst.remove(20)
resultado_remocao["Após remover 20"] = exibir_arvore(bst)

bst.remove(25)
resultado_remocao["Após remover 25"] = exibir_arvore(bst)

bst.remove(45)
resultado_remocao["Após remover 45"] = exibir_arvore(bst)

(print(resultado_remocao))

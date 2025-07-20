class Node:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sag = None

# Ağacı elle oluşturalım
kök = Node('A')             # Kök düğüm
kök.sol = Node('B')         # 1. seviye sol
kök.sag = Node('C')         # 1. seviye sağ
kök.sol.sol = Node('D')     # 2. seviye sol
kök.sol.sag = Node('E')     # 2. seviye sağ
kök.sag.sag = Node('F')     # 2. seviye sağ

# Preorder: Kök -> Sol -> Sağ
def preorder(node):
    if node:
        print(node.veri, end=' ')
        preorder(node.sol)
        preorder(node.sag)

# Inorder: Sol -> Kök -> Sağ
def inorder(node):
    if node:
        inorder(node.sol)
        print(node.veri, end=' ')
        inorder(node.sag)

# Postorder: Sol -> Sağ -> Kök
def postorder(node):
    if node:
        postorder(node.sol)
        postorder(node.sag)
        print(node.veri, end=' ')

# Derinlik hesaplama (maksimum seviye)
def agac_derinligi(node):
    if node is None:
        return 0
    return 1 + max(agac_derinligi(node.sol), agac_derinligi(node.sag))

print("Preorder dolaşım:")
preorder(kök)
print("\nInorder dolaşım:")
inorder(kök)
print("\nPostorder dolaşım:")
postorder(kök)
print(f"\nAğacın derinliği: {agac_derinligi(kök)}")

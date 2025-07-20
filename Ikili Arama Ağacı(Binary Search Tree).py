class BSTNode:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sag = None

class BST:
    def __init__(self):
        self.kök = None

    def ekle(self, kök, veri):
        if kök is None:
            return BSTNode(veri)
        if veri < kök.veri:
            kök.sol = self.ekle(kök.sol, veri)
        else:
            kök.sag = self.ekle(kök.sag, veri)
        return kök

    def inorder(self, node):
        if node:
            self.inorder(node.sol)
            print(node.veri, end=' ')
            self.inorder(node.sag)

    def ara(self, kök, veri):
        if kök is None or kök.veri == veri:
            return kök
        if veri < kök.veri:
            return self.ara(kök.sol, veri)
        return self.ara(kök.sag, veri)

    def min_deger(self, kök):
        while kök.sol:
            kök = kök.sol
        return kök.veri

    def max_deger(self, kök):
        while kök.sag:
            kök = kök.sag
        return kök.veri

    def derinlik(self, kök):
        if kök is None:
            return 0
        return 1 + max(self.derinlik(kök.sol), self.derinlik(kök.sag))


# Kullanım
agac = BST()
veriler = [50, 30, 70, 20, 40, 60, 80]
for v in veriler:
    agac.kök = agac.ekle(agac.kök, v)

print("BST Inorder (küçükten büyüğe):")
agac.inorder(agac.kök)

print("\n60 var mı?:", "Var" if agac.ara(agac.kök, 60) else "Yok")
print("Min değer:", agac.min_deger(agac.kök))
print("Max değer:", agac.max_deger(agac.kök))
print("Ağacın derinliği:", agac.derinlik(agac.kök))

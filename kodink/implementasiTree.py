class Node:
    def __init__(self, value):
        self.value = value  # Set nilai untuk node
        self.left = None  # Pointer ke node anak kiri
        self.right = None  # Pointer ke node anak kanan

class BinaryTree:
    def __init__(self, root):
        self.root = root  # Inisialisasi pohon biner dengan node root

    # Mendapatkan semua leluhur dari suatu node yang memiliki nilai target
    def get_ancestors(self, node, target):
        if node is None:
            return False  # Jika node adalah None, maka kembalikan False
        
        if node.value == target:  # Jika nilai node sama dengan target, maka kembalikan True
            return True
        
        # Rekursif untuk mencari leluhur dari node target
        if (self.get_ancestors(node.left, target) or self.get_ancestors(node.right, target)):
            print(node.value, end=" ")  # Cetak nilai leluhur
            return True

        return False

    # Mendapatkan semua keturunan dari suatu node
    def get_descendants(self, node, descendants=[]):
        if node is None:
            return []  # Jika node adalah None, maka kembalikan list kosong
        
        if node.left:
            descendants.append(node.left.value)  # Tambahkan nilai anak kiri ke dalam daftar keturunan
            self.get_descendants(node.left, descendants)  # Rekursif untuk mendapatkan keturunan dari anak kiri
        
        if node.right:
            descendants.append(node.right.value)  # Tambahkan nilai anak kanan ke dalam daftar keturunan
            self.get_descendants(node.right, descendants)  # Rekursif untuk mendapatkan keturunan dari anak kanan
        
        return descendants  # Kembalikan daftar keturunan

    # Mendapatkan nilai induk dari suatu node target
    def get_parent(self, node, target, parent=None):
        if node is None:
            return None  # Jika node adalah None, maka kembalikan None
        
        if node.value == target:
            return parent.value if parent else None  # Jika node adalah target, kembalikan nilai induk jika ada, jika tidak kembalikan None
        
        left = self.get_parent(node.left, target, node)  # Cari induk di anak kiri
        if left:
            return left
        
        return self.get_parent(node.right, target, node)  # Cari induk di anak kanan

    # Mendapatkan nilai anak dari suatu node target
    def get_children(self, node, target):
        if node is None:
            return []  # Jika node adalah None, maka kembalikan list kosong
        
        if node.value == target:
            children = []
            if node.left:
                children.append(node.left.value)  # Tambahkan nilai anak kiri jika ada
            if node.right:
                children.append(node.right.value)  # Tambahkan nilai anak kanan jika ada
            return children
        
        left = self.get_children(node.left, target)  # Cari anak di anak kiri
        if left:
            return left
        
        return self.get_children(node.right, target)  # Cari anak di anak kanan
    
    # Mendapatkan nilai saudara dari suatu node target
    def get_siblings(self, node, target):
        if node is None or node.value == target:
            return []  # Jika node adalah None atau node adalah target, maka kembalikan list kosong
        
        if node.left and node.right:
            if node.left.value == target:
                return [node.right.value]  # Jika node target adalah anak kiri, kembalikan nilai anak kanan
            if node.right.value == target:
                return [node.left.value]  # Jika node target adalah anak kanan, kembalikan nilai anak kiri
        
        left = self.get_siblings(node.left, target)  # Cari saudara di anak kiri
        if left:
            return left
        
        return self.get_siblings(node.right, target)  # Cari saudara di anak kanan
    
    # Menghitung ukuran pohon
    def get_size(self, node):
        if node is None:
            return 0  # Jika node adalah None, maka kembalikan 0
        return 1 + self.get_size(node.left) + self.get_size(node.right)  # Hitung ukuran pohon secara rekursif

# Membuat node
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

# Membangun pohon
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

# Inisialisasi pohon biner dengan node root A
tree = BinaryTree(A)

# Menguji fungsi-fungsi
print("Leluhur dari F: ", end="")
tree.get_ancestors(tree.root, 'F')
print()

print("Keturunan dari C:", tree.get_descendants(C))
print("Induk dari D:", tree.get_parent(tree.root, 'D'))
print("Anak-anak dari A:", tree.get_children(tree.root, 'A'))
print("Saudara dari F:", tree.get_siblings(tree.root, 'F'))
print("Ukuran pohon:", tree.get_size(tree.root))
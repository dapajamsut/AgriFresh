class TreeNode:
    def __init__(self, name):
        # Inisialisasi node dengan nama dan list kosong untuk menyimpan anak-anaknya
        self.name = name
        self.children = []

    def add_child(self, child_node):
        # Method untuk menambahkan anak baru ke dalam node ini
        self.children.append(child_node)

def print_tree(node, depth=0):
    # Fungsi rekursif untuk mencetak struktur pohon secara rekursif
    # Depth digunakan untuk menentukan tingkat kedalaman node dalam pohon
    # Fungsi ini mencetak nama node dengan indentasi berdasarkan kedalaman node
    print("  " * depth + "- " + node.name)
    # Iterasi melalui setiap anak dari node saat ini
    for child in node.children:
        # Rekursif memanggil print_tree untuk setiap anak
        # Dengan menambahkan 1 pada kedalaman (depth)
        print_tree(child, depth + 1)

# Membangun struktur pohon
root = TreeNode("Gedung")  # Node root yang merupakan kategori utama
kelas = TreeNode("Kelas")     # Node untuk kelas
canteen = TreeNode("Kantin")  # Node untuk jenis kantin
gsg_class = TreeNode("GSG")       # Node untuk jenis GSG
aa_class = TreeNode("AA")              # Node untuk jenis AA
prodi = TreeNode("Prodi")             # Node untuk jenis Prodi

# Menambahkan anak-anak ke node root
root.add_child(kelas)
root.add_child(canteen)
root.add_child(prodi)

# Menambahkan anak-anak ke node Kaos
kelas.add_child(gsg_class)
kelas.add_child(aa_class)

# Menampilkan struktur pohon
print_tree(root)

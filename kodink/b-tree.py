# Kelas untuk mendefinisikan node pada pohon biner
class NodePohon:
    def __init__(self, kunci):
        self.kiri = None   # Pointer ke anak kiri
        self.kanan = None  # Pointer ke anak kanan
        self.nilai = kunci # Nilai dari node

# Kelas untuk mendefinisikan pohon biner
class PohonBiner:
    def __init__(self):
        self.akar = None  # Inisialisasi akar pohon biner

    # Metode untuk menyisipkan kunci baru ke dalam pohon biner
    def sisipkan(self, kunci):
        # Jika pohon kosong, buat node akar baru
        if self.akar is None:
            self.akar = NodePohon(kunci)
        else:
            # Jika tidak, sisipkan kunci ke posisi yang sesuai
            self._sisipkan(self.akar, kunci)

    # Metode rekursif untuk menyisipkan kunci baru ke dalam pohon
    def _sisipkan(self, akar, kunci):
        # Bandingkan kunci dengan nilai akar untuk menentukan posisi
        if kunci < akar.nilai:
            # Jika lebih kecil, periksa anak kiri
            if akar.kiri is None:
                # Jika anak kiri kosong, buat node baru
                akar.kiri = NodePohon(kunci)
            else:
                # Jika tidak, lanjutkan pencarian ke anak kiri
                self._sisipkan(akar.kiri, kunci)
        else:
            # Jika lebih besar atau sama dengan, periksa anak kanan
            if akar.kanan is None:
                # Jika anak kanan kosong, buat node baru
                akar.kanan = NodePohon(kunci)
            else:
                # Jika tidak, lanjutkan pencarian ke anak kanan
                self._sisipkan(akar.kanan, kunci)

    # Metode untuk melakukan traversal inorder (kiri, akar, kanan)
    def traversal_inorder(self):
        return self._traversal_inorder(self.akar, [])

    # Metode rekursif untuk traversal inorder
    def _traversal_inorder(self, akar, traversal):
        if akar is not None:
            # Kunjungi anak kiri terlebih dahulu
            self._traversal_inorder(akar.kiri, traversal)
            # Kunjungi akar
            traversal.append(akar.nilai)
            # Kunjungi anak kanan
            self._traversal_inorder(akar.kanan, traversal)
        return traversal

    # Metode untuk melakukan traversal preorder (akar, kiri, kanan)
    def traversal_preorder(self):
        return self._traversal_preorder(self.akar, [])

    # Metode rekursif untuk traversal preorder
    def _traversal_preorder(self, akar, traversal):
        if akar is not None:
            # Kunjungi akar terlebih dahulu
            traversal.append(akar.nilai)
            # Kunjungi anak kiri
            self._traversal_preorder(akar.kiri, traversal)
            # Kunjungi anak kanan
            self._traversal_preorder(akar.kanan, traversal)
        return traversal

    # Metode untuk melakukan traversal postorder (kiri, kanan, akar)
    def traversal_postorder(self):
        return self._traversal_postorder(self.akar, [])

    # Metode rekursif untuk traversal postorder
    def _traversal_postorder(self, akar, traversal):
        if akar is not None:
            # Kunjungi anak kiri terlebih dahulu
            self._traversal_postorder(akar.kiri, traversal)
            # Kunjungi anak kanan
            self._traversal_postorder(akar.kanan, traversal)
            # Kunjungi akar
            traversal.append(akar.nilai)
        return traversal

# Contoh penggunaan PohonBiner
if __name__ == "__main__":
    pohon = PohonBiner()
    kunci_kunci = ["Gedung", "Kelas", "Kantin", "Meja", "Etalase", "Kulkas", "Kursi", "Minum"]

    # Menyisipkan setiap kunci ke dalam pohon
    for kunci in kunci_kunci:
        pohon.sisipkan(kunci)

    # Menampilkan hasil traversal inorder
    print("Traversal inorder dari Pohon Biner yang dibentuk adalah:")
    print(pohon.traversal_inorder())

    # Menampilkan hasil traversal preorder
    print("Traversal preorder dari Pohon Biner yang dibentuk adalah:")
    print(pohon.traversal_preorder())

    # Menampilkan hasil traversal postorder
    print("Traversal postorder dari Pohon Biner yang dibentuk adalah:")
    print(pohon.traversal_postorder())

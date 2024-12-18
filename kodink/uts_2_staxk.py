# Definisikan kelas Gudang untuk mengelola stok barang
class Gudang:
    def __init__(self):
        self.gudang = {}  # menyimpan data barang di gudang

    # MENAMBAH BARANG
    def add_barang(self, nama_barang, no_barang, jumlah_barang):
        if no_barang not in self.gudang:  # Periksa apakah nomor barang sudah ada di gudang
            # Jika belum ada, tambahkan sebagai item baru dengan jumlah barang yang ditentukan
            self.gudang[no_barang] = {'name': nama_barang, 'jumlah_barang': jumlah_barang}
        else:
            # Jika sudah ada, tambahkan jumlah barang yang baru ke jumlah yang sudah ada
            self.gudang[no_barang]['jumlah_barang'] += jumlah_barang

    # MENCARI ITEM
    def search_item(self, keyword):
        result = []  # list kosong untuk menyimpan hasil pencarian
        for no_barang, info_barang in self.gudang.items():
            # Periksa apakah kata kunci cocok dengan nama barang atau nomor barang
            if keyword.lower() in info_barang['name'].lower() or keyword.lower() == no_barang.lower():
                # Jika cocok, tambahkan barang tersebut ke dalam hasil pencarian
                result.append((no_barang, info_barang['name'], info_barang['jumlah_barang']))
        return result  # Kembalikan hasil pencarian

    # MENGHAPUS BARANG
    def remove_item(self, no_barang):
        if no_barang in self.gudang:  # Periksa apakah nomor barang ada di gudang
            del self.gudang[no_barang]  # Jika ada, hapus barang tersebut dari gudang
            print("Barang sudah dihapus dari gudang.")
        else:
            print("Barang tidak ditemukan.")  # Jika tidak ada, tampilkan pesan kesalahan

    # MENGEDIT JUMLAH BARANG
    def update_quantity(self, no_barang, jumlah_baru):
        if no_barang in self.gudang:  # Periksa apakah nomor barang ada di gudang
            self.gudang[no_barang]['jumlah_barang'] = jumlah_baru  # Perbarui jumlah barang
            print("Berhasil mengubah jumlah barang.")
        else:
            print("Barang tidak ada di gudang.")  # Jika tidak ada, tampilkan pesan kesalahan

    # MELIHAT SEMUA BARANG
    def review_inventory(self):
        print("Current Inventory:")  # Tampilkan pesan header
        for no_barang, info_barang in self.gudang.items():  # Iterasi melalui setiap barang di gudang
            # Tampilkan detail barang, termasuk nomor barang, nama barang, dan jumlah barang
            print(f"Item Code: {no_barang}, Name: {info_barang['name']}, Quantity: {info_barang['jumlah_barang']}")

# Bagian utama program, ini akan dieksekusi saat program dijalankan
if __name__ == "__main__":
    warehouse = Gudang()  # Buat objek gudang untuk mengelola stok barang

    while True:  # Loop tak terbatas untuk menu interaktif
        # Tampilkan menu pilihan untuk pengguna
        print("1. ADD ITEM")
        print("2. FIND ITEM")
        print("3. REMOVE ITEM")
        print("4. UPDATE ITEM")
        print("5. REVIEW ITEM")
        print("6. EXIT")

        choice = input("Masukkan pilihan (1-6): ")  # Meminta pengguna memilih menu

        if choice == '1':
            # Meminta input dari pengguna dan menambahkan barang baru ke dalam gudang
            nama_barang = input("Masukkan nama barang: ")
            no_barang = input("Masukkan nomor barang: ")
            jumlah_barang = int(input("Masukkan jumlah barang: "))
            warehouse.add_barang(nama_barang, no_barang, jumlah_barang)
        elif choice == '2':
            # Meminta input dari pengguna dan mencari barang di gudang
            keyword = input("Masukkan kata kunci untuk mencari barang: ")
            search_result = warehouse.search_item(keyword)
            if search_result:  # Jika ada hasil pencarian, tampilkan hasilnya
                print("Hasil Pencarian:")
                for item in search_result:
                    print(f"Nomor Barang: {item[0]}, Nama Barang: {item[1]}, Jumlah: {item[2]}")
            else:  # Jika tidak ada hasil pencarian, tampilkan pesan
                print("Barang tidak ditemukan.")
        elif choice == '3':
            # Meminta input dari pengguna dan menghapus barang dari gudang
            no_barang = input("Masukkan nomor barang yang ingin dihapus: ")
            warehouse.remove_item(no_barang)
        elif choice == '4':
            # Meminta input dari pengguna dan memperbarui jumlah barang di gudang
            no_barang = input("Masukkan nomor barang yang ingin diupdate jumlahnya: ")
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            warehouse.update_quantity(no_barang, jumlah_baru)
        elif choice == '5':
            # Meninjau gudang dengan menampilkan semua barang yang ada
            warehouse.review_inventory()
        elif choice == '6':
            print("Terima kasih telah menggunakan sistem manajemen gudang.")
            break  # Keluar dari loop jika pengguna memilih keluar
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar (1-6).")  # Pesan untuk pilihan tidak valid
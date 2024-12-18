class hospital:
    def __init__(self):
        self.antrian = []  #  antrian kosong

    def tambah_pasien(self, name, status):
        # Menambahkan pasien ke dalam antrian sesuai dengan statusnya
        if status == "darurat":
            self.antrian.insert(0, (name, status))
        elif status == "janji":
            self.antrian.append((name, status))
        else:
            self.antrian.append((name, "umum"))

    def pemeriksaan_pasien(self):
        if self.antrian:
            # Mengecek apakah ada pasien darurat di antrian
            for id, (name, status) in enumerate(self.antrian):
                if status == "darurat":
                    print(f"Pasien darurat {name} dipanggil untuk pemeriksaan.")
                    del self.antrian[id]  # Menghapus pasien dari antrian setelah dipanggil
                    return
            # Mengecek apakah ada pasien dengan janji di antrian
            for id, (name, status) in enumerate(self.antrian):
                if status == "janji":
                    print(f"Pasien {name} dengan janji dipanggil untuk pemeriksaan.")
                    del self.antrian[id]  # Menghapus pasien dari antrian setelah dipanggil
                    return
            # Jika tidak ada pasien darurat atau dengan janji, panggil pasien umum
            name, status = self.antrian.pop(0)
            print(f"Pasien {name} umum dipanggil untuk pemeriksaan.")
        else:
            print("Antrian kosong.")

    def hapus_pasien(self, name):
        # Menghapus pasien dari antrian setelah selesai diperiksa
        for id, (name_pasien, _) in enumerate(self.antrian):
            if name_pasien == name:
                del self.antrian[id]
                print(f"Pasien {name} telah selesai diperiksa dan dihapus dari antrian.")
                return
        print(f"Pasien {name} tidak ditemukan.")

# Bagian utama program
if __name__ == "__main__":
    rumah_sakit = hospital()

    while True:

        print("1. ADD PATIENT")
        print("2. CHECK PATIENT")
        print("3. REMOVE PATIENT")
        print("4. EXIT")

        choice = input("Pilih menu (1-4): ")

        if choice == '1':
            name = input("Masukkan name pasien: ")
            status = input("Masukkan status pasien (darurat/janji/umum): ").lower()
            rumah_sakit.tambah_pasien(name, status)
            print(f"Pasien {name} berhasil ditambahkan ke dalam antrian.")
        elif choice == '2':
            rumah_sakit.pemeriksaan_pasien()
        elif choice == '3':
            name = input("Masukkan name pasien yang selesai diperiksa: ")
            rumah_sakit.hapus_pasien(name)
        elif choice == '4':
            print("Terima kasih telah menggunakan sistem rumah sakit.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar (1-4).")
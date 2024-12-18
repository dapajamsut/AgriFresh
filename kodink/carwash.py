class Mobil:
    def __init__(self, no_antrian, merk_mobil):
        self.no_antrian = no_antrian
        self.merk_mobil = merk_mobil
        self.next = None

class carwash:
    def __init__(self, maks_ukuran):
        self.head = None
        self.tail = None
        self.maks_ukuran = maks_ukuran
        self.ukuran = 0

    def enqueue(self, mobil):
        if self.is_full():
            print("Antrian sudah penuh. Tidak bisa menambahkan mobil baru.")
            return

        if self.is_empty():
            self.head = self.tail = mobil
        else:
            self.tail.next = mobil
            self.tail = mobil

        self.ukuran += 1
        print(f"Mobil {mobil.merk_mobil} dengan nomor antrian {mobil.no_antrian} telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada Mobil yang bisa dihapus.")
            return

        mobil = self.head
        self.head = self.head.next
        mobil.next = None
        self.ukuran -= 1

        print(f"Mobil {mobil.merk_mobil} dengan nomor antrian {mobil.no_antrian} telah dilayani.")

        if self.is_empty():
            self.tail = None

    def is_empty(self):
        return self.ukuran == 0

    def is_full(self):
        return self.ukuran >= self.maks_ukuran

def main():
    # Membuat objek antrian carwash dengan maksimum 5 Mobil
    antrian_carwash = carwash(5)

    # Menambahkan beberapa Mobil ke dalam antrian
    antrian_carwash.enqueue(Mobil(1, "Avanza"))
    antrian_carwash.enqueue(Mobil(2, "Ford"))
    antrian_carwash.enqueue(Mobil(3, "BMW"))
    antrian_carwash.enqueue(Mobil(4, "Ferrari"))
    antrian_carwash.enqueue(Mobil(5, "Tesla"))

    # Menyimpan mobil jika antrian penuh
    antrian_carwash.enqueue(Mobil(6, "MclAren"))  # Antrian sudah penuh

    # Menghapus Mobil dari antrian
    antrian_carwash.dequeue()
    antrian_carwash.dequeue()

    # Menambahkan Mobil baru ke dalam antrian setelah beberapa Mobil dihapus
    antrian_carwash.enqueue(Mobil(6, "Ayla"))

if __name__ == "__main__":
    main()
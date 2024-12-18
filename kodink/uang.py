class Uang:
    def __init__(self, uang):
        self.uang = uang
        self.selanjutnya = None

class Nominal:
    def __init__(self,nominal_uang):
        self.nominal_jumlah_uang = nominal_uang

class Comand:
    def __init__(self):
        self.duluan = None  # Menginisialisasi kepala tumpukan sebagai None saat objek Comand dibuat

    def push(self, uang):
        jumlah_uang = Uang(uang)
        jumlah_uang.selanjutnya = self.duluan  # Menyisipkan objek baru di depan tumpukan
        self.duluan = jumlah_uang  # Memperbarui kepala tumpukan menjadi objek baru

    def pop(self):
        if self.is_empty():  # Memeriksa apakah tumpukan kosong
            print("Uang Habis, Tidak ada yang bisa ditumpuk")
            return None
        buangan = self.duluan.uang  # Mengambil uang dari tumpukan
        self.duluan = self.duluan.selanjutnya  # Menghapus uang dari tumpukan
        return buangan

    def peek(self):
        if self.is_empty():  # Memeriksa apakah tumpukan kosong
            print("Tidak ada uang yang ditumpuk")
            return None
        return self.duluan.uang  # Mengembalikan uang dari tumpukan tanpa menghapusnya

    def is_empty(self):
        return self.duluan is None  # Mengembalikan True jika tumpukan kosong, False jika tidak

def Output():
    nominal_jumlah_uang = Comand()

    nominal_jumlah_uang.push(Nominal("Rp.10.000"))
    nominal_jumlah_uang.push(Nominal("Rp.50.000"))
    nominal_jumlah_uang.push(Nominal("Rp.5000")) 

    nominal_duluan = nominal_jumlah_uang.peek()
    if nominal_duluan:
        print("Uang pertama yang akan ditumpuk :", nominal_duluan.nominal_jumlah_uang)

    buangan = nominal_jumlah_uang.pop()
    if buangan:
        print("Uang pertama-" ,buangan.nominal_jumlah_uang, "-sudah ditumpuk")

    if nominal_jumlah_uang.is_empty():
        print("Uang Habis")
    else:
        print("Masih ada uang")
    

if __name__ == "__main__":
    Output()

#Impelentasi Code Queue pada Studi kasus peminjaman baju di sebuah toko
#2307421016_Ardhiansyah Firdaus_TMJ-2A
class Peminjam:
    def __init__(self, no_antrian, nama_peminjam, brand_baju, tanggal_pengembalian):
        self.no_antrian = no_antrian
        #no_antrian: Atribut ini berisi nomor antrian peminjam.
        self.nama_peminjam = nama_peminjam
        # nama_peminjam: atribut ini berisi nama peminjam yang meminjam baju.
        self.brand_baju = brand_baju
        # nama_buku: atribut ini berisi nama buku yang dipinjam.
        self.tanggal_pengembalian = tanggal_pengembalian
        # tanggal_pengembalian: atribut ini berisi tanggal pengembalian buku yang dipinjam.
        self.next = None
        # next: atribut ini berisi referensi ke objek peminjam berikutnya dalam suatu daftar peminjam.

class Baju:
    # kelas Buku yang digunakan untuk menginisialisasi objek Baju.
    def __init__(self, max_size):
    #__init__yang digunakan untuk menginisialisasi atribut dari objek tersebut dibuat.
        self.front = None
        # front: antribut ini berisi referensi ke elemen depan dalam linked list baju.
        self.rear = None
        # rear: atribut ini berisi referensi ke elemen belakang dalam linked list baju.
        self.max_size = max_size
        # max_size: atribut ini berisi ukuran maksimum linked list buku yang dapat diisi.
        self.size = 0
        # size: atribut ini berisi ukuran sebenarnya linked list baju yang telah diisi.

    def enqueue(self, peminjam):
    # enqueue yang digunakan untuk menambahkan objek peminjam ke dalam linked list baju.
        if self.is_full():
            print("Antrian sudah penuh. Tidak bisa menambahkan Peminjam baru.")
            return
    # Jika antrian sudah penuh, maka kode ini akan mencetak pesan "Antrian sudah penuh".
    # Tidak bisa menambahkan peminjam baru.

        if self.is_empty():
            self.front = self.rear = peminjam
            # Jika antrian kosong, maka kode ini akan menginisialisasi front dan rear dengan objek peminjam yang baru ditambahkan.
        else:
            self.rear.next = peminjam
            self.rear = peminjam
        # (self.rear.next = peminjam), dan kemudian mengupdate rear dengan elemen yang baru ditambahkan (self.rear = peminjam).

        self.size += 1
        # self.size += 1. Ukuran antrian ini digunakan untuk menentukan apakah antrian sudah penuh atau tidak.
        print(f"Peminjam {peminjam.nama_peminjam} dengan nomor antrian {peminjam.no_antrian} - brand baju {peminjam.brand_baju} dengan tanggal pengembalian {peminjam.tanggal_pengembalian}")
        # mencetak pesan konfirmasi bahwa objek peminjam telah ditambahkan ke dalam antrian.

    def dequeue(self):
    # dequeue (menghapus elemen dari depan) pada linked list baju.
        if self.is_empty():
            print("Antrian kosong.")
            return
    # Jika antrian kosong, maka kode ini akan mencetak pesan

        peminjam = self.front
        self.front = self.front.next
        peminjam.next = None
        self.size -= 1
    # mengupdate front dengan elemen yang sebelumnya ada di depan (self.front = self.front.next)
    # Kemudian, kode ini menghapus referensi ke elemen yang sebelumnya ada di depan dengan mengupdate next menjadi None (peminjam.next = None).
    # mengurangi ukuran antrian dengan 1 menggunakan operasi self.size -= 1

        print(f"Peminjam {peminjam.nama_peminjam} dengan nomor antrian {peminjam.no_antrian} telah dilayani.")
    # Kode ini mencetak pesan konfirmasi bahwa elemen dari depan telah dihapus

        if self.is_empty():
            self.rear = None
    # Jika antrian kosong setelah menghapus elemen dari depan, maka kode ini akan mengupdate rear dengan
    # None untuk menghapus referensi ke elemen yang sebelumnya ada di belakang.

    def is_empty(self):
    # is_empty digunakan untuk menentukan apakah antrian kosong.
        return self.size == 0
    # Kode ini mengembalikaan nila true jika ukuran antrian (self.size) sama dengan 0, dan
    # False jika ukuran antrian tidak sama dengan 0. Jika antrian kosong, maka metode ini
    # akan mengembalikan nilai true, yang berarti antrian tidak memiliki elemen.

    def is_full(self):
    # is_full digunakan untuk menentukan apakah antrian penuh.
        return self.size >= self.max_size
    # kode ini mengembalikan nilai true jika ukuran antrian(self.size) sama dengan atau lebih besar
    # dari ukuran maksimun (self.max_size), dan false jika ukuran antrian tidak sama dengan atau lebih
    # besar dari ukuran maksimum. jika antrian penuh, maka metode ini akan mengembalikan nilai true,
    # yang berarti antrian tidak dapat menampung elemen tambahan.

def main():
    antrian_baju = Baju(5)
    # membuat objek antrian toko kopi dengan maksimum 5 peminjam

    while True:
    # kode ini memiliki loop utama yang berulang sampai pengguna memilih opsi keluar
        print("\n")
        print("1. Menambahkan Peminjam ke Antrian")
        print("2. Hapus Peminjam dari Antrian")
        print("3. Keluar")
        # pilihan pengguna

        pilihan = int(input("Masukkan Pilihan: "))

        if pilihan == 1:
            no_antrian = int(input("Nomor Antrian: "))
            nama_peminjam = input("Nama Peminjam: ")
            brand_baju = input("Masukkan merek/brand baju: ")
            tanggal_pengembalian = input("Tanggal Pengembalian: ")

            peminjam = Peminjam(no_antrian, nama_peminjam, brand_baju, tanggal_pengembalian)
            antrian_baju.enqueue(peminjam)

            # kode ini meminta pengguna untuk memasukan nomor antrian, nama peminjam, nama, buku, dan
            # tanggal pengembalian. kemudian, kode ini membuat objek peminjam dengan informasi yang
            # diberikan dan menambahkan objek tersebut ke antrian menggunakan metode enqueue.

        elif pilihan == 2:
            antrian_baju.dequeue()
        # kode ini mengahapus peminjam dari antrian menggunakan metode dequeue.

        elif pilihan == 3:
            antrian_baju.dequeue()
            break
        # kode ini menghentikan loop utama dan mengakhiri program.

        else:
            print("Pilihan tidak tersedia. silahkan coba lagi.")
        # kode ini mencetak pesan jika pengguna memilih opsi yang tidak tersedia.


if __name__ == "__main__":
    main()

# # ========================== Stack ==========================
# # Impelentasi Code Queue pada atudi kasus pengelola baju di sebuah toko
# # #2307421016_Ardhiansyah Firdaus_TMJ-2A

# class Node:
# # class node adalah sebuah class yang digunakan untuk membuat node-node dalam linked list.
#     def __init__(self, item):
#     # __init__ adalah sebuah method yang digunakan untuk membuat objek dari class node.
#         self.item = item
#         self.next = None
#         # item akan disimpan dalam variabel self.item, dan next akan disimpan dalam variabel
#         # self.next dengan nilai none.

# class Item:
# # class item adalah sebuah class yang digunakan untuk membuat objek dari item-item yang akan
# # disimpan dalam linked list.
#     def __init__(self, no_item, nama_item, harga_item):
#     # __init__ adalah sebuah method yang digunakan untuk membuat objek dari class item.
#         self.no_item = no_item
#         self.nama_item = nama_item
#         self.harga_item = harga_item
#     # no_item akan disimpan dalam atribut self.no_item, nama_item akan disimpan dalam
#     # atribut self.nama_item, dan harga_item disimpan dalam atribut self.harga_item.

# class Stack:
# # class stack adalah sebuah class yang digunakan untuk membuat objek dari stack, yaitu 
# # sebuah struktur data yang memungkinkan pengguna untuk menambahkan, menghapus, dan melihat
# # item-item yang sedang menunggu
#     def __init__(self):
#     # __init__ adalah sebuah method yang digunakan untuk membuat objek dari class stack.
#     # self, yang digunakan untuk menginisialisasi atribut-atribut dari class stack
#         self.top = None
#         # top akan disimpan dengan nilai none, yang berarti stack masih kosong.
#     def push(self, item):
#     # push adalah sebuah method yang digunakan untuk menambahkan item baru ke dalam stack.
#         new_node = Node(item)
#         new_node.next = self.top
#         self.top = new_node
#     # Objek node akan dibuat dengan menggunakan parameter item, dan atribut next dari objek node
#     # akan diset dengan nilai self.top. Kemudian, atribut top dari objek stack akan diset dengan nilai objek node yang baru dibuat

#     def pop(self):
#     # pop adalah sebuah method yang digunakan untuk menghapus item teratas dari stack
#         if self.is_empty():
#             print("Stack kosong. Tidak ada item yang bisa dihapus")
#             return None
#     # Jika stack masih kosong, maka method akan mencetak pesan "stack kosong"
#         popped_item = self.top.item
#         self.top = self.top.next
#         return popped_item
#     # jika stack tidak kosong, maka method akan menghapus item teratas dari stack
#     # dengan mengubah atribut top dari objek stack menjadi objek node yang berikutanya,
#     # dan mengembalikan nilai item yang dihapus.

#     def peek(self):
#     # peek adalah sebuah method yang digunakan untuk melihat item teratas dari stack tanpa menghapusnya.
#         if self.is_empty():
#             print("Stack kosong. Tidak ada item yang bisa dilihat.")
#             return None
#     # Jika stack masih kosong, maka method akan mencetak pesan "Stack kosong. Tidak ada item yang bisa dilihat." dan mengembalikan nilai None.
#         return self.top.item
#     # Jika stack tidak kosong, maka method akan mengembalikan nilai item teratas dari stack.
#     def is_empty(self):
#         return self.top == None

# def main():
# # main adalah untuk membuat objek dari class stack dan menambahkan beberapa item ke dalam stack.
#     stack_item = Stack()
#     # Membuat objek dari class stack dan menamainya sebagai stack_item

#     stack_item.push(Item(1, "Baju", 240000))
#     stack_item.push(Item(2, "Topi", 82000))
#     stack_item.push(Item(3, "Jacket", 2000000))
#     stack_item.push(Item(4, "Hoodie", 1500000))
#     stack_item.push(Item(5, "Blazer", 540000))
#     # Menambahkan beberapa item ke dalam stack

#     print("Daftar Item:")
#     print("1. Baju")
#     print("2. Topi")
#     print("3. Jaket")
#     print("4. Hoodie")
#     print("5. Blazer\n")
#     # Menampilkan list item

#     item_paling_atas = stack_item.peek()
#     # Mengembalikan item teratas dari stack menggunakan method peek.
#     if item_paling_atas:
#         print("Item paling atas dalam stack:", item_paling_atas.nama_item)
#     # Jika item teratas ada, maka fungsi ini akan mencetak pesan
#     popped_item = stack_item.pop()
#     # menghapus item teratas dari stack menggunakan method pop
#     if popped_item:
#         print("item paling atas telah diambil dan dihapus dari stack:", popped_item.nama_item)
#         # jika item teratas dihapus, maka fungsi ini akan mencetak pesan
#     if stack_item.is_empty():
#         print("Stack Kosong.")
#     # Jika stack masih kosong, maka fungsi ini akan mencetak pesan
#     else:
#         print("stack tidak kosong.")
#     # Jika stack tidak kosong, maka fungsi ini akan mencetak pesan

# if __name__ == "__main__":
#     main()
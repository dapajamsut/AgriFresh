#LIST
pegawai_list = [
    {"id_pegawai": "001", "nama_pegawai": "nabil", "password": "123"},
    {"id_pegawai": "002", "nama_pegawai": "paw", "password": "456"},
    {"id_pegawai": "003", "nama_pegawai": "pais", "password": "789"}
]

#ARRAY
# Daftar Jamaah menggunakan Antrian (Queue) sebagai list
antrian_jamaah = []

#ARRAY
# menambahkan Jamaah ke dalam antrian
def tambah_jamaah(nama_lengkap, nik, alamat, nohp, nowa, email, password, umur, jenkel, pernah_haji, provinsi, paket, harga):
    jamaah = {
        "id_jamaah": len(antrian_jamaah) + 1,
        "nama_lengkap": nama_lengkap,
        "nik": nik,
        "alamat": alamat,
        "nohp": nohp,
        "nowa": nowa,
        "email": email,
        "password": password,
        "umur": umur,
        "jenkel": jenkel,
        "pernah_haji": pernah_haji,
        "provinsi": provinsi,
        "paket": paket,
        "status_jamaah": "Pending",
        "harga": harga
    }
    antrian_jamaah.append(jamaah)

#QUEUE
# menampilkan antrian Jamaah
def tampilkan_antrian():
    if len(antrian_jamaah) > 0:
        print("Antrian Jamaah:")
        for i, jamaah in enumerate(antrian_jamaah, start=1):
            print(f"{i}. ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, NIK: {jamaah['nik']}, Jenis Kelamin: {jamaah['jenkel']}, Email: {jamaah['email']}, No HP: {jamaah['nohp']}, Status: {jamaah['status_jamaah']}, Paket: {jamaah['paket']}")
    else:
        print("Antrian kosong")

#QUEUE
# menampilkan Jamaah berdasarkan prioritas umur dan pernah haji
def tampilkan_prioritas_umur():
    # Mengambil hanya jamaah dengan paket Haji
    antrian_jamaah_haji = [jamaah for jamaah in antrian_jamaah if jamaah['paket'] == "Haji"]
    
    # Mengurutkan antrian jamaah Haji berdasarkan umur dan prioritas pernah haji
    antrian_jamaah_sorted = sorted(antrian_jamaah_haji, key=lambda x: (x['umur'], x['pernah_haji']), reverse=True)
    
    for jamaah in antrian_jamaah_sorted:
        umur = jamaah['umur']
        pernah_haji = jamaah['pernah_haji']
        if 80 <= umur <= 100 and pernah_haji == 1:
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Ya, Prioritas 2")
        elif 80 <= umur <= 100 and pernah_haji == 2:
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Tidak, Prioritas 1")
        elif 50 <= umur <= 79 and pernah_haji == 1: 
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Ya, Prioritas 2")
        elif 50 <= umur <= 79 and pernah_haji == 2:
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Tidak, Prioritas 2")
        elif 35 <= umur <= 49 and pernah_haji == 1: 
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Ya, Prioritas 2")
        elif 35 <= umur <= 49 and pernah_haji == 2:
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Tidak, Prioritas 2")
        elif 26 <= umur <= 34 and pernah_haji == 1:
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Ya, Prioritas 3")
        elif 26 <= umur <= 34 and pernah_haji == 2:
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Tidak, Prioritas 2")
        elif 17 <= umur <= 26 and pernah_haji == 1:
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Ya, Prioritas 3")
        elif 17 <= umur <= 26 and pernah_haji == 2:
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, Umur: {umur}, Pernah Haji: Tidak, Prioritas 3")

#LIST
# fitur pencarian
def pencarian():
    kata_kunci = input("Masukkan Nama Lengkap : ")
                       
    if kata_kunci:
        hasil = [jamaah for jamaah in antrian_jamaah if kata_kunci.lower() in jamaah['nama_lengkap'].lower()]
    else:
        print("Kriteria tidak valid.")
        return

    if hasil:
        for jamaah in hasil:
            print(f"ID Jamaah: {jamaah['id_jamaah']}, Nama Lengkap: {jamaah['nama_lengkap']}, NIK: {jamaah['nik']}, Email: {jamaah['email']}, No HP: {jamaah['nohp']}, Status: {jamaah['status_jamaah']}, Harga: {jamaah['harga']}")
    else:
        print("Jamaah tidak ditemukan.")

#LIST
def berangkatkan_jamaah():
    pilihan = input("Jamaah Paket apa yang ingin diberangkatkan: ")
    if pilihan == "haji":
    # Mengambil hanya jamaah dengan paket Haji yang masih Pending
        antrian_jamaah_haji = [jamaah for jamaah in antrian_jamaah if jamaah['paket'] == "Haji" and jamaah['status_jamaah'] == "Pending"]
        antrian_jamaah_sorted = sorted(antrian_jamaah_haji, key=lambda x: (x['umur'], x['pernah_haji']), reverse=True)
        if len(antrian_jamaah_sorted) > 0:
            jamaah_diberangkatkan = antrian_jamaah_sorted[0]
            jamaah_diberangkatkan['status_jamaah'] = "Berangkat"
            print(f"Jamaah dengan ID {jamaah_diberangkatkan['id_jamaah']} dan Nama {jamaah_diberangkatkan['nama_lengkap']} berhasil diberangkatkan!")
        else:
            print("Tidak ada jamaah yang siap diberangkatkan.")
    
    elif pilihan == "umroh":
        antrian_jamaah_umroh = [jamaah for jamaah in antrian_jamaah if jamaah['paket'] == "Umroh" and jamaah['status_jamaah'] == "Pending"]
        antrian_jamaah_sorted = sorted(antrian_jamaah_umroh, key=lambda x: (x['id_jamaah']))                  
        if len(antrian_jamaah_sorted) > 0:
            jamaah_diberangkatkan = antrian_jamaah_sorted[0]
            jamaah_diberangkatkan['status_jamaah'] = "Berangkat"
            print(f"Jamaah dengan ID {jamaah_diberangkatkan['id_jamaah']} dan Nama {jamaah_diberangkatkan['nama_lengkap']} berhasil diberangkatkan!")
        else:
            print("Tidak ada jamaah yang siap diberangkatkan.")
    else:
        print("Tidak ada jamaah yang siap diberangkatkan.")

#LIST
# Login Pegawai
while True:
    id_pegawai_input = input("Masukkan ID Pegawai: ")
    nama_pegawai_input = input("Masukkan Nama Pegawai: ")
    password_input = input("Masukkan Password Pegawai: ")

    pegawai_valid = any(p['id_pegawai'] == id_pegawai_input and p['nama_pegawai'] == nama_pegawai_input and p['password'] == password_input for p in pegawai_list)

    if pegawai_valid:
        print("Login Berhasil!")
        break
    else:
        print("ID Pegawai, Nama Pegawai, atau Password Salah. Silahkan coba lagi.")

#ARRAY
# Menu Tambah Jamaah
while True:
    print("\nMenu Tambah Jamaah")
    print("1. Tambah Jamaah")
    print("2. Tampilkan Antrian")
    print("3. Tampilkan Prioritas")
    print("4. Cari")
    print("5. Berangkatkan Jamaah")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        # Input Data Jamaah
        nama_lengkap = input("Masukkan Nama Lengkap: ")
        nik = input("Masukkan NIK: ")
        alamat = input("Masukkan Alamat: ")
        nohp = input("Masukkan No HP: ")
        nowa = input("Masukkan No WA: ")
        email = input("Masukkan Email: ")
        password = input("Masukkan Password: ")
        umur = int(input("Masukkan Umur: "))
        jenkel = input("Masukkan Jenis Kelamin (L/P): ")
        provinsi = input("Masukkan Provinsi: ")
        print("Pilih Paket:")
        print("1. Haji")
        print("2. Umroh")
        pilihan_paket = input("Pilih paket (1/2): ")
        if pilihan_paket == '1':
            pernah_haji = int(input("Pernah Haji Sebelumnya? (1. Ya / 2. Tidak): "))
            paket = "Haji"
            harga = 20000000
        elif pilihan_paket == '2':
            pernah_haji = 2  # Tidak pernah haji
            paket = "Umroh"
            harga = 15000000
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")
            continue

        if umur > 58:
            print ("Maaf kamu tidak bisa mengikuti program ini")
            break

        # Menambahkan Jamaah ke dalam antrian
        tambah_jamaah(nama_lengkap, nik, alamat, nohp, nowa, email, password, umur, jenkel, pernah_haji, provinsi, paket, harga)
        print("Jamaah berhasil ditambahkan!")

    elif pilihan == '2':
        tampilkan_antrian()

    elif pilihan == '3':
        tampilkan_prioritas_umur()

    elif pilihan == "4":
        pencarian()

    elif pilihan == "5":
        berangkatkan_jamaah()

    elif pilihan == '6':
        break

    else:
        print("Pilihan tidak valid. Silahkan coba lagi.")

print("Program Selesai.")
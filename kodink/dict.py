# nama = "dapa"
# umur = 19
# thisdict = {
#   "nama": nama,
#   "umur": umur,
#   "tahun": 2005,
#   "pendidikan": ['SD', 'SMP','SMA'],
#   "Alamat" : "Jln. Beringin"
# }
# print(thisdict)
# print(len(thisdict))
# print(thisdict['nama'])


# thisdict2 = dict(nama = nama, umur = umur, tahun = "2005", pendidikan = ['SD', 'SMP', 'SMA'], Alamat = "Jln. Beringin")
# dict3 = dict(thisdict)
# print((dict3))
# print((thisdict2))

# for key, value in thisdict.items():
#     print(key, "= ", value)


# Input = ["Ford", "Volvo", "BMW"]
# Output: {'Ford': 1, 'Volvo': 2, 'BMW': 3}
#langkah2 menurut bahasa kalian sendiri

# membuat inputan
cars = input("Masukkan nama-nama mobil, dipisahkan oleh koma: ")
# untuk
input_list = cars.split(", ")

dict = {}

value = 1

for mobil in input_list:
    dict[mobil] = value
    value += 1

print(dict)
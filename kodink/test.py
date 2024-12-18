class heros:
    def __init__(self, name, type, role):
        self.id = id
        self.name = name
        self.type = type
        self.role = role

    # def skill1(self):
    #     print("Memulihkan HP tim")
    #     print("Memberikan efek slow")
    # def skill2(self):
    #     print("Menembak kedepan")
    #     print("Stun lawan")

    def create(create):
        create.name= input("Masukkan nama hero: ")
        create.type= input("Masukkan tipe hero: ")
        create.role= input("Masukkan role hero: ")

    def read(read):
        print("")
        print ("[ID] - [Nama] - [Tipe] - [Role]")
        print(read.id, "-",read.name, "-",read.type, "-",read.role)

    def update(update):
        id = id = int(input("Pilih Data yang Ingin diupdate : "))
        id = id - 1
        array_hero.pop(id)
        name= input("Masukkan nama hero: ")
        type= input("Masukkan tipe hero: ")
        role= input("Masukkan role hero: ")
        Hero = hero(name, type, role)
        array_hero.append(Hero)


    
array_hero = []
while True:
    id = 0
    print("\n1. Create [Masukkan data] ")
    print("2. Read   [Tampilkan data]")
    print("3. Update [Ubah data]   ")
    print("4. Delete [Hapus data]    ")
    print("5. EXIT")
    menu = (input("Pilih Menu : "))

    if menu == "1":
        Hero = heros("", "", "")
        Hero.create()
        array_hero.append(Hero)
    
    elif menu == "2":
        print("")
        print ("[ID] - [Nama] - [Tipe] - [Role]")
        for data in array_hero:
            id = id + 1
            print(id, "-",data.name, "-",data.type, "-",data.role)
    
    elif menu == "3":
        for data in array_hero:
            id = id = int(input("Pilih Data yang Ingin diupdate : "))
            id = id - 1
            array_hero.pop(id)
            name= input("Masukkan nama hero: ")
            type= input("Masukkan tipe hero: ")
            role= input("Masukkan role hero: ")
            Hero = heros(name, type, role)
            array_hero.append(Hero)
            break

    elif menu == "4":
        for data in array_hero:
            hapus = int(input("Pilih Data yang Ingin dihapus : "))
            hapus = hapus - 1
            array_hero.pop(hapus)
            break
    else:
     break





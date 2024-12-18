class hero:
    def __init__(self, name, type, role):
        self.name = name
        self.type = type
        self.role = role

    def skill1(self):
        print("Memulihkan HP tim")
        print("Memberikan efek slow")
    def skill2(self):
        print("Menembak kedepan")
        print("Stun lawan")

array_hero = []
id = 0
while True:
    name= input("Masukkan nama hero: ")
    type= input("Masukkan tipe hero: ")
    role= input("Masukkan role hero: ")

    Hero= hero(name, type, role)
    array_hero.append(Hero)

    a = input("Ketik X untuk Stop, Enter untuk Continue : ")
    a.lower()
    if a != "":
        break
print("")
print ("[ID] - [Nama] - [Tipe] - [Role]")
for data in array_hero:
    id = id + 1
    print(id, "-",data.name, "-",data.type, "-",data.role)




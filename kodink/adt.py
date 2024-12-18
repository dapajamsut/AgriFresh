
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
# ========================================
array_hero = []
estes = hero(name= "Estes", type = "Magic", role = "Support")
clint = hero(name= "Clint", type = "Physical", role = "Marksman")
array_hero.append(estes)
array_hero.append(clint)


for data in array_hero:
    print(data.name, "-", data.type, "-",data.role)


print(estes.name)
print(estes.type)
print(estes.role)
print(estes.skill1())
print(clint.name)
print(clint.type)
print(clint.role)
print(clint.skill2())


# class Person():
#     name = "ryo"

# print(Person.name)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
         return f"Hai, nama saya {self.name}, umur {self.age}"

    #     self.__address = address

    # def greeting(self):
    #     return f"Hai, nama saya {self.name}, umur {self.age}, alamat di {self.getAddress}"

    # def setAddress(self, newAddress):
    #     self.__address = newAddress
    #     return self.__address

    # def getAddress(self):
    #     return self.__address
    
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def greeting(self):
#         return f"Hai, saya mahasiswa dengan nama {self.name}, dengan umur {self.age}"
#     # def __del__(self):
#     #     print(f"{self.name} destroyed")

# ryo = Student
# ryo = Person("Ryo", 21, "Salatiga")
# print(ryo.getAddress())
# ryo.setAddress("Surakarta")
# print(ryo.getAddress())
# roy  =  Person("roy", 21, "Gunkid")
# del roy

# print(ryo.name)
# print(ryo.getAddress())
    # print(f"Nama saya adalah {self.name} umurnya {self.umur}")

class Kendaraan:
    def __init__(self, Jenis):
        self.Jenis = str(Jenis)
    
    # def __str__(self) -> str:
    #     return self.Jenis

class RodaDua(Kendaraan):
    def __init__(self, Jenis):
        super().__init__(Jenis)

class RodaEmpat(Kendaraan):
    def __init__(self, Jenis):
        super().__init__(Jenis)

kendaraanRodaDua = RodaDua('Honda')
print(kendaraanRodaDua.Jenis)
kendaraanRodaEmpat = RodaEmpat('Toyota')
print(kendaraanRodaEmpat.Jenis)

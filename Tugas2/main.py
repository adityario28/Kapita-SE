import volume as vol

#1. fungsi untuk mencari bilangan prima
def prima(awal, akhir):
    hasil = []
    akhir += 1
    for angka in range(awal, akhir):
        if all(angka % i != 0 for i in range(2,angka)):
            hasil.append(angka)
    return hasil

print("1. Bilangan prima dari range 1-35 adalah : ", prima(1,31))


#2. fungsi untuk mencari bilangan ganjil
def ganjil(awal, akhir):
    hasil = []
    akhir += 1
    for angka in range(awal, akhir):
        if angka % 2 != 0:
            hasil.append(angka)
    return hasil

print("2. Bilangan ganjil dari range 1-48 adlaah : ", ganjil(1,48))


#3. fungsi untuk mencari bilangan prima ganjil

def primaganjil(awal, akhir):
    bil_prima = prima(awal, akhir)
    bil_ganjil = ganjil (awal, akhir)
    return [angka for angka in bil_prima if angka in bil_ganjil]

print("3. Bilangan prima ganjil dari range 1-35 adalah : ", primaganjil(1,10))


#4. fungsi membalikkan karakter input string
def kebalikan(input):
    return input[::-1]

print("4. Kata rexus apabila ditulis secara berkebalikan adalah : ", kebalikan("rexus"))


#5. fungsi untuk mengecek palindrom sebuah kata
masukan = "kakak"

def palindrom(input):
    return input == input[::-1]

print("5. Kata", masukan, "adalah palindrom (T/F) :", palindrom(masukan))


#6. fungsi untuk mencari selisih dari angka tertinggi dan terendah pada suatu list
bilangan = [12,41,25,23,29,33,39,40,82,37,98,27,11,9,98,40,2] #max 98, min 2

def selisih(angka):
    return max(angka) - min(angka)

print("6. Selisih dari bilangan max (98) dan min (2) adalah : ", selisih(bilangan))


#7. fungsi menghitung huruf vokal dan konsonan

vowel = "aiueoAIUEO"

def vow(kata):
    jumlah_vokal = 0
    jumlah_konsonan = 0
    for huruf in kata:
        if huruf in vowel:
            jumlah_vokal += 1
        elif huruf.isalpha():
            jumlah_konsonan += 1
    return jumlah_vokal, jumlah_konsonan
    # return jumlah_vokal, jumlah_konsonan

print("7. Jumlah huruf vokal dan konsonan adalah =", vow("you are my everything"))


#8. fungsi untuk mencari bilangan tertentu beserta index
bilangan = [12,41,25,23,29,33,39,40,82,37,98,27,11,9,98,40,2]

def spec(list, target):
    if target in list:
        return {"Status" : True, "Index" : list.index(target)}
    else:
        return {"Status" : False, "Index" : None}

print("8. Bilangan yang dicari :", spec(bilangan, 2))

#9. fungsi aritmatika
def aritmatik(op, angka1=1, angka2=1):
    try:
        if not isinstance(angka1, int) or not isinstance(angka2, int):
            raise TypeError("Bilangan harus angka")
    
        if op == "+":
            return angka1 + angka2
        elif op == "-":
            return angka1 - angka2
        elif op == "*":
            return angka1 * angka2
        elif op == "/":
            return round((angka1 / angka2), 2)
        else:
            return "Operator salah coy"
        
    except ZeroDivisionError:
        return "tidak bisa membagi 0"
    except TypeError as error:
        return error

print("9. Bilangan yang dicari :", aritmatik("/", 3, 9))


#10. modul volume
print("10. Volume Kubus dengan sisi 4 :", vol.kubus(4))
print("    Volume Balok :", vol.balok(5,7,6))
print("    Volume Limas segi 4 :", vol.limas4(4, 4, 3))
print("    Volume Prisma :", vol.prisma(5,10,8))
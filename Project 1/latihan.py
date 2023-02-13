# 1. Buatlah fungsi untuk menghitung total bilangan pada list, tidak boleh pakai built in function
#    input  : list bilangan
#    output : total bilangan (int)
bilangan = [1,3,5,7,9]

def hitungtotal(bilangan):
        total = 0
        for bil in bilangan:
            total += bil
        return total 

print(hitungtotal(bilangan)) #hasil 25 = 1+3+5+7+9

# 2. Buatlah fungsi untuk menghitung volume balok
#    input : panjang, lebar , tinggi (int)
#    output: volume balok (int)
def hitungVolumeBalok(panjang, lebar, tinggi):
      return panjang * lebar * tinggi

print(hitungVolumeBalok(5,7,6)) #rumus balok panjang * lebar * tinggi



# 3. Buatlah fungsi untuk mencetak kalimat perkenalan seperti berikut:
#    "Halo, nama saya {} dan saya berasal dari {kota asal}" 
#    input  : nama
#    output : print string 
def intro(nama, kota):
      return "Halo, nama saya {} dan saya berasal dari {}".format(nama, kota)

print(intro("Ryo", "Salatiga"))


# 4. Buatlah fungsi untuk membuat kalimat panjang dari sebuah list
#    input  : list string
#    output : string
kata = ["Saaatnya", " Mengkodink"]

def kalimat(kata):
    hasil = ""
    for ka in kata:
        hasil += ka
    return hasil

print(kalimat(kata))


# 5. Buatlah fungsi untuk mencetak bilangan ganjil yang ada pada sebuah list
#    input  : list bilangan
#    output : print list bilangan ganjil
angka = [2, 3, 7, 6, 0, 4, 3, 25, 93, 25, 24]
def ganjil(angka):
    ganj = []
    for ang in angka:
          if ang % 2 != 0:
                ganj.append(ang)
    return ganj

print(ganjil(angka))

def total(*bilangan, **keywords):
     hitung = 0

     for bil in bilangan:
          hitung += bil

     for key in keywords:
          hitung += keywords[key]
     return hitung

print('versi 1 : ', total(1,2,3,4,5)) # versi berapapun parameter yg masuk
print('versi 2 : ', total(daging = 2, sayur = 10, buah = 3)) # versi parameter apapun yg boleh masuk
print('versi 3 : ', total(7,8,9,sayur = 10, buah = 3, daging =2)) # versi gabungan + kwargs dibalik
# ================================================================================================================ #
def contKwargs(**kwargs):
     #kwargs
     varParamA = kwargs.get('paramA', 100)
     print(varParamA)

contKwargs(paramA = 200)
contKwargs()


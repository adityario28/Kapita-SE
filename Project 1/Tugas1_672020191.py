print("Nama : Caroluce Ricky Harkris Nowo")
print("NIM  : 672020191")
print("---------------- JAWABAN-------------------")

priceTuple = (10000, 13000, 8000, 9000, 16000)
fruitTuple = ('mangga', 'apel', 'jeruk', 'semangka', 'anggur')

# Soal 1
# Buatlah dictionary dengan nama fruitDict dari kedua tuple di atas sehingga menjadi
# {'mangga': 10000, 'apel': 13000, dst...}
# -------------------------- Jawaban --------------------------------------------------

combineFruit = zip(fruitTuple, priceTuple)  # Melakukan join pada 2 tuple
fruitDict = dict(combineFruit)  # Membuat dictionary dengan tuple combineFruit
print("Jawaban 1 :", fruitDict)

# ====================================================================================
# Soal 2
# Dari dictionary fruitDict yang sudah terbuat, hitunglah rata-rata harga buah
# -------------------------- Jawaban --------------------------------------------------

totalFruitPrice = sum(fruitDict.values())  # Menjumlahkan semua values pada dictionary
amountFruit = len(fruitDict)  # Menghitung panjang dictionary
averageFruitPrice = totalFruitPrice / amountFruit
print("Jawaban 2 :", averageFruitPrice)

# ====================================================================================

test_list = [4, 1, {'tiga': 3, 'tujuh': 7}, (9, 8, [2, 5]), 6]

# Soal 3
# Dari test_list di atas, buatlah sebuah string dengan isi : '1 2 3 4 5 6 7 8 9'
# -------------------------- Jawaban --------------------------------------------------

stringList = []  # Mendeklarasikan variable list


def convert_dict(a_dict):  # Merubah tipe data dictionary ke list kemudian menggabungkannya
    for value in range(len(a_dict)):
        stringList.append(list(a_dict.values())[value])


def convert_list(a_list):  # Menggabungkan tipe data list
    for value in range(len(a_list)):
        stringList.append(a_list[value])


def find_type(a_list):  # Mengelompokkan data sesuai dengan tipenya
    for data in a_list:
        if isinstance(data, int):
            stringList.append(data)  # Memasukkan data berbentuk integer kedalam list
        if isinstance(data, dict):
            convert_dict(data)  # Memanggil convert_dict dengan argumen bertipe data dictionary
        if isinstance(data, tuple):
            find_type(list(data))  # Merubah tipe data tuple menjadi list dan memanggil kembali find_type
        if isinstance(data, list):
            convert_list(data)  # Memanggil convert_list dengan argumen bertipe data list


find_type(test_list)  # Memanggil find_type dengan parameter list yang ingin di rubah
sortList = sorted(stringList)  # Mengurutkan data pada list
convertString = ' '.join(str(convert) for convert in sortList)  # Merubah data dan list ke string
print("Jawaban 3 :", convertString)

# =====================================================================================

# Soal 4
# Dari string tersebut pecahlah kembali menjadi sebuah list yang berisi integer, kemudian hitung nilai total dari
# isi list
# -------------------------- Jawaban --------------------------------------------------

convertList = list(convertString.split(" "))  # Memecah string ke dalam list
newList = [eval(a_int) for a_int in convertList]  # Merubah isi list ke bentuk integer
totalList = sum(newList)  # Menjumlah semua data pada list
print("Jawaban 4 :", totalList)

# =====================================================================================

str1 = "teknik informatika fakultas teknologi informasi universitas kristen satya wacana"
str2 = "sedang belajar bahasa pemrograman"
tupleMahasiswa = ('DEVA', 'IVAN')
dictKelas = {'IF001': 'Kapita Selekta', 'IF002': 'Matematika Diskrit', 'IF003': 'Pemrograman Web'}
listPython = ['p', 'y', 't', 'h', 'o', 'n']

# Soal 5
# Dari variable di atas, buatlah string sebagai berikut
# - 'Hari ini Deva tidak mengikuti mata kuliah Pemrograman Web'
# - 'Matematika Diskrit IF002 adalah salah satu mata kuliah di progdi Teknik Informatika Universitas Kristen Satya
# Wacana'
# - 'Ivan belajar bahasa pemrograman Python di mata kuliah Kapita Selekta'
# -------------------------- Jawaban --------------------------------------------------

stringDeva = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"
string1 = stringDeva.format(listPython[3].upper(), str2[3], str2[13], str1[4], str1[6], str1[4],
                            str1[3:5], str1[6], tupleMahasiswa[0].capitalize(), str1[6], listPython[2],
                            str1[4], str2[2], str2[3], str1[2], str1[6], str1[12], str2[1], str1[3], str2[5],
                            str1[4], str1[2], str1[22], str1[14:16], str1[6], str1[12:15], str2[3], str1[6],
                            str1[5], str1[22:24], str1[4], str2[3], listPython[3], str1[6], dictKelas['IF003'])

stringMatematika = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"
string2 = stringMatematika.format(dictKelas['IF002'], str1[6], list(dictKelas.keys())[1], str1[6], str2[3],
                                  str2[2], str2[3], str2[9], str2[3], listPython[3], str1[6], str2[0], str2[3],
                                  str2[9], str2[3], listPython[3], str1[67:71], str1[22], str1[6],
                                  string1.split(" ")[5], str1[6], string1.split(" ")[6], str1[6], str2[2], str1[4],
                                  str1[6], listPython[0], str2[25:28], str2[2], str1[4], str1[6], str1[0:18].title(),
                                  str1[47:].title())

stringIvan = "{}{}{}{}{}{}{}"
string3 = stringIvan.format(tupleMahasiswa[1].capitalize(), str2[6:], str1[6], ''.join(listPython).capitalize(),
                            string2[54:58], string1[30:42], dictKelas['IF001'])

print("Jawaban 5 :", string1)
print("          :", string2)
print("          :", string3)

# =====================================================================================

listHari = ['Senin', 'Rabu', 'Jumat', 'Sabtu']

# Soal 6
# Tambahkan hari 'Selasa', 'Kamis', dan 'Minggu', sehingga listHari tersebut menjadi
# ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
# -------------------------- Jawaban --------------------------------------------------

listHari.insert(1, 'Selasa')  # Memasukkan selasa pada index ke 1
listHari.insert(3, 'Kamis')   # Memasukkan kamis pada index ke 3
listHari.append('Minggu')     # Memasukkan minggu pada index terakhir pada list
print("Jawaban 6 :", listHari)

# =====================================================================================
# Soal 7
# Hapus hari 'Sabtu' dan 'Minggu' dari listHari, kemudian copy list listHari ke variable tupleHariKerja dengan
# tipe data tuple
# -------------------------- Jawaban --------------------------------------------------

listHari.pop()  # Menghapus list terakhir yaitu minggu
listHari.pop()  # Menghapus list terakhir yaitu sabtu
tupleHariKerja = tuple(listHari)  # Merubah list ke bentuk tuple
print("Jawaban 7 :", tupleHariKerja)

# =====================================================================================

#####================================================================================#####
priceTuple = (10000, 13000, 8000, 9000, 16000)
fruitTuple = ('mangga', 'apel', 'jeruk', 'semangka', 'anggur')

# Soal 1
# Buatlah dictionary dengan nama fruitDict dari kedua tuple di atas sehingga menjadi
# {'mangga': 10000, 'apel': 13000, dst...}

# Jawaban 1
fruitDict = {fruit:price for [fruit, price] in zip(fruitTuple, priceTuple)} #digunakan untuk menggabungkan 2 tuple ke dalam sebuah directory
print("Dictionary : ", fruitDict)
#####================================================================================#####

print()

#####================================================================================#####
# Soal 2
# Dari dictionary fruitDict yang sudah terbuat, hitunglah rata-rata harga buah

# Jawaban 2
nilai = list(fruitDict.values()) #digunakan untuk mengekstrak value pada fruiDict, dan meletakannya ke nilai dalam format list.
avg = sum(nilai) / len(nilai) #lalu proses penghitungan rata-rata dilakukan dengan membagi nilai total pada list nilai, dengan panjang nilai
print("Rata-rata harga buah : ", avg)
#####================================================================================#####

print()

#####================================================================================#####
test_list = [4, 1, {'tiga': 3, 'tujuh': 7}, (9, 8, [2, 5]), 6]
# Soal 3
# Dari test_list di atas, buatlah sebuah string dengan isi : '1 2 3 4 5 6 7 8 9'

# Jawaban 3
hasil = [] #Membuat sebuah list kosong sebagai wadah

for i in test_list: #melakukan perulangan pada list test_list
    if isinstance(i, int): #apabila i bertipe data int, maka i akan ditambahkan pada list hasil
        hasil.append(i)
    elif isinstance(i, tuple): #apabila i bertipe tuple, maka akan dilakukan perulangan
        for index in i: #perulangan digunakan untuk mengekstrak nilai dalam tuple
            if isinstance(index, list): #dan apabila nilai pada tuple adalah bertipe list
                for num in index : 
                    hasil.append(num) #maka nilai dalam list akan dimasukkan ke dalam list hasil
            elif isinstance(index, int): #namun apabila nilai bernilai integer dalam tuple
                hasil.append(index) #maka nilai akan langsung dimasukkan ke dalam list hasil
    elif isinstance(i, dict): #kemudiana apabila i bertipe dictionary, maka value dari i akan ditambahkan ke dalam list hasil
        hasil.extend(i.values())

hasil = sorted(hasil) #melakukan penyortiran secara ascending (kecil ke besar)
hasil = ' '.join(str(index) for index in hasil) #kemudian melakukan konversi dari list ke bentuk string
print("String : " + hasil)
#####================================================================================#####

print()

#####================================================================================#####
# Soal 4
# Dari string tersebut pecahlah kembali menjadi sebuah list yang berisi integer, kemudian hitung nilai total dari isi list

# Jawaban 4
hasil_list = [int(index) for index in hasil.split()] #default parameter split adalah menggunakan spasi, apabila menggunakan format lain dalam susunan, gunakan hasil_list = hasil.split(',') <- untuk memisahkan koma; lalu menggunakan int() untuk mengubahnya menjadi bentuk integer (default: string)
total = sum(hasil_list) #melakukan penjumlahan nilai dalam list hasil_list 
print("Total list : ", total)
#####================================================================================#####

print()

#####================================================================================#####
str1 = "teknik informatika fakultas teknologi informasi universitas kristen satya wacana"
str2 = "sedang belajar bahasa pemrograman"
tupleMahasiswa = ('DEVA', 'IVAN')
dictKelas = {'IF001': 'Kapita Selekta', 'IF002': 'Matematika Diskrit', 'IF003': 'Pemrograman Web'}
listPython = ['p', 'y', 't', 'h', 'o', 'n']

# Soal 5
# Dari variable di atas, buatlah string sebagai berikut
# - 'Hari ini Deva tidak mengikuti mata kuliah Pemrograman Web'
# - 'Matematika Diskrit IF002 adalah salah satu mata kuliah di progdi Teknik Informatika Universitas Kristen Satya Wacana'
# - 'Ivan belajar bahasa pemrograman Python di mata kuliah Kapita Selekta'

# Jawaban 5
key = next(kode for kode, matkul in dictKelas.items() if matkul == 'Matematika Diskrit') #perulangan digunakan untuk mengekstrak key/kunci pada dictionary, yang valuenya adalah Matematika Diskrit
bahasa = ''.join(listPython) #.join digunakan untuk mengkonversi list ke bentuk string

ans1 = "Hari ini " + str.title(tupleMahasiswa[0]) + " " + "tidak mengikuti mata kuliah " + dictKelas['IF003'] #str.title digunakan capitalize huruf awal pada suatu kata
ans2 = dictKelas['IF002'] + " " + key + " adalah salah satu mata kuliah di progdi " + str.title(str1[0:18]  + " " + str1[48:]) 
ans3 = str.title(tupleMahasiswa[1]) + " " + str2[7:] + " " + str.title(bahasa) + " di mata kuliah " + dictKelas['IF001'] 

print("String 1 : " + ans1)
print("String 2 : " + ans2)
print("String 3 : " + ans3)
#####================================================================================#####

print()

#####================================================================================#####
listHari = ['Senin', 'Rabu', 'Jumat', 'Sabtu']

# Soal 6
# Tambahkan hari 'Selasa', 'Kamis', dan 'Minggu', sehingga listHari tersebut menjadi ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

# Jawaban 6
listHari.insert(1, 'Selasa') #insert() digunakan untuk memasukkan data baru ke dalam sebuah list dengan spesifik, gunakan parameter ('nomor index', 'nama data yang hendak dimasukkan')
listHari.insert(3, 'Kamis')
listHari.append('Minggu') #append() digunakan untuk menambahkan data baru ke bagian akhir dari sebuah list

print("List hari lengkap : ", listHari)
#####================================================================================#####

print()

#####================================================================================#####
# Soal 7
# Hapus hari 'Sabtu' dan 'Minggu' dari listHari, kemudian copy list listHari ke variable tupleHariKerja dengan tipe data tuple

# Jawaban 7
listHari.pop(5) #pop() digunakan untuk menghapus elemen dari suatu list, apabila pop dilakukan tanpa memasukkan index, maka bagian paling belakang yang akan dihapus 
listHari.remove('Minggu') #remove() digunakan untuk menghapus suatu elemen dari suatu list, remove() digunakan apabila terdapat suatu elemen yang sama dalam satu list, dan remove() akan menghapus nilai yang muncul pertama

print("List Hari Kerja : ", listHari)

tupleHariKerja = tuple(listHari) #tuple() digunakan untuk membuat tuple

print("Tuple Hari Kerja : ", tupleHariKerja)
#####================================================================================#####

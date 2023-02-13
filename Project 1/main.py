#single line comment menggunakan "#"
#berikut contoh kode scripts

'''sedangkan 
multi line comment
menggunakan petik 3x
'''

#print("hello world")

# nilai = 1
# print(nilai)
# print(type(nilai))


# kalimat = "aku belajar python uhuy"
# print(kalimat)
# print(type(kalimat))
# print("huruf range 1-3:", kalimat[0:3])
# print("length kalimat adalah : ", len(kalimat))


# nominal = 2.90
# print(nominal)
# print(type(nominal))
# nilai = "tes"

# print(nilai)

# test = "ini adalah kata test"

# print("Berikut adalah cara penambahan/update : ", test[:-1]+" Update Python")

# print(test.strip(test[-1]))

# result = test[0:]

nama = "Anggasta"
subject = "Python"
kelas = "Kelas Kapita SE"
tgl = "Tanggal Januari"
hari = 1

# result = "Anggasta Mengikuti Kelas Python, Kapita SE"
# # ikuti hasil pada variable result, dengan manipulasi variable

# print(result)

# print(nama + " Mengikuti " + kelas[0:5] + " " + subject + ", " + kelas[6:])

# # method2
# method2 = "{0} Mengikuti {1} {2}, {3}"
# print(method2.format(nama, kelas[0:5], subject, kelas[6:]))

# # method3
# print(f"{nama} Mengikuti {kelas.split()[0]} {subject}, {kelas[6:]}")

# result2 = "Anggasta Mengikuti Kelas Python, Kapita SE Tanggal 1 Januari"

# print(nama + " Mengikuti " + kelas[0:5] + " " + subject + ", " + kelas[6:] + " " +  tgl[0:7] + " " + str(hari) + " " + tgl[8:])

# # method2
# method2 = "{0} Mengikuti {1} {2}, {3} {4} {5} {6}"
# print(method2.format(nama, kelas[0:5], subject, kelas[6:], tgl[0:7], hari, tgl[8:]))

# # method3
splittgl = tgl.split()
#  print(f"{nama} Mengikuti {kelas.split()[0]} {subject}, {kelas[6:]} {splittgl[0]} {hari} {splittgl[1]} ")


# result = "Python 1"

# print(subject + " " + str(hari)) #agar tidak error

# untuk menghapus variable gunakan syntax del(*variable*)

result = "Anggast"
nama = nama[:-1]
print(nama)
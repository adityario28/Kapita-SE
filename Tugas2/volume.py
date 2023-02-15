def balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def kubus(sisi):
    # return sisi*sisi*sisi
    return sisi^3

def limas4(panjang, lebar, tinggi):
    return round(((panjang * lebar * tinggi) / 3),2)

def prisma(alas, tinggi, tinggiP):
    return round((((alas * tinggi)/2) * tinggiP),2)

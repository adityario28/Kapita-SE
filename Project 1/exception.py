try:
    print("Halo ini lagi testing exception")
    print(2/0)
except ZeroDivisionError:
    print("Gaboleh dibagi 0")
else:
    print("Jika melewati exception, maka akan mencetak")
finally:
    print("ini pasti akan dicetak")


# else (di try except)
#     Jika program masuk ke exception, maka TIDAK menjalankan else
#     Jika program melewati exception, maka menjalankan else

# finally
#     Program akan tetap menjalankan finally, baik kondisi masuk ke exception maupun tidak

angka = 1

if angka == 0:
    raise ValueError("salah, nilai gaboleh 0")
else:
    print("betul banget nih, nilai bisa berupa", str(angka))
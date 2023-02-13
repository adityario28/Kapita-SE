import volume as vol

#1. fungsi untuk mencari bilangan prima
def prima(awal, akhir):
    hasil = []
    for angka in range(awal, akhir + 1):
        if all(angka % i != 0 for i in range(2,angka)):
            hasil.append(angka)
    return hasil

print("1. Bilangan prima dari range 1-35 adalah : ", prima(1,35))

# The function prime_numbers takes two parameters, start and end, which represent the beginning and end of the range of numbers to search for prime numbers.

# The variable primes is an empty list that will be used to store the prime numbers found within the given range.

# The for loop iterates over the numbers in the range from start to end.

# Within the loop, the if statement checks if the current number num is prime. To do this, it uses the all function, which returns True if all elements in the given iterable are True.

# The iterable passed to all is a generator expression that evaluates to True if num is not divisible by any number i in the range from 2 to num - 1. If num is not divisible by any of these numbers, it is a prime number.

# If the current number num is prime, it is appended to the list primes.

# After the for loop has completed, the function returns the list of prime numbers, primes.



#2. fungsi untuk mencari bilangan ganjil
def ganjil(awal, akhir):
    hasil = []
    for angka in range(awal, akhir + 1):
        if angka % 2 != 0:
            hasil.append(angka)
    return hasil

print("2. Bilangan ganjil dari range 1-48 adlaah : ", ganjil(1,48))

# The function odd_numbers takes two parameters, start and end, which represent the beginning and end of the range of numbers to search for odd numbers.

# The variable odds is an empty list that will be used to store the odd numbers found within the given range.

# The for loop iterates over the numbers in the range from start to end.

# Within the loop, the if statement checks if the current number num is odd. To do this, it calculates the remainder of num divided by 2 using the modulo operator (%).

# If the remainder is not 0, it means that num is odd.

# If the current number num is odd, it is appended to the list odds.

# After the for loop has completed, the function returns the list of odd numbers, odds.



#3. fungsi untuk mencari bilangan prima ganjil

def primaganjil(awal, akhir):
    bil_prima = prima(awal, akhir)
    bil_ganjil = ganjil (awal, akhir)
    return [angka for angka in bil_prima if angka in bil_ganjil]

print("3. Bilangan prima ganjil dari range 1-35 adalah : ", primaganjil(1,35))





#4. fungsi membalikkan karakter input string
def kebalikan(input):
    return input[::-1]

print("4. Kata rexus apabila ditulis secara berkebalikan adalah : ", kebalikan("rexus"))


#5. fungsi untuk mengecek palindrom sebuah kata
def palindrom(input):
    return input == input[::-1]

print("5. Kata fantech adalah palindrom ialah(T/F) : ", palindrom("fantech"))


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


#10. modul volume
print(vol.kubus(4))
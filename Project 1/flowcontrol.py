# a = 1

# if a == 1 : 
#     if a==2 or a !=1 :
#         print("a bernilai 2 dan buka merupakan dari nilai 1")
#     else : 
#         print("a bernilai 1 dan a bernilai 2")
# else :
#     print("a bernilai selain a dan 2")

# a = [1,2,3,4,5,6,7,8,9]
# b = ['a', 'b', 'c', 'd', 'e', 'f']

# for x in a :
#     for y in b : 
#         if x == 2 and y == 'f' :
#             print("x bernilai 2 dan y bernilai 'f'")



# for x in range(4,1,) :
    # print(x)

# # stop sampai nilai x == 5 tanpa print karena print dibawah break
# for x in a :
#     if x == 5:
#         break
#         print(f"nilai {x}")
#     print(x)

# # skip nilai x == 5, tanpa print karena print ada dibawah continue
# for x in a :
#     if x == 5:
#         continue
#         print(f"nilai {x}")
#     print(x)

# # menahan output, lalu assign nilai karena menggunakan pass
# for x in a :
#     if x == 5:
#         pass
#         print(f"nilai {x}")
#     print(x)

############ FILE HANDLING ##############

# a = ('a', 'b', 'c', 'd')
# # a =  ('a', 'b', 'c', 'd')
# # a = ''.join(str(index) for index in a)
# fopen = open("text.txt", "w")
# # fopen.write(a) #write() hanya untuk string
# # wrielines() bisa dimasukkan list
# for i in a:
#     fopen.writelines(i + "\n")
# fopen.close()

# def index(nama="reza"): #untuk default values
#     print(f"hello {nama}")

# index() #print hello reza

# index("bebas") #print hello bebas

# def tapel(a,b,c):
#     return a,b,c

# varA = tapel(1,2,3)

# # print(varA)

# nilai1, nilai2, nilai3 = varA

# print(nilai1)
# print(nilai2)
# print(nilai3)
# # print(nilai4)

import datetime


def indexa():
    print("hello world A")
def indexb():
    print("hello world B")
def indexc():
    print("hello world C")

if __name__ == "__main__":
    indexa()
    indexb()

print(datetime.datetime.now())
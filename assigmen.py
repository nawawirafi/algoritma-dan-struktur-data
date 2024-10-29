#Operator Assignment
#Operator assignment juga memiliki variasi penulisan yang disebut sebagai operator 
#assignment gabungan (compound assignment).  Operator assignment gabungan adalah cara 
#penulisan singkat operator assignment yang digabung dengan dengan operator lain. Dalam 
#bahasa Python, operator assignment gabungan ini terdiri dari operator assignment dengan 
#operator lain seperti operator aritmatika dan bitwise.

#Tabel berikut merangkum semua operator assignment dalam bahasa Python:
# Operator	Contoh	Penjelasan
# +=	a += b	a = a + b
# -=	a -= b	a = a – b
# *=	a *= b	a = a * b
# /=	a /= b	a = a / b
# &=	a &= b	a = a & b
# |=	a |= b	a = a | b
# ^=	a ^= b	a = a ^ b
# <<=	a <<= b	a = a << b
# >>=	a >>= b	a = a >> b

#Contoh Kode Program Operator Assignment Python
#Dalam prakteknya, operator assignment juga bisa dipakai "bertingkat" seperti contoh 
#berikut:

i = 2
j = 4
j = j + 1
k = i + j
l = k + k + i
m = (k + l)* i
print('Isi variabel i:',i)
print('Isi variabel j:',j)
print('Isi variabel k:',k)
print('Isi variabel l:',l)
print('Isi variabel m:',m)

#Tabel berikut merangkum semua operator assignment dalam bahasa Python:
# Operator	Contoh	Penjelasan
# +=	a += b	a = a + b
# -=	a -= b	a = a – b
# *=	a *= b	a = a * b
# /=	a /= b	a = a / b
# %=	a %= b	a = a % b
# &=	a &= b	a = a & b
# |=	a |= b	a = a | b
# ^=	a ^= b	a = a ^ b
# <<=	a <<= b	a = a << b
# >>=	a >>= b	a = a >> b

n = 10
n += 5
print('n += 5  :',n) 
n = 10
n /= 5
print('n /= 5  :',n)  
n = 10
n **= 5
print('n *= 5 :',n)
n = 10
n <<= 2
print('n <<= 2 :',n)
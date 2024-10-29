#Operator identitas adalah operator yang bisa dipakai untuk memeriksa apakah nilai 
#sebuah variabel ada di tempat yang sama (di memory) atau tidak. Operator ini dikenal 
#juga sebagai identity operators.

#Operator ini terdiri dari 2 jenis:
# Operator	Penjelasan
# is	Bernilai True jika kedua operand merujuk ke object yang sama dan berisi nilai 
#       yang sama.
# is not Bernilai True jika kedua operand merujuk ke object yang tidak sama

o = 5
p = 5
q = 6
print('o is p :', o is p)
print('o is q :', o is q)
print('o is not q:', o is not q)
print('\n')
  
r = 'Duniailkom'
s = 'Duniailkom'
print('r is s :', r is s)
print('r is not s :', r is not s)
print('\n');

t = ['a','b','c']
v = ['a','b','c']
print('t is v :', t is v)
print('t is not v :', t is not v)

#Pengertian dan Contoh Operator Keanggotaan Python
#Operator keanggotaan adalah operator yang dipakai untuk memeriksa apakah suatu nilai 
#ada di dalam sebuah himpunan atau tidak. Himpunan yang dimaksud terdiri dari tipe data 
#"berbentuk array" seperti string, list, tuple, set dan dictionary. Operator ini dikenal 
#juga sebagai membership operators.

#Operator ini terdiri dari 2 jenis:
#Operator	Penjelasan
# in	Bernilai True jika nilai yang dicari ada di dalam himpunan
# not in	Bernilai True jika nilai yang dicari tidak ada dalam himpunan

w = 'Duniailkom'
print('w :',w)
print('\'i\' in w    :', 'i' in w)
print('\'k\' not in w :', 'k' not in w)
print('\'d\' not in w :', 'd' not in w)
print('\n')
 
 
x = ['a','b','c']
print('x :',x)
print('\'a\' in x    :', 'a' in x)
print('\'a\' not in x :', 'a' not in x)
print('\'d\' not in x :', 'd' not in x)
print('\n')
 
y = (12,43,102,55)
print('y :',y)
print('102 in y    :', 102 in y)
print('102 not in y :', 102 not in y)
print('35 not in y  :', 35 in y)
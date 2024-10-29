#Sebagai contoh saya akan buat kode program sederhana, yakni melihat apakah 
#sebuah angka lebih besar dari angka lain, lalu tampilkan hasilnya jika kondisi terpenuhi:

a = 20
b = 10

if a > b:
    print('a lebih besar dari b')

c = 15
d = 15
 
if c > d:
  print('Variabel c lebih besar dari variabel d')
if c < d:
  print('Variabel c lebih kecil dari variabel d')
if d == d:
  print('Variabel d sama dengan variabel d')

# kode program yang bisa menebak apakah angka yang diinput merupakan bilangan 
# genap atau bilangan ganjil:

e = 17
 
if (e % 2) == 0:
  print('Variabel e berisi angka genap')
if (e % 2) != 0:
  print('Variabel e berisi angka ganjil')
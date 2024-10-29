#Pengertian Struktur Perulangan For Bahasa Python
#Berbeda dengan mayoritas bahasa pemrograman lain, di dalam Python perulangan for 
#lebih ke perulangan untuk memproses array / himpunan.

#Berikut format dasar struktur perulangan for dalam bahasa Python:
# foo = [a, b, ...] 
# for i in foo:
  # kode program yang akan diulang
  # kode program yang akan diulang

#kode program perulangan for untuk menampilkan nama-nama warna:

warna = ['hitam','putih','creame','Biru']
for a in warna:
  print(a)

#Perulangan for juga bisa dipakai untuk tipe data lain, misalnya tipe data set:

warna = {'hitam','putih','biru','Biru'}
for b in warna:
  print(b)

#bila ada data nya kembar hanya 1 yang dibaca karena perilaku dari tipe data set Python, 
#dimana jika terdapat data yang berulang, data tersebut tidak akan disimpan.

#tipe data string juga bisa:

me = 'prezekc'
for name in me:
     print(name)

#Penggunaan Function range()
#Struktur perulangan di bahasa Python sepintas tidak memungkinkan kita untuk 
#membuat perulangan angka naik, misalnya dari 1, 2, 3, dst. Namun ini bisa dibuat 
#dengan bantuan fungsi atau function range().

for c in range(5):
  print(c)

#Namun kita bisa mengatur jangkauan yang diinginkan. Caranya, tambah angka kedua ke 
#dalam function range():

for d in range(5,10):
  print(d)

#Tidak hanya itu, kita juga bisa mengatur tingkat "kenaikan" atau increment dari 
#range dengan cara menambah 1 lagi angka pada saat pemanggilan function range():

for e in range(5,25,5):
  print(e)
#Pengertian Struktur Perulangan While Bahasa Python
#Struktur perulangan (atau dalam bahasa inggris disebut dengan loop) adalah 
#instruksi kode program yang bertujuan untuk mengulang beberapa baris perintah.

#Berikut format dasar struktur perulangan while dalam bahasa Python:
# start;
# while condition:
  # kode program yang akan diulang
  # kode program yang akan diulang
#  increment

#Contoh Kode Program Perulangan While Bahasa Python
#Sebagai praktek pertama, berikut kode program perulangan While untuk menampilkan 
#teks "sisfo" sebanyak 5 kali:

a = 1
while a <= 5:
  print('sisfo')
  a +=1

#Di dalam blok perulangan, kita juga bisa mengakses nilai dari variabel counter b:

b = 1
while b <= 5:
  print('sisfo', b)
  b +=1

#Bagaimana dengan perulangan menurun? tidak masalah. Kita tinggal mengatur kondisi awal, 
#kondisi akhir, serta proses decrement:

c = 20
while c > 15:
  print('Duniailkom', c)
  c -= 1

i = 10
while i <= 5:
  print('Duniailkom', i)
  i -= 1
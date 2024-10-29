#Pengertian Arbitrary Arguments (*args) Python
#Arbitrary arguments adalah istilah untuk menyebut jumlah argumen yang tidak bisa
#ditentukan atau berubah-ubah.

def sapa_teman(nama1, nama2, nama3):
  print("Halo",nama1)
  print("Halo",nama2)
  print("Halo",nama3)   
sapa_teman("fateh","jefri","lee jen hou")

#Dengan menggunakan teknik arbitrary arguments, kita bisa membuat sebuah fungsi untuk 
#menerima 3, 4 atau 100 argumen sekaligus. Caranya, buat satu parameter dengan tanda 
#bintang di awal seperti berikut:

def sapa_teman(*args):
  print(args)
  print(type(args))   
sapa_teman("james artur","zain malik","juastin bieber","james smith")

#Karena hasil akhirnya berbentuk tuple, maka kita bisa menggunakan perulangan untuk 
#mengakses setiap element tuple. Berikut modifikasi dari kode program sebelumnya:

def sapa_teman(*nama):
  for i in nama:
    print("Halo",i)  
sapa_teman("ade","siti","rosmala","citra","fitra","nabila")

#Contoh Kode Program *args Python
#Arbitrary arguments cocok dipakai untuk fungsi dengan tipe data argumen seragam, 
#terutama yang melibatkan perhitungan matematika.

#Sebagai contoh, berikut fungsi tambah() yang akan menambahkan semua argumen:

def jumlah(*args):
  hasil = 0
  for i in args:
    hasil += i
  return hasil 
print( jumlah(1,2) )
print( jumlah(3,4,5,6) )
print( jumlah(7,8,9,10,11,12,13,14) )

#Baik, berikut kode program Python untuk mencari nilai rata-rata menggunakan arbitrary
#arguments:

def jumlah(*args):
  hasil = 0
  for i in args:
    hasil += i
  return hasil / len(args) 
print( jumlah(1,2) )
print( jumlah(3,4,5,6) )
print( jumlah(7,8,9,10,11,12,13,14) )
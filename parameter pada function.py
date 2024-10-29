#Pengertian Default Parameter dalam Python
#Default Parameter adalah istilah untuk parameter yang memiliki nilai awal, atau nilai 
#default. Kadang fitur ini disebut juga sebagai Default Argument.

#Sebagai contoh, misalkan kita membuat fungsi sederhana: tambah(). Fungsi ini perlu 2 
#buah parameter berupa nilai yang ingin ditambahkan. Berikut contoh kode programnya:

def tambah(var1, var2):
  return var1 + var2
print(tambah(2,5))
print(tambah(2,6))

#Penempatan Default Parameter
#Sebuah fungsi bisa memiliki banyak default parameter, namun tidak boleh ada parameter 
#tanpa nilai default yang ditulis setelah parameter dengan nilai default.

#Contoh pendefinisian fungsi berikut ini akan menyebabkan error di Python:

#Membuat Fungsi Pemangkatan
#Sebagai latihan dari default parameter dan juga pemrograman Python secara umum, 
#bisakah anda buat fungsi pangkat() yang ketika dijalankan akan menampilkan hasil 
#sebagai berikut?

#Baik, berikut kode program lengkap dari pembuatan function pangkat():

def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
 
print( pangkat(2) )      
print( pangkat(3) )      
print( pangkat(4) )     
print( pangkat(5,5) )    
print( pangkat(6,6) )    
print( pangkat(7,7) )    
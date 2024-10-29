#Pengertian Perintah Return di dalam Function
#Sebelum ini kita sudah membuat beberapa function yang ketika di panggil akan 
#langsung menampilkan teks. Berikut contoh yang dimaksud:

def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
    
hitung_luas_segitiga(5, 7)

#Langsung saja kita lihat modifikasi dari function hitung_luas_segitiga() dengan 
#penambahan perintah return:

def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  return luas
    
var1 = hitung_luas_segitiga(5, 7)
print("Luas segitiga adalah:",var1)

#Mengembalikan Langsung Hasil Operasi
#Dalam contoh di atas kita mengembalikan nilai dari variabel. Namun juga bisa langsung 
#mengembalikan nilai yang berasal dari hasil operasi. Perhatikan kode program berikut ini:

def hitung_luas_segitiga(alas, tinggi):
  return (alas * tinggi) / 2
    
print("Luas segitiga adalah:", hitung_luas_segitiga(5, 7))

#Perintah Return Akan Menghentikan Function
#Di dalam function, perintah return berfungsi mirip seperti break dalam perulangan. 
#Jika ditemukan perintah return, pemrosesan function akan berhenti dan tidak akan 
#mengeksekusi kode dibawahnya:

def hitung_luas_segitiga(alas, tinggi):
  return (alas * tinggi) / 2
  print ("Belajar Python di Duniailkom")
    
print("Luas segitiga adalah:", hitung_luas_segitiga(5, 7))

def harga_setelah_pajak(harga_dasar):
  return harga_dasar + (harga_dasar * 10/100)
 
harga_bakwan = 1000
harga_final_bakwan = harga_setelah_pajak(harga_bakwan)
print("Harga bakwan 10 porsi Rp.", harga_final_bakwan)
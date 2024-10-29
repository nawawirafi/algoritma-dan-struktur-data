#Pengertian Fungsi (Function) dalam Bahasa Python
#Secara sederhana, fungsi atau function adalah kode program yang dirancang untuk 
#menyelesaikan sebuah tugas tertentu, dan merupakan bagian dari program utama. Ketika 
#di sadur ke dalam bahasa indonesia, function ini di sebut juga sebagai fungsi.

#Berdasarkan siapa yang membuat, fungsi bisa dibedakan ke dalam 2 kelompok:
#Built-In Function 
#User Defined Function
#Built-In Function adalah sebutan untuk fungsi yang sudah ada secara bawaan dari 
#dalam bahasa pemrograman. Sedangkan User Defined Function adalah fungsi yang kita 
#(sebagai programmer) membuatnya sendiri.

#Berikut format dasar cara pendefinisian fungsi dalam bahasa Python:
# def nama_function():
  # Isi function disini...
  # Isi function disini...
#  return nilai

#Agar bisa berjalan, sebuah function harus "dipanggil" dengan cara menulis nama 
#fungsi tersebut. Berikut contoh format dasarnya:

def sapa_duniailkom():
    print("Halo Duniailkom")

#Sebuah kode program bisa saja memiliki banyak fungsi. Berikut contohnya:
def artis():
  print("cholo papi");
 
def paling_best():
  print("cholo papi");
 
def sapa_dia():
  print("Halo bro,..");

#Variabel di Dalam Function
#Untuk fungsi yang kompleks, kita bisa menulis variabel di dalam fungsi tersebut. 
#Berikut contoh penggunaannya:

def hitung_luas_segitiga():
  alas = 8
  tinggi = 6
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
   
hitung_luas_segitiga()
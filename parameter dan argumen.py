#Parameter adalah sebutan untuk nilai inputan fungsi pada saat fungsi itu di 
#definisikan, sedangkan argumen adalah sebutan untuk nilai inputan fungsi pada saat 
#fungsi itu dipanggil.

#Berikut format dasar fungsi Python dengan parameter dan argumen:
# def nama_function(param1, param2):
  # Isi function disini...
  # Isi function disini...
#  return nilai

def jefri():
  print("chulo papi");
jefri()

#Kita bisa menjalankan fungsi sapa_teman() dengan argumen yang berbeda-beda:

def artis(nama):
  print("Hai",nama);
 
artis("jefri")
artis("ari irham")
artis("chicho")

#Membuat Fungsi dengan Lebih dari 1 Parameter / Argumen
#fungsi tersebut juga ditulis dengan lebih dari satu parameter.

def sapa_teman(nama1, nama2, nama3, nama4, nama5, nama6):
  print("Hai", nama1, nama2, nama3, nama4, nama5, nama6)
 
sapa_teman("siti", "mala", "citra", "ade","fitra","seleb")

#Membuat Function hitung_luas_segitiga()
#Sebagai contoh terakhir, berikut modifikasi fungsi hitung_luas_segitiga() yang bisa 
#menerima 2 argumen angka:

def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
    
hitung_luas_segitiga(5, 7)
hitung_luas_segitiga(2, 10)
hitung_luas_segitiga(191, 357)
#Pengertian Arbitrary Keyword Arguments (**kwargs) Python
#Arbitrary keyword arguments adalah istilah untuk menyebut jumlah named argumen fungsi 
#yang tidak bisa ditentukan atau berubah-ubah.

#Menampilkan Nilai **kwargs Fungsi Python
#Sesampainya di dalam function, isi parameter **kwargs bisa diakses dengan perulangan 
#for. Ini kurang lebih sama seperti di dalam *args. Namun ada sedikit kendala yang bisa 
#terjadi seperti percobaan berikut:

def sambung_kata(**kata):
  for i in kata:
     print(i) 
sambung_kata(a="mari", b="kita", c="senantiasa", d="sholat")

#Jika kita ingin menampilkan value dictionary dalam sebuah perulangan for, bisa 
#menggunakan kode berikut:

def sambung_kata(**kata):
  for i in kata.values():
     print(i) 
sambung_kata(a="mari", b="kita", c="senantiasa", d="sholat")

#Bagaimana jika kita ingin menyambung setiap kata dalam satu baris panjang?, berikut 
#modifikasi kode programnya:

def sambung_kata(**kata):
  hasil = ""
  for i in kata.values():
     hasil += i + " "
  return hasil;
print( sambung_kata(a="mari", b="kita", c="senantiasa", d="sholat") )

#Menggabung Argument Biasa + *args + kwargs
#Untuk fungsi yang kompleks, kita bisa menggabung penulisan argument atau parameter 
#biasa dengan arbitrary arguments (*args) serta arbitrary keyword arguments (**kwargs).

#Jika sebuah fungsi punya ketiga jenis argument ini, maka urutannya harus sebagai berikut:

# 1.Argument / parameter biasa
# 2.Arbitrary arguments (*args)
# 3.Arbitrary keyword arguments (**kwargs)

#Berikut contoh kode program yang menggabung ketiganya

def test(var1, var2, *args,**kwargs):
  print(var1)
  print(var2)
  print(args)
  print(kwargs)
test(10, 20, 30, 40, 50, a = 60, b = 70, c = 80)



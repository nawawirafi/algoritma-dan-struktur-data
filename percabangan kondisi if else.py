#Pengertian Kondisi If Else If Bahasa Python
#Pada dasarnya, kondisi If Else If adalah sebuah struktur logika program yang di 
#dapat dengan cara menyambung beberapa kondisi If Else menjadi sebuah kesatuan.

#Jika kondisi pertama tidak terpenuhi atau bernilai False, maka kode program akan 
#lanjut ke kondisi If di bawahnya. Jika ternyata tidak juga terpenuhi, akan lanjut 
#lagi ke kondisi If di bawahnya, dst hingga blok Else terakhir atau terdapat kondisi 
#If yang bernilai True.

nilai = 'B'
 
if nilai == 'A':
  print('Pertahankan')
elif nilai == 'B':
  print('Harus lebih baik lagi')
elif nilai == 'C':
  print('Perbanyak belajar')
elif nilai == 'D':
  print('Jangan keseringan main')
elif nilai == 'E':
  print('Kebanyakan bolos...')
else:
  print('Maaf, format nilai tidak sesuai')

#Setiap kondisi dari block elif ini bisa diisi dengan perbandingan yang lebih
#kompleks, seperti contoh berikut:

nilai = 74.9
print('Nilai:',nilai)
 
if nilai >= 90:
  print('welcome tu UI')
elif (nilai >= 80) and (nilai < 90):
  print('iyh anda lulus di UI')
elif (nilai >= 60) and (nilai < 80):
  print('wah maaf bangat anda tidak lulus')
elif (nilai >= 40) and (nilai < 60):
  print('cok, anda tidak lulus')
elif nilai < 40:
  print('hp terossss...')
else:
  print('Maaf, format nilai tidak sesuai')
  
# program menentukan bilangan ganjil dan genap
print('## 1. program bilangan ganjil dan genap ##')
print('====================')

# input bilangan 
bilangan = int(input('masukkan bilangan : '))

if bilangan % 2 == 0:
    print(f'{bilangan} adalah bilangan genap')
else:
    print(f'{bilangan} adalah bilangan ganjil')

# program menentukan nilai ujian 
print('## 2. program menentukan nilai ujian ##')
print()

# input nilai
nilai_ujian = int(input('masukan nilai anda: '))

# proses dan output
if nilai_ujian >= 75:
    print('anda lulus')
else:
    print('anda tidak lulus')

# program menentukan nilai usia
print('## 3. menentukan usia dan status ##')
print()

# input usia
usia = int(input('masukkan usia : '))

if usia >= 18:
    print('anda sudah dewasa')
elif usia >= 13 and usia <= 17:
    print('anda remaja')
else:
    print('anda masih anak-anak')

#soal 4

status_anggota = input("Masukan status keanggotaan anda: ")
if status_anggota == "gold" or status_anggota == "silver":
   print("Selamat anda mendapatkan diskon")
else :
   print("Maaf anda tidak mendapatkan diskon, coba lagi..")

# 5.Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.
print('## 5.program yang meminta pengguna untuk memasukkan jumlah pembelian ##')
print ('======================')

#input status
jumlah_pembelian = int(input("masukkan jumlah pembelian"))
harga_item = 100
harga_diskon = harga_item * jumlah_pembelian * (10/100)
harga_total = harga_item * jumlah_pembelian 
total = harga_total - harga_diskon
print(f"Anda mendapatkan diskon 10%, harga per item {harga_item} jadi total yang harus dibayar {total}")







# 1. Buatlah program python untuk menuliskan profil pribadi (nama, nim, kelas, no telp, alamat) menggunakan variabel dan di cetak (print)
#Soal 1
nama = 'Muthia fadly'
nim = '0110124095'
rombel = 'SI07'
no_telp = '6289601743519'
alamat = 'Kp cipayung, sukmajaya, Kota Depok'

print ('nama saya adalah:', nama)
print ('nim saya adalah:', nim)
print ('rombel saya adalah:', rombel)
print ('nomor telepon saya adalah:', no_telp)
print ('alamat saya adalah:', alamat)
print ('======================')


# 2. buat seperti no 1 tapi 1 nama teman kalian
#Soal 2
nama = 'Tazkia Badzlina'
nim = '0110124102'
rombel = 'SI05'
no_telp = '628567370716'
alamat = 'Atang sanjaya'

print ('nama teman saya adalah:', nama)
print ('nim teman saya adalah:', nim)
print ('rombel teman saya adalah:', rombel)
print ('nomor teman telepon saya adalah:', no_telp)
print ('alamat teman saya adalah:', alamat)
print ('======================')


#3. buat program python untuk mencari nilai berat badan ideal
# rumus = (tinggi badan - 155) - ((tinggi badan - 155) * 0.15)
TB = int (input('masukan tinggi badan :'))
bb_ideal = (TB - 50) - ((TB - 50) * 0.15 )
print ('berat badan ideal adalah :', bb_ideal)
print ('======================')

#4. menghitung celcius ke fahreinhit
print("celcius ke fanrenheit")
celcius = int(input("masukan nilai celcius :"))
rumus = (9/5 *celcius) + 32

print("hasilnya adalah : ", rumus)
print ('======================')


#5. buat program python untuk mencari luas dan keliling tabung.
print("luas dan keliling tabung")
phi = 22/7
r = int(input ("masukan jari jari :"))
t = int(input ("masukan tinggi :"))
p = int(input ("masukan panjang :"))

luas = 2 * phi * r * (r + t)
keliling = 2 * (p + t)

print("hasil luas :",luas)
print("hasil keliling :",keliling)
pilih = int(input("""selamat datang diaplikasi menghitung
                  1. untuk menghitung luas pesegi
                  2. untuk menghitung luas lingkaran
                  3. untuk menghitung luas segitiga
                  masukan pilihan anda : """))

match pilih:
    case 1 :
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input('masukan sisi persegi: '))
        luasPsg = sisi * sisi
        print('luas persegi yang sisinya',sisi, "adalah", luasPsg)
    case 2 :
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari2 = int(input("masukan jari-jari lingkaran: "))
        luasLkr = 3.14 * jari2 * jari2
        print('luas lingkaran yang jari-jarinya',jari2, "adalah", luasLkr)
    case 3 :
        print("kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("masukan alas segitiga: "))
        tinggi = int(input("masukan tinggi segitiga: "))
        luasSegitiga = 0.5 * alas * tinggi
        print('luas segitiga yang alas',alas,"dan tinggi",tinggi, "adalah", luasSegitiga)
    case _:
        print("anda salah pilih")
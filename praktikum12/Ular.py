#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

#buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 

#buat minimal 2 objek untuk setiap class childnya.


from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, berkembang_biak, racun):
        super().__init__(nama, makanan, berkembang_biak, racun)
        self.racun = racun
        self.makanan = makanan

    def cetak_Ular(self):
        super().info_animal()
        print("panjang \t\t", self.racun,
        "\nRacun \t\t", self.makanan)
        
Ular_anaconda = Ular("anaconda", "daging", "bertelur", "tidak berbisa")
Ular_anaconda.cetak_Ular()
print("==========================================")
Ular_piton = Ular("piton", "daging", "bertelur", "tidak berbisa")
Ular_piton.cetak_Ular()
print("==========================================")
Ular_kobra = Ular("kobra", "daging", "bertelur", "berbisa")
Ular_kobra.cetak_Ular()

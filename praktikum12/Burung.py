#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

#buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 

#buat minimal 2 objek untuk setiap class childnya.

from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.warna_bulu = warna_bulu

    def info_burung(self):
        super().info_animal()
        print("paruh \t\t\t :", self.paruh,
        "\nwarna Bulu \t\t :", self.warna_bulu)

burung_beo = Burung("beo", "jagung", "darat", "bertelur", "melengkung", "warna warni",)
burung_beo.info_burung()
print("==========================================")
burung_merpati = Burung("merpati", "beras", "darat", "bertelur", "lurus", "putih",)
burung_merpati.info_burung()
print("==========================================")
burung_gereja = Burung("Gereja", "jagung", "udara", "telur", "lurus", "coklat",)
burung_gereja.info_burung()
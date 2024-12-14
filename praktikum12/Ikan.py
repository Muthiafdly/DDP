#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

#buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 

#buat minimal 2 objek untuk setiap class childnya.

from Animal import Animal

class Ikan(Animal):
    def __init__ (self, nama, makanan, hidup, berkembang_biak, habitat, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.ukuran = ukuran

    def info_Ikan(self):
        super().info_animal()
        print("habitat \t: ", self.habitat, 
        "\nUkuran \t: ", self.ukuran)

Ikan_Hiu = Ikan("Hiu", "Daging", "Laut", "Telur", "Laut", "Besar",)
Ikan_Hiu.info_Ikan()
print("==========================================")
Ikan_Mas = Ikan("Mas", "Pakan Ikan", "Air Tawar", "Telur", "Kolam", "Kecil",)
Ikan_Mas.info_Ikan()
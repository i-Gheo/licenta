#superclass Automobil
class Automobil():
    def __init__(self, marca, viteza_maxima):
        self.marca = marca
        self.viteza_maxima = viteza_maxima

    def printAuto(self):
        print("Superclass Automobil -> marca: ", self.marca, "vmax: ", self.viteza_maxima)

#subclass Camion
class Camion(Automobil):
    def __init__(self, marca, viteza_maxima):
        super().__init__(marca, viteza_maxima)
        self.gabarit = 2500
    
    def printCamion(self):
        print("Subclass Camion -> marca: ", self.marca, "vmax: ", self.viteza_maxima, "gabarit: ", self.gabarit)

Camion1 = Camion("Scania", 190)
Camion2 = Camion("Tesla", 220)

Camion1.printCamion()
Camion2.printCamion()
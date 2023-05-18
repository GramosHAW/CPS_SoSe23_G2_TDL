from random import random


class Auto:
    def __init__(self, id):
        self.id = id
        self.belegePlaetze = 0
        self.parkpositon = []
        self.laenge_eines_auto = [2, 4]
        laenge = self.laenge_eines_auto(random.randint(0, 1))
        if laenge == 2:
            self.Model = 'Klein Auto'
            self.belegePlaetze = 2
        elif laenge == 4:
            self.Model = 'Gross Auto'
            self.Model = 4




# # Beispielverwendung:
# auto1 = Auto("ABC123", 4.5)
# print(auto1.id)     # Ausgabe: ABC123
# print(auto1.length) # Ausgabe: 4.5

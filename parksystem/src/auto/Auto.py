
from random import random
from random import randint
import threading
import random as rd

class Auto:
    # Variablen die wir noch bauchen
    # ------------------------------------
    # parkzeit = Länge der Parkzeit
    # parksucheDauer = Dauer der Parkplatz suche
    # lebenszeit = länge der Lebenszeit in der Simulation, seit dem erzeugen

    liste_aller_Auto_ID = set()
    def __init__(self, id):






        # Die Topic die wir publischen
        self.__liste_aller_topic_out = ["auto/Einparken", "auto/Ausparken",
                                 ""]
        # Die Topic die wir abonnieren
        self.__liste_aller_topic_int = [""]
        self.__id = id
        self.__belegePlaetze = 0
        self.__parkpositon = []
        self.__set_eigenschaft_auto()



    def __set_eigenschaft_auto(self):
        self.__laenge_eines_auto = [2, 4]  # Kleines Auto hat die Länge 2 und größe Länge 4
        self.__laenge = self.__laenge_eines_auto[rd.randint(0, 1)]
        self.__Model = ""
        if self.__laenge == 2:
            self.__Model = 'Klein Auto'
            self.__belegePlaetze = 2
        elif self.__laenge == 4:
            self.__Model = 'Gross Auto'
            self.__belegePlaetze = 4
        print(f"Auto mit ID {threading.get_ident()} und der länge {self.__laenge}")

    def liste_aller_Auto_IDs(self):
        Auto.liste_aller_Auto_ID.add(self.__id)
        return Auto.liste_aller_Auto_ID


import random as rd

class parkwaechter:
    def __init__(self):
        # Die Topic die wir publischen
        self.__liste_aller_topic_out = ["App/",
                                        ""]
        # Die Topic die wir abonnieren
        self.__liste_aller_topic_in = ["Auto/Einparken", "Auto/Ausparken", "Parkmanager/Freie_Parkplatz",
                                       "Parkmanager/Keine_Freie_Parkplatz"]

        self.__kapazitaet = rd.randint(40, 60)
        self.__belegung = [False] * self.__kapazitaet


    def parken(self, fahrzeug):
        if len(self.__belegung) < self.__kapazitaet:
            self.__belegung.append(fahrzeug)
            print(f"{fahrzeug} wurde geparkt.")
        else:
            print("Der Parkplatz ist voll.")

    def ausparken(self, fahrzeug):
        if fahrzeug in self.__belegung:
            self.__belegung.remove(fahrzeug)
            print(f"{fahrzeug} wurde aus der Parkbucht entfernt.")
        else:
            print(f"{fahrzeug} befindet sich nicht auf dem Parkplatz.")

    def ist_parkplatz_voll(self):
        return len(self.__belegung) == self.__kapazitaet

    def verfuegbare_plaetze(self):
        return self.__kapazitaet - len(self.__belegung)

    def parkbucht_verwalten(self):
        print("")


    def prueft_auf_freie_parkplatz(self):
        print()

    def rechne_dauer_wartezeit(self):
        print()

    def auto_verschieben(self):
        print()


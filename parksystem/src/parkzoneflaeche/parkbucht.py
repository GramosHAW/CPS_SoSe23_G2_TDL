import threading


class parkbucht:
    # Erzeuge ein Lock-Objekt

    def __init__(self, parklaenge):
        self.parklaenge = parklaenge
        self.__parkflaeche = ["frei"] * parklaenge
        self.lock = threading.Lock()

    def einparken(self, anfangsPosition, endPosition):
        # self.lock.acquire()

        for i in range(anfangsPosition, endPosition):
            self.__parkflaeche[i] = "belegt"

        # self.lock.release()

    def ausparken(self, anfangsPosition, endPosition):
        for i in range(anfangsPosition, endPosition):
            self.__parkflaeche[i] = "frei"

    def getParkflaeche(self):
        return self.__parkflaeche

    def sucheParkplatz(self, autolaenge):
        i = 0
        anzahlFreierPlaetze = 0
        while i < self.parklaenge:
            if self.__parkflaeche[i] == "frei":
                anzahlFreierPlaetze = anzahlFreierPlaetze + 1
                if anzahlFreierPlaetze == (autolaenge + 2):
                    return True
            else:
                anzahlFreierPlaetze = 0

        return False

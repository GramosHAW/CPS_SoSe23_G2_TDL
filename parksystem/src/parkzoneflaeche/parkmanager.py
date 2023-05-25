class parkmanager:

    def __int__(self):
        # Die Topic die wir publischen
        self.__liste_aller_topic_out = ["Parkmanager/Freie_Parkplatz", "Parkmanager/Keine_Freie_Parkplatz",
                                 ""]
        # Die Topic die wir abonnieren
        self.__liste_aller_topic_in = [""]


    #def __frage_andere_
from random import random
from random import randint
import threading
import random as rd
import sys
import json
from random import seed
#from mqtt.mqtt_wrapper import MQTTWrapper

class Auto:
    # Variablen die wir noch bauchen
    # ------------------------------------
    # parkzeit = Länge der Parkzeit
    # parksucheDauer = Dauer der Parkplatz suche
    # lebenszeit = länge der Lebenszeit in der Simulation, seit dem erzeugen

    #liste_aller_Auto_ID = set()

    def __init__(self, id):

        # Die Topic die wir publischen
        self.__liste_aller_topic_out = ["auto/Einparken", "auto/Ausparken", ""]

        # Die Topic die wir abonnieren
        self.__liste_aller_topic_in = ["App/was", "App/wass"]
        self.__id = id
        self.__belegePlaetze = 0
        self.__parkpositon = []
        self.__set_eigenschaft_auto()
        #self.topics_subscriben()

    def __set_eigenschaft_auto(self):
        self.__laenge_eines_auto = [3, 5]  # Kleines Auto hat die Länge 3 und größe Länge 5
        self.__laenge = self.__laenge_eines_auto[rd.randint(0, 1)]
        self.__model = ""
        if self.__laenge == 3:
            self.__model = 'Kleines Auto'
            self.__belegePlaetze = 3
        elif self.__laenge == 5:
            self.__model = 'Grosses Auto'
            self.__belegePlaetze = 5
        # print(f"Auto mit ID {self.__id } und der länge {self.__laenge}")
        return self.__id, self.__laenge, self.__belegePlaetze

    def __str__(self):
        return f"Auto ID: {self.__id}, Länge: {self.__laenge}"

    def liste_aller_Auto_IDs(self):
        Auto.liste_aller_Auto_ID.add(self.__id)
        return Auto.liste_aller_Auto_ID


    DATA_TOPIC = "Auto/Einparken"

    # def __on_message_tick(self, client, userdata, msg):
    #     global DATA_TOPIC
    #     #ts_iso = msg.payload.decode("utf-8")
    #     #value = randint(0, 100)
    #     data = {"payload": "", "timestamp": 1}
    #     client.publish(DATA_TOPIC, json.dumps(data))
    #
    # def topics_subscriben(self):
    #     SEED = 10
    #     seed(SEED)
    #     mqtt = MQTTWrapper('mqttbroker', 1883, name='auto_1')
    #     for topic in self.__liste_aller_topic_in:
    #         mqtt.subscribe(topic)
    #         mqtt.subscribe_with_callback(topic, self.__on_message_tick)
    #
    #     try:
    #         mqtt.loop_forever()
    #     except(KeyboardInterrupt, SystemExit):
    #         mqtt.stop()
    #         sys.exit("KeyboardInterrupt -- shutdown gracefully.")
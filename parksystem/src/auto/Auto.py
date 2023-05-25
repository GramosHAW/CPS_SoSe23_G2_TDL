import random as rd
import sys
import json
from random import seed
from mqtt.mqtt_wrapper import MQTTWrapper

class Auto:
    liste_aller_Auto_ID = set()
    def __init__(self, id):
        # Die Topic die wir publischen
        self.__liste_aller_topic_out = ["Auto/Einparken", "Auto/Ausparken",
                                 ""]
        # Die Topic die wir abonnieren
        self.__liste_aller_topic_in = ["App/was", "App/wass"]
        self.__id = id
        self.__belegePlaetze = 0
        self.__parkpositon = []
        self.__set_eigenschaft_auto()
        #self.topics_subscriben()


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
        return self.__id, self.__laenge, self.__belegePlaetze

    def liste_aller_Auto_IDs(self):
        Auto.liste_aller_Auto_ID.add(self.__id)
        return Auto.liste_aller_Auto_ID


    DATA_TOPIC = "Auto/Einparken"

    def __on_message_tick(self, client, userdata, msg):
        global DATA_TOPIC
        #ts_iso = msg.payload.decode("utf-8")
        #value = randint(0, 100)
        data = {"payload": "", "timestamp": 1}
        client.publish(DATA_TOPIC, json.dumps(data))

    def topics_subscriben(self):
        SEED = 10
        seed(SEED)
        mqtt = MQTTWrapper('mqttbroker', 1883, name='auto_1')
        for topic in self.__liste_aller_topic_in:
            mqtt.subscribe(topic)
            mqtt.subscribe_with_callback(topic, self.__on_message_tick)

        try:
            mqtt.loop_forever()
        except(KeyboardInterrupt, SystemExit):
            mqtt.stop()
            sys.exit("KeyboardInterrupt -- shutdown gracefully.")

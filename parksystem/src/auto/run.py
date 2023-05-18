import sys
import json
import time
import logging
from datetime import datetime, timedelta
from random import seed
from random import randint

import numpy as np


import random

from Auto import Auto as auto

#-------------------------------------------------------------------------------------------------------------------

SENSOR_TOPIC = "auto/sensorwert"
SEED = 42

TICK_TOPIC = "chaossensor/1/data"

kleines_auto = auto(1,3)
PARKBUCHTLAENGE = 30
parkbucht = [False] * PARKBUCHTLAENGE
start_index = 15
end_index = 18
for i in range(start_index, end_index + 1):
    parkbucht[i] = True


print(parkbucht)


random_number = random.randint(0, 30)
print(random_number)
def on_message_auto(client, userdata, msg):
    global SENSOR_TOPIC
    ts_iso = msg.payload.decode("utf-8")
    value = "Joshuaaaaaa"
    data = {"payload": value, "timestamp": ts_iso}
    client.publish(SENSOR_TOPIC, json.dumps(data))


def main():
    # seed(SEED)
    # mqtt = MQTTWrapper('mqttbroker', 1883, name='auto_sensor')
    # #mqtt.subscribe(TICK_TOPIC)
    # mqtt.subscribe_with_callback(TICK_TOPIC, on_message_auto)
    #
    # try:
    #     mqtt.loop_forever()
    # except(KeyboardInterrupt, SystemExit):
    #     mqtt.stop()
    #     sys.exit("KeyboardInterrupt -- shutdown gracefully.")
    print("ausgabe Hallor es geht")




if __name__ == '__main__':
    main()

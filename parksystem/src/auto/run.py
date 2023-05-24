
import sys
import json
import time
import logging
from datetime import datetime, timedelta
import random
from random import seed
from random import randint

import threading
import concurrent.futures
from concurrent.futures  import ThreadPoolExecutor


import random
from Auto import Auto

# -------------------------------------------------------------------------------------------------------------------


auto1 = Auto(1)



PARKBUCHTLAENGE = 30
parkbucht = [False] * PARKBUCHTLAENGE
start_index = 15
end_index = 18
for i in range(start_index, end_index + 1):
    parkbucht[i] = True

# print(parkbucht)


random_number = random.randint(0, 30)
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# print(random_number)
def on_message_auto(client, userdata, msg):
    global SENSOR_TOPIC
    ts_iso = msg.payload.decode("utf-8")
    value = "Joshuaaaaaa"
    data = {"payload": value, "timestamp": ts_iso}
    client.publish(SENSOR_TOPIC, json.dumps(data))

auto2 = Auto(40)


parkbucht = [False] * 2


print("")

# def main():
#     # seed(SEED)
#     # mqtt = MQTTWrapper('mqttbroker', 1883, name='auto_sensor')
#     # #mqtt.subscribe(TICK_TOPIC)
#     # mqtt.subscribe_with_callback(TICK_TOPIC, on_message_auto)
#     #
#     # try:
#     #     mqtt.loop_forever()
#     # except(KeyboardInterrupt, SystemExit):
#     #     mqtt.stop()
#     #     sys.exit("KeyboardInterrupt -- shutdown gracefully.")
#     print("ausgabe Hallor es geht")
autolist = []
def pool(item):
    autox = Auto(3)

    autolist.append(autox)
    zeit = random.randrange(1, 10)
    # logging.info(f'Thread {item}: id= {threading.getident()}')
    logging.info(f'Thread {item}: id= {threading.get_ident()}')
    #print(f"Thread time: {zeit}")
    #logging.info(f'Thread {item}: name= {threading.current_thread().name()}')
    logging.info(f'Thread {item}: sleeping for= {zeit}')
    time.sleep(zeit)
    logging.info(f'Thread {item}: finished')


def task_function(item):
    print(f"Aufgabe {item} wird ausgeführt.")
    zeit = random.randrange(1, 10)
    # logging.info(f'Thread {item}: id= {threading.getident()}')
    logging.info(f'Thread {item}: id= {threading.get_ident()}')



def main():

    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Threadpool Start')
    worker = 5
    item = 15

    with ThreadPoolExecutor(max_workers=worker) as executor:
        executor.map(pool, range(item))
    #thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=worker)
    # for i in range(item):
    #thread_pool.submit(pool, item)
    #
    #
    logging.info('Threadpool Finished----------')
    # Erstelle einen ThreadPoolExecutor mit 3 Threads


if __name__ == '__main__':
    main()
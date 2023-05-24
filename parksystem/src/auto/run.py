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
from concurrent.futures import ThreadPoolExecutor

import random
from Auto import Auto

# -------------------------------------------------------------------------------------------------------------------


PARKBUCHTLAENGE = 30
parkbucht = [False] * PARKBUCHTLAENGE
start_index = 15
end_index = 18
for i in range(start_index, end_index + 1):
    parkbucht[i] = True

# print(parkbucht)


random_number = random.randint(0, 30)


# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# print(random_number)
def on_message_auto(client, userdata, msg):
    global SENSOR_TOPIC
    ts_iso = msg.payload.decode("utf-8")
    value = "Joshuaaaaaa"
    data = {"payload": value, "timestamp": ts_iso}
    client.publish(SENSOR_TOPIC, json.dumps(data))


auto2 = Auto(40)

parkbucht = [False] * 2

autolist = [auto2]

autotext = ""

def pool(item):
    global autotext
    autox = Auto(item)
    autotext += str(autox) + " "
    autolist.append(autox)
    zeit = random.randrange(1, 10)
    # logging.info(f'Thread {item}: id= {threading.getident()}')
    logging.info(f'Thread {item}: id= {threading.get_ident()}')
    # logging.info(f'Thread {item}: sleeping for= {zeit} Sekunden')
    if item % 10 == 9:
        parkprinter()
    # time.sleep(zeit)
    autolist.remove(autox)
    logging.info(f'Thread {item}: finished')


def parkprinter():

    print(autotext)


def task_function(item):
    print(f"Aufgabe {item} wird ausgeführt.")
    zeit = random.randrange(1, 10)
    # logging.info(f'Thread {item}: id= {threading.getident()}')
    logging.info(f'Thread {item}: id= {threading.get_ident()}')


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Threadpool Start')
    worker = 5
    item = 20

    with ThreadPoolExecutor(max_workers=worker) as executor:
        # while(True):
        executor.map(pool, range(item))

    logging.info('Threadpool Finished----------')
    # Erstelle einen ThreadPoolExecutor mit 3 Threads


if __name__ == '__main__':
    main()

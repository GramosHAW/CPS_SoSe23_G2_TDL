
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

PARKBUCHTLAENGE = 30
parkbucht1 = [False] * PARKBUCHTLAENGE
parkbucht2 = [False] * PARKBUCHTLAENGE
parkbucht3 = [False] * PARKBUCHTLAENGE


def init():
    global parkbucht1
    global parkbucht2
    global parkbucht3


start_index = 15
end_index = 18
for i in range(start_index, end_index + 1):
    parkbucht1[i] = True

print(parkbucht1)

random_number = random.randint(0, 30)

def parken(parkbucht, warteschlange, lock):

    return True


# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
def on_message_auto(client, userdata, msg):
    global SENSOR_TOPIC
    ts_iso = msg.payload.decode("utf-8")
    value = "Joshuaaaaaa"
    data = {"payload": value, "timestamp": ts_iso}
    client.publish(SENSOR_TOPIC, json.dumps(data))


auto2 = Auto(40)

# parkbucht1 = [False] * 2

autolist = [auto2]

autotext = ""


def autoPool(item):
    autox = Auto(item)

    autolist.append(autox)
    zeit = random.randrange(1, 10)
    # logging.info(f'Thread {item}: id= {threading.getident()}')
    logging.info(f'Thread {item}: id= {threading.get_ident()}')
    # logging.info(f'Thread {item}: sleeping for= {zeit} Sekunden')
    time.sleep(zeit)
    autolist.remove(autox)
    logging.info(f'Thread {item}: finished')

    # global autotext
    # autotext += str(autox) + " "
    # if item % 10 == 9:
    #     parkprinter()


def parkprinter():
    print(autotext)



def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Threadpool Start')
    worker = 5
    item = 1000

    # with ThreadPoolExecutor(max_workers=worker) as executor:
    #     # while(True):
    #     executor.map(pool, range(item))
    #
    # logging.info('Threadpool Finished----------')


if __name__ == '__main__':
    main()

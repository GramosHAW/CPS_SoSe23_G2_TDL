import threading
from queue import Queue

from parkbucht import parkbucht

class Parkzone:

    def __init__(self):
        parkleange = 30

        self.parkbucht1 = parkbucht(parkleange)
        self.parkbucht2 = parkbucht(parkleange)
        self.parkbucht3 = parkbucht(parkleange)
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()
        self.warteschlange1 = Queue()
        self.warteschlange2 = Queue()
        self.warteschlange3 = Queue()


    def einparken(self, auto):
        self.lock1.acquire()
        #Conditon Variable wenn kein platz frei
        self.parkbucht1.einparken()


        self.lock1.release()

        self.lock2.acquire()
        self.parkbucht2.einparken()
        self.lock2.release()

        self.lock3.acquire()
        self.parkbucht3.einparken()
        self.lock3.release()

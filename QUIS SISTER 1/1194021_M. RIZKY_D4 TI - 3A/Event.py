import logging
import threading
import time
import random


LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


items = []
event = threading.Event()


class Service(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Pelayan"


    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            item = items.pop()
            logging.info('Mengambil makanan untuk meja No. {} dan sedang di antarkan oleh {} ke meja tamu'.format(item, self.name))


class Chef(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Master Chef"


    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info('Chef membuat makanan di meja No. {} di buat oleh {}'.format(item, self.name))
            event.set()
            event.clear()


if __name__ == "__main__":
    t1 = Chef()
    t2 = Service()


    t1.start()
    t2.start()


    t1.join()
    t2.join()

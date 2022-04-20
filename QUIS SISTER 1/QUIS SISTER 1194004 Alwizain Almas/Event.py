import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()


class Pelanggan(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            item = items.pop()
            logging.info('Kendaraan dengan no. urut {} telah dicuci {} dan siap dikeluarkan'.format(item, self.name))

class Pencuci(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(5):
            time.sleep(3)
            item = random.randint(0, 100)
            items.append(item)
            logging.info('Kendaraan dengan no. urut {} masuk ke ruang cuci yang dikendarai oleh petugas cuci {}'.format(item, self.name))
            event.set()
            event.clear()

if __name__ == "__main__":
    t1 = Pencuci()
    t2 = Pelanggan()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

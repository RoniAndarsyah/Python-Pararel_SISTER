import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()


class Peserta(threading.Thread):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            item = items.pop()
            logging.info('Peserta dengan nomor urut: {} Menuju ke ruangan {}'\
                         .format(item, self.name))

class Juri(threading.Thread):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info('Juri telah approv peserta nomor urut {}'\
                         .format(item, self.name))
            event.set()
            event.clear()

if __name__ == "__main__":
    t1 = Peserta()
    t2 = Juri()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
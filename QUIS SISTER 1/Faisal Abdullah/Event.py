import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


items = []
event = threading.Event()


class Japati(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Japati"


    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            item = items.pop()
            logging.info('Menerima surat dari No {} dikirim dengan menggunakan {} ke tujuan'.format(item, self.name))


class Pengirim(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Pengirim Surat"


    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info('Pengirim surat di alamat {} di buat oleh {}'.format(item, self.name))
            event.set()
            event.clear()


if __name__ == "__main__":
    t1 = Pengirim()
    t2 = Japati()


    t1.start()
    t2.start()


    t1.join()
    t2.join()
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:43:25 2022

@author: syiar
"""

import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = ["nasi goreng", "mie goreng", "kwetiaw"]
event = threading.Event()


class Pelayan(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            item = items.pop()
            logging.info('Pelayan memberitahukan: pesanan {} telah berhasil diantar'\
                         .format(item))

class Koki(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(len(items)):
            time.sleep(2)
            item = items[-1]
            logging.info('Koki memberitahukan: pesanan {} telah selesai dimasak'\
                         .format(item))
            event.set()
            event.clear()

if __name__ == "__main__":
    t1 = Koki()
    t2 = Pelayan()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

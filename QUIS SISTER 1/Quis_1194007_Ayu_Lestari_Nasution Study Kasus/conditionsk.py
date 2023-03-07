# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:45:59 2022

@author: Acer
"""

import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Pasien(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def daftar(self):

        with condition:

            if len(items) == 5:
                logging.info('no daftar')
                condition.wait()

            items.pop()
            logging.info('no daftar {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(7):
            time.sleep(2)
            self.daftar()


class Dokter(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def periksa(self):

        with condition:

            if len(items) == 13:
                logging.info('periksa {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('waktu periksa {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.periksa()


def main():
    daftar = Pasien(name='Pasien')
    periksa = Dokter(name='Dokter')

    daftar.start()
    periksa.start()

    daftar.join()
    periksa.join()


if __name__ == "__main__":
    main()

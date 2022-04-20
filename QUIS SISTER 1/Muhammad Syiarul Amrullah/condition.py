# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:44:06 2022

@author: syiar
"""

import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

fuel_tanks = []
condition = threading.Condition()


class Mesin(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):

        with condition:

            if len(fuel_tanks) == 0:
                logging.info('bensin telah habis')
                condition.wait()

            fuel_tanks.pop()
            logging.info('mesin menghabiskan 1 liter bensin')

            condition.notify()

    def run(self):
        for i in range(11):
            time.sleep(2)
            self.consume()


class Fuel_tanks(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def assign(self):

        with condition:

            if len(fuel_tanks) == 10:
                logging.info('fuel tanks {}. sudah penuh'.format(len(fuel_tanks)))
                condition.wait()

            fuel_tanks.append(1)
            logging.info('fuel tanks telah mengisi {}'.format(len(fuel_tanks)))

            condition.notify()

    def run(self):
        for i in range(10):    
            time.sleep(0.5)
            self.assign()


def main():
    fuel_tanks = Fuel_tanks(name='tangki bensin')
    mesin = Mesin(name='mesin')

    fuel_tanks.start()
    mesin.start()

    fuel_tanks.join()
    mesin.join()


if __name__ == "__main__":
    main()

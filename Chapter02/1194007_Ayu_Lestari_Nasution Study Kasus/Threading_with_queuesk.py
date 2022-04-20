# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:58:46 2022

@author: Acer
"""

""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random


class Daftar(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(3):
            item = random.randint(0, 10)
            self.queue.put(item)
            print('Daftar Notify : no daftar  di proses olehy %s\n'\
                  % (item, self.name))
            time.sleep(1)


class Pemeriksaan(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Pemeriksaan  notify : no daftar %d segera menuju ruang periksa '\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue(

    t1 = Daftar(queue)
    t2 = Pemeriksaan(queue)
    t3 = Pemeriksaan(queue)
    t4 = Pemeriksaan(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

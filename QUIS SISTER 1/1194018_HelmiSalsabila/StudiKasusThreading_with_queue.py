""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random


class Panitia(Thread):

    def init(self, queue):
        Thread.init(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Penerima kurban dengan nomor %d ditambahkan pada antrian oleh %s\n'\
                  % (item, self.name))
            time.sleep(1)


class Peserta(Thread):

    def init(self, queue):
        Thread.init(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Penerima nomor %d  Penerima Kurban dimunculkan oleh %s'\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '_main_':
    queue = Queue()

    t1 = Panitia(queue)
    t2 = Peserta(queue)
    t3 = Peserta(queue)
    t4 = Peserta(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
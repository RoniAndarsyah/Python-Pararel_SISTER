""""Thread synchronisation with queue"""
#studi kasus tentang antrian pemberian zakat

from threading import Thread
from queue import Queue
import time
import random


class PemberiZakat(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Pemberi Zakat notify : penerima zakat dengan nomor %d ditambahkan pada antrian oleh %s\n'\
                  % (item, self.name))
            time.sleep(1)


class PenerimaZakat(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Penerima Zakat notify :nomor %d  penerima zakat dimunculkan oleh %s'\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()

    t1 = PemberiZakat(queue)
    t2 = PenerimaZakat(queue)
    t3 = PenerimaZakat(queue)
    t4 = PenerimaZakat(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

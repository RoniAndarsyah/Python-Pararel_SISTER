""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random


class CuciMobil(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(1, 20)
            self.queue.put(item)
            print('Informasi : mobil dengan antrian nomor urut %d silahkan masuk -> %s\n'\
                  % (item, self.name))
            time.sleep(1)


class Pengunjung(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Mobil dengan nomor urut %d memasuki ruang cuci -> %s'\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()

    t1 = CuciMobil(queue)
    t2 = Pengunjung(queue)
    t3 = Pengunjung(queue)
    t4 = Pengunjung(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
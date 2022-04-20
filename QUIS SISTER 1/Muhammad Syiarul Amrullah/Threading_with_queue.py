""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random


class Antrian(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(2):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Antrian menghasilkan : no antrian %d by %s \n'\
                  % (item, self.name))
            time.sleep(1)


class Pengunjung(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Pengunjung mendapatkan : %d sebagai nomor antrian dari %s \n'\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()

    t1 = Antrian(queue)
    t2 = Pengunjung(queue)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

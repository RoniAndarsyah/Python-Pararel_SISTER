""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random


class Chef(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.name = "Master Chef"

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Chef membuat makanan di meja No. {} di buat oleh {}'.format(item, self.name))
            time.sleep(1)


class Service(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.name = "Pelayan"

    def run(self):
        while True:
            item = self.queue.get()
            print('Mengambil makanan untuk meja No. {} dan sedang di antarkan oleh {} ke meja tamu'.format(item, self.name))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()

    t1 = Chef(queue)
    t2 = Service(queue)
    t3 = Service(queue)
    t4 = Service(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

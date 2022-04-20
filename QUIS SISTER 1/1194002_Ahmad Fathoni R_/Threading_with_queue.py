""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random


class pedagang(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('pedagang menambahkan : item N°%d melalui %s\n'\
                  % (item, self.name))
            time.sleep(1)


class pelanggan(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('pelanggan notify : %d popped from queue by %s'\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()

    t1 = pedagang(queue)
    t2 = pelanggan(queue)
    t3 = pelanggan(queue)
    t4 = pelanggan(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

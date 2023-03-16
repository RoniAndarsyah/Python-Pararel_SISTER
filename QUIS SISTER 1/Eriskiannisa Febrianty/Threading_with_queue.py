# Tugas Studi Kasus
from threading import Thread
from queue import Queue
import time
import random


class Pembeli(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Pembeli: item N°%d ditambahkan ke keranjang oleh %s\n'\
                  % (item, self.name))
            time.sleep(1)


class Penjual(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Penjual : Notifikasi Item %d Pesanan dari %s'\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()


    t1 = Pembeli(queue)
    t2 = Penjual(queue)
    t3 = Penjual(queue)
    t4 = Penjual(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

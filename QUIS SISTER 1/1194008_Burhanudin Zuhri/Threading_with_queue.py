from threading import Thread
from queue import Queue
import time
import random


class Pelayan(Thread):

    def _init_(self, queue):
        Thread._init_(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 20)
            self.queue.put(item)
            print('Pelayan akan memberitahu bahwa : antrian nomor %d akan mendapat giliran selanjutnya %s\n'\
                  % (item, self.name))
            time.sleep(1)


class Pelanggan(Thread):

    def _init_(self, queue):
        Thread._init_(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('%d Muncul antrian dari %s'\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '_main_':
    queue = Queue()

    t1 = Pelayan(queue)
    t2 = Pelanggan(queue)
    t3 = Pelanggan(queue)
    t4 = Pelanggan(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    
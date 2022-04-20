""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
import random


class Japati(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.name = 'Japati'



    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Menerima surat dari No {} dikirim dengan menggunakan {} ke tujuan'.format(item, self.name))
            time.sleep(1)


class Pengirim(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.name = 'Pengirim'


    def run(self):
        while True:
            item = self.queue.get()
            print('Pengirim surat di alamat {} di buat oleh {}'.format(item, self.name))
            self.queue.task_done()
    

if __name__ == '__main__':
    queue = Queue()

    t1 = Japati(queue)
    t2 = Pengirim(queue)
    t3 = Pengirim(queue)
    t4 = Pengirim(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
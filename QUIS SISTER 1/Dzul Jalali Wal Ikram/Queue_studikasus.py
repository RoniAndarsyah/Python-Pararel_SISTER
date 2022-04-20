from threading import Thread
from queue import Queue
import time
import random


class CustomerService(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 20)
            self.queue.put(item)
            print('System memberitahu : antrian nomor %d akan mendapat giliran selanjutnya %s\n'\
                  % (item, self.name))
            time.sleep(1)


class Costumer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('%d muncul dari antrian oleh %s'\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()

    t1 = CustomerService(queue)
    t2 = Costumer(queue)
    t3 = Costumer(queue)
    t4 = Costumer(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

from threading import Thread
from queue import Queue
import time
import random


class Pemesanan(Thread):

    def _init_(self, queue):
        Thread._init_(self)
        self.queue = queue

    def run(self):
        for i in range(3):
            item = random.randint(0, 20)
            self.queue.put(item)
            print('Antrian pesanan : antrian nomor %d diproses oleh %s\n'\
                  % (item, self.name))
            time.sleep(3) #membuat delay random selama 1-3 detik


class Pembayaran(Thread):

    def _init_(self, queue):
        Thread._init_(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Antrian pembayaran : antrian nomor %d muncul tagihan pembayaran dari %s'\
                  % (item, self.name))
            self.queue.task_done()

if __name__ == '_main_':
    queue = Queue()
    
#declare objek dari tiap kelas
    t1 = Pemesanan(queue) #Thread untuk proses pemesanan
    t2 = Pembayaran(queue) #Threat untuk proses pembayaran
   
#mulai running threads
    t1.start()
    t2.start()
#tunggu proses selesai 
    t1.join()
    t2.join()
    
    print("Selesai")
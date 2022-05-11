import multiprocessing
import random
import time


class pemilik(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(4):
            kostrakan = random.randrange(0, 20)
            self.queue.put(kostrakan) 
            print ("Proses Pemilik : Pemilik dengan ID %d Menambahkan Bangunan ke dalam list kos dan kontrakan"\
                   % (kostrakan))
            time.sleep(1)
            print ("Jumlah kos dan kontrakan adalah %s"\
                   % self.queue.qsize())
       
class pencari(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("Tidak Ada Bangunan yang tersedia saat ini :(")
                break
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Proses Pencari : Bangunan %d Tersedia \
                        dimiliki oleh %s \n'\
                       % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
        queue = multiprocessing.Queue()
        process_Pemilik = pemilik(queue)
        process_pencari = pencari(queue)
        process_Pemilik.start()
        process_pencari.start()
        process_Pemilik.join()
        process_pencari.join()
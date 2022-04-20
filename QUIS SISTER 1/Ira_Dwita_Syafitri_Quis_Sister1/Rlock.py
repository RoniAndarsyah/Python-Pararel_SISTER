import threading
import time
from random import randint

class Kuis:
    def __init__(self):
        self.rlock = threading.RLock()
        self.stock_baju = 0

    def stok(self,value):
        with self.rlock:
            self.stock_baju += value

    def tambah(self):
        with self.rlock:
            self.stok(1)

    def terjual(self):
        with self.rlock:
            self.stok(-1)

def tambah(Kuis, baju):
    print("Tambahan stok ", baju)
    while baju:
        Kuis.tambah()
        time.sleep(randint(1,5))
        baju -= 1
        print("stok baju yang di dijual", baju)

def terjual(Kuis, baju):
    print("Stok yang terjual")
    while baju:
        Kuis.terjual()
        time.sleep(randint(1,5))
        baju -= 1
        print("stok baju yang ditambahkan", baju)


def main():
    items = 10
    kuis = Kuis()

    t1 = threading.Thread(target=tambah, \
                          args=(kuis, randint(10,20)))
    t2 = threading.Thread(target=terjual, \
                          args=(kuis, randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()

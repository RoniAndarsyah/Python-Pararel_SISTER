import threading
import time
import random


class kunci_reenant:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

def penambah(box, items):
    print("{} barang masuk gudang \n".format(items))
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print("1 barang telah masuk -->{} item akan masuk gudang \n".format(items))



def pengurang(box, items):
    print("{} barang keluar dari gudang \n".format(items))
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print("1 barang telah keluar -->{} item akan keluar dari gudang \n".format(items))


def main():
    kunci = kunci_reenant()

    t1 = threading.Thread(target=penambah, \
                          args=(kunci, random.randint(10,20)))
    t2 = threading.Thread(target=pengurang, \
                          args=(kunci, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()

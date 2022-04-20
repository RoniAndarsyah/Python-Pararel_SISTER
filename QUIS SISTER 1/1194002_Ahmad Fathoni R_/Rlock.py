import threading
import time
import random


class Kemasan:
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

def penambah(Kemasan, items):
    print("N° {} items to ADD \n".format(items))
    while items:
        Kemasan.add()
        time.sleep(1)
        items -= 1
        print("menamnbahkan satu barang -->{} barang yang akan ditambahkan \n".format(items))



def pengurang(Kemasan, items):
    print("N° {} barang yang akan dihapus \n".format(items))
    while items:
        Kemasan.remove()
        time.sleep(1)
        items -= 1
        print("menghapus satu barang -->{} barang yang dihapus \n".format(items))


def main():
    items = 10
    Kemasan = Kemasan()

    t1 = threading.Thread(target=penambah, \
                          args=(Kemasan, random.randint(10,20)))
    t2 = threading.Thread(target=pengurang, \
                          args=(Kemasan, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()

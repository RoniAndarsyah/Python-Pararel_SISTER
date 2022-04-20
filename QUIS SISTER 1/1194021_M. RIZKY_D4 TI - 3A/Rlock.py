import threading
import time
import random


class Warehouse:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0


    def execute(self, value):
        with self.lock:
            self.total_items += value


    def keep(self):
        with self.lock:
            self.execute(1)


    def take(self):
        with self.lock:
            self.execute(-1)


def keeping(box, items):
    print("Terdapat {} barang yang akan ditambahkan dalam gudang \n".format(items))
    while items:
        box.keep()
        time.sleep(1)
        items -= 1
        print("Menambahkan satu barang dengan ID : {} Barang ditambahkan dalam gudang \n".format(items))


def taking(box, items):
    print("Terdapat {} barang yang akan di ambil \n".format(items))
    while items:
        box.take()
        time.sleep(1)
        items -= 1
        print("Mengambil satu barang dengan ID : {} Barang di ambil dari dalam gudang \n".format(items))


def main():
    box = Warehouse()


    t1 = threading.Thread(target=keeping, args=(box, random.randint(10,20)))
    t2 = threading.Thread(target=taking, args=(box, random.randint(1,10)))


    t1.start()
    t2.start()


    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

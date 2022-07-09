import threading
import time
import random


class Barang:
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

def adder(Barang, items):
    print("Banyaknya produk {} yang ditambahkan \n".format(items))
    while items:
        Barang.add()
        time.sleep(1)
        items -= 1
        print("stok produk saat ini --> {} buah \n".format(items))



def remover(Barang, items):
    print("banyaknya produk {} yang di jual \n".format(items))
    while items:
        Barang.remove()
        time.sleep(1)
        items -= 1
        print("produk yang dijual --> {} buah \n".format(items))


def main():
    items = 12
    box = Barang()

    t1 = threading.Thread(target=adder, \
                          args=(box, random.randint(1,10)))
    t2 = threading.Thread(target=remover, \
                          args=(box, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()

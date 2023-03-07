import threading
import time
import random


class Periksa:
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

def adder(periksa, items):
    print("Banyaknya orang periksa hari ini {} jumlah to ADD \n".format(items))
    while items:
        periksa.add()
        time.sleep(1)
        items -= 1
        print("jumlah pendaftar saat ini -->{} org \n".format(items))



def remover(periksa, items):
    print("banyaknya org yang selesai di periksa{} no periksa to REMOVE \n".format(items))
    while items:
        periksa.remove()
        time.sleep(1)
        items -= 1
        print("pasien sudah selesai melakukan pemeriksaan -->{} jml \n".format(items))


def main():
    items = 10
    periksa = Periksa()

    t1 = threading.Thread(target=adder, \
                          args=(periksa, random.randint(10,20)))
    t2 = threading.Thread(target=remover, \
                          args=(periksa, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()

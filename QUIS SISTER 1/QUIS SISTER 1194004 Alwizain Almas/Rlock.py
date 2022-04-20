import threading
import time
import random


class RuangCuci:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def masuk(self):
        with self.lock:
            self.execute(1)

    def keluar(self):
        with self.lock:
            self.execute(-1)

def memasukkan(ruangcuci, items):
    print("Terdapat {} kendaraan yang akan dicuci \n".format(items))
    while items:
        ruangcuci.masuk()
        time.sleep(1)
        items -= 1
        print("1 kendaraan telah masuk -->{} kendaraan menunggu untuk masuk \n".format(items))



def mengeluarkan(ruangcuci, items):
    print("Terdapat {} slot tempat pencucian. Kendaraan harus segera diselesaikan dan dikeluarkan \n".format(items))
    while items:
        ruangcuci.keluar()
        time.sleep(1)
        items -= 1
        print("1 kendaraan telah keluar -->{} kendaraan nanti akan dikeluarkan bertahap \n".format(items))


def main():
    items = 10
    ruangcuci = RuangCuci()

    t1 = threading.Thread(target=memasukkan, \
                          args=(ruangcuci, random.randint(10,20)))
    t2 = threading.Thread(target=mengeluarkan, \
                          args=(ruangcuci, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()

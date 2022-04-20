import threading
import time
import random

noabsen = int(input('Masukan No Absen Anda : '))

if noabsen > 100   :
    print("Anda Anggota Dapartemen Manifest")
elif noabsen > 1 < 80 :
    print("Anda Anggota Dapartemen Beacukai")
else:
    print("Anda Pegawai Operation")

class Container:
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

def getin(container, items):
    print("Barang {} Telah Masuk \n".format(items))
    while items:
        container.add()
        time.sleep(1)
        items -= 1
        print("Menambahkan Satu Barang -->{} Barang Ditambahkan \n".format(items))



def getout(container, items):
    print("Barang {} Telah Keluar \n".format(items))
    while items:
        container.remove()
        time.sleep(1)
        items -= 1
        print("Mengeluarkan Satu Barang -->{} Barang Dikeluarkan \n".format(items))


def main():
    items = 10
    container = Container()

    t1 = threading.Thread(target=getin, \
                          args=(container, random.randint(10,20)))
    t2 = threading.Thread(target=getout, \
                          args=(container, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main()
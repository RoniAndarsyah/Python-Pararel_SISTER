import threading
import time
import random


class Kelas:
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

def lapangan(box, items):
    print("Murid sebanyak {} orang harus keluar kelas dan berkumpul dilapangan \n".format(items))
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print("Satu Murid sampai dilapangan -->{} Murid yang harus ke lapangan \n".format(items))



def kelas(box, items):
    print("Jumlah murid {} yang tidak berangkat ke lapangan \n".format(items))
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print("Murid izin tidak kelapangan -->{} Murid yang tidak ke lapangan \n".format(items))


def main():
    items = 10
    box = Kelas()

    t1 = threading.Thread(target=lapangan, \
                          args=(box, random.randint(10,20)))
    t2 = threading.Thread(target=kelas, \
                          args=(box, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()

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

def aula(box, items):
    print("mahasiswa sebanyak {} orang harus keluar kelas dan berkumpul di aula \n".format(items))
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print("Satu mahasiswa sampai di aula -->{} mahasiswa yang harus ke aula \n".format(items))



def kelas(box, items):
    print("Jumlah mahasiswa {} yang tidak berangkat ke aula \n".format(items))
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print("mahasiswa izin tidak kelapangan -->{} mahasiswa yang tidak ke aula \n".format(items))


def main():
    items = 10
    box = Kelas()

    t1 = threading.Thread(target=aula, \
                          args=(box, random.randint(10,20)))
    t2 = threading.Thread(target=kelas, \
                          args=(box, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()
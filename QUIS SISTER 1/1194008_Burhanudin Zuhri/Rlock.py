import threading
import time
import random


class Ricecooker:
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

def adder(kotak_nasi, items):
    print("Banyaknya nasi {} kg yang ditambahkan \n".format(items))
    while items:
        kotak_nasi.add()
        time.sleep(1)
        items -= 1
        print("Sisa nasi saat ini -->{} kg \n".format(items))



def remover(kotak_nasi, items):
    print("Banyaknya nasi {} kg yang dimakan \n".format(items))
    while items:
        kotak_nasi.remove()
        time.sleep(1)
        items -= 1
        print("Nasi yang dimakan -->{} kg \n".format(items))


def main():
    items = 10
    kotak_nasi = Ricecooker()

    t1 = threading.Thread(target=adder, \
                          args=(kotak_nasi, random.randint(10,20)))
    t2 = threading.Thread(target=remover, \
                          args=(kotak_nasi, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()

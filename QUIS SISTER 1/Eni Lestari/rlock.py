import threading
import time
import random


class BoxKurma:
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

def adder(boxkurma, items):
    print("Banyaknya kurma {} yang ditambahkan \n".format(items))
    while items:
        boxkurma.add()
        time.sleep(1)
        items -= 1
        print("stok buah kurma saat ini -->{} buah \n".format(items))



def remover(boxkurma, items):
    print("banyaknya kurma {} yang di jual \n".format(items))
    while items:
        boxkurma.remove()
        time.sleep(1)
        items -= 1
        print("kurma yang dijual -->{} buah \n".format(items))


def main():
    items = 12
    box = BoxKurma()

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

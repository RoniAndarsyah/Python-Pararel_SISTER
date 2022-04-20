import threading
import time
import random


class Box:
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

def adder(box, items):
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print("ADDED 1 item ke Chart -->{} item to Chart \n".format(items))



def remover(box, items):
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print("REMOVED one item dari Chart -->{} item to Chart \n".format(items))


def main():
    items = 10
    box = Box()

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
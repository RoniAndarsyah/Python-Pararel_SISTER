# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:46:39 2022

@author: Acer
"""

import threading
import time
import random


class BoxChocolate:
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

def adder(boxchocolate, items):
    print("Banyaknya chocolate {} yang ditambahkan \n".format(items))
    while items:
        boxchocolate.add()
        time.sleep(1)
        items -= 1
        print("stok buah chocolate saat ini -->{} buah \n".format(items))



def remover(boxchocolate, items):
    print("banyaknya chocolate {} yang di jual \n".format(items))
    while items:
        boxchocolate.remove()
        time.sleep(1)
        items -= 1
        print("chocolate yang dijual -->{} buah \n".format(items))


def main():
    items = 12
    box = BoxChocolate()

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

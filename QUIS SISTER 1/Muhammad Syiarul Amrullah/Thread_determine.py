# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:11:29 2022

@author: syiar
"""
import threading
import time
import random

def generate_random_A():
    print (threading.currentThread().getName()+str( '--> mulai generate \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str('--> menghasilkan random number {} \n').format(random.randint(10, 100)))
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='generate_random_A', target=generate_random_A)
    t2 = threading.Thread(name='generate_random_B', target=generate_random_A)
    t3 = threading.Thread(name='generate_random_C', target=generate_random_A) 

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
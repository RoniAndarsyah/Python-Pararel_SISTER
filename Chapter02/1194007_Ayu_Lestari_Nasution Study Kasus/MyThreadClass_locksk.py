# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:20:40 2022

@author: Acer
"""

import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class MyPasien(Thread):
   def _init_(self, name, duration):
      Thread._init_(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> " + self.name + \
             " no daftar adalah "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " selesai diberikan no daftar\n")
      #Release the Lock
      threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    thread1 = MyPasien("no pasien ", randint(1,10))
    thread2 = MyPasien("pasien no ", randint(1,10))

   

    # Thread Running
    thread1.start()
    thread2.start()

    

    # Thread joining
    thread1.join()
    thread2.join()

    
    #Execution Time
    print("waktu yang dibutuhkan untuk mengerjakan soal %s  seconds soal" % (time.time() - start_time))



if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:39:08 2022

@author: Acer
"""

import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class Mahasiswa (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
       threadLock.acquire()
       print ("---> Pemenangnya adalah " + self.name + "\n")
       threadLock.release()
       time.sleep(self.duration)
       print ("---> Selamat Kepada " + self.name)


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Mahasiswa("Rezkia", randint(1,10))
    thread2 = Mahasiswa("caca", randint(1,10))
    

    # Thread Running
    thread1.start()
    thread2.start()
   

    # Thread joining
    thread1.join()
    thread2.join()
    



if __name__ == "__main__":
    main()
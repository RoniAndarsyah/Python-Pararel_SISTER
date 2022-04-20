# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:17:34 2022

@author: Acer
"""

import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class MyPasien (Thread):
   def _init_(self, name, duration):
      Thread._init_(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> " + self.name + \
             "  pasien, ID pasiens "\
             + str(os.getpid()) + "\n")
      threadLock.release()
      time.sleep(self.duration)
      print ("---> " + self.name + " selesai\n")
      #Release the Lock


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = MyPasien("daftar pasien {}", randint(1,10))
    thread2 = MyPasien("daftar pasien {}", randint(1,10))
    

    # Thread Running
    thread1.start()
    thread2.start()
   

    # Thread joining
    thread1.join()
    thread2.join()
    

  
    # End
    print("End")

    #Execution Time
    print("--- %s detik ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    

    
#class_lock2
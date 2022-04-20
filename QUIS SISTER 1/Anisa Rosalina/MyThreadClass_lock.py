# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:37:46 2022

@author: Acer
"""

import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class Giveaway (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> Pemenangnya adalah " + self.name + "\n")
      threadLock.release()
      time.sleep(self.duration)
      print ("---> Selamat Kepada " + self.name)
      #Release the Lock


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Giveaway("Rezkia ", randint(1,10))
    thread2 = Giveaway("Caca", randint(1,10))

    

    # Thread Running
    thread1.start()
    thread2.start()

    

    # Thread joining
    thread1.join()
    thread2.join()




if __name__ == "__main__":
    main()
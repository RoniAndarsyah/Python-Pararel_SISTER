# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:38:34 2022

@author: Acer
"""

import time
import os
from random import randint
from threading import Thread

class Giveaway (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> Pemenangnya adalah " + self.name + "\n")
      time.sleep(self.duration)
      print ("---> Selamat Kepada " + self.name)


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
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:53:13 2022

@author: Hp
"""

import time
import os
from random import randint
from threading import Thread

class MyThreadClass (Thread):
   def _init_(self, name, duration):
      Thread._init_(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> " + self.name + \
             " mulai presentasi, NPM "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " melakukan presentasi\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    Audry1 = MyThreadClass("Audry ", randint(6,10))
    Artha2 = MyThreadClass("Artha ", randint(6,10))
    Lina3 = MyThreadClass("Lina ", randint(6,10))
    Jimin4 = MyThreadClass("Jimin ", randint(6,10))
    Wooyoung5 = MyThreadClass("Wooyoung ", randint(6,10))
    Haruto6 = MyThreadClass("Haruto ", randint(6,10))
  
    # Thread Running
    Audry1.start()
    Artha2.start()
    Lina3.start()
    Jimin4.start()
    Wooyoung5.start()
    Haruto6.start()

    # Thread joining
    Audry1.join()
    Artha2.join()
    Lina3.join()
    Jimin4.join()
    Wooyoung5.join()
    Haruto6.join()

    # End 
    print("End")

    #Execution Time
    print("--- waktu presentasi %s seconds ---" % (time.time() - start_time))


if _name_ == "_main_":
    main()
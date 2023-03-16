# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:31:30 2022

@author: Acer
"""

from threading import Thread
import time
import os

class MakananClass (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Makanan Khas Jawa Barat {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # Thread Creation
    thread1 = MakananClass("Karedok")
    thread2 = MakananClass("Tutug Oncom") 
    thread3 = MakananClass("Ubi Cilembo")
    thread4 = MakananClass("Nasi Jamblang")
  
    # Thread Running
    thread4.start()
    thread2.start()
    thread3.start()
    thread1.start()


    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    # End 
    print("End")

if __name__ == "__main__":
    main()
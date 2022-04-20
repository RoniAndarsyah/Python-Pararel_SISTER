from threading import Thread
from random import randint
import time
import os

class balapan (Thread):
   def __init__(self, rider, posisi):
      Thread.__init__(self)
      self.rider = rider
      self.posisi = posisi
 
   def run(self):
       print(self.rider,"di posisi",self.posisi)

def main():
    print("Hasil Balapan")

    t1 = balapan("Rossi",randint(1,10))
    t2 = balapan("Marques",randint(1,10))
    t3 = balapan("Lorenzo",randint(1,10))
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()

    



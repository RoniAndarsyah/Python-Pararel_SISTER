from threading import Thread
import time
import os

class TarianClass (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Tarian Khas Sumatera Selatan {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # Thread Creation
    thread1 = TarianClass("Gending Sriwijaya")
    thread2 = TarianClass("Tanggai") 
    thread3 = TarianClass("Erai-Erai")
    thread4 = TarianClass("Setudung Sedulang")
  
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
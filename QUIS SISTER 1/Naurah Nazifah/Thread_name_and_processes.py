from threading import Thread
import time
import os

class MakananClass (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("makanan khas sumut {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # Thread Creation
    thread1 = MakananClass("Mie Gomak ")
    thread2 = MakananClass("Sambal Tuktuk") 
    thread3 = MakananClass("Bika Ambon")
    thread4 = MakananClass("Sumur Jengkol ")
  
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

    



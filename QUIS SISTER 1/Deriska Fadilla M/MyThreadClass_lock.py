import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class MyPasien (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> " + self.name + \
             " pasien diberikan no daftar "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " penuh\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = MyPasien("no daftar pasien ", randint(1,5))
    thread2 = MyPasien("no daftar pasien", randint(1,5))
    

    # Thread Running
    thread1.start()
    thread2.start()
   

    # Thread joining
    thread1.join()
    thread2.join()
    

    # End 
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    
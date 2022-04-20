import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class Mysiswa (Thread):
   def _init_(self, name, duration):
      Thread._init_(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> " + self.name + \
             " siswa diberikan no absen "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " over\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Mysiswa("no absen siswa ", randint(1,10))
    thread2 = Mysiswa("no absen siswa", randint(1,10))
    

    # Thread Running
    thread1.start()
    thread2.start()
   

    # Thread joining
    thread1.join()
    thread2.join()
    

    # End 
    print("selesai")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if _name_ == "_main_":
    main()
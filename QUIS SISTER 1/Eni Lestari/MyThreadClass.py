import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class CerdasCermat (Thread):
   def _init_(self, name, duration):
      Thread._init_(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> " + self.name + \
             " kodenya adalah "\
             + str(os.getpid()) + "\n")
      threadLock.release()
      time.sleep(self.duration)
      print ("---> " + self.name + " telah siap \n")
      #Release the Lock


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = CerdasCermat("Ruangan Cerdas cermat IPA yang digunakan ", randint(1,10))
    thread2 = CerdasCermat("Soal 4", randint(1,10))

    

    # Thread Running
    thread1.start()
    thread2.start()

    

    # Thread joining
    thread1.join()
    thread2.join()

    
    # End
    print("Selamat Datang di Ruangan Cerdas cermat IPA  para peserta acara lomba ")
    print("Selamat Mengerjakan ")

    #Execution Time
    print("waktu yang dibutuhkan untuk mengerjakan soal %s  seconds soal" % (time.time() - start_time))



if __name__ == "_main_":
    main()
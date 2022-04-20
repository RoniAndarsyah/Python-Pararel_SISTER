import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class Montir (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> " + self.name + \
             " sedang bekerja, memperbaiki mobil dengan plat nomor "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " istirahat\n")
      #Release the Lock
      threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    thread1 = Montir("Montir 1 ", randint(1,10))
    thread2 = Montir("Montir 2 ", randint(1,10))
    thread3 = Montir("Montir 3 ", randint(1,10))

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()

    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()

    # End 
    print("Mobil selesai diperbaiki")

    #Execution Time
    print("Perbaikan memakan waktu %s detik" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    



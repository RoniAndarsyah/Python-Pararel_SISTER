import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class Absen(Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> " + self.name + \
             " dengan absen "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " selesai absen\n")
      #Release the Lock
      threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    thread1 = Absen("Siswa", randint(1,10))
    thread2 = Absen("Guru", randint(1,10))



    # Thread Running
    thread1.start()
    thread2.start()



    # Thread joining
    thread1.join()
    thread2.join()



    # End 
    print("Jagalah ketertiban")

    #Execution Time
    print("Waktu yang dibutuhkan untuk mengabsen siswa dan guru yaitu %s  detik" % (time.time() - start_time))


if __name__ == "__main__":
    main()
    
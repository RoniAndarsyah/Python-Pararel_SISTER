import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class AnggotaKelas (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> " + self.name + \
             " Sedang Belajar, Dalam Kelas ini ada "\
             + str(os.getpid()) + "\n")
      threadLock.release()
      time.sleep(self.duration)
      print ("---> " + self.name + " kelebihan\n")
      #Release the Lock


def main():
    start_time = time.time()
    
    # Thread Creation
    murid1 = AnggotaKelas("murid#1 ", randint(1,10))
    murid2 = AnggotaKelas("murid#2 ", randint(1,10))
    murid3 = AnggotaKelas("murid#3 ", randint(1,10))
    murid4 = AnggotaKelas("murid#4 ", randint(1,10))
    murid5 = AnggotaKelas("murid#5 ", randint(1,10))
    murid6 = AnggotaKelas("murid#6 ", randint(1,10))
    murid7 = AnggotaKelas("murid#7 ", randint(1,10))
    murid8 = AnggotaKelas("murid#8 ", randint(1,10))
    murid9 = AnggotaKelas("murid#9 ", randint(1,10))

    # murid Running
    murid1.start()
    murid2.start()
    murid3.start()
    murid4.start()
    murid5.start()
    murid6.start()
    murid7.start()
    murid8.start()
    murid9.start()

    # murid joining
    murid1.join()
    murid2.join()
    murid3.join()
    murid4.join()
    murid5.join()
    murid6.join()
    murid7.join()
    murid8.join()
    murid9.join()

    # End
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    



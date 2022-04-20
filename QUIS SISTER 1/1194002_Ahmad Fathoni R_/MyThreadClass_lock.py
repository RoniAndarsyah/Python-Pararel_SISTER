import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class AnggotaMhs (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> " + self.name + \
             " Setiap orang Di kelas membawa bekal sebesar,  "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " over\n")
      #Release the Lock
      threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    mahasiswa1 = AnggotaMhs("mahasiswa#1 ", randint(1,10))
    mahasiswa2 = AnggotaMhs("mahasiswa#2 ", randint(1,10))
    mahasiswa3 = AnggotaMhs("mahasiswa#3 ", randint(1,10))
    mahasiswa4 = AnggotaMhs("mahasiswa#4 ", randint(1,10))
    mahasiswa5 = AnggotaMhs("mahasiswa#5 ", randint(1,10))
    mahasiswa6 = AnggotaMhs("mahasiswa#6 ", randint(1,10))
    mahasiswa7 = AnggotaMhs("mahasiswa#7 ", randint(1,10))
    mahasiswa8 = AnggotaMhs("mahasiswa#8 ", randint(1,10))
    mahasiswa9 = AnggotaMhs("mahasiswa#9 ", randint(1,10))

    # mahasiswa Running
    mahasiswa1.start()
    mahasiswa2.start()
    mahasiswa3.start()
    mahasiswa4.start()
    mahasiswa5.start()
    mahasiswa6.start()
    mahasiswa7.start()
    mahasiswa8.start()
    mahasiswa9.start()

    # mahasiswa joining
    mahasiswa1.join()
    mahasiswa2.join()
    mahasiswa3.join()
    mahasiswa4.join()
    mahasiswa5.join()
    mahasiswa6.join()
    mahasiswa7.join()
    mahasiswa8.join()
    mahasiswa9.join()

    # End 
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    



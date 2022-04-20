import time
import os
from random import randint
from threading import Thread

class PetugasCucian (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> " + self.name + \
             " sedang bekerja, mencuci kendaraan dengan plat nomor "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " telah selesai mengerjakan\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = PetugasCucian("Petugas 1 ", randint(1,10))
    thread2 = PetugasCucian("Petugas 2 ", randint(1,10))
    thread3 = PetugasCucian("Petugas 3 ", randint(1,10))

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()

    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()

    # End 
    print("Kendaraan diserahkan ke pemilik")

    #Execution Time
    print("Total waktu mencuci dengan 3 orang pekerja adalah %s detik" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    



import time
import os
from random import randint
from threading import Thread

class Mahasiswa (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> " + self.name + \
             " Sedang mengerjakan ujian dengan nomor ujian "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " pengerjaan ujian telah berakhir\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Mahasiswa("Mahasiswa#1 ", randint(1,10))
    thread2 = Mahasiswa("Mahasiswa#2 ", randint(1,10))
    thread3 = Mahasiswa("Mahasiswa#3 ", randint(1,10))
    thread4 = Mahasiswa("Mahasiswa#4 ", randint(1,10))
    thread5 = Mahasiswa("Mahasiswa#5 ", randint(1,10))
    thread6 = Mahasiswa("Mahasiswa#6 ", randint(1,10))
    thread7 = Mahasiswa("Mahasiswa#7 ", randint(1,10))
    thread8 = Mahasiswa("Mahasiswa#8 ", randint(1,10))
    thread9 = Mahasiswa("Mahasiswa#9 ", randint(1,10))

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    # End 
    print("Selesai")

    #Execution Time
    print("--- %s detik ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

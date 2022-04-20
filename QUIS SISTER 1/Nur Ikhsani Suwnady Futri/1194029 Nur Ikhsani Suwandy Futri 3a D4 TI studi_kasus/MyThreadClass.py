
#studi kasus tentang perlombaan cerdas cermat mengenai pendaftaran
import time
import os
from random import randint
from threading import Thread

class Tes (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> " + self.name + \
             " menggunkan kode pendaftaran yaitu "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " Segera dilaksanakan\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = Tes("Perlombaan ini ", randint(1,10))





    # Thread Running
    thread1.start()



    

    # Thread joining
    thread1.join()



    

    # End 
    print("Selamat Mengikuti Perlombaan")

    #Execution Time
    print("Waktu yang diperlukan dalam mendaftar %s seconds perorang yang mendaftar" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    



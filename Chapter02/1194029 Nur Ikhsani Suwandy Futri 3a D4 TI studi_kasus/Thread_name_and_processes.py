#studi kasus tentang perlombaan cerdas cermat
from threading import Thread
import time
import os

class Tes (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Soal dibagikan kepada peserta {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # Thread Creation
    thread1 = Tes("soal 1 ")
    thread2 = Tes("soal 2 ")
  
    # Thread Running
    thread1.start()
    thread2.start()


    # Thread joining
    thread1.join()
    thread2.join()

    # End 
    print("soal selesai dibagikan")


if __name__ == "__main__":
    main()

    



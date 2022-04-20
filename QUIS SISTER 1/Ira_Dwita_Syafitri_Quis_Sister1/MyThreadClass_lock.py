import threading
import time
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class Paket (Thread):
   def __init__(self, barang, waktu):
      Thread.__init__(self)
      self.barang = barang
      self.waktu = waktu
   def run(self):
      threadLock.acquire()      
      print ("Paket " + self.barang +  "dikirim \n")
      time.sleep(self.waktu)
      print ("Paket " + self.barang + " diterima  dalam ",self.waktu,"hari\n")
      threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    t1 = Paket("Pakaian ", randint(3,7))
    t2 = Paket("Sepatu ", randint(3,7))
    t3 = Paket("Kerudung ", randint(3,7))
    # Thread Running
    t1.start()
    t2.start()
    t3.start()

    # Thread joining
    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()

    



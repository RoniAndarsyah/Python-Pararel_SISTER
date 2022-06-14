from threading import Thread
import time
import os

class Komputer(Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Komputer yang masih bekerja yaitu komputer {}".format(self.name))

def main():
    from random import randint
    # pembuatan thread
    proses1 = Komputer("bernomor 1 ")
    proses2 = Komputer("bernomor 2 ")
    proses3 = Komputer("bernomor 3 ")
  
    # memulai proses threading
    proses1.start()
    proses2.start()
    proses3.start()


    # Thread joining
    proses1.join()
    proses2.join()
    proses3.join()

    # End
    print("Selesai")


if __name__ == "__main__":
    main()

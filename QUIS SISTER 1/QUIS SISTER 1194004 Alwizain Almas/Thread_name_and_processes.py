from threading import Thread
import time
import os

class Loket (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Penumpang yang sedang melakukan check-in berada pada {}".format(self.name))

def main():
    from random import randint
    antrian1 = Loket("Loket 1 ")
    antrian2 = Loket("Loket 2 ")
    antrian3 = Loket("Loket 3 ")
  
    antrian1.start()
    antrian2.start()
    antrian3.start()

    antrian1.join()
    antrian2.join()
    antrian3.join()

    print("Selesai!")


if __name__ == "__main__":
    main()

    



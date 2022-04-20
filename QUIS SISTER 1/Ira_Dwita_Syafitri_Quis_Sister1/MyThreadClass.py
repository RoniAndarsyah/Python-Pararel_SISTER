from random import randint
from threading import Thread
import time

class balapan (Thread):
   def __init__(self, x, duration):
      Thread.__init__(self)
      self.x = x
      self.duration = duration
   def run(self):
      print (self.x + "\n")
      time.sleep(self.duration)
      print (self.x + " finish dalam",self.duration,"detik \n")


def main():
    print("Bersedia")
    time.sleep(randint(1,5))
    print("Mulai \n")
    # Thread Creation
    thread1 = balapan("Rosi", randint(1,10))
    thread2 = balapan("Marques", randint(1,10))
    thread3 = balapan("Lorenzo", randint(1,10))

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()

    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    main()

    



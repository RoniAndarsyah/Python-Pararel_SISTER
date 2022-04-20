import threading
import random
from threading import Thread
import time


# Lock Definition
threadLock = threading.Lock()

class subclassThread (Thread):
    def __init__(self, name):
      Thread.__init__(self)
      self.name = name
    def run(self): 
      threadLock.acquire()
      print("jalankan proses generate random number proses  {}".format(self.name))
      threads = list()
      randomNumber = GenerateRandomNumber()
      time.sleep(random.randint(1,10))
      print("hasil generate random number {} dari operasi {}".format(randomNumber, self.name))
      threadLock.release()
def GenerateRandomNumber():
        listRandom = list()
        for i in range(0,10):
            listRandom.append("arul")
        return listRandom

def main(): 
    thread1 = subclassThread("Generate Random Number #1 ")
    thread2 = subclassThread("Generate Random Number #2 ")
  
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End")


if __name__ == "__main__":
    main()

    



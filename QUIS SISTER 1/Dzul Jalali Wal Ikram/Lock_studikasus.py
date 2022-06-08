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
      print(self.name, "Sedang Mengantri untuk membayar")
      time.sleep(random.randint(1,10))
      print(self.name, "Selesai Mengantri")
      threadLock.release()


def main(): 
    thread1 = subclassThread("Person #1 ")
    thread2 = subclassThread("Person #2 ")
  
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End")


if __name__ == "__main__":
    main()
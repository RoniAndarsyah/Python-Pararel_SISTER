from threading import Thread
import time
import os

class ThreadSaya (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Proses yang sedang berjalan dengan ID {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # pembuatan thread
    proses1 = ThreadSaya("Thread ID 1 ")
    proses2 = ThreadSaya("Thread ID 2 ")
    proses3 = ThreadSaya("Thread ID 3 ")
  
    # memulai proses threading
    proses1.start()
    proses2.start()
    proses3.start()


    # Thread joining
    proses1.join()
    proses2.join()
    proses3.join()

    # Selesai
    print("Selesai")


if __name__ == "__main__":
    main()

    



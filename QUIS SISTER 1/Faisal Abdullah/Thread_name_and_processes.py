from threading import Thread
import time
import os

class AbdulThread (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Proses yang sedang berjalan dengan ID {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # pembuatan thread
    t1 = AbdulThread(" 1 ")
    t2 = AbdulThread(" 2 ")
    t3 = AbdulThread(" 3 ")
  
    # memulai proses threading
    t1.start()
    t2.start()
    t3.start()


    # Thread joining
    t1.join()
    t2.join()
    t3.join()

    # Selesai
    print("Selesai")


if __name__ == "__main__":
    main()

    



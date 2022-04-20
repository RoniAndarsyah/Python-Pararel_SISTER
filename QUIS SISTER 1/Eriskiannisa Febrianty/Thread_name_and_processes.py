# Tugas studi Kasus
from threading import Thread

class MyThreadClass (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Kereta Sedang Menuju ke {}".format(self.name)) 

def main():
    from random import randint
    # Thread Creation
    thread1 = MyThreadClass("Stasiun 1 ")
    thread2 = MyThreadClass("Stasiun 2 ")
  
    # Thread Running
    thread1.start()
    thread2.start()


    # Thread joining
    thread1.join()
    thread2.join()

    # End 
    print("Kereta Sampai di tujuan")


if __name__ == "__main__":
    main()

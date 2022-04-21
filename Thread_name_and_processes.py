from threading import Thread
import time
import os

class Drakor (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
     
   def run(self):
       print("Rekomendasi Drama Korea 2022 {}".format(self.name)) 
       time.sleep(4)
      

def main():
 
    # Thread Creation
    thread1 = Drakor(": Prosposal Business   ")
    thread2 = Drakor(": Twenty-Five Twenty-One   ")
  
    # Thread Running
    thread1.start()
    thread2.start()


    # Thread joining
    thread1.join()
    thread2.join()

    # End 
    print("Selamat Menonton")


if __name__ == "__main__":
    main()

    



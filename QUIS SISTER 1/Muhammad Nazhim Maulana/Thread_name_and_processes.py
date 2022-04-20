from threading import Thread
import time
import os

class MyThreadClass (Thread):
   def __init__(self, nama, umur):
      Thread.__init__(self)
      self.nama = nama
      self.umur = umur
 
   def run(self):
       print("Pemain Dengan Nomor Punggung {} Sudah berusia {}".format(self.nama, self.umur))

def main():
    from random import randint
    # Thread Creation
    mulai = time.time()
    for i in range(21):
        thread1 = MyThreadClass("#" + str(i), randint(17, 23))
        thread2 = MyThreadClass("#" + str(i + 5), randint(17, 23))
    
        # Thread Running
        thread1.start()
        time.sleep(randint(5,10))
        thread2.start()


        # Thread joining
        thread1.join()
        thread2.join()

    # End 
    print("End")

    # Waktu Eksekusi
    print("--- %s seconds ---" % (time.time() - mulai))

if __name__ == "__main__":
    main()

    



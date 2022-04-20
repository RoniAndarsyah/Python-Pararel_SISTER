import time
from random import randint
from threading import Thread
from time import ctime

print('\n ### Perocbaan Sendiri ###')

class ProduksiThread (Thread):
   def __init__(self, nama, umur, asal, mulai_eksekusi):
      Thread.__init__(self)
      self.nama = nama
      self.umur = umur
      self.asal = asal
      self.mulai_eksekusi = mulai_eksekusi
   def run(self):
      print ("---> " + self.nama + \
             " berjalan, dengan umur "\
             + str(self.umur) + " Berasal dari " + self.asal + "Berangkat pada" + self.mulai_eksekusi +"\n")
      time.sleep(randint(1,10))
      print ("---> " + self.nama + " selesai dengan Waktu " + self.mulai_eksekusi + "\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    orang1 = ProduksiThread("Orang#1 ", randint(1,10), "Indonesia", ctime())
    orang2 = ProduksiThread("Orang#2 ", randint(1,10), "Indonesia", ctime())
    orang3 = ProduksiThread("Orang#3 ", randint(1,10), "Indonesia", ctime())
    orang4 = ProduksiThread("Orang#4 ", randint(1,10), "Indonesia", ctime())
    orang5 = ProduksiThread("Orang#5 ", randint(1,10), "Indonesia", ctime())
    orang6 = ProduksiThread("Orang#6 ", randint(1,10), "Indonesia", ctime())
    orang7 = ProduksiThread("Orang#7 ", randint(1,10), "Indonesia", ctime())
    orang8 = ProduksiThread("Orang#8 ", randint(1,10), "Indonesia", ctime())
    orang9 = ProduksiThread("Orang#9 ", randint(1,10), "Indonesia", ctime())

    # Thread Running
    orang1.start()
    orang2.start()
    orang3.start()
    orang4.start()
    orang5.start()
    orang6.start()
    orang7.start()
    orang8.start()
    orang9.start()

    # Thread joining
    orang1.join()
    orang2.join()
    orang3.join()
    orang4.join()
    orang5.join()
    orang6.join()
    orang7.join()
    orang8.join()
    orang9.join()

    # End 
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
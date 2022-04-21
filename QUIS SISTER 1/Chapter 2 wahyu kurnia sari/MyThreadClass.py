import time
import os
from random import randint
from threading import Thread


class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        print("---> " + self.name + \
              " Total Stok Smartphone tahun 2022 di BEC yaitu, " \
              + str(os.getpid()) + "\n")
        time.sleep(self.duration)
        print("---> " + self.name + " Update Terkini Stok habis\n")


def main():
    start_time = time.time()

    thread1 = MyThreadClass("Tersedia Merk Samsung ", randint(1, 10))
    thread2 = MyThreadClass("Tersedia Merk Iphone ", randint(1, 10))
    thread3 = MyThreadClass("Tersedia Merk Redmi ", randint(1, 10))
    thread4 = MyThreadClass("Tersedia Merk Oppo ", randint(1, 10))
    thread5 = MyThreadClass("Tersedia Merk Xiomi ", randint(1, 10))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()


    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    # End
    print("Tunggu sampai barang tersedia kembali")

    # Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()





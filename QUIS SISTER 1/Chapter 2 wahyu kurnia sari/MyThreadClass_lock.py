import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()


class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Acquire the Lock
        threadLock.acquire()
        print("---> " + self.name + \
              " Jumlah stock motor di indonesia berdasarkan merk" \
              + str(os.getpid()) + "\n")
        time.sleep(self.duration)
        print("---> " + self.name + " matic\n")
        # Release the Lock
        threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    thread1 = MyThreadClass("Vario#1 ", randint(1, 10))
    thread2 = MyThreadClass("Beat#2 ", randint(1, 10))
    thread3 = MyThreadClass("PCX#3 ", randint(1, 10))
    thread4 = MyThreadClass("Piaggio#4 ", randint(1, 10))
    thread5 = MyThreadClass("Mio#5 ", randint(1, 10))
    thread6 = MyThreadClass("Nmax#6 ", randint(1, 10))
    thread7 = MyThreadClass("Lexi#7 ", randint(1, 10))
    thread8 = MyThreadClass("Aerox#8 ", randint(1, 10))
    thread9 = MyThreadClass("ADV#9 ", randint(1, 10))

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    # End
    print("Motor Matic Siap di Distribusikan")

    # Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()





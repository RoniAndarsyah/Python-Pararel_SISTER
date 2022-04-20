 
     
from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

jumlah_running = 5
selesai = Barrier(jumlah_running)
mobil = ['Honda', 'Toyota', 'Daihatsu', 'Hyundai', 'Suzuki', 'Mitsubishi', 'Nissan']

def jenis():
    brand = mobil.pop()
    sleep(randrange(2, 5))
    print('%s Merupakan brand mobil \n' % (brand))
    selesai.wait()

def main():
    threads = []
    print('Jenis Brand Mobil!')
    for i in range(jumlah_running):
        threads.append(Thread(target=jenis))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Udah Dulu Ya!')

if __name__ == "__main__":
    main()

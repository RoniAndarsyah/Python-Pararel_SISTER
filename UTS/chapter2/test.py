#Dzul Jalali Wal Ikram

from random import randrange
import threading
from time import ctime, sleep
from threading import Barrier, Thread

num_siswa = 3
threadsynchronizer = threading.Barrier(num_siswa)
nama_siswa = ['Udin', 'Asep', 'Cecep']

def skip(n):
    name = nama_siswa.pop()
    sleep(randrange(2, 5))
    print("{} tidak hadir pada hari {} dikarenakan Sakit".format(name, ctime()))
    threadsynchronizer.wait()
    print("{} Surat Sakit sampai pada: {} ".format(name, ctime()))

def total(test=None):
    print("Jumlah siswa yang sakit pada hari {} adalah {} orang".format(ctime(), test))

def main():
    threads = []
    print('Saatnya Absen')
    for i in range(num_siswa):
        threads.append(Thread(target=skip, name="skip", args=(num_siswa,), group=None, kwargs=None))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Absen Selesai!')


# dict2 = {'name': 'Udin'}
my_dict = {'test': num_siswa}

thread2 = threading.Thread(target=total,name="total", group=None, kwargs=my_dict)

thread2.start()

thread2.join()


if __name__ == "__main__":
    main()
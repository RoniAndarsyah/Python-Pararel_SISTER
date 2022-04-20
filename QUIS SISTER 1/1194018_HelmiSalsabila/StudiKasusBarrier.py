# example of using a barrier
from time import ctime, sleep
from random import random
from threading import Thread, Barrier

name = ['Farhan', 'Kevin', 'Putri', 'Helmi', 'Salsabila']
def main(barrier, number):
    value = random() * 10
    mhs = name.pop()
    sleep(value)
    print(f'No urut {number} %s sudah sampai di kampus, pada hari %s dengan waktu: {value} \n' % (mhs, ctime()))
    # menunggu semuanya slesai
    barrier.wait()

# buat barrier
case = Barrier(5 + 1)
for i in range(5):
    gasin = Thread(target=main, args=(case, i))
    gasin.start()
print('Mulai..')
case.wait()
print('Selesai')
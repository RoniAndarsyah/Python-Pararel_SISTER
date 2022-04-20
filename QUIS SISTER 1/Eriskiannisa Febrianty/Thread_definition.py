# Tugas Studi Kasus
import time
from threading import Thread

def Proses(i):
    print("Thread %i memproses dalam 5 detik." % i)
    time.sleep(5)
    print("Thread %i selesai di proses." % i)

for i in range(10):
    th = Thread(target=Proses, args=(i, ))
    th.start()
    th.join()
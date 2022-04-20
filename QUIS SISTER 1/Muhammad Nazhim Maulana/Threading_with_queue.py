""""Thread synchronisation with queue"""

from threading import Thread
from queue import Queue
import time
from random import randint

def func(q, nomor_tugas):
    while True:
        task = q.get()
        time.sleep(randint(4,9))
        q.task_done()
        print(f'Anto #{nomor_tugas} sedang mengerjakan tugas #{task} dalam antrean.')

q = Queue()

print('### Antrean Pengerjaan Tugas ###')
mulai = time.time()

# Mulai proses antrean
for i in range(4):
    pekerja = Thread(target=func, args=(q, i,), daemon=True)
    if i > 2:
        time.sleep(randint(6,9))
    else:
        time.sleep(randint(0,1))
    # Memulai Thread
    pekerja.start()

# Memasukkan ke dalam Antrean
for j in range(10):
    q.put(j)
    
q.join()

# End 
print("Antrean Selesai")

#Execution Time
print("--- %s seconds ---" % (time.time() - mulai))
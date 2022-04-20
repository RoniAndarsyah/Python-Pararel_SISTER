#%% Thread definition = suatu proses yang dapat dijadwalkan untuk di execute
import time
from threading import Thread

def ngaduk(i):
    print ("proses ngaduk semen %d" % i)
    time.sleep(2)
    print ("ngaduk semen beres dalam %d" % i)

for i in range(10):
    t = Thread(target=ngaduk, args=(i,))
    t.start()
# %%

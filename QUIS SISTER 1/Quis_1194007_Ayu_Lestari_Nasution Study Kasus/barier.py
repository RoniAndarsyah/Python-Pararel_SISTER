from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep
num = 4
# 4 threads will need to pass this barrier to get released.
b = Barrier(num)
names = ['India', 'Japan', 'USA', 'China']
def player():
   name = names.pop()
   sleep(randrange(2, 5))
   print('%s reached the barrier at: %s \n' % (name, ctime()))
   b.wait()
threads = []
print("Race starts now…")
for i in range(num):
   threads.append(Thread(target=player))
   threads[-1].start()
"""
Below loop enables waiting for the threads to complete before moving on with the main script.
"""
for thread in threads:
   thread.join()
print("All Reached Barrier Point!")
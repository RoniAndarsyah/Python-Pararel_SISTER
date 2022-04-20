# program to illustrate the use of RLocks

# importing the module
from csv import list_dialects
import threading

# initializing the shared resource
Lidiya = 18

# creating an RLock object instead
# of Lock object
lock = threading.RLock()

# the below thread is trying to access
# the shared resource
lock.acquire()
Lidiya = Lidiya + 19

# the below thread is trying to access
# the shared resource
lock.acquire()
Lidiya = Lidiya - 24
lock.release()
lock.release()

# displaying the value of shared resource
print(Lidiya)
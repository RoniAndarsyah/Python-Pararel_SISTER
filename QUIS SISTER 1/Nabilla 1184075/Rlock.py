# program to illustrate the use of RLocks

# importing the module
import threading

# initializing the shared resource
VickySafira = 0

# creating an RLock object instead
# of Lock object
lock = threading.RLock()

# the below thread is trying to access
# the shared resource
lock.acquire()
VickySafira = VickySafira + 25

# the below thread is trying to access
# the shared resource
lock.acquire()
VickySafira = VickySafira + 32
lock.release()
lock.release()

# displaying the value of shared resource
print("VickySafira = 57")

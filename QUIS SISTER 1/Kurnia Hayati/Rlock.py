# importing the module
import threading
from time import ctime

# initializing the shared resource, isialisasi sumber daya
fanny = 0

# creating an RLock object instead, membuat objek RLock sebagsi pengganti lock objek 
# of Lock object
lock = threading.RLock()

# the below thread is trying to access, untuk mengakses 
# the shared resource
lock.acquire() # metode mengunci data hingga terblokir 
fanny = fanny + 4

# the below thread is trying to access
# the shared resource
lock.acquire()
fanny = fanny + 2
lock.release() # melepaskan kunci
lock.release()

# displaying the value of shared resource, menampilkan nilai sumber daya
print('No %s menyelesaikan ujian dengan waktu  %s' % (fanny, ctime()))
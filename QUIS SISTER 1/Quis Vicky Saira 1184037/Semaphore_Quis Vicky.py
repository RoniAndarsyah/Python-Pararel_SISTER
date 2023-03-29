# importing the modules
from threading import *		
import time		

# creating thread instance where count = 3
obj = Semaphore(1)

# creating instance
def display(name):	
	
	# calling acquire method
	obj.acquire()				
	for i in range(1):
		print('Jenis Bakso, ', end = '')
		time.sleep(1)
		print(name)
		
		# calling release method
		obj.release()	
		
# creating multiple thread
t1 = Thread(target = display , args = ('Urat-1',))
t2 = Thread(target = display , args = ('Beranak-2',))
t3 = Thread(target = display , args = ('Mercon-3',))
t4 = Thread(target = display , args = ('Telur-4',))
t5 = Thread(target = display , args = ('Kecil-5',))

# calling the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

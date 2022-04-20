# importing the modules
from threading import *		
import time		

# creating thread instance where count = 3
obj = Semaphore(2)		

# creating instance
def display(name):	
	
	# calling acquire method
	obj.acquire()				
	for i in range(7):
		print('M.Ihsan, ', end = ' Diyaa')
		time.sleep(1)
		print(name)
		
		# calling release method
		obj.release()	
		
# creating multiple thread
t1 = Thread(target = display , args = ('Thread-1',))
t2 = Thread(target = display , args = ('Thread-2',))
t3 = Thread(target = display , args = ('Thread-3',))
t4 = Thread(target = display , args = ('Thread-4',))
t5 = Thread(target = display , args = ('Thread-5',))
t6 = Thread(target = display , args = ('Thread-6',))
t7 = Thread(target = display , args = ('Thread-7',))

# calling the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
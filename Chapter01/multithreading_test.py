from do_something import *
import time
import threading

if __name__ == "__main__": # Memastikan code ada pada main function/tidak diimport.
    start_time = time.time()
    size = 10000000
    threads = 10  
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=do_something(size, out_list)) # Membuat Thread
        jobs.append(thread)
    for j in jobs:
        j.start()  # memulai proses

    
    for j in jobs:
        j.join() # menyelesaikan proses

    print ("List processing complete.") #proses selesai
    end_time = time.time()
    print("multithreading time=", end_time - start_time)
	

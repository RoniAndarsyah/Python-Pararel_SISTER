from do_something import *
import time
import multiprocessing


if __name__ == "__main__":  # Memastikan code ada pada main function/tidak diimport.
    start_time = time.time()
    size = 10000000   
    procs = 10   
    jobs = []
    for i in range(0, procs): #Membuat proses
        out_list = list()
        process = multiprocessing.Process\
                  (target=do_something,args=(size,out_list)) # Menginisiasi proses dengan argument
        jobs.append(process)

    for j in jobs:
        j.start() # memulai proses

    for j in jobs: # menyelesaikan proses
        j.join()

    print ("List processing complete.") # proses selesai
    end_time = time.time()
    print("multiprocesses time=", end_time - start_time)

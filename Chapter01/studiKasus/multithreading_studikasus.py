from do_studikasus import totalKaryawan
import time
import threading

if __name__ == "__main__":
    start_time = time.time()
    count = 10
    procs = 1   
    process = []
    for i in range(0, procs):
        out_list = list()
        thread = threading.Thread(target=totalKaryawan(count,out_list))
        process.append(thread)

    for j in process:
        j.start()

    for j in process:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multithreading time=", end_time - start_time)
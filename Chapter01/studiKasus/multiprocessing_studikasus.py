from do_studikasus import totalKaryawan
import time
import multiprocessing

if __name__ == "__main__":
    start_time = time.time()
    size = 1000
    procs = 10   
    list_karyawan = []
    # out_list = list()
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process\
                    (target=totalKaryawan,args=(size,out_list))
        list_karyawan.append(process)

    for j in list_karyawan:
        j.start()

    for j in list_karyawan:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multiprocesses time=", end_time - start_time)
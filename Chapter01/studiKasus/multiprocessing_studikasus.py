
from multiprocessing import Process
import time

def karyawan(daftar='Asia'):
    print('Nama Karyawan : ', daftar)

if __name__ == "__main__":  # Memastikan code ada pada main function/tidak diimport.
    start_time = time.time()
    names = ['Udin Wazowski', 'Jon cool', 'Asoyy gamink']
    procs = []
    proc = Process(target=karyawan)  # Menginisiasi proses tanpa argument
    procs.append(proc)
    proc.start()

    # Menjalankan proses dengan argumen
    for name in names:
        # print(name)
        proc = Process(target=karyawan, args=(name,))
        procs.append(proc)
        proc.start()

    # menyelesaikan proses
    for proc in procs:
        proc.join()

    print ("List processing complete.") # proses selesai
    end_time = time.time()
    print("multiprocesses time=", end_time - start_time)
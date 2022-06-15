import multiprocessing
import time

def simple_looping():
    arrHero = ['Budi Utomo', 'Salahudin Yani', 'Soekarno']
    name = multiprocessing.current_process().name
    print ("Memulai memanggil nama pasien dengan Poli : %s \n" %name)
    for i in range(3):
        time.sleep(1)
        print(arrHero[i])
    print ("Berhenti Looping nama proses = %s \n" %name)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='Poli Mata', target=simple_looping)
    process_with_name.start()
    process_with_name.join()
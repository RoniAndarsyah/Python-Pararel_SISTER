import tugas
import time

if __name__ == '__main__':
    result = tugas.longtime_add.delay(1,2)
    print ('Menunggu Proses Selesai ')
    time.sleep(10)
    print ('Proses telah selesai')
    
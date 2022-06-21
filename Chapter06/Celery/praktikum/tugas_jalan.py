import tugas
import time

if __name__ == '__main__':
    result = tugas.longtime_add.delay(1,2)
    # at this time, our task is not finished, so it will return False
    print ('Menunggu Proses Selesai ')
    print ('Task result: ')
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print ('Proses telah selesai')
    
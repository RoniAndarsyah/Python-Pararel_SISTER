import multiprocessing
from time import ctime

class MyProcess(multiprocessing.Process):

    def run(self):
        print ('%s produk selesai di inputkan pada tanggal %s' %(self.name, ctime()))
        return

if __name__ == '__main__':
    for i in range(10):
        process = MyProcess()
        process.start()
        process.join()


import multiprocessing
import time

class MyProcess(multiprocessing.Process):

    def run(self):
        print ('Menjalankan fungsi dengan proses %s' %self.name)
        time.sleep(1)
        return

if __name__ == '__main__':
    for i in range(10):
        process = MyProcess()
        process.start()
        process.join()


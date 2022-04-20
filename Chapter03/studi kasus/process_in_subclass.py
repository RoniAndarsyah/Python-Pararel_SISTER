import multiprocessing

class Suhu(multiprocessing.Process):

    def run(self):
        print ('suhu pada suatu daerah dapat bernilai %s derajat' %self.name)
        return

if __name__ == '__main__':
    for i in range(10):
        process = Suhu()
        process.start()
        process.join()


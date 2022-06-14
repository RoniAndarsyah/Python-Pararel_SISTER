#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def inifunction(i):
    print ('Mengecheck user dengan Role: %s' %i)
    for j in range (0,i):
        print('Jumlah User :%s' %j)
    return

if __name__ == '__main__':
    for i in range(5):
        process = multiprocessing.Process(target=inifunction, args=(i,))
        process.start()
        process.join()
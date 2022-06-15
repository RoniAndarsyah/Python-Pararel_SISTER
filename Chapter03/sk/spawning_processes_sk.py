#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def CustomFunction(i):
    print ('Menjalankan fungsi dengan process no : %s' %i)
    for j in range (0,i):
        print('Hasil looping fungsi dengan no : %s' %j)
    return

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=CustomFunction, args=(i,))
        process.start()
        process.join()
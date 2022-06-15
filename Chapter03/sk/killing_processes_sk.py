import multiprocessing
import time

def foo():
    print ('Starting function')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Finished function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Proses sebelum dimulai:', p, p.is_alive())
    p.start()
    print ('Proses berjalan:', p, p.is_alive())
    p.terminate()
    print ('Proses dihentikan:', p, p.is_alive())
    p.join()
    print ('Proses disatukan:', p, p.is_alive())
    print ('Proses exit code:', p.exitcode)

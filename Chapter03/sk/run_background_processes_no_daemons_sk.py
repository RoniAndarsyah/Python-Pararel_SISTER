import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'bg_process':
        for i in range(0,5):
            print('---> %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('---> %d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    bg_process = multiprocessing.Process(name='bg_process', target=foo)
    bg_process.daemon = False

    no_bg_process = multiprocessing.Process(name='no_bg_process', target=foo)
    no_bg_process.daemon = False

    bg_process.start()
    no_bg_process.start()
#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

def pangkat_2_plus_2(data):
    return data*data+2


if __name__ == '__main__':
    inputs = list(range(0, 10))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(pangkat_2_plus_2, inputs)

    pool.close() 
    pool.join()  
    print ('Pool : ', pool_outputs)
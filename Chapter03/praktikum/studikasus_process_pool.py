#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing
from time import ctime, sleep
from random import random

def function_square(data):
    result = data*data
    return result

produk1 = 'Ram'
produk2 = 'Matherboard'
produk3 = 'Komputer'
if __name__ == '__main__':
    inputs1 = list(range(9,10))
    inputs2 = list(range(19,20))
    inputs3 = list(range(29,30))
    
    pool = multiprocessing.Pool(processes=4)
    pool_outputs1 = pool.map(function_square, inputs1)
    pool_outputs2 = pool.map(function_square, inputs2)
    pool_outputs3 = pool.map(function_square, inputs3)
    
    mhs1 = produk1
    mhs2 = produk2
    mhs3 = produk3
    
    value = random() * 10
    sleep(value)
    
    print (f'Pembagian Nomor Produk: \n Nama Produk: %s \n Nomor Produk: %s \n Waktu render: {value} \n Tanggal: %s \n' % (mhs1, pool_outputs1, ctime()))
    print (f'Pembagian Nomor Produk: \n Nama Produk: %s \n Nomor Produk: %s \n Waktu render: {value} \n Tanggal: %s \n' % (mhs2, pool_outputs2, ctime()))
    print (f'Pembagian Nomor Produk: \n Nama Produk: %s \n Nomor Produk: %s \n Waktu render: {value} \n Tanggal: %s \n' % (mhs3, pool_outputs3, ctime()))
    
    pool.close() 
    pool.join()  
    print('Selesai')
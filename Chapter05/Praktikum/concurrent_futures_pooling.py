import concurrent.futures
import time

jumlah_buku = list(range(1, 5))


def menghitung(number):
    for i in range(50000):
        i += 1
    return i*number


def menilai(item):
    result_item = menghitung(item)
    print('Jika anda membeli %s buku, harganya %s' % (item, result_item))

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.process_time()
    for item in jumlah_buku:
        menilai(item)
    print('Waktu eksekusi Sequential dalam %s detik' % (time.process_time() - start_time))

   
    # Thread Pool Execution
    start_time = time.process_time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in jumlah_buku:
            executor.submit(menilai, item)
    print('Waktu eksekusi Thread Pool dalam %s detik' % (time.process_time() - start_time))

      
    # Process Pool Execution
    start_time = time.process_time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in jumlah_buku:
            executor.submit(menilai, item)
    print('Waktu eksekusi Process Pool dalam %s detik' % (time.process_time() - start_time))

import concurrent.futures
from datetime import datetime

urutan_bilangan = list(range(1, 11))


def hitung_looping(angka):
    for i in range(0,10000000):
        i += 1
    return i*angka


def evaluate(bilangan):
    hasil_bilangan = hitung_looping(bilangan)
    print('Looping %s, dengan hasil %s' % (bilangan, hasil_bilangan))

if __name__ == '__main__':
    # Sequential Execution
    mulai = datetime.now()
    for bilangan in urutan_bilangan:
        evaluate(bilangan)
    print('Metode Sequential dengan waktu %s detik' % (datetime.now() - mulai))

    # Thread Pool Execution
    mulai = datetime.now()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for bilangan in urutan_bilangan:
            executor.submit(evaluate, bilangan)
    print('Metode Thread Pool dengan waktu %s detik' % (datetime.now() - mulai))

    # Process Pool Execution
    mulai = datetime.now()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for bilangan in urutan_bilangan:
            executor.submit(evaluate, bilangan)
    print('Metode Process Pool dengan waktu %s detik' % (datetime.now() - mulai))

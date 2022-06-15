"""Asyncio using Asyncio.Task to execute three math functions in parallel"""

import asyncio


@asyncio.coroutine
def hitung_faktorial(number):
    fact = 1
    for i in range(2, number + 1):
        print('Perhitungan Faktorial(%s)' % i)
        yield from asyncio.sleep(1)
        fact *= i
    print('Hasil Perhitungan Faktorial(%s) = %s' % (number, fact))


@asyncio.coroutine
def hitung_fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print('Perhitungan Fibonacci(%s)' % i)
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print('Hasil Perhitungan Fibonacci(%s) = %s' % (number, a))


@asyncio.coroutine
def hitung_binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result*(n - i + 1)/i
        print('Perhitungan Binomial Coefficient(%s)' % i)
        yield from asyncio.sleep(1)
    print('Hasil Perhitungan Binomial Coefficient(%s, %s) = %s' % (n, k, result))


if __name__ == '__main__':
    task_list = [asyncio.Task(hitung_faktorial(7)),
                 asyncio.Task(hitung_fibonacci(15)),
                 asyncio.Task(hitung_binomial_coefficient(17, 6))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()

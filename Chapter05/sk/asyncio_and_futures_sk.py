import asyncio
import sys


@asyncio.coroutine
def Program1(future, num):
    count = 0
    for i in range(1, num + 1):
        count += i
    yield from asyncio.sleep(4)
    future.set_result('Program 1 hasil penjumlahan looping = %s' % count)


@asyncio.coroutine
def Program2(future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    yield from asyncio.sleep(4)
    future.set_result('Program 2 hasil perhitungan faktorial = %s' % count)


def got_result(future):
    print(future.result())

if __name__ == '__main__':
    num1 = 17
    num2 = 28

    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    tasks = [Program1(future1, num1),
             Program2(future2, num2)]

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

import asyncio
import time
from random import randint


@asyncio.coroutine
def Start_Program():
    print('Memulai menjalankan program\n')
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = yield from Program2(input_value)
    else:
        result = yield from Program1(input_value)
    print('Melanjutkan untuk menjalankan program : \nMenjalankan program ' + result)


@asyncio.coroutine
def Program1(transition_value):
    output_value = 'Program 1 dengan nilai input = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...memproses...')
    if input_value == 0:
        result = yield from Program3(input_value)
    else:
        result = yield from Program2(input_value)

    return output_value + 'Menjalankan program 1a %s' % result


@asyncio.coroutine
def Program2(transition_value):
    output_value = 'Program 2 dengan nilai input = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...memproses...')
    if input_value == 0:
        result = yield from Program1(input_value)
    else:
        result = yield from Program3(input_value)

    return output_value + 'Menjalankan program 2 %s' % result


@asyncio.coroutine
def Program3(transition_value):
    output_value = 'Program 3 dengan nilai input = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...memproses...')
    if input_value == 0:
        result = yield from Program1(input_value)
    else:
        result = yield from End_Program(input_value)

    return output_value + 'Menjalankan program 3 %s' % result


@asyncio.coroutine
def End_Program(transition_value):
    output_value = 'Menghentikan program dengan nilai input = %s\n' % transition_value
    print('...berhenti menjalankan program...')
    return output_value


if __name__ == '__main__':
    print('Menjalankan program dengan Asyncio Coroutine selesai')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Start_Program())

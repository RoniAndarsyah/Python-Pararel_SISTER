import asyncio
import time
from random import randint


@asyncio.coroutine
def start_state():
    print('Memulai Tahapan awal\n')
    input_value = randint(0, 1)
    time.sleep(1)

    if input_value == 0:
        result = yield from tahap2(input_value)
    else:
        result = yield from tahap1(input_value)

    print('Mencoba Coroutine : \nStart State menuju ' + result)


@asyncio.coroutine
def tahap1(transition_value):
    output_value = 'Tahap 1 dengan value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...Mengevaluasi Tahapan...')
    if input_value == 0:
        result = yield from tahap3(input_value)
    else:
        result = yield from tahap2(input_value)

    return output_value + 'Tahap 1 menuju %s' % result


@asyncio.coroutine
def tahap2(transition_value):
    output_value = 'Tahap 2 dengan value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...Mengevaluasi Tahapan...')
    if input_value == 0:
        result = yield from tahap1(input_value)
    else:
        result = yield from tahap3(input_value)

    return output_value + 'Tahap 2 menuju %s' % result


@asyncio.coroutine
def tahap3(transition_value):
    output_value = 'Tahap 3 dengan value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...Mengevaluasi Tahapan...')
    if input_value == 0:
        result = yield from tahap1(input_value)
    else:
        result = yield from end_state(input_value)

    return output_value + 'Tahap 3 menuju %s' % result


@asyncio.coroutine
def end_state(transition_value):
    output_value = 'Tahap akhir value = %s\n' % transition_value
    print('...stop computation...')
    return output_value


if __name__ == '__main__':
    print('Finite state Machine simulation with Asyncio Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())

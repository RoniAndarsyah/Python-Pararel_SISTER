import asyncio
import time
from random import randint


@asyncio.coroutine
def memulai_aktivitas():
    print('Mendatangi toko buku\n')
    input_value = randint(0, 1)
    time.sleep(1)

    if input_value == 0:
        result = yield from aktivitas_2(input_value)
    else:
        result = yield from aktivitas_1(input_value)

    print('Memulai aktivitas dengan ' + result)


@asyncio.coroutine
def aktivitas_1(transition_value):
    output_value = 'Memilih buku dengan transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...mengevaluasi...')
    if input_value == 0:
        result = yield from aktivitas_3(input_value)
    else:
        result = yield from aktivitas_2(input_value)

    return output_value + 'Aktivitas 1 dilanjutkan dengan %s' % result


@asyncio.coroutine
def aktivitas_2(transition_value):
    output_value = 'Mengecek buku dengan transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...mengevaluasi...')
    if input_value == 0:
        result = yield from aktivitas_1(input_value)
    else:
        result = yield from aktivitas_3(input_value)

    return output_value + 'Aktivitas 2 dilanjutkan dengan %s' % result


@asyncio.coroutine
def aktivitas_3(transition_value):
    output_value = 'Membeli buku dengan transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...mengevaluasi...')
    if input_value == 0:
        result = yield from aktivitas_1(input_value)
    else:
        result = yield from mengakhiri_aktivitas(input_value)

    return output_value + 'Aktivitas 3 dilanjutkan dengan %s' % result


@asyncio.coroutine
def mengakhiri_aktivitas(transition_value):
    output_value = 'Membawa buku dengan transition value = %s\n' % transition_value
    print('...aktivitas berhenti...')
    return output_value


if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(memulai_aktivitas())

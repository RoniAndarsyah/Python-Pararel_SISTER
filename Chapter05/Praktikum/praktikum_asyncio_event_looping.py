import asyncio
import time
import random

def task_A(end_time, loop):
    print ("task_A dijalankan")
    start_time = time.time()
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        print('Proses tidak memenuhi kebutuhan, melanjutkan ke proses selanjutnya', (loop.time() + 1.0) < end_time)
        loop.call_later(1, task_B, end_time, loop)
    else:
        print('Proses memenuhi kebutuhan, menghentikan proses', (loop.time() + 1.0) < end_time)
        loop.stop()

def task_B(end_time, loop):
    print ("task_B dijalankan ")
    start_time = time.time()
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        print('Proses tidak memenuhi kebutuhan, melanjutkan ke proses selanjutnya', (loop.time() + 1.0) < end_time)
        loop.call_later(1, task_C, end_time, loop)
    else:
        print('Proses memenuhi kebutuhan, menghentikan proses', (loop.time() + 1.0) < end_time)
        loop.stop()

def task_C(end_time, loop):
    print ("task_C dijalankan")
    start_time = time.time()
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        print('Proses tidak memenuhi kebutuhan, melanjutkan ke proses selanjutnya', (loop.time() + 1.0) < end_time)
        loop.call_later(1, task_A, end_time, loop)
    else:
        print('Proses memenuhi kebutuhan, melanjutkan ke proses selanjutnya', (loop.time() + 1.0) < end_time)
        print('Proses Dihentikan')
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 60
loop.call_soon(task_A, end_loop, loop)
loop.run_forever()
loop.close()


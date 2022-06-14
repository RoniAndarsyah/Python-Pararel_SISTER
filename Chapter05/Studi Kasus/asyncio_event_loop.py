import asyncio
import time
import random

print("Mengecek Ketersediaan Buku")

def buku_A(end_time, loop):
    print ("Buku A")
    print ("Mengecek ketersediaan Buku A")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, buku_B, end_time, loop)
        print("Buku kosong, lanjut mengecek buku lainnya")
    else:
        print("Buku tersedia dan dapat dijual")
        print(end_time)
        loop.stop()

def buku_B(end_time, loop):
    print ("Buku B")
    print ("Mengecek ketersediaan Buku B")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, buku_C, end_time, loop)
        print("Buku kosong, lanjut mengecek buku lainnya")
    else:
        print("Buku tersedia dan dapat dijual")
        print(end_time)
        loop.stop()

def buku_C(end_time, loop):
    print ("Buku C")
    print ("Mengecek ketersediaan Buku B")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, buku_A, end_time, loop)
        print("Buku kosong, lanjut mengecek buku lainnya")
    else:
        print("Buku tersedia dan dapat dijual")
        print(end_time)
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 30
loop.call_soon(buku_A, end_loop, loop)
loop.run_forever()
loop.close()


import asyncio
import time
import random

def Program_A(end_time, loop):
    print ("Program A dijalankan. Proses berlangsung. . .")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        print ("Program A Selesai. Menjalankan program selanjutnya. . .")
        loop.call_later(1, Program_B, end_time, loop)
    else:
        print ("Timeout. Program tidak bisa di jalanlan lagi. . .")
        loop.stop()

def Program_B(end_time, loop):
    print ("Program B dijalankan. Proses berlangsung. . .")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        print ("Program B Selesai. Menjalankan program selanjutnya. . .")
        loop.call_later(1, Program_C, end_time, loop)
    else:
        print ("Timeout. Program tidak bisa di jalanlan lagi. . .")
        loop.stop()

def Program_C(end_time, loop):
    print ("Program C dijalankan. Proses berlangsung. . .")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        print ("Program C Selesai. Kembali ke program awal. . .")
        loop.call_later(1, Program_A, end_time, loop)
    else:
        print ("Timeout. Program tidak bisa di jalanlan lagi. . .")
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 60
loop.call_soon(Program_A, end_loop, loop)
loop.run_forever()
loop.close()
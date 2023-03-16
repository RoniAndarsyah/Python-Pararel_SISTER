# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:20:41 2022

@author: Acer
"""

import threading


def Chocolate(thread_number):
    return print('Jumlah Chocolate yang tersedia ditoko{} pcs'.format(thread_number))


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=Chocolate, args=(i,))
        threads.append(t)
        t.start()
        t.join()


if __name__ == "__main__":
    main()

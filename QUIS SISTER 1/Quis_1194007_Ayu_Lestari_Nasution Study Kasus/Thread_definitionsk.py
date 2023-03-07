# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:43:10 2022

@author: Acer
"""

import threading


def pasien(thread_number):
    return print('pasien called by dokter {}'.format(thread_number))


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=pasien, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()

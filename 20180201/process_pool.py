#!/usr/bin/env python3

from multiprocessing import Pool
import time
import os

def f(i):
    print('process name is {}, pid is {}, ppid is {}'.format(i, os.getpid(), os.getppid()))
    time.sleep(1)
    print('process {} is end.'.format(i))
def main():
    print("pid is {}".format(os.getpid()))
    pool = Pool(processes=3)
    for i in range(15):
        pool.apply(f, (i,))
    print("start...")
    pool.close()
    pool.join()
    print("end...")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import os
from multiprocessing import Process,Pipe,Queue

queue = Queue(maxsize=2)
queue.put(1)
queue.put(2)
print(queue.full(),'shifou duilie manle')
print(queue.get(),'diyici huoqu')
print(queue.full(),'shifou duilie manle')
print(queue.empty(),'shifou duilie kongle')
print(queue.get(),'dierci huoqu')
print(queue.empty(),'shifou duilie kongle')

'''
def f1():
    queue.put('Hello shiyanlou')

def f2():
    data = queue.get()
    print(data,queue.empty())

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__ == '__main__':
    main()

conn1, conn2 = Pipe()

def f1():
    conn1.send('Hello shiyanlou')

def f2():
    data = conn2.recv()
    print(data)

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__ == '__main__':
    main()

def hello(name):
    print('child process: {}'.format(os.getpid()))
    print('Hello '+name)

def main():
    p = Process(target=hello, args=('shiyanlou', ))
    print('parent process: {}'.format(os.getpid()))
    p.start()
    p.join()
    print("game over")

if __name__ == '__main__':
    main()
'''

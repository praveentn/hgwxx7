# multiprocessing example

import os
from multiprocessing import Process

def f(name):
    print('Hello,', name)

name = input('Name:')

if __name__ == '__main__':
    print('Parent process', name)
    p = Process(target=f, args=[os.environ.get('USER', 'Unknown user')])
    p.start()
    p.join()

# Parent process <name>
# Hello <os user id>

# unlike multi=threading, here we cannot share variables between processes

#!/usr/bin/env python3

import os
import time

num = 0
pid = os.fork()

if pid == 0:
    num += 1
    print('hehe1-----num = {}, pid = {}'.format(num, pid))
else:
    time.sleep(1)
    num += 1
    print('hehe2-----num = {}, pid = {}'.format(num, pid))

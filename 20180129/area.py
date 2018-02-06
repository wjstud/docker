#!/usr/bin/env python3
from math import pi
while True:
    r = input('plase enter yuan de banjin: ')
    if r == 'q':
        print('you exit!bay!')
        break
    else:
        if r.isdigit():
            print(int(r) * int(r) * pi)
        else:
            print('plase enter yuan de banjin again')
            continue

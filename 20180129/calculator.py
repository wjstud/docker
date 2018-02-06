#!/usr/bin/env python3
import sys

print(sys.argv,len(sys.argv))
if not len(sys.argv) == 2:
    print('Parameter Error')
else:
    try:
        b = int(sys.argv[1])
        a = b - 3500
        if a <= 1500:
            print(format(a*0.03, '0.2f'))
        elif a > 1500 and a <= 4500:
            print('{:.2f}'.format(a*0.1-105))
        elif a > 4500 and a <= 9000:
            print('{:.2f}'.format(a*0.2-555))
        elif a > 9000 and a <= 35000:
            print('{:.2f}'.format(a*0.25-1005))
        elif a > 35000 and a <= 55000:
            print('{:.2f}'.format(a*0.3-2755))
        elif a > 55000 and a <= 80000:
            print('{:.2f}'.format(a*0.35-5505))
        else:
            print('{}'.format(a*0.45-13505, '.2f'))
    except:
        print("Parameter Error")


         

#!/usr/bin/env python3
import sys

if not len(sys.argv) >= 2:
    print('Parameter Error')
else:
    for arg in sys.argv[1:]:
        arglist = arg.split(":")
        if len(arglist) == 2:
            try:
                GZ = int(arglist[-1]) # GZ=工资
                WXYJ = GZ * (0.08 + 0.02 + 0.005 + 0 + 0 + 0.06) # WXYJ=五险一金
                a = GZ - WXYJ - 3500 # YNSSDE=应纳税所得额
                if GZ > 3500:
                    if a <= 1500:
                        print('{}:{:.2f}'.format(arglist[0], GZ - (a * 0.03 - 0) - WXYJ))
                    elif 1500 < a <= 4500:
                        print('{}:{:.2f}'.format(arglist[0], GZ - (a * 0.1 - 105) - WXYJ))
                    elif 4500 < a <= 9000:
                        print('{}:{:.2f}'.format(arglist[0], GZ - (a * 0.2 - 555) - WXYJ))
                    elif 9000 < a <= 35000:
                        print('{}:{:.2f}'.format(arglist[0], GZ - (a * 0.25 - 1005) - WXYJ))
                    elif 35000 < a <= 55000:
                        print('{}:{:.2f}'.format(arglist[0], GZ - (a * 0.3 - 2755) - WXYJ))
                    elif 55000 < a <= 80000:
                        print('{}:{:.2f}'.format(arglist[0], GZ - (a * 0.35 - 5505) - WXYJ))
                    else:
                        print('{}:{:.2f}'.format(arglist[0], GZ - (a * 0.45 - 13505) - WXYJ))
                else:
                    print('{}:{:.2f}'.format(arglist[0], GZ - WXYJ))
            except:
                print("Parameter Error")
        else:
            print("Parameter Error")
         

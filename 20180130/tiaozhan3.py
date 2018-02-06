#!/usr/bin/env python3
import sys
import csv

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
        try:
            self.c = args.index('-c')
            self.configfile = args[c+1]
            self.d = args.index('-d')
            self.userfile = args[d+1]
            self.o = args.index('-o')
            self.gzfile = args[o+1]
        except:
            print("Parameter Error")

class Config(object):
    def __init__(self):
        self.config = self._read_config()   
    def _read_config(self):
        config = {}
        with open(Args.configfile, 'r') as f:
            config_list = f.readlines()
            for i in config_list:
                try:
                    list_i = i.strip().split('=')
                    config[list_i[0]] = list_i[1]
                except:
                    print("Parameter Error")
        return config

class UserData(object):
    def __init__(self):
        self.userdata = self._read_users_data()
    def _read_users_data(self):
        userdata = []
        with open(Args.userfile, 'r') as f:
             user_list = f.readlines()
             for i in user_list:
                 try:
                     list_i = i.strip().split(',')
                     userdata.apped(tuple(list_i))
                 except:
                     print("Parameter Error")
        return userdata
 
class IncomeTaxCalculator(object):
    def calc_for_all_userdata(self):
        for i in UserData._read_users_data:
            GH = i[0]
            GZ = int(i[1])
            if 2193 >= GZ:
                WXYJ = 2193*(0.08+0.02+0.005+0+0+0.06)
            elif 2193 < GZ < 16446:
                WXYJ = GZ*(0.08+0.02+0.005+0+0+0.06)
            else:
                WXYJ = 16446*(0.08+0.02+0.005+0+0+0.06)
            a = GZ - WXYJ - 3500
            if GZ > 3500:
                if a <= 1500:
                    GS = 
               
    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open(Args.gzfile, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':
    
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
         

#!/usr/bin/env python3

import sys
import csv
from multiprocessing import Queue,Process
#import threading

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def get_args(self):
        if len(self.args) == 6:
            try:
                c = self.args.index('-c')
                configfile = self.args[c+1]
                d = self.args.index('-d')
                userfile = self.args[d+1]
                o = self.args.index('-o')
                gzfile = self.args[o+1]
            except:
                print("Parameter Error1")
        else:
            print("Parameter Error2")
        return configfile,userfile,gzfile

class Config(Args):
    def _read_config(self):
        config = {}
        with open(self.get_args()[0], 'r') as f:
            config_list = f.readlines()
            for i in config_list:
                try:
                    list_i = i.strip().split('=')
                    config[list_i[0]] = list_i[1]
                except:
                    print("Parameter Error")
        return config

class UserData(Args):
    def _read_users_data(self):
        userdata = []
        with open(self.get_args()[1], 'r') as f:
             user_list = f.readlines()
             for i in user_list:
                 try:
                     list_i = i.strip().split(',')
                     userdata.append(tuple(list_i))
                 except:
                     print("Parameter Error")
        return userdata

class IncomeTaxCalculator(Config,UserData):
    def calc_for_all_userdata(self):
        gongzibiao = []
        for i in self._read_users_data():
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
                    GS = a*0.03-0 
                    SHGZ = GZ - GS - WXYJ
                elif 1500 < a <= 4500:
                    GS = a*0.1-105
                    SHGZ = GZ - GS - WXYJ
                elif 4500 < a <= 9000:
                    GS = a*0.2 - 555
                    SHGZ = GZ - GS - WXYJ
                elif 9000 < a <= 35000:
                    GS = a*0.25 - 1005
                    SHGZ = GZ - GS - WXYJ
                elif 35000 < a <= 55000:
                    GS = a*0.3 - 2755
                    SHGZ = GZ - GS - WXYJ
                elif 55000 < a <= 80000:
                    GS = a*0.35 - 5505
                    SHGZ = GZ - GS - WXYJ
                else:
                    GS = a*0.45 - 13505
                    SHGZ = GZ - GS - WXYJ
            else:
                GS = 0
                SHGZ = GZ - GS - WXYJ
            gongzidan = '{},{},{:.2f},{:.2f},{:.2f}'.format(GH, GZ, WXYJ, GS, SHGZ)
            gongzidan_list = gongzidan.split(',')
            gongzibiao.append(tuple(gongzidan_list))
        return gongzibiao

    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open(self.get_args()[2], 'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)
    def process(self):
        p = Process(target=IncomeTaxCalculator.export,args=(self,))
        p.start()
        p.join()

if __name__ == '__main__':
    f = IncomeTaxCalculator()
    f.process()

#!/usr/bin/env python3

import sys,getopt
import csv

def usage():
    print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata")

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def get_args(self):
        if len(self.args) == 8:
            try:
                opts,args = getopt.getopt(self.args,"hC:c:d:o:",["help"])
                for opt,arg in opts:
                    if opt in ("-h","--help"):
                        usage()
                        sys.exit(1)
                    elif opt == '-C':
                        cityname = arg
                    elif opt == '-c':
                        configfile = arg
                    elif opt == '-d':
                        userfile = arg
                    else:
                        gzfile = arg
            except:
                print("Parameter Error1 try error")
        else:
            print("Parameter Error2 len(self.args) error")
        return configfile,userfile,gzfile,cityname

class Config(Args):
    def _read_config(self):
        config = {}
        with open(self.get_args()[0], 'r') as f:
            config_list = f.readlines()
            b = len(config_list)
            for i,j in zip(config_list,range(b)):
                if len(i) < 11:
                    config_wxyj = {}  
                    if self.get_args()[3] in i:
                        config_list_city = config_list[j:j+8]
                        for i in config_list_city:
                            try: 
                                list_i = i.strip().split('=')
                                config_wxyj[list_i[0]] = list_i[1]
                                
                            except:
                                print("Parameter Error")
                        config[self.get_args()[3]] = config_wxyj
                    else:
                        config_list_city = config_list[1:9]
                        for i in  config_list_city:
                            try:
                                list_i = i.strip().split('=')
                                config_wxyj[list_i[0]] = list_i[1]
                            except:
                                print("Parameter Error")
                        config[self.get_args()[3]] = config_wxyj
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
        aa = self._read_config()
        for i,j in self._read_config().items():
            if i == self.get_args()[3]:
                wxyj = sum([float(x) for x in j.values() if 1.00 > float(x.strip())])
                for i in self._read_users_data():
                    GH = i[0]
                    GZ = int(i[1])
                    if 2193 >= GZ:
                        WXYJ = 2193*wxyj
                    elif 2193 < GZ < 16446:
                        WXYJ = GZ*wxyj
                    else:
                        WXYJ = 16446*wxyj
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

if __name__ == '__main__':
    f = IncomeTaxCalculator()
    f.export()

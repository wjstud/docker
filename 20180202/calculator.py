#!/usr/bin/env python3

import sys,getopt,configparser,csv
from datetime import datetime

def usage():
    print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata")

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def get_args(self):
        cityname = ""
        configfile = ""
        userfile = ""
        gzfile = ""
        try:
            opts,args = getopt.getopt(self.args,"hC:c:d:o:",["help"])
            for opt,arg in opts:
                if opt in ("-h","--help"):
                    usage()
                    break
                elif opt == '-C':
                    cityname = arg.upper()
                elif opt == '-c':
                    configfile = arg
                elif opt == '-d':
                    userfile = arg
                else:
                    gzfile = arg
        except:
                print("Parameter Error1 try error")
        return configfile,userfile,gzfile,cityname

class Config(Args):
    def _read_config(self):
        config = {}
        _config = configparser.ConfigParser()
        _config.read(self.get_args()[0])
        secs = _config.sections()
        if self.get_args()[3] in secs:
            kvs = _config.items(self.get_args()[3])
            config[self.get_args()[3]] = kvs
        else:
            kvs = _config.items('MOREN')
            config['MOREN'] = kvs
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
                     print("Parameter Error4")
        return userdata

class IncomeTaxCalculator(Config,UserData):
    def calc_for_all_userdata(self):
        gongzibiao = []
        for i,j in self._read_config().items():
            if i == self.get_args()[3]:
                wxyj = sum([float(y) for x,y in j if 1.00 > float(y.strip())])
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
                    gongzidan = '{},{},{:.2f},{:.2f},{:.2f},{}'.format(GH, GZ, WXYJ, GS, SHGZ, datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
                    gongzidan_list = gongzidan.split(',')
           
                    gongzibiao.append(tuple(gongzidan_list))
            else:
                wxyj = sum([float(y) for x,y in self._read_config()['MOREN'] if 1.00 > float(y.strip())])
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
                    gongzidan = '{},{},{:.2f},{:.2f},{:.2f},{}'.format(GH, GZ, WXYJ, GS, SHGZ, datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
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

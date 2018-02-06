#!/usr/bin/env python3
# coding:utf-8

import sys
from multiprocessing import Queue,Process

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    def get_args(self,arg):
        value = self.args[self.args.index(arg) + 1]
        return value

class SheBao_conf(object):
    def __init__(self,file):
        self.jishu_l,self.jishu_h,self.wxyj = self.get_sbconf(file)
    def get_sbconf(self,file):
        wxyj = 0
        with open(file,'r') as f:
            for line in f:
                key,value = line.split("=")
                if key.strip() == 'JiShuL':
                    jishu_l = float(value.strip())
                
                elif key.strip() == 'JiShuH':
                    jishu_h = float(value.strip())
                else:
                    wxyj += float(value.strip())
        return jishu_l,jishu_h,wxyj

class User_conf(Process):
    def __init__(self,file,output_queue):
        self.file = file
        self.output_q = output_queue
        super().__init__()

    def get_uconf(self):
        with open(self.file,'r') as f:
            for line in f:
                GH,GZ = line.split(",")
                yield GH.strip(),int(GZ.strip())
    def run(self):
        for item in self.get_uconf():
            self.output_q.put(item)

class Make_gongzidan(Process):
    gongzi_js = 3500
    sljss = [(80000,0.45,13505),
             (55000,0.35,5505),
             (35000,0.3,2755),
             (9000,0.25,1005),
             (4500,0.2,555),
             (1500,0.1,105),
             (0,0.03,0)]
    def __init__(self,config,input_queue,output_queue):
        self.config = config
        self.input_q = input_queue
        self.output_q = output_queue
        super().__init__()

    def gongzidan(self,data_item):
        gonghao,gongzi = data_item
        if gongzi < self.config.jishu_l:
            shebao = self.config.jishu_l * self.config.wxyj
        elif self.config.jishu_l < gongzi < self.config.jishu_h:
            shebao = gongzi * self.config.wxyj
        else:
            shebao = self.config.jishu_h * self.config.wxyj
        left_gongzi = gongzi - shebao
        tax_gongzi = left_gongzi - self.gongzi_js
        if tax_gongzi < 0:
            geshui = 0
        else:
            for item in self.sljss:
                if tax_gongzi > item[0]:
                    geshui = tax_gongzi * item[1] - item[2]
                    break
        SHGZ = left_gongzi - geshui
        return '{},{},{:.2f},{:.2f},{:.2f}\n'.format(gonghao,gongzi,shebao,geshui,SHGZ)
    def run(self):
        while True:
            try:
                item = self.input_q.get(timeout=1)
            except:
                return
        result = self.gongzidan(item)
        self.output_q.put(result)

class Write_file(Process):
    def __init__(self,file,input_queue):
        self.file = file
        self.input_q = input_queue
    def export(self,data):
        with open(self.file,'a') as f:
            f.write(data)
    def run(self):
        while True:
            try:
                item = self.input_q.get(timeout=1)
            except:
                self.close()
                return
            self.export(item)
    
if __name__ == '__main__':
    args = Args()
    sb = SheBao_conf(args.get_args('-c'))
    q1 = Queue()
    q2 = Queue()
    us = User_conf(args.get_args('-d'),q1)
    gzd = Write_file(args.get_args('-o'),q2)
    
    f = Make_gongzidan(sb,q1,q2)
    for i in us.get_uconf():
        gzd.export(f.gongzidan(i))

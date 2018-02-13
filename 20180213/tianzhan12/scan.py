# coding: utf-8

from socket import *
import sys,getopt

def usage():
    print("Usage1: {} --host 127.0.0.1 --port 22\nUsage2: {} --host 127.0.0.1 --port 80-100".format(sys.argv[0],sys.argv[0]))

def low_scan(host, port):

    s = socket()
    s.settimeout(0.1)
    result = s.connect_ex((host, port))
    if result == 0:
        print("{} open".format(port))
        s.close()
    else:
        print("{} closed".format(port))

if __name__ == '__main__':
    host = ''
    port = ''
    try:
        args,opts = getopt.getopt(sys.argv[1:],"h",["help","host=","port="])
    except:
        print("Parameter Error")
        usage()
        sys.exit(1)
    if len(sys.argv) == 5:
        for opt,arg in args:
            if opt in ('-h','--help'):
                usage()
                sys.exit(2)
            elif opt == '--host':
                host = arg
            elif opt == '--port':
                port = arg
        if len(str(host).split(".")) == 4:
            if "-" in str(port):
                port_start, port_end = str(port).split("-")
                for i in range(int(port_start),int(port_end) + 1):
                    low_scan(host,i)
            else:
                low_scan(host,int(port))
        else:
            print("Enter a valid host ip ")

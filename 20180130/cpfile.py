#!/usr/bin/env python3

import sys

def copy_file(src,dst):
    with open(src, 'r') as s:
        with open(dst, 'w') as d:
            d.write(s.read())

if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_file(sys.argv[1], sys.argv[2])
    else:
        print("Parameter Error")
        print("Usage: ", sys.argv[0], "srcfile dstfile")
        sys.exit(-1)
    sys.exit(0)

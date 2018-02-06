#!/usr/bin/env python3

def char_count(str):
    countdict = {}
    for i in str:
        c = countdict.get(i)
        if c == None:
            countdict[i] = 1
        else:
            countdict[i] += 1
    print(countdict)

if __name__ == '__main__':
    r = input("Please enter a str: ")
    char_count(r)

#!/usr/bin/env python3

filename = input("Please Enter the file name: ")

try:
    with open(filename) as f:
        count = 0
        for line in f:
            count += 1
            print(line)
        print('Lines: ', count)
except:
    print("Enter Error")

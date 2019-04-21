#!/usr/bin/env python
"""mapper.py"""
import sys

lst = []
for line in sys.stdin:
    data = line.strip()
    data = data[:len(data) -1]
    lst.append(data)
for i in range(1,len(lst) - 1):
    pair1 = "(" + lst[i] + "," + lst[i-1] + ")   1"
    pair2 = "(" + lst[i] + "," + lst[i+1] + ")   1"
    print(pair1)
    print(pair2)
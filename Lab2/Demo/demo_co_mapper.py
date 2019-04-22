#!/usr/bin/env python
"""mapper.py"""
import sys

with open("demo_clean.txt","r") as demo:
    lst = []
    demodata = demo.readlines()
    for data in demodata:
        data = data.strip()
        lst.append(data)

    with open("mapper_output.txt","w") as demomap:
        for i in range(1,len(lst) - 1):
            pair1 = "(" + lst[i] + "," + lst[i-1] + ")   1"
            demomap.write(pair1 + "\n")
demo.close()
demomap.close()
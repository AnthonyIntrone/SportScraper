#!/usr/bin/env python
"""mapper.py"""
import sys

with open("../../../part1/data/NYT/NYT.txt","r") as nyt:
    lst = []
    nytdata = nyt.readlines()
    for data in nytdata:
        data = data.strip()
        lst.append(data)

    with open("../../NYT/Co-OccurrenceData/mapper_output.txt","w") as nytmap:
        for i in range(1,len(lst) - 1):
            pair1 = "(" + lst[i] + "," + lst[i-1] + ")   1"
            nytmap.write(pair1 + "\n")

nyt.close()
nytmap.close()

with open("../../../part1/data/Twitter/Twitter.txt","r") as twitter:
    lst = []
    twdata = twitter.readlines()
    for data in twdata:
        data = data.strip()
        lst.append(data)
    with open("../../Twitter/Co-OccurrenceData/mapper_output.txt","w") as twmap:
        for i in range(1,len(lst) - 1):
            pair1 = "(" + lst[i] + "," + lst[i-1] + ")   1"
            twmap.write(pair1 + "\n")

twitter.close()
twmap.close()
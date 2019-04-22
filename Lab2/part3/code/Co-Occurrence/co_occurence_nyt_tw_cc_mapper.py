#!/usr/bin/env python
"""mapper.py"""
#Authors: Anthony Introne
#         Michael Klein
import sys

# Mapping each word with its neighbor and writing to another file
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

# Mapping each word with its neighbor and writing to another file
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

# Mapping each word with its neighbor and writing to another file
with open("../../../part1/data/CommonCrawl/cc.txt","r") as cc:
    lst = []
    ccdata = cc.readlines()
    for data in ccdata:
        data = data.strip()
        lst.append(data)
    with open("../../CommonCrawl/Co-OccurrenceData/mapper_output.txt","w") as ccmap:
        for i in range(1,len(lst) - 1):
            pair1 = "(" + lst[i] + "," + lst[i-1] + ")   1"
            ccmap.write(pair1 + "\n")

cc.close()
ccmap.close()